# 🤖 CrewAI News Agent

A multi-agent AI system built with [CrewAI](https://www.crewai.com/) and Google Gemini that researches any topic and writes a well-structured report automatically.

## 🚀 How It Works

This project uses two AI agents working together:

| Agent | Role |
|-------|------|
| 🔍 **Researcher** | Gathers detailed information on the given topic |
| ✍️ **Writer** | Turns the research into a clear, readable report |

The agents run sequentially — the Writer receives the Researcher's output as context and produces a final report saved as `report.txt`.

## 📁 Project Structure

```
crewai-news-project/
├── main.py           # Main script - runs the AI agents
├── requirements.txt  # Python dependencies
├── .env              # Your API key (never commit this!)
├── .gitignore        # Ignores .env, venv, cache files
└── README.md         # This file
```

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/nandukl/crewai-news-agent.git
cd crewai-news-agent
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment
```bash
# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up your API key

Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

> Get your free API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## ▶️ Running the Project

```bash
# Make sure venv is activated first!
.\venv\Scripts\activate

python main.py
```

You'll be prompted to enter a topic:
```
Enter a topic to research: Artificial Intelligence
```

The agents will then research and write a report. The final output is saved as `report.txt` in the project folder.

## 🛠️ Built With

- [CrewAI](https://www.crewai.com/) — Multi-agent AI framework
- [Google Gemini 2.5 Flash](https://deepmind.google/technologies/gemini/) — LLM powering the agents
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Loads environment variables from `.env`

## ⚠️ Security Note

Never commit your `.env` file to version control. The `.gitignore` in this project already excludes it. Always keep your API keys private.
