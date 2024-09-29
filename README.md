# Medic - Your Health Assistant

![image](https://github.com/user-attachments/assets/f14a0170-d29f-4a59-b9aa-ef593a86ce40)
Prototype Drive link : (https://drive.google.com/file/d/1yIviUvTXwYfdw8XAxR_XDKks21D8vwhV/view?usp=sharing)
## Made By Team Phenix
<h5>1. Mayur Jadhav      2. Ameya Kalgutkar      3.Pratham Gupta</h5>

**Medic** is a responsive web application developed using **Flutter**. It is designed to streamline patient management, providing easy tools for profiling patients, scheduling appointments, and interacting with MedicAI—an intelligent chatbot trained on medical data to assist with medical inquiries and suggestions.

## Features

1. **Patient Profiling**:  
   Allows users to create and manage patient profiles. Each profile stores essential medical details such as personal information , history , known conditions , allergies , addiction status , current medications. this profile later used by MedicAI for generate personalise responses. 

2. **Appointment Scheduling**:  
   Helps users manage and schedule appointments with doctors or healthcare professionals. Features include booking, rescheduling, and sending reminders.

3. **MedicAI (Chatbot)**:  
   A chatbot designed to assist with medical queries. It is trained on relevant medical data and can provide basic advice, clarify doubts, and offer general healthcare information.

4. **Responsive Design**:  
   Optimized for both desktop and mobile devices, the application adjusts fluidly to various screen sizes, ensuring a smooth user experience.

## Tech Stack

- **Flutter**: A UI toolkit for crafting natively compiled web, mobile, and desktop applications from a single codebase.
- **Dart**: The programming language used for Flutter development.
- **Firebase/Backend**: For managing real-time databases, authentication, and backend storage (if applicable).
- **AI Integration**: The chatbot, MedicAI, is powered by an AI model trained on medical datasets and integrated into the Flutter app.

## Getting Started

### Prerequisites

- **Flutter SDK**: Ensure that the Flutter SDK is installed on your machine. You can download it from [Flutter's official site](https://flutter.dev/).
- **Dart SDK**: The Dart SDK should be installed alongside Flutter.
- **Code Editor**: It's recommended to use Visual Studio Code or Android Studio for Flutter development.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/m-spunky/medic.git
   ```

2. **Install dependencies**:
   Run the following command to install all dependencies from `pubspec.yaml`:
   ```bash
   flutter pub get
   ```

3. **Run the app**:
   Use the following command to run the application on a web browser:
   ```bash
   flutter run -d chrome
   ```

### Firebase Setup (Optional)

- If you're using Firebase for backend services such as authentication, real-time data, or storage, configure Firebase as per the instructions in the [Firebase for Flutter documentation](https://firebase.flutter.dev/docs/overview).


