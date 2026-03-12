"""
AI Cost Optimizer Example
Using Synstar to reduce LLM API costs
"""

from synstar import chat

response = chat(
    "Explain what artificial intelligence is in simple terms."
)

print(response)
