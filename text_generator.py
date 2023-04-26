import requests
import const as c


def generate_card_text(reason, person, likes="", tones=""):
    print("Generating Card Message...")
    url = "https://api.openai.com/v1/chat/completions"

    prompt = f"write a creative inside message of a maximum of 50 words for {reason}, to {person}"
    if likes:
        prompt = prompt + f", who likes {likes}"
    if tones:
        prompt = f"write a creative {tones} inside message of a maximum of 50 words for {reason}, to {person}, who " \
                 f"likes {likes}. "

    json = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
    }
    headers = {
        "Accept": "application/json",
        "Content-type": "application/json",
        "Authorization": "Bearer " + c.OPENAI_API_KEY,
    }
    response = requests.post(
        url,
        headers=headers,
        json=json,
        timeout=200,
    )

    if response.json().get("error"):
        return response.json().get("error")["message"]

    return response.json()["choices"][0]["message"]["content"]
