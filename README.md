# Example MCP Server

This repository contains a minimal MCP server implementation using the FastMCP library. It exposes two tools required by the OpenAI MCP protocol: **search** and **fetch**.

## Running Locally

To run this server locally with Python 3 and FastMCP installed:

```bash
pip install fastmcp
python server.py
```

The server will start on `http://localhost:8000/mcp` by default. Use the `search` tool to find documents by keyword and `fetch` to retrieve full document contents.

## Dataset

The server uses simple text files under the `data/` directory as its data source. Add additional `.txt` files to `data/` to extend the dataset. Each file name (without extension) becomes the document ID and title (underscores replaced with spaces).

## Deployment on Render

1. Create a new Web Service on Render and link this GitHub repository.
2. Set **Build Command** to `pip install -r requirements.txt`.
3. Set **Start Command** to `python server.py`.
4. Ensure that FastMCP can connect to the internet to install dependencies.
5. Expose port 8000.

Once deployed, the MCP endpoint will be available at `https://<your-service>.onrender.com/mcp`.
