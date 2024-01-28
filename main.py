from senha_api import API_KEY
import requests
import json

headers = { "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"

id_modelo = "gpt-3.5-turbo"

body_mensagem = {

    "model": f"{id_modelo}",
    "messages": [
      {
        "role": "user",
        "content": "Como eu posso começar a aprender Machine Learning?"
      }
    ]
}

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)

resposta_formatada = requisicao.json()

resposta_gpt = resposta_formatada["choices"][0]["message"]["content"]

print(resposta_gpt)