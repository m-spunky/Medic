# [Medic AI: A Medical Chat Model Fine-tuned on LLaMA 3.2 Model using Medical Domain Knowledge]
## BY TEAM PHOENIX
<h5>1. Mayur Jadhav          2. Ameya Kalgutkar       3. Pratham Gupta</h5>

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 

## News
We uploaded both datasets on Drive, [MEDIC](https://drive.google.com/drive/folders/1XGu6hJOu3UDlIjeDBii4VRThOplNLcW_?usp=drive_link)
mail us on (nflix6528@gmail.com) for access.

## Overview
MedicAI is a next-generation AI doctor model that is based on the [LLaMA](https://huggingface.co/meta-llama/Llama-3.2-1B) model. The goal of this project is to provide patients with an intelligent and reliable healthcare companion that can answer their medical queries and provide them with personalized medical advice.

The MedicAI is an advanced language model that is specifically designed for medical applications. It has been trained on a large corpus of medical literature and has a deep understanding of medical terminology, procedures, and diagnoses. This model serves as the foundation for MedicAI, enabling it to analyze patients' symptoms and medical history, provide accurate diagnoses, and suggest appropriate treatment options.

The MedicAI model is designed to simulate a conversation between a doctor and a patient, using natural language processing (NLP) and machine learning techniques. Patients can interact with the MedicAI model through a chat interface, asking questions about their health, symptoms, or medical conditions. The model will then analyze the input and provide a response that is tailored to the patient's unique situation.

One of the key features of the MedicAI model is its ability to learn and adapt over time. As more patients interact with the model, it will continue to refine its responses and improve its accuracy. This means that patients can expect to receive increasingly personalized and accurate medical advice over time.


 ## Inference:
 use this Colab, run:
(https://colab.research.google.com/drive/1VYOdBSokimxUKFjJipPk3kSX3Ov3Xy49?usp=sharing)


## Examples:

Below are some example that describes the medical conversational task. 
 ```
 ### Patient: I've been experiencing a burning sensation in my chest and a sour taste in my mouth. What could be causing these symptoms?
 
 ### Medic: These symptoms are likely due to gastroesophageal reflux disease (GERD) or acidity. It is characterized by the backflow of acidic stomach contents into the esophagus.

 ### Patient: What usually causes acidity? I don't always eat spicy food, but it still happens.

 ### Medic: It can be caused by factors like eating spicy food, acidic drinks, and certain medications, and even it can happen without any known triggers.

 ### Patient: How can I prevent acidity from happening?

 ### Medic: To reduce acidity, limit dairy and sugar intake, and consume alkaline-rich foods.

 ### Patient:Are there any home remedies that might help?

 ### Medic: Honey and lemon can be beneficial, but consult a healthcare provider for personalized advice.

 ### Patient: Can I take any over-the-counter medicines for this?

 ### Medic: Omeprazole is often used to manage indigestion and heartburn. You may also want to consider taking ginger, which can aid digestion.
 ```
 

 ## Data and model:
 ### 1. Medic Training Dataset:
You can download the following training dataset
1. Data Scraped from Web : (https://drive.google.com/drive/folders/1XGu6hJOu3UDlIjeDBii4VRThOplNLcW_?usp=drive_link)
    For scraping engine refer (https://github.com/m-spunky/medic/tree/main/_MedicChatbot/scraper_engine)

2. Curated Dataset : (https://drive.google.com/file/d/1lyfqIwlLSClhgrCutWuEe_IACNq6XNUt/view)
 
 ### 2. Model Weights:
You can download the following model weights .bin file:
Medic Version 1.0: available on huggingface

 ### 3. Model Preparation & Fine Tuning:
Follow process of below Colab:
(https://colab.research.google.com/drive/1YkCdco1XTSTtcTmQUCws1mHE_Y0kCfb-?usp=sharing)

 ## Hyperparameters
 ```python
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        # num_train_epochs = 1,
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not is_bfloat16_supported(),
        bf16 = is_bfloat16_supported(),
        logging_steps = 1,
        optim = "adamw_8bit",
        weight_decay = 0.01,
        lr_scheduler_type = "linear",
        seed = 3407,
        output_dir = "outputs",
    )
 ```
 

## Reference

github : (https://huggingface.co/Net007/medic_phoenix)
```