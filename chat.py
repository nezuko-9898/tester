from transformers import pipeline

# Load a pre-trained text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Define a prompt
prompt = "hello,"

# Generate text
output = generator(
    prompt,
    max_length=100,      # total number of tokens in output
    num_return_sequences=1,  # how many completions to generate
    temperature=0.7,     # creativity level (higher = more random)
    top_p=0.9,           # nucleus sampling
    do_sample=True       # enables stochastic sampling
)

# Display the generated text
print(output[0]["generated_text"])
