"""Validated analytics metric definitions with dependency resolution."""
import re

_NAME = re.compile(r"^[a-z][a-z0-9_]*$")

class MetricDictionary:
    def __init__(self):
        self.definitions = {}

    def add(self, name, description, unit="count", depends_on=()):
        if not isinstance(name, str) or not _NAME.fullmatch(name):
            raise ValueError("metric name must be snake_case")
        if name in self.definitions:
            raise ValueError("duplicate metric")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("description required")
        if not isinstance(unit, str) or not unit.strip():
            raise ValueError("unit required")
        if isinstance(depends_on, str):
            raise ValueError("dependencies must be a sequence")
        dependencies = tuple(depends_on)
        if any(not isinstance(dep, str) or not _NAME.fullmatch(dep) for dep in dependencies):
            raise ValueError("invalid dependency")
        if len(dependencies) != len(set(dependencies)):
            raise ValueError("duplicate dependencies")
        self.definitions[name] = {"name": name, "description": description.strip(),
                                  "unit": unit.strip(), "depends_on": dependencies}

    def order(self, selected=None):
        requested = sorted(self.definitions) if selected is None else list(selected)
        output, state = [], {}
        def visit(name):
            if name not in self.definitions:
                raise ValueError("unknown metric: " + str(name))
            if state.get(name) == 1:
                raise ValueError("dependency cycle")
            if state.get(name) == 2:
                return
            state[name] = 1
            for dep in self.definitions[name]["depends_on"]:
                visit(dep)
            state[name] = 2
            output.append(name)
        for name in requested:
            visit(name)
        return output

    def export(self):
        self.order()
        return [{**self.definitions[name], "depends_on": list(self.definitions[name]["depends_on"])}
                for name in sorted(self.definitions)]
