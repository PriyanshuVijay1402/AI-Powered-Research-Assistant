# 🔬 AI-Powered Personal Research Assistant

This project is a multi-agent AI assistant built with [CrewAI](https://github.com/joaomdmoura/crewAI), capable of interpreting user queries, searching arXiv, summarizing papers, and formatting a structured research report.

## 🚀 Features

- Understands research queries
- Searches academic papers via arXiv
- Summarizes key findings
- Formats a clean research report

## 🛠️ Tech Stack

- Python
- CrewAI (multi-agent framework)
- LangChain (LLM integration)
- OpenRouter API (Mistral-7B)
- arXiv API

## 📦 Setup

```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
python main.py

