from duckduckgo_search import DDGS


def get_live_news(sport):
    query = f"{sport} latest tournament winners recent sports news"

    results_text = []

    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=3)

            for result in results:
                title = result.get("title", "")
                body = result.get("body", "")
                results_text.append(f"{title}\n{body}")

    except Exception as e:
        return f"Web search failed: {e}"

    return "\n\n".join(results_text)