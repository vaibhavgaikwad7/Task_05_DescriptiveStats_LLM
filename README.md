# 🧠 Task_05_DescriptiveStats_LLM

This research task explores how well Large Language Models (LLMs) like ChatGPT interpret and respond to natural language questions grounded in real sports data. For this task, we use the **2022–2023 Syracuse University Men’s Basketball** statistics and evaluate the accuracy and reasoning ability of LLMs in extracting insights.

---

## 📂 Project Structure

.
├── data/ # Local data (not pushed to GitHub)
│ └── syracuse_mbb_2023_core_stats.csv
├── prompts/ # LLM question-answer experiments
│ └── llm_interactions.md
├── scripts/ # Code to analyze and validate data
│ └── stats_summary.py
├── .gitignore
├── README.md



---

## 📊 Dataset

- **Name:** Syracuse Men’s Basketball Stats (2022–2023)
- **Source:** [Cuse.com Team Stats](https://cuse.com/sports/mens-basketball/stats/2022-23)
- **Fields:** Player, Games Played, Points, Rebounds, Assists, Steals, etc.

> **Note:** The actual dataset CSV file is not committed to GitHub. Please place it in the `data/` directory manually.

---

## 🔍 How to Run the Script

To generate basic descriptive statistics using pandas:

```bash
python scripts/stats_summary.py
```

## 💬 Prompts & Validation
All LLM questions and their responses are stored in:

prompts/llm_interactions.md


Each prompt is structured as:

Q: The natural language question.

LLM Answer: The LLM’s raw output.

Validation: Manual evaluation of correctness based on actual data.

✨ Example Prompts
Q: How many total games did Syracuse play in the 2022–23 season?
LLM Answer: 32 games
Validation: ✅ Matches breakdown (17 wins + 15 losses = 32)

Q: Who had the highest scoring average?
LLM Answer: Joe Girard III
Validation: ✅ Correct. He led with 16.4 PPG over 32 games.

📌 Goal of This Task
Evaluate LLMs' ability to perform reasoning on real-world structured data.

Practice prompt engineering to improve model responses.

Document failures and successes during LLM interaction.

📮 Submission Guidelines
Repository: ✅ Public

Includes:

 Scripts

 Prompt Logs

 README

Dataset excluded from version control (data/ folder is .gitignored)

👨‍💻 Author
Vaibhav Gaikwad
