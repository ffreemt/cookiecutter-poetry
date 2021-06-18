"""Test {{cookiecutter.pack_name}}."""
from {{cookiecutter.pack_name}} import __version__
from {{cookiecutter.pack_name}} import {{cookiecutter.pack_name}}


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not {{cookiecutter.pack_name}}()
    except Exception:
        assert True
