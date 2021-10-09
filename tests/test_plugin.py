import pytest
from opyrator.objects import Plugin


@pytest.fixture
def example_plugin_dict():
    return {
        "name": "Navigator",
        "description": "Display the ATT&CK Navigator and export layers",
        "version": "01d33d8cbb14afffdf57e6ccc174fd46",
        "native": False
    }


def test_plugin():
    plugin = Plugin()
    assert type(plugin) == Plugin


def test_plugin_name(example_plugin_dict):
    plugin = Plugin()
    plugin.from_dict(**example_plugin_dict)
    assert plugin.name == "Navigator"


def test_plugin_description(example_plugin_dict):
    plugin = Plugin()
    plugin.from_dict(**example_plugin_dict)
    assert plugin.description == "Display the ATT&CK Navigator and export layers"


def test_plugin_version(example_plugin_dict):
    plugin = Plugin()
    plugin.from_dict(**example_plugin_dict)
    assert plugin.version == "01d33d8cbb14afffdf57e6ccc174fd46"


def test_plugin_native(example_plugin_dict):
    plugin = Plugin()
    plugin.from_dict(**example_plugin_dict)
    assert plugin.native is False
