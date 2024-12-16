from pydantic_ai import Agent
from pydantic import BaseModel

# Use TestModel to avoid API costs during testing
agent = Agent('test')

# Test basic functionality
result = agent.run_sync('What is 2+2?')
print("Basic test result:", result.data)

# Test with structured output
class MathResult(BaseModel):
    answer: int
    explanation: str

agent_structured = Agent('test', result_type=MathResult)
result_structured = agent_structured.run_sync('What is 2+2?')
print("\nStructured test result:", result_structured.data)
