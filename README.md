# TWERPS DEMO

Welcome to **TWERPS** — *The World's Easiest Role-Playing System*!  
This project is a **LangChain Hello World** that demonstrates:

- Function calling (LangChain Tools)
- Retrieval-Augmented Generation (RAG)
- Stateful agent interaction
- A mini RPG game using OpenAI's GPT model

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

**Setup Your OpenAI API Key**  
Get your API key from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

Open the `config.py` file and paste your API key in the `OPENAI_API_KEY` variable like this:

```python
# config.py
OPENAI_API_KEY = "sk-REPLACE-WITH-YOUR-KEY"
```

**Important:** Do not share this key publicly.

---

**Run the Game**  
Run the main file from terminal:

```bash
python main.py
```
