# import torch
# from transformers import GPTNeoForCausalLM, GPT2Tokenizer
# from peft import get_peft_model, LoraConfig, TaskType
# from datasets import load_dataset
# from transformers import TrainingArguments, Trainer

# def main():
#     model_name = "EleutherAI/gpt-neo-125m"

#     # Load tokenizer and model
#     tokenizer = GPT2Tokenizer.from_pretrained(model_name)
#     model = GPTNeoForCausalLM.from_pretrained(
#         model_name,
#         device_map="auto",
#         torch_dtype=torch.float16,
#         low_cpu_mem_usage=True,
#     )

#     # Add pad token if missing (GPT2 tokenizer doesn't have it by default)
#     if tokenizer.pad_token is None:
#         tokenizer.pad_token = tokenizer.eos_token
#         model.config.pad_token_id = tokenizer.eos_token_id

#     # LoRA config
#     peft_config = LoraConfig(
#         task_type=TaskType.CAUSAL_LM,
#         inference_mode=False,
#         r=16,
#         lora_alpha=32,
#         lora_dropout=0.1,
#     )
#     model = get_peft_model(model, peft_config)
# # 
#     # Load dataset - make sure this path is correct relative to your script
#     # dataset = load_dataset("json", data_files="../data/fine_tune_dataset.jsonl")["train"]
#     dataset = load_dataset("json", data_files="data/fine_tune_dataset.jsonl")["train"]


#     def preprocess(example):
#         prompt = f"Question: {example['instruction']}\nAnswer: {example['response']}\n"
#         inputs = tokenizer(prompt, truncation=True, max_length=512, padding="max_length")
#         inputs["labels"] = inputs["input_ids"].copy()
#         return inputs

#     dataset = dataset.map(preprocess, remove_columns=dataset.column_names)

#     training_args = TrainingArguments(
#         output_dir="./lora-finetuned",
#         per_device_train_batch_size=2,
#         num_train_epochs=3,
#         learning_rate=2e-4,
#         logging_steps=10,
#         save_steps=100,
#         save_total_limit=2,
#         fp16=True,
#         # evaluation_strategy="no",  # or "steps" if you want eval
#     )

#     trainer = Trainer(
#         model=model,
#         args=training_args,
#         train_dataset=dataset,
#         tokenizer=tokenizer,
#     )

#     trainer.train()
#     trainer.save_model("./lora-finetuned")

# if __name__ == "__main__":
#     main()



import torch
from transformers import GPTNeoForCausalLM, GPT2Tokenizer
from peft import get_peft_model, LoraConfig, TaskType
from datasets import load_dataset
from transformers import TrainingArguments, Trainer

def main():
    model_name = "EleutherAI/gpt-neo-125m"

    # Load tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPTNeoForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True,
    )

    # Add pad token if missing (GPT2 tokenizer doesn't have it by default)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        model.config.pad_token_id = tokenizer.eos_token_id

    # LoRA config
    peft_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        inference_mode=False,
        r=16,
        lora_alpha=32,
        lora_dropout=0.1,
    )
    model = get_peft_model(model, peft_config)

    # Correct relative path to your dataset file
    data_file_path = "../data/fine_tune_dataset.jsonl"

    # Load dataset from JSONL file
    dataset = load_dataset("json", data_files=data_file_path)["train"]
    print(f"Loaded {len(dataset)} samples from {data_file_path}")

    # Preprocess the data for training
    def preprocess(example):
        prompt = f"Question: {example['instruction']}\nAnswer: {example['response']}\n"
        inputs = tokenizer(prompt, truncation=True, max_length=512, padding="max_length")
        inputs["labels"] = inputs["input_ids"].copy()
        return inputs

    dataset = dataset.map(preprocess, remove_columns=dataset.column_names)

    training_args = TrainingArguments(
        output_dir="./lora-finetuned",
        per_device_train_batch_size=2,
        num_train_epochs=3,
        learning_rate=2e-4,
        logging_steps=10,
        save_steps=100,
        save_total_limit=2,
        fp16=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
    )

    trainer.train()
    trainer.save_model("./lora-finetuned")

if __name__ == "__main__":
    main()
