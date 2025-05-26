from tools.reservation import ReservationTool
from tools.recommend import RecommendationTool
from llm.llama3 import LlamaClient

# PUT YOUR API KEY HERE
API_KEY = "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"  # Replace with your actual key

def test_tools():
    print("🧪 Testing Tools...")
    
    # Test recommendation tool
    recommender = RecommendationTool()
    italian_restaurants = recommender.recommend_by_cuisine("Italian")
    print(f"Found {len(italian_restaurants)} Italian restaurants")
    
    # Test reservation tool
    reservation_tool = ReservationTool()
    restaurants = reservation_tool.load_restaurants()
    print(f"Loaded {len(restaurants)} restaurants")
    
    # Test LLaMA with API key
    llama_client = LlamaClient(API_KEY)
    response = llama_client.detect_intent("I want Italian food")
    print(f"Intent detected: {response}")
    
    print("✅ Tools working!")

if __name__ == "__main__":
    test_tools()
