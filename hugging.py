from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "The future of ML is,"
output = generator(prompt, num_return_sequences=2, max_new_tokens=1, temperature=0.7)

print(output)


