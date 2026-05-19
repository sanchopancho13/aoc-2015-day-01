from solutions.part2 import get_basement_position

def test_should_handle_simplest_case():
    instructions = ")"
    position = get_basement_position(instructions)
    assert position == 1

def test_should_handle_complex_case():
    instructions = "()())"
    position = get_basement_position(instructions)
    assert position == 5
