import pytest
from flabpal import blue, yellow, green, red, gray, grey, orange, pink, brown, purple
from matplotlib.colors import is_color_like


@pytest.mark.parametrize('color', [blue, yellow, green, red, gray, grey, orange, pink, brown, purple])
def test_valid_color(color):
    assert is_color_like(color)


@pytest.mark.parametrize('color', [blue, yellow, green, red, gray, grey, orange, pink, brown, purple])
def test_repr(color):
    r = repr(color)
    print(r)
    assert r != '(0, 0, 0)'
    assert r != '(0.0, 0.0, 0.0)'
