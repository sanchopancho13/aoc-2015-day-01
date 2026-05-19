from solutions.part1 import get_floor

def test_should_handle_empty_string():
    instructions = ""
    floor = get_floor(instructions)
    assert floor == 0

def test_should_stay_for_same_up_and_down():
    instructions = "()"
    floor = get_floor(instructions)
    assert floor == 0

def test_should_move_to_correct_floor():
    instructions = ")())())"
    floor = get_floor(instructions)
    assert floor == -3
