from ai_graph import graph

result = graph.invoke(
    {
        "text":
        "Met Dr. Ramesh today at Apollo Hospital. Discussed CardioPlus. Distributed 5 samples. Doctor showed positive interest. Follow up on July 21."
    }
)

print(result)