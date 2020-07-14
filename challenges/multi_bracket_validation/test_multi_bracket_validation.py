from multi_bracket_validation import multi_bracket_validation
import pytest

@pytest.mark.parametrize('input,bool', [
    ('()', True),
    ('{}(){}', True),
    ('()[[Extra Characters]]', True),
    ('(){}[[]]', True),
    ('{}{Code}[Fellows](())', True),
    ('[({}]', False),
    ('(](', False),
    ('{(})', False),
    ('{', False),
    ('(', False),
    ('[', False),
    ('', False),
    ('m', False),
    ('{k', False),
    ('{(hey}', False)
])

def test_multi_bracket(input, bool):
    assert multi_bracket_validation(input) == bool