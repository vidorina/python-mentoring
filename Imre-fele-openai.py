import openai
import re
import time

openai.api_key = "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"

# ez itt a "sentiment", az alapviselkedese az llm-nek ;)
sIntro = "Te egy nagyon kreatív mesemondó vagy, es minden kérdésre adott válaszod egy 3-4 mondatos csattanós történet, természetesen válaszolsz is a történettel a kérdésre."

# ------------------------------------------------
response = openai.ChatCompletion.create(
  model = "gpt-4",
  messages = [
    { 'role': 'system', 'content': sIntro },
    { 'role': 'user', 'content': 'milyen időjárás várható az irodában holnap?' }
  ],
  max_tokens = 2000
)

sResponse = response.choices[0].message.content
print( f'-------------------------------------------\ntotal used tokens in gpt is {response.usage.total_tokens}' )
print( f'answer -> {sResponse}\n' )