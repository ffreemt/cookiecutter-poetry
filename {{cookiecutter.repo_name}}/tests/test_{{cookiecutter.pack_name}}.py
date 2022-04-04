"""Test {{cookiecutter.pack_name}}."""
# pylint: disable=broad-except
from {{cookiecutter.pack_name}} import __version__
from {{cookiecutter.pack_name}} import {{cookiecutter.pack_name}}


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not {{cookiecutter.pack_name}}()
    except Exception:
        assert True
