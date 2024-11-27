import os
from dotenv import load_dotenv
import dspy
from openai import OpenAI
import sys

# Load environment variables from .env file
load_dotenv()

def test_openai():
    """Test direct OpenAI API connection"""
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY environment variable not found")
            return False
            
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": "Say 'OpenAI test successful'"}],
            max_tokens=20
        )
        print("✅ OpenAI API test successful")
        print(f"Response: {response.choices[0].message.content}")
        return True
    except Exception as e:
        print(f"❌ OpenAI API test failed: {str(e)}")
        return False

def test_dspy():
    """Test DSPy configuration and basic functionality"""
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            print("❌ OPENAI_API_KEY environment variable not found")
            return False
            
        # Configure DSPy
        dspy.configure(api_key=api_key)
        openai_lm = dspy.OpenAI(model="gpt-4", api_key=api_key)
        dspy.settings.configure(lm=openai_lm)
        
        # Create a simple DSPy module for testing
        class SimpleModule(dspy.Module):
            def __init__(self):
                super().__init__()
                self.generate = dspy.ChainOfThought("input -> output")
            
            def forward(self, input_text):
                return self.generate(input=input_text)
        
        # Test the module
        module = SimpleModule()
        result = module("Say 'DSPy test successful'")
        print("✅ DSPy test successful")
        print(f"Response: {result.output}")
        return True
    except Exception as e:
        print(f"❌ DSPy test failed: {str(e)}")
        return False

def main():
    print("\n=== Testing OpenAI API ===")
    openai_success = test_openai()
    
    print("\n=== Testing DSPy ===")
    dspy_success = test_dspy()
    
    if not (openai_success and dspy_success):
        sys.exit(1)

if __name__ == "__main__":
    main()
