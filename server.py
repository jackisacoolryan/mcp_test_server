from fastmcp import MCP
import os

mcp = MCP("example_mcp")

# Load dataset from files in the data directory
base_dir = os.path.join(os.path.dirname(__file__), 'data')

def load_docs():
    docs = []
    for filename in os.listdir(base_dir):
        if filename.endswith('.txt'):
            path = os.path.join(base_dir, filename)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            doc_id = os.path.splitext(filename)[0]
            title = doc_id.replace('_', ' ').title()
            docs.append({
                'id': doc_id,
                'title': title,
                'text': text,
                'url': f'https://example.com/{doc_id}'
            })
    return docs

DATA = load_docs()

@mcp.tool
def search(query: str) -> list:
    """Return a list of documents matching the query."""
    query_lower = query.lower()
    results = []
    for doc in DATA:
        idx = doc['text'].lower().find(query_lower)
        if idx != -1:
            start = max(0, idx - 50)
            end = min(len(doc['text']), idx + 150)
            snippet = doc['text'][start:end]
            results.append({
                'id': doc['id'],
                'title': doc['title'],
                'text': snippet,
                'url': doc['url']
            })
    return results

@mcp.tool
def fetch(doc_id: str) -> dict:
    """Retrieve the full document content for the given identifier."""
    for doc in DATA:
        if doc['id'] == doc_id:
            return doc
    return {'id': doc_id, 'title': '', 'text': '', 'url': '', 'metadata': {}}

if __name__ == '__main__':
    port = int(os.getenv('PORT', '8000'))
    mcp.run(transport='http', host='0.0.0.0', port=port, path='/mcp')
