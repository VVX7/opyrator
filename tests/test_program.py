import pytest
from opyrator.objects import Program, Course, Challenge, Flag, FlagTemplate


@pytest.fixture
def example_program_dict(example_course_dict):
    return {
        "id": "introduction",
        "name": "Introduction",
        "description": "Learn how to",
        "license": "community",
        "courses": [example_course_dict]

    }


@pytest.fixture
def example_course_dict(example_challenge_dict):
    return {
        "id": "introductiontraining",
        "name": "training",
        "description": "Things to know",
        "challenges": [example_challenge_dict]
    }


@pytest.fixture
def example_challenge_dict(example_flag_dict):
    return {
        "id": "699d3250-88f6-4294-92f6-de4aeaad4b94.yml",
        "key": "training/introduction/training/699d3250-88f6-4294-92f6-de4aeaad4b94.yml",
        "attempts": 1,
        "completed": 1,
        "difficulty": 1,
        "flag": example_flag_dict
    }


@pytest.fixture
def example_flag_dict(example_flag_template_dict):
    return {
        "id": "699d3250-88f6-4294-92f6-de4aeaad4b94",
        "template": example_flag_template_dict,
        "name": "Welcome to Operator training",
        "challenge": "Orient yourself with the course sidebar",
        "context": "Training is",
        "resources": {},
        "answer": "Number(0)",
        "hints": [],
        "blocks": {
            "Click the grey dots!": "Every time you",
            "Create your own training": "Did you know",
            "Features = Flags": "As you progress using",
            "Pink Badge": "Pink Badge is a self-paced"
        }
    }


@pytest.fixture
def example_flag_template_dict():
    return {"name": "submit", "data": []}


def test_course():
    course = Course()
    assert type(course) == Course


def test_program():
    program = Program()
    assert type(program) == Program


def test_challenge():
    challenge = Challenge()
    assert type(challenge) == Challenge


def test_flag():
    flag = Flag()
    assert type(flag) == Flag


def test_flag_template():
    flag = FlagTemplate()
    assert type(flag) == FlagTemplate


def test_program_id(example_program_dict):
    program = Program()
    program.from_dict(**example_program_dict)
    assert program.id == "introduction"


def test_program_name(example_program_dict):
    program = Program()
    program.from_dict(**example_program_dict)
    assert program.name == "Introduction"


def test_program_description(example_program_dict):
    program = Program()
    program.from_dict(**example_program_dict)
    assert program.description == "Learn how to"


def test_program_license(example_program_dict):
    program = Program()
    program.from_dict(**example_program_dict)
    assert program.license == "community"


def test_program_license(example_program_dict):
    program = Program()
    program.from_dict(**example_program_dict)
    assert program.license == "community"


def test_program_courses_id(example_course_dict):
    course = Course()
    course.from_dict(**example_course_dict)
    assert course.id == "introductiontraining"


def test_program_courses_name(example_course_dict):
    course = Course()
    course.from_dict(**example_course_dict)
    assert course.name == "training"


def test_program_courses_description(example_course_dict):
    course = Course()
    course.from_dict(**example_course_dict)
    assert course.description == "Things to know"


def test_program_courses_challenges(example_course_dict, example_challenge_dict):
    course = Course()
    course.from_dict(**example_course_dict)
    assert course.challenges == [example_challenge_dict]


def test_program_challenge_id(example_challenge_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.id == "699d3250-88f6-4294-92f6-de4aeaad4b94.yml"


def test_program_challenge_key(example_challenge_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.key == "training/introduction/training/699d3250-88f6-4294-92f6-de4aeaad4b94.yml"


def test_program_challenge_attempts(example_challenge_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.attempts == 1


def test_program_challenge_completed(example_challenge_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.completed == 1


def test_program_challenge_difficulty(example_challenge_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.difficulty == 1


def test_program_challenge_flag(example_challenge_dict, example_flag_dict):
    challenge = Challenge()
    challenge.from_dict(**example_challenge_dict)
    assert challenge.flag == example_flag_dict


def test_program_flag_id(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.id == "699d3250-88f6-4294-92f6-de4aeaad4b94"


def test_program_flag_template(example_flag_dict, example_flag_template_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.template == example_flag_template_dict


def test_program_flag_name(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.name == "Welcome to Operator training"


def test_program_flag_challenge(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.challenge == "Orient yourself with the course sidebar"


def test_program_flag_context(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.context == "Training is"


def test_program_flag_resources(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.resources == {}


def test_program_flag_answer(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.answer == "Number(0)"


def test_program_flag_hints(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.hints == []


def test_program_flag_blocks(example_flag_dict):
    flag = Flag()
    flag.from_dict(**example_flag_dict)
    assert flag.blocks == {
        "Click the grey dots!": "Every time you",
        "Create your own training": "Did you know",
        "Features = Flags": "As you progress using",
        "Pink Badge": "Pink Badge is a self-paced"
    }


def test_program_flag_template_name(example_flag_template_dict):
    flag = FlagTemplate()
    flag.from_dict(**example_flag_template_dict)
    assert flag.name == "submit"


def test_program_flag_template_data(example_flag_template_dict):
    flag = FlagTemplate()
    flag.from_dict(**example_flag_template_dict)
    assert flag.data == []
