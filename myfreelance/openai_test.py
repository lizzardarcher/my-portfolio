from openai import OpenAI

client = OpenAI(api_key='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')


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a product description and seed words, and your task is to generate product names."
    },
    {
      "role": "user",
      "content": "Product description: A home milkshake maker\n    Seed words: fast, healthy, compact."
    }
  ],
  temperature=0.8,
  max_tokens=64,
  top_p=1
)

text = str(response.choices[0].message)

print(text)