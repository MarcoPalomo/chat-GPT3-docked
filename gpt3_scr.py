import openai
import os

# Add your OpenAI API key
openai.api_key_path = ".env"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

generated_text = generate_text("Give a warm welcome to the people living in Aquitania Boyacá")
print(generated_text)
