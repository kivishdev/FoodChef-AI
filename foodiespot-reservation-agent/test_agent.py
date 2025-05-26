from backend.agent import FoodieSpotAgent

# Your API key
API_KEY = "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"

def test_agent():
    print("🤖 Testing FoodieSpot Agent...")
    
    # Initialize agent
    agent = FoodieSpotAgent(API_KEY)
    
    # Test different types of messages
    test_messages = [
        "Hello! What restaurants do you have?",
        "I want Italian food recommendations",
        "I need to make a reservation for tonight",
        "Tell me about FoodieSpot Downtown"
    ]
    
    for message in test_messages:
        print(f"\n👤 User: {message}")
        response = agent.process_message(message)
        print(f"🤖 Agent: {response}")
        print("-" * 50)

if __name__ == "__main__":
    test_agent()
