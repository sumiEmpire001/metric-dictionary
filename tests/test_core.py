import unittest
from metric_dictionary import MetricDictionary

class Tests(unittest.TestCase):
    def test_dependency_order(self):
        d = MetricDictionary()
        d.add("conversion", "Ratio", depends_on=["visits","sales"])
        d.add("visits", "Visits")
        d.add("sales", "Sales")
        order = d.order(["conversion"])
        self.assertLess(order.index("visits"), order.index("conversion"))
        self.assertLess(order.index("sales"), order.index("conversion"))
        self.assertEqual(len(d.export()), 3)
    def test_cycle(self):
        d = MetricDictionary()
        d.add("a", "A", depends_on=["b"])
        d.add("b", "B", depends_on=["a"])
        with self.assertRaisesRegex(ValueError, "cycle"):
            d.order()
    def test_missing_and_invalid(self):
        d = MetricDictionary()
        d.add("a", "A", depends_on=["missing"])
        with self.assertRaisesRegex(ValueError, "unknown"):
            d.order()
        with self.assertRaises(ValueError):
            d.add("Bad Name", "bad")
        with self.assertRaises(ValueError):
            d.add("a", "duplicate")
