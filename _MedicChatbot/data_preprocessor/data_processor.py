# !pip -q install langchain tiktoken replicate

import os

import json
import textwrap
import torch

os.environ["REPLICATE_API_TOKEN"] = ""


from langchain.llms import Replicate
from langchain import PromptTemplate, LLMChain

llm = Replicate(
    model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",
    input={"temperature": 0.75,
           "max_length": 500,
           "top_p": 1},
)


B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
DEFAULT_SYSTEM_PROMPT = """
Generate a conversational data list based on the provided JSON data about a disease. Assume the role of a medical assistant, and the user will be a patient describing their symptoms and asking for causes, prevention, remedies, and general medicines. Use natural, conversational language to answer the questions. Follow this structure: - The patient starts by describing their symptoms. - The assistant responds by identifying the disease and explaining it. - The patient then asks about the causes of the disease. - The assistant explains possible causes in detail. - The patient asks for preventive measures. - The assistant provides preventive tips. - The patient asks for home remedies. - The assistant gives a few home remedies. - The patient asks for any over-the-counter medicines. - The assistant suggests common OTC medicines. 
response should be in this format : [[ { "from": "human", "value": "I've been experiencing a burning sensation in my chest and a sour taste in my mouth. What could be causing these symptoms?" }, { "from": "gpt", "value": "Based on your symptoms, it sounds like you might be experiencing acidity. This is a common condition where excess stomach acid can cause heartburn, which is the burning sensation you're feeling, along with regurgitation, leading to a sour taste in your mouth. Acidity can be triggered by eating spicy or oily foods, stress, or even lying down too soon after eating. It may also be caused by conditions like gastroesophageal reflux disease (GERD)." },]. and keep gpt value short and crisp like of per 200 gpt tokens.
[json data]
"""


def get_prompt(instruction, new_system_prompt=DEFAULT_SYSTEM_PROMPT ):
    SYSTEM_PROMPT = B_SYS + new_system_prompt + E_SYS
    prompt_template =  B_INST + SYSTEM_PROMPT + instruction + E_INST
    return prompt_template

def parse_text(text):
        wrapped_text = textwrap.fill(text, width=100)
        print(wrapped_text +'\n\n')
        return wrapped_text


system_prompt = "You are an advanced assistant that excels at Medical Information. "
instruction = DEFAULT_SYSTEM_PROMPT
template = get_prompt(instruction, system_prompt)
print(template)

prompt = PromptTemplate(template=template, input_variables=["text"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

# example
JSONDATA = [
  {
    "title": "Acidity",
    "description about disease": "Acidity is one of the most common ailments that almost everyone experiences once in their lifetimes. In simple terms, it is a condition that causes excess acid production in the stomach. This not only causes discomfort in the stomach but also leads to other symptoms, such as a sour taste in the mouth, difficulty swallowing, andindigestion.There are numerous causes of acidity, right from poor eating habits and excessive stress to the use of certain medications. Moreover, lifestyle factors, such as smoking and consuming foods loaded with oil, fats, and spices, can also up your risk of acidity.If you experience acidity once in a while, it may not indicate any health issues. However, if you suffer from frequent bouts of acidity, where the symptoms occur at least two or more days per week, there might be some underlying disorder associated with it. It is advised to consult your doctor in such cases.You can fight acidity with simple lifestyle changes and effective home remedies, such astulsi, mint,fennel seeds, and cold milk. In most cases, over-the-counter medications to reduce/neutralize the acid are known to be of great help.",
    "symptoms of disease": "['1. Heartburn', '2. Regurgitation', '3. Sour taste in the mouth', '4. Difficulty in swallowing', '5. Sore throat', '6. Indigestion']",
    "causes of disease": "['Eating foods containing excessive amounts of chillies, pepper, vinegar, and paprika', 'Deep fried and oily foods', 'Excessive intake of caffeine in the form of tea, coffee, and chocolate', 'High intake of table salt', 'Diet low in fiber', 'Overeating or eating at irregular intervals', 'Unhealthy habits, like lying down just after eating', 'Eating just before strenuous physical exercise', 'Frequent smoking', 'Excessive intake of alcohol, soda, or carbonated drinks', 'Lack of sleep', 'Lack of physical activity', 'Excessive stress,anxiety, ordepression', 'Stomach diseases, likepeptic ulcer, gastroesophageal reflux disease, and stomach cancer', 'Medications, like painkillers, antibiotics, chemotherapy medications, and antidepressants']",
    "prevention from disease": "['1. Eat small, frequent meals', '2. Eat a low-carb diet', '3. Chew your food properly', '4. Avoid eating late at night', '5. Limit consumption of spicy and deep-fried foods', '6. Limit caffeine and carbonated beverages intake', '', '7. Limit your alcohol intake', '', '8. Quit smoking', '9. Avoid strenuous physical activity right after eating', '10. Do not sleep immediately after meals', '11. Raise the head of the bed', '12. Try to lose weight', '13. Check your medicines']",
    "home_remedy to disease": "['1.Holy basil (Tulsi) leaves', '2.Cinnamon (Dalchini)', '3.Cumin seeds (Jeera)', '4. Cold milk (Doodh)', '5. Buttermilk (Chaach)', '6.Carom seeds (Ajwain)', 'Yoga for acidity']"
  },
  {
    "title": "Acne",
    "description about disease": "Acne is a common condition that most of us have dealt with at some point in our lives. Acne, or acne vulgaris, is a skin condition in which the pores and hair follicles of the skin get clogged with sebum, an oily, wax-textured substance secreted from the skin glands. Though the face is the most commonly affected area, acne can occur anywhere on the body, like the chest, shoulders, and upper back.Acne is mainly of two types, comedogenic and non-comedogenic. Comedogenic acne is mainly non-inflammatory and can be seen in the form of whiteheads and blackheads. On the other hand, non-comedogenic acne is inflammatory and may be red, pus-filled, and painful.The treatment of acne comprises topical, systemic, and lifestyle remedies. Topical remedies include prescribed ointments or cleansers. Systemic therapy consists of antibiotics or hormonal preparations to keep acne at bay. Lifestyle changes for acne majorly include a clean diet, better hydration, and regular exercise. Timely treatment of acne can greatly help prevent acne scars in the future.",
    "symptoms of disease": "[]",
    "causes of disease": "[]",
    "prevention from disease": "['Diet & Acne']",
    "home_remedy to disease": "['Alternative Therapies For Acne', 'Ayurveda', 'Turmeric (Haldi):', 'Honey (Sahed)andLemon (Nimbu):', 'Neem leaves:', 'Pimples can be caused due to various reasons. Read to know the home remedies to get rid of them.Click Here', 'Homeopathy', 'Pulsatilla', 'Silicea', 'Sulfur', 'Acne scars not only mar the appearance and reduce confidence, but they are also not very easy to get rid of. Read about some effective natural remedies to help remove acne scars.', 'Tap Here']"
  },]

result = []

for json in JSONDATA:
    text = json
    output = llm_chain.run(text)

    result.append(parse_text(output))
