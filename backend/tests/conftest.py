import pytest
import os
from dotenv import load_dotenv

@pytest.fixture(autouse=True)
def setup_test_env():
    """Setup test environment variables"""
    load_dotenv()
    # Ensure we have a mock API key for testing
    if not os.getenv("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = "test-api-key" 