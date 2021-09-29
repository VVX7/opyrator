# opyrator

opyrator is a REST API client library for the Prelude Operator.

## Getting started

```python
from opyrator.api import API

client = API(url="http://localhost:8888",
             key="operator_session_key_here",
             ssl=False)

adversaries = client.get_adversaries()
```

## Swagger

See the Operator Swagger docs for more info.

`http://localhost:8888/docs/`


## Notes

Thanks to [PyMISP](https://github.com/MISP/PyMISP) library. I copied some of their code in the base class :)