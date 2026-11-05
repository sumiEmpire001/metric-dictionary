# metric-dictionary

An in-memory metric catalog that validates metric names and metadata, resolves dependency order, detects cycles and missing definitions, and exports JSON-compatible definitions. No metric execution, SQL generation, database integration or persistence.

## Run

Python 3.10+; no third-party dependencies.

```bash
python -m unittest discover -s tests -v
```

## Python example

```python
from metric_dictionary import MetricDictionary
catalog = MetricDictionary()
catalog.add("visits", "Total visits")
print(catalog.export())
```

GitHub Actions runs tests on Python 3.10, 3.12, and 3.13. Check the latest run before claiming verification.
