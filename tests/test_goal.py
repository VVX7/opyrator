import pytest
from opyrator.objects import Goal


@pytest.fixture
def example_goal_dict():
    return {
        "key": "foo",
        "val": "bar",
        "criteria": "baz"
    }


def test_goal():
    goal = Goal()
    assert type(goal) == Goal


def test_goal_key(example_goal_dict):
    goal = Goal()
    goal.from_dict(**example_goal_dict)
    assert goal.key == "foo"


def test_goal_val(example_goal_dict):
    goal = Goal()
    goal.from_dict(**example_goal_dict)
    assert goal.val == "bar"


def test_goal_criteria(example_goal_dict):
    goal = Goal()
    goal.from_dict(**example_goal_dict)
    assert goal.criteria == "baz"
