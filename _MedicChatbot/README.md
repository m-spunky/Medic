# MedicAI: A Retrieval-Augmented Fine-Tuning (RAFT) System for Medical Question Answering

## Overview

The **Medic Model** is a specialized system designed for accurate and efficient medical question answering. Our approach combines **Retrieval-Augmented Fine-Tuning (RAFT)** with the state-of-the-art **Retrieval-Augmented Generation (RAG)** technique. This enables users to receive highly accurate, contextually curated responses based on both fine-tuned models and retrieval from relevant data sources.

## Key Components

### 1. Data Collection and Preparation
Our team, **Phoenix**, sourced the medical data from web scraping various trusted medical resources, including **TATA's 1MG** and other publicly available websites. The scraped data was saved in `.xlsx` format and then processed to generate **question-answer (QA) pairs**. These QA pairs were compiled into a large dataset in **JSON format** for further processing.

### 2. Fine-Tuning the Model
We fine-tuned the model using the **QLoRA** approach and the **LLaMA 3.2** architecture. This involved running multiple experiments with different hyperparameter combinations to find the optimal setup for our use case. The final **adapter model** is hosted on **Hugging Face** for easy accessibility and deployment.

#### Tools and Techniques:
- **Fine-Tuning Framework**: QLoRA
- **Model Architecture**: LLaMA 3.2
- **Hyperparameter Optimization**: Experimented with various combinations to achieve the best performance.

### 3. Retrieval-Augmented Generation (RAG)
The **RAG engine** is used alongside the fine-tuned model to deliver the best possible results. It leverages embeddings stored in a **FAISS vectorstore** for fast and efficient retrieval. We employed **two large language models (LLMs)**:
- **GPT-4o**: Known for its state-of-the-art performance.
- **Gemini**: A cost-efficient alternative that provides competitive accuracy at a lower cost.

#### RAG Pipeline:
- Dataset split into manageable chunks.
- Embeddings generated and stored in **FAISS vectorstore**.
- Curated prompts ensure precise retrieval from the stored data.

### 4. Combined Approach for Accurate Responses
By integrating **fine-tuning** (using RAFT) with **RAG**, we created a robust **manager LLM** that curates responses leveraging both techniques. This results in accurate and contextually relevant answers for medical questions.

## How It Works
1. **Data Retrieval**: The system fetches the most relevant pieces of information from the FAISS vectorstore.
2. **Curated Prompting**: The manager LLM constructs a detailed prompt using both retrieved data and fine-tuned model knowledge.
3. **Response Generation**: The user receives a highly accurate and contextually correct answer, informed by both RAFT and RAG techniques.

## Use Cases
- **Medical Question Answering**: Providing users with accurate responses to complex medical queries.
- **Healthcare Professionals**: Assisting doctors, nurses, and pharmacists with up-to-date and precise medical information.
- **Telemedicine Platforms**: Enhancing patient interaction by delivering quick and reliable medical information.

## Deployment and Hosting
- **Fine-Tuned Adapter Model**: Hosted on [Hugging Face](https://huggingface.co/).
- **RAG Engine**: Runs on both **GPT-4o** and **Gemini**, providing flexibility in balancing performance and cost.

## Future Work
- Expanding the dataset with more diverse medical sources.
- Further optimization of hyperparameters for enhanced accuracy.
- Integrating more cost-efficient LLMs to reduce operational costs.



![image](https://github.com/user-attachments/assets/51ac44ea-3fd7-42ca-816b-8fefb2733d0c)

