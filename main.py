
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


import pickle
import numpy as np

MODEL_PATH = "model.pkl"


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@tool
def predict_with_model(features: str) -> str:
    """
    Predict using the uploaded ML model.
    Input should be comma-separated numeric values.
    """
    try:
        values = [float(x.strip()) for x in features.split(",")]
        X = np.array(values).reshape(1, -1)
        prediction = model.predict(X)
        return f"Predicted output: {prediction[0]}"
    except Exception as e:
        return f"Prediction failed: {str(e)}"


llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
    api_key=os.environ["GROQ_API_KEY"]
)
agent = create_agent(llm, tools=[predict_with_model],)


response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "Predict using these values: 45, 78, 23, 56, 89, 12, 67, 34"
        }
    ]
})

print(response["messages"].content)




