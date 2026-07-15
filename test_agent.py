from agent import extract_interaction

text = """
Met Dr. Ramesh today at Apollo Hospital.
Discussed CardioPlus.
Distributed 5 samples.
Doctor showed positive interest.
Follow up on July 21.
"""

result = extract_interaction(text)

print(result)