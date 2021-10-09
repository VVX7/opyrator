import pytest
from opyrator.objects import Agent, AgentHandler, Fact


@pytest.fixture
def example_agent_dict():
    return {
        "name": "foo",
        "label": "foo",
        "history": [
            "2021-10-06T14:40:32.872Z",
            "2021-10-06T23:56:28.102Z"
        ],
        "queue": [],
        "links": [
            {
                "unique": "6185dad6-d224-45ce-bc80-4cd0b013d57c",
                "tag": "fe3e9c69-5519-4b50-95d0-4c0f9366cab9",
                "host": "user",
                "platform": "linux",
                "timestamp": 1633475723744,
                "ttp": "db87077c-66ed-11eb-ae93-0242ac130002",
                "executor": "sh",
                "request": "echo $PATH",
                "response": "/usr/local/go/bin",
                "status": 0,
                "pid": "66318",
                "tactic": "discovery",
                "technique": "T1082",
                "operation": "ab3dbc4b-0576-4bb3-af76-0856542ea950"
            },
            {
                "unique": "6c8239ea-25a7-4ee6-b831-e77ceed5a65e",
                "tag": "fe3e9c69-5519-4b50-95d0-4c0f9366cab9",
                "host": "user",
                "platform": "linux",
                "timestamp": 1633475723744,
                "ttp": "1d83bce0-5454-4600-ae2d-e38ea4e56804",
                "executor": "sh",
                "request": "uname -a",
                "response": "GNU/Linux",
                "status": 0,
                "pid": "66319",
                "tactic": "discovery",
                "technique": "T1007",
                "operation": "ab3dbc4b-0576-4bb3-af76-0856542ea950"
            }
        ],
        "executing": {},
        "facts": {
            "custom": [],
            "6185dad6-d224-45ce-bc80-4cd0b013d57c": [
                {
                    "host": "user",
                    "key": "file.T1082",
                    "value": "/usr/local/bin",
                    "linkID": "6185dad6-d224-45ce-bc80-4cd0b013d57c",
                    "ttp": "db87077c-66ed-11eb-ae93-0242ac130002"
                }
            ]
        },
        "automaticFacts": [
            {
                "host": "automatic",
                "key": "operator.session",
                "value": "bar",
                "linkID": "automatic",
                "ttp": ""
            },
            {
                "host": "automatic",
                "key": "operator.http",
                "value": "http://127.0.0.1:3391",
                "linkID": "automatic",
                "ttp": ""
            }
        ],
        "locked": False,
        "location": "/tmp/pneuma-linux",
        "target": "127.0.0.1",
        "hostname": "operator",
        "state": 2,
        "key": "foobarkey",
        "busy": False,
        "handler": {
            "name": "n/a",
            "active": True
        },
        "interval": 3,
        "platform": "linux",
        "executors": [
            "keyword",
            "python",
            "sh",
            "bash"
        ],
        "range": "red",
        "touched": "2021-10-06T23:56:36.184Z",
        "encryptor": "default",
        "sleep": 5
    }


@pytest.fixture
def example_agent_handler_dict():
    return {"name": "n/a", "active": True}


@pytest.fixture
def example_fact_dict():
    return {
        "host": "user",
        "key": "file.T1082",
        "value": "/usr/local/bin",
        "linkID": "6185dad6-d224-45ce-bc80-4cd0b013d57c",
        "ttp": "db87077c-66ed-11eb-ae93-0242ac130002"
    }


def test_agent():
    adversary = Agent()
    assert type(adversary) == Agent


def test_agent_handler():
    agent_handler = AgentHandler()
    assert type(agent_handler) == AgentHandler


def test_fact():
    fact = Fact()
    assert type(fact) == Fact


def test_agent_name(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.name == "foo"


def test_agent_label(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.label == "foo"


def test_agent_history(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.history == ["2021-10-06T14:40:32.872Z", "2021-10-06T23:56:28.102Z"]


def test_agent_queue(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.queue == []


def test_agent_links(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.links == [
        {
            "unique": "6185dad6-d224-45ce-bc80-4cd0b013d57c",
            "tag": "fe3e9c69-5519-4b50-95d0-4c0f9366cab9",
            "host": "user",
            "platform": "linux",
            "timestamp": 1633475723744,
            "ttp": "db87077c-66ed-11eb-ae93-0242ac130002",
            "executor": "sh",
            "request": "echo $PATH",
            "response": "/usr/local/go/bin",
            "status": 0,
            "pid": "66318",
            "tactic": "discovery",
            "technique": "T1082",
            "operation": "ab3dbc4b-0576-4bb3-af76-0856542ea950"
        },
        {
            "unique": "6c8239ea-25a7-4ee6-b831-e77ceed5a65e",
            "tag": "fe3e9c69-5519-4b50-95d0-4c0f9366cab9",
            "host": "user",
            "platform": "linux",
            "timestamp": 1633475723744,
            "ttp": "1d83bce0-5454-4600-ae2d-e38ea4e56804",
            "executor": "sh",
            "request": "uname -a",
            "response": "GNU/Linux",
            "status": 0,
            "pid": "66319",
            "tactic": "discovery",
            "technique": "T1007",
            "operation": "ab3dbc4b-0576-4bb3-af76-0856542ea950"
        }
    ]


def test_agent_executing(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.executing == {}


def test_agent_facts(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.facts == {
            "custom": [],
            "6185dad6-d224-45ce-bc80-4cd0b013d57c": [
                {
                    "host": "user",
                    "key": "file.T1082",
                    "value": "/usr/local/bin",
                    "linkID": "6185dad6-d224-45ce-bc80-4cd0b013d57c",
                    "ttp": "db87077c-66ed-11eb-ae93-0242ac130002"
                }
            ]
        }


def test_agent_automatic_facts(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.automaticFacts == [
            {
                "host": "automatic",
                "key": "operator.session",
                "value": "bar",
                "linkID": "automatic",
                "ttp": ""
            },
            {
                "host": "automatic",
                "key": "operator.http",
                "value": "http://127.0.0.1:3391",
                "linkID": "automatic",
                "ttp": ""
            }
        ]


def test_agent_locked(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.locked is False


def test_agent_location(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.location == "/tmp/pneuma-linux"


def test_agent_target(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.target == "127.0.0.1"


def test_agent_hostname(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.hostname == "operator"


def test_agent_state(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.state == 2


def test_agent_key(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.key == "foobarkey"


def test_agent_busy(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.busy is False


def test_agent_interval(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.interval == 3


def test_agent_platform(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.platform == "linux"


def test_agent_executors(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.executors == ["keyword", "python", "sh", "bash"]


def test_agent_range(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.range == "red"


def test_agent_touched(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.touched == "2021-10-06T23:56:36.184Z"


def test_agent_encryptor(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.encryptor == "default"


def test_agent_sleep(example_agent_dict):
    agent = Agent()
    agent.from_dict(**example_agent_dict)
    assert agent.sleep == 5


def test_agent_handler_name(example_agent_handler_dict):
    agent = AgentHandler()
    agent.from_dict(**example_agent_handler_dict)
    assert agent.name == "n/a"


def test_agent_handler_active(example_agent_handler_dict):
    agent = AgentHandler()
    agent.from_dict(**example_agent_handler_dict)
    assert agent.active is True
