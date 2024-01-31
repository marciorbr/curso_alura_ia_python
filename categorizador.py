from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = 'gpt-4'


def categorizar_produto(nome_produto, lista_categorias_validas):
        prompt_sistema = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.

                # Lista de Categorias Válidas
                {lista_categorias_validas.split(",")}

                # Formato da Saída
                Produto: Nome do Produto
                Categoria: apresente a categoria do produto

                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Categoria: Eletrônicos Verdes
        """

        """
        O que esse categorizador vai fazer? Assumiremos que temos o seguinte problema: 
        receberemos um produto e precisaremos informar a qual categoria de produtos ele pertence.
        Para isso, usaremos IA generativa para analisar o contexto e definir qual categoria ele pode ser melhor associado.
        """
        resposta = cliente.chat.completions.create(
                messages=[
                        {
                                "role":"system",
                                "content": prompt_sistema
                        },
                        {
                                "role" : "user",
                                "content": nome_produto
                        }
                ],
                model=modelo,
                temperature=0,
                max_tokens=200,
        )

        return resposta.choices[0].message.content

categorias_validas = input("Digite as categorias válidas: ")

while(True):
    nome_produto = input("Digite o nome de um produto: ")
    resposta = categorizar_produto(nome_produto, categorias_validas)
    print (resposta)