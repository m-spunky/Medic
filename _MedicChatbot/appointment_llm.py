import json
import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
client = openai.OpenAI(api_key="ENTER YOUR OPENAI KEY")

def load_doctors():
    with open('doctors.json', 'r') as f:
        return json.load(f)

def save_doctors(doctors):
    with open('doctors_o.json', 'w') as f:
        json.dump(doctors, f, indent=4)

doctors = load_doctors()

def find_doctors(criteria):
    symptom = criteria.get('symptom')
    specialization = criteria.get('specialization')
    input_criteria = criteria.get('symptom', '').lower()  # Ensure we're checking the right field
    words = input_criteria.split()

    common_words = {"i", "need", "a", "the", "doctor", "doctors"}
    filtered_words = [word for word in words if word not in common_words]

    filtered_doctors = []

    for doctor in doctors['doctors']:
        if specialization and specialization.lower() in doctor.get('specialization', '').lower():
            if doctor not in filtered_doctors:
                filtered_doctors.append(doctor)
        for keyword in filtered_words: 
            if keyword in [k.lower() for k in doctor.get('keywords', [])]:
                filtered_doctors.append(doctor)      

    if not filtered_doctors:
        return "Sorry, no doctors found for your criteria."
    
    response = "Here are some doctors you might consider:\n"
    for doc in filtered_doctors:
        response += f"- Dr. {doc['name']}, specializing in {doc['specialization']}.\n"
        response += "  Available Slots:\n"
        for day, slots in doc['available_slots'].items():
            response += f"    {day}: {', '.join(slots)}\n"
    
    return response

def get_available_slots(doctor_name):
    for doctor in doctors['doctors']:
        if doctor['name'] == doctor_name:
            slots = doctor['available_slots']
            if not slots:
                return "No available slots for this doctor."
            response = f"Available slots for Dr. {doctor_name}:\n"
            for day, slot_list in slots.items():
                response += f"- {day}: {', '.join(slot_list)}\n"
            return response
    return "Doctor not found."

def book_appointment(doctor_name, time_slot):
    doctor = next((doc for doc in doctors['doctors'] if doc['name'] == doctor_name), None)
    
    if not doctor:
        return f"Dr. {doctor_name} does not exist."

    for day, slots in doctor['available_slots'].items():
        if time_slot in slots:
            slots.remove(time_slot)
            if not slots:
                del doctor['available_slots'][day]
                if not doctor['available_slots']:
                    doctors['doctors'].remove(doctor)
            save_doctors(doctors)        
            return f"Appointment with Dr. {doctor_name} at {time_slot} has been booked."

    available_slots = []
    for day, slots in doctor['available_slots'].items():
        available_slots.append(f"{day}: {', '.join(slots)}")
    
    if available_slots:
        return f"The selected time slot is not available. Here are the available slots:\n" + "\n".join(available_slots)
    else:
        return f"Dr. {doctor_name} has no available slots left."

@app.route('/api/find_doctors', methods=['POST'])
def api_find_doctors():
    criteria = request.json.get('criteria', {})
    result = find_doctors(criteria)
    return jsonify({"result": result})

@app.route('/api/get_available_slots', methods=['POST'])
def api_get_available_slots():
    doctor_name = request.json.get('doctor_name')
    result = get_available_slots(doctor_name)
    return jsonify({"result": result})

@app.route('/api/book_appointment', methods=['POST'])
def api_book_appointment():
    doctor_name = request.json.get('doctor_name')
    time_slot = request.json.get('time_slot')
    result = book_appointment(doctor_name, time_slot)
    return jsonify({"result": result})

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    history = request.json.get('history', [])
    
    prompt = """
    You are a doctor appointment booking assistant. 
    Chat with people to help them find available doctors based on their symptoms like leg pain, eye infection, headache, and fever. Respond in a helpful manner by providing doctors' names, specializations, available days, and time slots.
    Give short and specific answers inclined to health-related only.
    Once they specify their needs and the day they want the appointment, provide available slots for that day.
    Confirm the booking once they select a slot.
    If there is AM or PM think it as time slot and if user wants to book appointment using 'from' and 'to' time, make it '-'.
    For example, if the user wants to book from 9 AM to 10 AM, make it 09:00 AM - 10:00 AM.
    """

    messages = [{"role": "system", "content": prompt}]
    
    for user_message, assistant_message in history:
        messages.append({"role": "user", "content": user_message})
        messages.append({"role": "assistant", "content": assistant_message})
    
    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
        max_tokens=100,
    )
    
    result = response.choices[0].message.content
    function_call = response.choices[0].message.function_call
    if function_call:
        function_name = function_call.name
        function_args = json.loads(function_call.arguments)
        
        if function_name == "find_doctors":
            result = find_doctors(function_args)
        elif function_name == "book_appointment":
            result = book_appointment(function_args['doctor_name'], function_args['time_slot'])
        
        return jsonify({"result": result})
    else:
        return jsonify({"result": result.strip()})

if __name__ == '__main__':
    app.run(debug=True)
