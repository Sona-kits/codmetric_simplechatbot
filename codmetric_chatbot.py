import tkinter as tk
import random
import datetime

# Bot response logic
def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return random.choice(["Hi there!", "Hello! 😊", "Hey!"])
    elif "how are you" in user_input:
        return "I'm doing great! How about you? 🤖"
    elif "good" in user_input or "fine" in user_input:
        return "That's good to know. How can I help you today?"
    elif "time" in user_input or "date" in user_input:
        now = datetime.datetime.now()
        date_str = now.strftime("%A, %B %d, %Y")
        time_str = now.strftime("%I:%M %p")
        return f"📅 {date_str}\n⏰ {time_str}"
    elif "joke" in user_input:
        return random.choice([
            "Why don't scientists trust atoms? Because they make up everything🧑‍🔬🧪!",
            "What do you call fake spaghetti? An impasta!🍝",
            "Why did the scarecrow win an award? He was outstanding in his field!👻"
        ])
    elif "fact" in user_input:
        return random.choice([
            "Octopuses have three hearts!🐙",
            "Bananas are berries, but strawberries aren't!🍌🍓",
            "Honey never spoils—even after 3000 years!🍯",
            "The human brain uses around 20% of the body's total oxygen and calories, even though it only makes up about 2% of body weight!🧠"
        ])
    elif "bye" in user_input:
        root.after(1000, root.destroy)
        return "Goodbye! Have a lovely day! 👋"
    elif "help" in user_input:
        return (
            "I can help you with:\n"
            "- Say hi or hello\n"
            "- Tell a joke (type 'joke')\n"
            "- Share a fun fact ('fact')\n"
            "- Show the time/date\n"
            "- Say goodbye ('bye')\n"
            "- Type 'help' to see this again"
        )
    else:
        return "Hmm... I'm still learning! Try saying 'help' 😊"

# Send user message and get bot response
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        chatbox.config(state='normal')
        chatbox.insert(tk.END, "Bot: Please type something! 😊\n\n", "bot")
        chatbox.config(state='disabled')
        chatbox.see(tk.END)
        return

    chatbox.config(state='normal')
    chatbox.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    bot_response = get_bot_response(user_input)
    chatbox.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")
    chatbox.config(state='disabled')
    chatbox.see(tk.END)

# Clear chat function with welcome reset
def clear_chat():
    chatbox.config(state='normal')
    chatbox.delete('1.0', tk.END)
    chatbox.insert(tk.END, "Bot: Hello! I'm your simple chatbot!🤖\n", "bot")
    chatbox.insert(tk.END, "Bot: Type 'help' to see what I can do!😌\n", "bot")
    chatbox.config(state='disabled')

# GUI setup
root = tk.Tk()
root.title("SIMPLE CHATBOT🤖")
root.configure(bg="lavender")

chatbox = tk.Text(root, height=20, width=60, font=("Comic Sans MS", 11), bg="mint cream", state='normal')
chatbox.pack(padx=10, pady=10)

# Tag colors
chatbox.tag_config("user", background="#d1ffd6", foreground="black")  # Light green
chatbox.tag_config("bot", background="#d9eaff", foreground="black")   # Light blue

# Initial welcome message
chatbox.insert(tk.END, "Bot: Hello! I'm your simple chatbot!🤖\n", "bot")
chatbox.insert(tk.END, "Bot: Type 'help' to see what I can do!😌\n", "bot")
chatbox.config(state='disabled')

entry = tk.Entry(root, font=("Comic Sans MS", 11), width=45)
entry.pack(side=tk.LEFT, padx=10, pady=10)
entry.bind("<Return>", lambda e: send_message())

send_button = tk.Button(root, text="Send", command=send_message, bg="seagreen", fg="white", font=("Comic Sans MS", 10, "bold"))
send_button.pack(side=tk.LEFT)

clear_button = tk.Button(root, text="Clear Chat", command=clear_chat, bg="tomato", fg="white", font=("Comic Sans MS", 10, "bold"))
clear_button.pack(side=tk.LEFT)

root.mainloop()
