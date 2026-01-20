# Natural Disaster Conversational Chatbot

def get_response(user_input):
    user_input = user_input.lower()

    # Earthquake
    if "earthquake" in user_input:
        return (
            "During an earthquake:\n"
            "- Drop, cover, and hold on.\n"
            "- Stay away from windows and heavy furniture.\n"
            "- Have an emergency kit ready with food, water, and medical supplies."
        )
    
    # Flood
    elif "flood" in user_input:
        return (
            "During a flood:\n"
            "- Move to higher ground immediately.\n"
            "- Avoid walking or driving through flood waters.\n"
            "- Keep emergency supplies ready and follow evacuation orders."
        )

    # Typhoon / Storm
    elif "typhoon" in user_input or "storm" in user_input:
        return (
            "During a typhoon or storm:\n"
            "- Stay indoors and away from windows.\n"
            "- Secure doors and windows.\n"
            "- Keep extra batteries, flashlights, and food ready."
        )
    
    # Volcano
    elif "volcano" in user_input or "eruption" in user_input:
        return (
            "During a volcanic eruption:\n"
            "- Evacuate if authorities advise.\n"
            "- Wear masks to avoid inhaling ash.\n"
            "- Keep emergency supplies ready in case you need to leave quickly."
        )
    
    # Unknown input
    else:
        return "Sorry, I don't have advice for that. Can you ask about an earthquake, flood, typhoon, or volcano?"

def chatbot():
    print("Hello! I'm SafeBot 🌪️")
    print("Ask me what to do during natural disasters, or type 'exit' to leave.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("SafeBot: Stay safe! Goodbye 👋")
            break
        response = get_response(user_input)
        print("SafeBot:", response, "\n")

if __name__ == "__main__":
    chatbot()
