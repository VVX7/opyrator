import json
from typing import Optional, Dict, Any, Union


def _int_to_str(d: Dict[str, Any]) -> Dict[str, Any]:
    # transform all integer back to string
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = _int_to_str(v)
        elif isinstance(v, int) and not isinstance(v, bool):
            d[k] = str(v)
    return d


class AbstractOperator():
    def __init__(self, **kwargs):
        """
        Abstract class for all the Operator objects.
        """
        super().__init__()

    def from_dict(self, **kwargs) -> None:
        for prop, value in kwargs.items():
            if value is None:
                continue
            setattr(self, prop, value)

    def from_json(self, json_string: str) -> None:
        self.from_dict(**json.loads(json_string))

    def to_json(self, sort_keys: bool = False, indent: Optional[int] = None) -> str:
        return json.dumps(self, default=operator_json_default, sort_keys=sort_keys, indent=indent)

    def jsonable(self) -> Dict:
        return self.__dict__


def operator_json_default(obj: AbstractOperator) -> Union[Dict, str]:
    return obj.jsonable()

