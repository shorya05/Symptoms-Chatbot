from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def main():
    model_path = "./lora-finetuned"
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    model.eval()
    if torch.cuda.is_available():
        model.to("cuda")

    print("Model loaded. Type your questions below (or 'exit' to quit):")

    while True:
        user_input = input("\nEnter your question (or 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Exiting...")
            break

        prompt = f"Instruction: {user_input}\nAnswer:"
        inputs = tokenizer(prompt, return_tensors="pt")
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k,v in inputs.items()}

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=150,
                do_sample=True,
                top_p=0.9,
                temperature=0.6,
                repetition_penalty=1.5,
                no_repeat_ngram_size=3,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )

        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Extract answer text after the prompt
        answer = generated_text[len(prompt):].strip()

        print("\nResponse:\n" + answer + "\n")

if __name__ == "__main__":
    main()
