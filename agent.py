from tools.search_tool import search_papers
from tools.summarize_tool import summarize_text
from tools.storage_tool import save_results
from memory.memory_store import AgentMemory
from planner import create_plan


class Agent:

    def __init__(self):
        self.memory = AgentMemory()

    def run(self, goal: str):

        plan = create_plan(goal)

        papers = search_papers("agriculture AI")

        results = []

        for paper in papers:
            summary = summarize_text(paper["content"])

            record = {
                "title": paper["title"],
                "summary": summary,
                "link": paper["link"]
            }

            results.append(record)
            self.memory.add(record)

        file_path = save_results(results)

        return {
            "goal": goal,
            "steps_executed": plan,
            "saved_to": file_path,
            "results": results
        }
