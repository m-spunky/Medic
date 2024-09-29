from peft import PeftModel, PeftConfig
# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
config = PeftConfig.from_pretrained("Net007/medic_phoenix")
base_model = AutoModelForCausalLM.from_pretrained("unsloth/llama-3.2-3b-instruct-bnb-4bit")
model = PeftModel.from_pretrained(base_model, "Net007/medic_phoenix")
tokenizer = AutoTokenizer.from_pretrained("unsloth/Llama-3.2-3B-Instruct-bnb-4bit")

conversation_history = [] 
from transformers import TextStreamer

def chat_with_model(model, tokenizer,query):
  
  user_input = str(query)

  conversation_history.append({"role": "user", "content": user_input})

  inputs = tokenizer.apply_chat_template(
  conversation_history,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt"
  ).to("cpu")

  text_streamer = TextStreamer(tokenizer, skip_prompt=True)
  

  generated_output = ""
  for new_text in model.generate(
      input_ids=inputs,
      streamer=text_streamer,
      max_new_tokens=256,
      use_cache=True,
      temperature=1.5,
      min_p=0.1
  ):
      generated_output += str(new_text)

  conversation_history.append({"role": "assistant", "content": generated_output.strip()})

chat_with_model(model, tokenizer,"provide some home remedies for jaundice")

# !pip install git+https://github.com/huggingface/accelerate.git
# !pip install git+https://github.com/huggingface/transformers.git
# !pip install bitsandbytes