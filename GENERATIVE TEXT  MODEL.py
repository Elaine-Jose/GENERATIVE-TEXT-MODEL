from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()
def generate_text(topic):
    prompt = f"Write a detailed paragraph about {topic}.\n"
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]
    with torch.no_grad():
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_length=250,
            min_length=100,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.9,
            pad_token_id=tokenizer.eos_token_id  
        )
    result = tokenizer.decode(output[0], skip_special_tokens=True)
    return result[len(prompt):].strip()  

if __name__ == "__main__":
    topic = input("Enter a topic to generate a paragraph: ")
    print("\nGenerated Paragraph:\n")
    print(generate_text(topic))
