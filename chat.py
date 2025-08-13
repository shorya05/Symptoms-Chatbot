# from app.model.lora_inference import generate_answer

# def get_response(question: str) -> str:
#     # You can add preprocessing here if needed
#     answer = generate_answer(question)
#     return answer


def get_response(question: str) -> str:
    # TODO: Replace with your chatbot logic, e.g. call a trained model or external API
    if "doctor" in question.lower():
        return "You should see a doctor if your abdominal pain is severe, persistent, or accompanied by other symptoms like fever or vomiting."
    elif "risk factors" in question.lower():
        return "Common risk factors include infection, injury, digestive issues, or chronic diseases."
    else:
        return "I'm sorry, I don't have information on that topic yet."

# import json
# import os

# # Path to your JSON file
# DATA_FILE = r"D:\Symptoms Chatbot\backend\app\api\chatbot_data.json"

# # Load chatbot data
# def load_chatbot_data():
#     if not os.path.exists(DATA_FILE):
#         raise FileNotFoundError(f"Chatbot data file not found at {DATA_FILE}")
    
#     with open(DATA_FILE, "r", encoding="utf-8") as f:
#         return json.load(f)

# chatbot_data = load_chatbot_data()

# # Get chatbot response
# def get_response(user_input: str, name: str = None, age: int = None, gender: str = None):
#     user_input_lower = user_input.strip().lower()

#     for entry in chatbot_data:
#         if entry["instruction"].lower() == user_input_lower:
#             base_response = entry["response"]

#             # Add extra context with name, age, and gender
#             if name or age is not None or gender:
#                 return (
#                     f"Hello {name if name else 'User'}, based on age {age if age is not None else 'N/A'}"
#                     f" and gender {gender if gender else 'N/A'}, here’s some advice: {base_response}"
#                 )
#             return base_response

#     # Default fallback if no match found
#     return (
#         f"Hello {name if name else 'User'}, please provide more details such as location, duration, "
#         f"severity, and other symptoms. 🚨 Seek urgent medical attention if you have sudden severe pain, "
#         f"chest pain, difficulty breathing, persistent vomiting, or blood in stool/vomit."
#     )



