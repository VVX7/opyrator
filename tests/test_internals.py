import pytest
from opyrator.objects import InternalSettings


@pytest.fixture
def example_internal_settings_dict():
    return {
        "local": example_workspace_dict(),
        "identity": "123",
        "account": example_account_dict()
    }


def example_account_dict():
    return {
        "email": "foo@bar.baz",
        "tag": "123",
        "license": "professional",
        "badges": [],
        "token": "123"
    }


def example_workspace_dict():
    return {
        "workspace": "login.prelude.org",
        "keys": example_workspace_keys_dict(),
        "server": "127.0.0.1",
        "tcp_port": "2323",
        "udp_port": "4545",

        "http_port": "3391",
        "shell_port": "3007",
        "publishers": example_workspace_publishers_dict(),
        "redirectors": {},
        "encryptors": {
            "default": True,
            "plaintext": False
        },
        "sources": [],
        "planner": "http://localhost:8888"
    }


def example_workspace_keys_dict():
    return {
        "agent": ["foobarkey"],
        "data": ["foo"]
    }


def example_workspace_publishers_dict():
    return {
        "local": True,
        "prelude": False
    }


def test_internal_settings():
    settings = InternalSettings()
    assert type(settings) == InternalSettings


def test_internal_settings_local(example_internal_settings_dict):
    settings = InternalSettings()
    settings.from_dict(**example_internal_settings_dict)
    assert settings.local == {"workspace": "login.prelude.org",
                              "keys": {
                                  "agent": ["foobarkey"],
                                  "data": ["foo"]
                              },
                              "server": "127.0.0.1",
                              "tcp_port": "2323",
                              "udp_port": "4545",

                              "http_port": "3391",
                              "shell_port": "3007",
                              "publishers": {
                                  "local": True,
                                  "prelude": False
                              },
                              "redirectors": {},
                              "encryptors": {
                                  "default": True,
                                  "plaintext": False
                              },
                              "sources": [],
                              "planner": "http://localhost:8888"}


def test_internal_settings_identity(example_internal_settings_dict):
    settings = InternalSettings()
    settings.from_dict(**example_internal_settings_dict)
    assert settings.identity == "123"


def test_internal_settings_account(example_internal_settings_dict):
    settings = InternalSettings()
    settings.from_dict(**example_internal_settings_dict)
    assert settings.account == {
        "email": "foo@bar.baz",
        "tag": "123",
        "license": "professional",
        "badges": [],
        "token": "123"}
