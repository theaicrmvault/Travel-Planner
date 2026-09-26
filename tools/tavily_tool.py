from tavily import TavilyClient
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")
client = TavilyClient(api_key=api_key)


def search_results(query:str):
    response = client.search(
        query=query,
        max_results=5
    )

    results = []
    
    for i, result in enumerate(response.results,1):
        title = result.get("title", "No title")
        url = result.get("url", "")
        snippet = result.get("content", "")
        if snippet and len(snippet) > 300:
            snippet = snippet[:300].rsplit(' ', 1)[0] + '...'
        results.append(f"{i}. {title}\nURL: {url}\nSnippet: {snippet}\n")

    return results

