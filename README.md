# curso_alura_ia_python
Repositório para utilização no curso da alura GPT e Python

## Os principais parâmetros, do modo chat, têm a seguinte funcionalidade:
* Mode (modo): define como você deseja que o modelo se comporte, e cada um dos modos tem seu próprio contexto e aplicação específicos. Atualmente, temos os modos:
1. chat: usado para criar interações de conversa com o modelo;
2. complete: uma forma de solicitar ao modelo que complete um texto ou código fornecido;
3. edit: projetado para auxiliar na edição e revisão de textos.

## Parâmetros Openai
### Maximum length
*  Limita o tamanho da resposta gerada pelo modelo. Você pode definir um número máximo de tokens (unidades de texto) que a resposta deve conter. Isso é útil para evitar que a saída seja muito longa e se ajustar às restrições do contexto em que o modelo está sendo usado. (tokens são contabilizados com dados de entradas e saídas)
### Temperature
* Controla a aleatoriedade da saída gerada pelo modelo. Valores mais altos de temperatura (por exemplo, 0,8) produzem saídas mais criativas e imprevisíveis, enquanto valores mais baixos (por exemplo, 0,2) geram saídas mais determinísticas e seguras.
### Stop sequence
* São tokens que indicam ao modelo que ele deve parar de gerar texto. Isso é útil para controlar quando e onde a saída deve terminar.

Os últimos três parâmetros são o "Top P", o "Frequency Penalty" (penalidade de frequência) e o "Presence Penalty" (penalidade de presença).

O que eles fazem é nos ajudar a entender qual é o espaço de criatividade que será observado pelo OpenAI na hora de compor uma frase. Isso trabalha em conjunto com a temperatura.

### Top P
* define qual será o universo de elementos que nossa IA observará, ou seja, os termos mais próximos. Se o valor for 1, ele observará todo o espaço amostral de palavras. Se for 0.5, observará apenas metade. E, se for 0, não terá nenhum espaço para observação.

Os dois parâmetros Frequency e Presence Penalty, trabalham de forma semelhante entre si, sendo que o primeiro evita a repetição de palavras e o segundo evita a repetição de ideias.

### Frequency penalty
* Controla a frequência com que o modelo repete palavras ou frases semelhantes. Valores mais altos desencorajam o modelo a repetir as mesmas palavras ou estruturas, tornando a saída mais diversificada.
### Presence penalty 
* Influencia a diversidade da saída, mas de maneira diferente do frequency penalty. Valores mais altos incentivam o modelo a explorar mais possibilidades e produzir respostas menos óbvias e mais criativas.

Se alterarmos esses parâmetros, colocando a Frequency Penalty em 2, que é o valor máximo e a Presence Penalty para 2 também, agora teremos alguma diretriz para o OpenAI para que ela não repita termos e não repita encadeamentos de ideias.

## Assistentes de IA
* Um Assistente possui instruções e pode usar modelos, ferramentas e conhecimento para responder a consultas de usuários. Já as threads são responsáveis por garantir que em um fluxo de troca de mensagens com os assistentes, seja possível acessar o histórico da troca de mensagens.