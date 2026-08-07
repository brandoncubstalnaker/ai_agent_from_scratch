import pytest
from agent.tools import calculator, TOOL_REGISTRY

def test_calculator_valid():
    assert calculator("2 + 2") == "4"
    assert calculator("10 * 5") == "50"

def test_calculator_invalid_chars():
    res = calculator("import os")
    assert "Error: Invalid characters" in res

def test_tool_registry_contains_calculator():
    assert "calculator" in TOOL_REGISTRY
