from vulnerabilities.improvers import default
from vulnerabilities import importers

IMPROVER_REGISTRY = [default.DefaultImprover, importers.nginx.NginxBasicImprover]

improver_mapping = {x.qualified_name(): x for x in IMPROVER_REGISTRY}
