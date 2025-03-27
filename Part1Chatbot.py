import tkinter as tk
import random

# Simple chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a simple bot, but I'm good!", "I don't have feelings, but I'm okay!"],
    "what is your name": ["I'm a chatbot created using Python!", "Just call me ChatBot!"],
    "bye": ["Goodbye! Have a great day.", "See you later!", "Bye!"]
}

# Function to handle user input
def chatbot_response():
    user_text = entry.get().lower()  # Get user input
    entry.delete(0, tk.END)  # Clear input field

    if user_text in responses:
        bot_reply = random.choice(responses[user_text])
    elif user_text == "bye":
        bot_reply = "Goodbye! Have a great day."
    else:
        bot_reply = "I don't understand that yet."

    chat_history.insert(tk.END, "You: " + user_text + "\n")
    chat_history.insert(tk.END, "Bot: " + bot_reply + "\n\n")

# Create GUI window
root = tk.Tk()
root.title("Chatbot")

# Chat history area
chat_history = tk.Text(root, height=15, width=50)
chat_history.pack()

# Entry field for user input
entry = tk.Entry(root, width=50)
entry.pack()

# Button to send message
send_button = tk.Button(root, text="Send", command=chatbot_response)
send_button.pack()

# Run the app
root.mainloop(
