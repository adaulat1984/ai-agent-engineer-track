# AI Agentic Engineer track

One-hour-a-day study log for a C# / .NET developer moving into building AI agents.

**Goal:** ship one public agent with tools, memory, RAG, a simple eval, and MCP.

**Today:** Day 1 of 180. See [PROGRESS.md](PROGRESS.md).

## How a day works

Each folder under `daily/` is one session of at most 60 minutes:

1. **20 min** — read the named course module.
2. **35 min** — finish the single `exercise.py` in that day's folder.
3. **5 min** — write `notes.md` in your own words and update `PROGRESS.md`.

Reply `done` plus the script output in the coaching chat to unlock the next day.

## Phases

| Phase | Weight | What "done" means |
|---|---|---|
| 1. Python transfer | 15% | Files, dicts, HTTP, JSON, SQL, and Python OOP syntax |
| 2. How LLMs work | 15% | Transformers, pre-training, fine-tuning, LoRA, RLHF, ReAct |
| 3. Build an agent yourself | 25% | An agent loop (Goals, Actions, Memory, Environment), tools, memory, safety |
| 4. RAG and multi-agent | 35% | LangChain, vector search, LangGraph, CrewAI, MCP, capstone |
| 5. Portfolio | 10% | One runnable agent and a short design note |

Courses, in order: [Python for Everybody](https://www.coursera.org/specializations/python), [Generative AI with Large Language Models](https://www.coursera.org/learn/generative-ai-with-llms), [AI Agent Developer](https://www.coursera.org/specializations/ai-agents), [IBM RAG and Agentic AI](https://www.coursera.org/professional-certificates/ibm-rag-and-agentic-ai).

## Day 1

```powershell
cd daily/day-001
python exercise.py
```

Python 3.13 is enough. Fill the three TODOs in `exercise.py`, then record both runs (a name, and an empty name) in `notes.md`.

## Layout

```text
PROGRESS.md          current day, phase, and percent
daily/day-001/       today's notes and starter script
```
