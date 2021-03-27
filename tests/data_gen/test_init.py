"""Test __init__.py."""

import toml

import data_gen


def test_version() -> None:
    """Test version."""
    path = 'pyproject.toml'
    with open(path, 'r') as f:
        d = toml.load(f)

    version = data_gen.__version__
    assert version == d['tool']['poetry']['version']
