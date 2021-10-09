import pytest
from opyrator.objects import Operation, OperationAudit, OperatorClient


@pytest.fixture
def example_operation_dict():
    return {
        "id": "0033fd08-57d4-42af-8ada-7f51172e6568",
        "adversary": {
            "id": "61cd733e-d43d-4228-b02a-859089b3e0b6",
            "name": "foo",
            "ttps": [
                "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "db87077c-66ed-11eb-ae93-0242ac130002",
                "1d83bce0-5454-4600-ae2d-e38ea4e56804"
            ]
        },
        "range": "red",
        "audit": {
            "agent1": {
                "status": 1,
                "links": [
                    "c8d841d8-cb2e-4a62-8d29-7cb86dbba98b",
                    "93ac9cdf-fd52-4926-93e4-b5fc206f8860",
                    "74c4627c-ad27-4d6c-9af2-46f8debc139d"
                ]
            }
        },
        "start": "2021-09-25T21:52:05.055Z",
        "end": "2021-09-25T21:52:05.063Z",
        "training": []
    }


@pytest.fixture
def example_operation_audit_dict():
    return {
        "agent1": {
            "status": 1,
            "links": [
                "c8d841d8-cb2e-4a62-8d29-7cb86dbba98b",
                "93ac9cdf-fd52-4926-93e4-b5fc206f8860",
                "74c4627c-ad27-4d6c-9af2-46f8debc139d"
            ]
        }
    }


def test_operation():
    operation = Operation()
    assert type(operation) == Operation


def test_operationAudit():
    operation = OperationAudit()
    assert type(operation) == OperationAudit


def test_operatorClient():
    operation = OperatorClient()
    assert type(operation) == OperatorClient


def test_operation_id(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.id == "0033fd08-57d4-42af-8ada-7f51172e6568"


def test_operation_adversary(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.adversary == {
            "id": "61cd733e-d43d-4228-b02a-859089b3e0b6",
            "name": "foo",
            "ttps": [
                "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "db87077c-66ed-11eb-ae93-0242ac130002",
                "1d83bce0-5454-4600-ae2d-e38ea4e56804"
            ]
        }


def test_operation_range(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.range == "red"


def test_operation_audit(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.audit == {
            "agent1": {
                "status": 1,
                "links": [
                    "c8d841d8-cb2e-4a62-8d29-7cb86dbba98b",
                    "93ac9cdf-fd52-4926-93e4-b5fc206f8860",
                    "74c4627c-ad27-4d6c-9af2-46f8debc139d"
                ]
            }
        }


def test_operation_start(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.start == "2021-09-25T21:52:05.055Z"


def test_operation_end(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.end == "2021-09-25T21:52:05.063Z"


def test_operation_training(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.training == []


def test_operation_audit_status(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.audit["agent1"]["status"] == 1


def test_operation_audit_status(example_operation_dict):
    operation = Operation()
    operation.from_dict(**example_operation_dict)
    assert operation.audit["agent1"]["links"] == [
                    "c8d841d8-cb2e-4a62-8d29-7cb86dbba98b",
                    "93ac9cdf-fd52-4926-93e4-b5fc206f8860",
                    "74c4627c-ad27-4d6c-9af2-46f8debc139d"
                ]
