from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

"""
O que esse categorizador vai fazer? Assumiremos que temos o seguinte problema: 
receberemos um produto e precisaremos informar a qual categoria de produtos ele pertence.
Para isso, usaremos IA generativa para analisar o contexto e definir qual categoria ele pode ser melhor associado.
"""

resposta = cliente.chat.completions.create(
        messages=[
                {
                        "role":"system",
                        "content": """
                        Classifique o produto abaixo em uma das categorias: Higiene 
                        Pessoal, Moda ou Casa e de uma descrição da categoria.
                        """
                },
                {
                        "role" : "user",
                        "content": """
                        Escova de dentes de bambu
                        """
                }
        ],
        model="gpt-4",
        temperature=0,
        max_tokens=200,
        n = 2,
)

[print(resposta.choices[cont].message.content) for cont in range(0, len(resposta.choices))]