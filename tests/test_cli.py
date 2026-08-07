from agent.tools import TOOL_REGISTRY

def test_cli_tool_registry_access():
    assert "calculator" in TOOL_REGISTRY
    assert TOOL_REGISTRY["calculator"]("25 * 4") == "100"
