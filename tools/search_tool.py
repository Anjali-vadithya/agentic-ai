import requests
import xml.etree.ElementTree as ET


def search_papers(query, top_k=3):
    url = f"http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={top_k}"

    response = requests.get(url)
    root = ET.fromstring(response.content)

    papers = []

    for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
        title = entry.find("{http://www.w3.org/2005/Atom}title").text
        summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
        link = entry.find("{http://www.w3.org/2005/Atom}id").text

        papers.append({
            "title": title.strip(),
            "content": summary.strip(),
            "link": link
        })

    return papers
