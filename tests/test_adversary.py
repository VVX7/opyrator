import pytest
from opyrator.objects import Adversary, AdversaryUpdate


@pytest.fixture
def example_adversary_dict():
    return {
        "id": "61cd733e-d43d-4228-b02a-859089b3e0b6",
        "name": "APT UwU",
        "ttps": [
            "00010203-0405-0607-0809-0a0b0c0d0e0f",
            "be674970-449b-4eb6-95c3-251ee90bea69"
        ],
        "goals": [
            {
                "key": "foo",
                "val": "bar",
                "criteria": "baz",
            }
        ]
    }


@pytest.fixture
def example_adversary_update_dict():
    return {
        "add": ["foo"],
        "remove": ["bar"]
    }


def test_adversary():
    adversary = Adversary()
    assert type(adversary) == Adversary


def test_adversary_update():
    adversary = AdversaryUpdate()
    assert type(adversary) == AdversaryUpdate


def test_adversary_id(example_adversary_dict):
    adversary = Adversary()
    adversary.from_dict(**example_adversary_dict)
    assert adversary.id == "61cd733e-d43d-4228-b02a-859089b3e0b6"


def test_adversary_name(example_adversary_dict):
    adversary = Adversary()
    adversary.from_dict(**example_adversary_dict)
    assert adversary.name == "APT UwU"


def test_adversary_ttps(example_adversary_dict):
    adversary = Adversary()
    adversary.from_dict(**example_adversary_dict)
    assert adversary.ttps == ["00010203-0405-0607-0809-0a0b0c0d0e0f", "be674970-449b-4eb6-95c3-251ee90bea69"]


def test_adversary_goals(example_adversary_dict):
    adversary = Adversary()
    adversary.from_dict(**example_adversary_dict)
    assert adversary.goals == [{"key": "foo", "val": "bar", "criteria": "baz"}]


def test_adversary_update_add(example_adversary_update_dict):
    adversary = AdversaryUpdate()
    adversary.from_dict(**example_adversary_update_dict)
    assert adversary.add == ["foo"]


def test_adversary_update_remove(example_adversary_update_dict):
    adversary = AdversaryUpdate()
    adversary.from_dict(**example_adversary_update_dict)
    assert adversary.remove == ["bar"]
