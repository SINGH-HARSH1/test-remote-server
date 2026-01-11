from fastmcp import FastMCP
import random
import json

# FastMCP server instance
mcp = FastMCP("Simple-Calculator-Server")

# Tool: Add two numbers
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers.
    Args:
        a (float): First number.
        b (float): Second number.
    Returns:
        float: The sum of the two numbers.
    """
    return a + b


# Tool: Generate a random number within a range
@mcp.tool()
def generate_random_number(min_value: float, max_value: float) -> float:
    """Generate a random number within a specified range.
    Args:
        min_value (float): Minimum value of the range.
        max_value (float): Maximum value of the range.
    Returns:
        float: A random number within the specified range.
    """
    return random.uniform(min_value, max_value)


#  Resource: Server Information
@mcp.resource("info://server")
def server_info() -> str:
    """Provide information about the server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A basic MCP server with math tools.",
        "tools": ["add", "generate_random_number"],
        "authors": ["Harsh Singh"],
    }
    return json.dumps(info, indent=2)


# Start the FastMCP server
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8080)

