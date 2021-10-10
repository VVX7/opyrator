import pytest
from opyrator.objects import Attack, AttackVersion, AttackMetadata, Platform, Executor


@pytest.fixture
def example_attack_dict(example_attack_metadata_dict, example_platform_dict):
    return {"id": "1d83bce0-5454-4600-ae2d-e38ea4e56804",
            "name": "Get system info",
            "description": "This discovers ...",
            "tactic": "discovery",
            "technique": {
                "id": "T1007",
                "name": "System Service Discovery"
            },
            "platforms": example_platform_dict,
            "metadata": example_attack_metadata_dict,
            "modified": False,
            "isModified": False}


@pytest.fixture
def example_attack_metadata_dict():
    return {"version": 1,
            "authors": ["khyberspache"],
            "tags": ["ransomware", "apt29"],
            "enabled": True,
            "checksum": "99bcaf9591f16bc5ed6275a651f39a5e7878e1e00ad675fc7c150bfe335908fa",
            "release_date": "2020-11-05",
            "license": "professional"}


@pytest.fixture
def example_command_variants_dict():
    return {"command": "foo", "payload": "foo"}


@pytest.fixture
def example_command_dict(example_command_variants_dict):
    return {"command": "foo",
            "payload": "foo",
            "variants": [example_command_variants_dict]}


@pytest.fixture
def example_executor_dict(example_command_dict):
    return {"psh": example_command_dict}


@pytest.fixture
def example_platform_dict(example_executor_dict):
    return {"windows": example_executor_dict}


@pytest.fixture
def example_attack_version_dict():
    return


def test_attack():
    adversary = Attack()
    assert type(adversary) == Attack


def test_attackMetadata():
    adversary = AttackMetadata()
    assert type(adversary) == AttackMetadata


def test_attackVersion():
    adversary = AttackVersion()
    assert type(adversary) == AttackVersion


def test_platform():
    platform = Platform()
    assert type(platform) == Platform


def test_executor():
    executor = Executor()
    assert type(executor) == Executor


def test_attack_id(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.id == "1d83bce0-5454-4600-ae2d-e38ea4e56804"


def test_attack_name(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.name == "Get system info"


def test_attack_description(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.description == "This discovers ..."


def test_attack_tactic(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.tactic == "discovery"


def test_attack_technique(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.technique == {"id": "T1007", "name": "System Service Discovery"}


def test_attack_platforms(example_attack_dict, example_platform_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.platforms == example_platform_dict


def test_attack_metadata(example_attack_dict, example_attack_metadata_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.metadata == example_attack_metadata_dict


def test_attack_modified(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.modified is False


def test_attack_is_modified(example_attack_dict):
    attack = Attack()
    attack.from_dict(**example_attack_dict)
    assert attack.isModified is False


def test_attack_metadata_authors(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.authors == ["khyberspache"]


def test_attack_metadata_tags(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.tags == ["ransomware", "apt29"]


def test_attack_metadata_enabled(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.enabled is True


def test_attack_metadata_checksum(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.checksum == "99bcaf9591f16bc5ed6275a651f39a5e7878e1e00ad675fc7c150bfe335908fa"


def test_attack_metadata_release_date(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.release_date == "2020-11-05"


def test_attack_metadata_version(example_attack_metadata_dict):
    attack = AttackMetadata()
    attack.from_dict(**example_attack_metadata_dict)
    assert attack.license == "professional"
