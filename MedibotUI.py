import tkinter as tk
from tkinter import scrolledtext

def medical_advice(user_input):
    if 'fever' in user_input or 'temperature' in user_input:
        return "High temperature is often a sign of infection. Rest and stay hydrated. If you have other severe symptoms, please see a doctor."
    elif 'headache' in user_input:
        return "For a headache, rest in a quiet and dark room. Stay hydrated and consider over-the-counter pain relief. If it persists, consult a doctor."
    elif 'covid' in user_input or 'coronavirus' in user_input:
        return "COVID-19 symptoms can include fever, cough, and difficulty breathing. Follow local health guidelines, wear a mask, and consult a healthcare provider for a test."
    elif 'diarrhea' in user_input:
        return "Stay hydrated and consider a BRAT diet (bananas, rice, applesauce, toast). If symptoms persist, consult a doctor."
    else:
        return "I'm sorry, I don't have an answer for that. It might be best to consult a medical professional."

def on_send_click():
    user_input = user_entry.get().lower()
    response = medical_advice(user_input)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.insert(tk.END, "Medibot: " + response + "\n\n")
    chat_history.see(tk.END)

# Create the main application window
root = tk.Tk()
root.title("Medibot - Your Medical Assistant")

# Load robot image
robot_image = tk.PhotoImage(file="robot_image.png")

# Create a label with the robot image as the background
background_label = tk.Label(root, image=robot_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create UI elements
label = tk.Label(root, text="Hello! I'm Medibot, your medical assistant chatbot.\nI can help you with basic medical information and advice.", bg="white", fg="#333", font= ("Helvetica", 12))
label.place(relx=0.5, rely=0.1, anchor="center")

chat_history = scrolledtext.ScrolledText(root, width=50, height=15, bg="white", fg="#333", font=("Helvetica", 10))
chat_history.place(relx=0.5, rely=0.4, anchor="center")

user_entry = tk.Entry(root, width=50, bg="white", fg="#333", font=("Helvetica", 10))
user_entry.place(relx=0.5, rely=0.8, anchor="center")
user_entry.bind("<Return>", lambda event: on_send_click())

send_button = tk.Button(root, text="Send", command=on_send_click, bg="#4caf50", fg="#fff", font=("Helvetica", 10))
send_button.place(relx=0.7, rely=0.8, anchor="center")

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#f44336", fg="#fff", font=("Helvetica", 10))
exit_button.place(relx=0.3, rely=0.8, anchor="center")

# Run the application
root.mainloop()

