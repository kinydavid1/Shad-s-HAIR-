import requests

API_KEY = "ton_api_key_ici"  # 🔁 Remplace par ta vraie clé
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def poser_question(prompt):
    data = {
        "model": "gpt-3.5-turbo",  # ou gpt-4 si ton compte le permet
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# Interface utilisateur dans le terminal
while True:
    question = input("Toi : ")
    if question.lower() in ["exit", "quit"]:
        break
    reponse = poser_question(question)
    print("\nChatGPT : " + reponse + "\n")
