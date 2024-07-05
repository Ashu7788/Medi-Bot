def medical_chatbot():
    print("Hello! I'm Medibot, your medical assistant chatbot.")
    print("I can help you with basic medical information and advice.")
    
    while True:
        print("\nHow can I help you today? (Type 'exit' to quit)")
        user_input = input().lower()

        if user_input == 'exit':
            print("Thank you for using Medibot. Stay healthy!")
            break
        
        elif 'fever' in user_input or 'temperature' in user_input:
            print("High temperature is often a sign of infection. Rest and stay hydrated. If you have other severe symptoms, please see a doctor.")
    
        elif 'headache' in user_input:
            print("For a headache, rest in a quiet and dark room. Stay hydrated and consider over-the-counter pain relief. If it persists, consult a doctor.")
        
        elif 'covid' in user_input or 'coronavirus' in user_input:
            print("COVID-19 symptoms can include fever, cough, and difficulty breathing. Follow local health guidelines, wear a mask, and consult a healthcare provider for a test.")
        
        elif 'diarrhea' in user_input:
            print("Stay hydrated and consider a BRAT diet (bananas, rice, applesauce, toast). If symptoms persist, consult a doctor.")
        
        else:
            print("I'm sorry, I don't have an answer for that. It might be best to consult a medical professional.")

if __name__ == '__main__':
    medical_chatbot()

