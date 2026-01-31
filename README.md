This project lets you predict using a Machine Learning model via natural language.
An AI agent understands your request and automatically runs the ML model for you.

🛠 Requirements

1.Python 3.10+

2.Git

3.Groq API Key

📥 Setup (From Scratch)
1️⃣ Clone the repository
git clone https://github.com/<username>/<repo-name>.git
cd <repo-name>

2️⃣ Create virtual environment
python -m venv .venv


Activate it:

Windows

.venv\Scripts\activate


3️⃣ Install dependencies
pip install -r requirements.txt


(or uv sync if using uv)

4️⃣ Set Groq API Key
Create a .env file:

GROQ_API_KEY=your_groq_api_key_here

▶️ Run the Project
python main.py

💬 Example Input
Predict using these values: 45, 78, 23, 56, 89, 12, 67, 34

📤 Output
Predicted output: <value>
