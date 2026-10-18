from tools.tavily_tool import search_results
from tools.flight_tool import search_flights
from backend import run_travel_agent


# results = search_flights("Plan a 7 days Japan trip from India")
# print(results)

# results = search_results("Best travel destinations in Europe")
# print("\n".join(results))
userInput = input("Enter your travel query: ")
res = run_travel_agent(user_input= userInput, thread_id='abc123'
)

print("Flight Results:", res)
print("Flight Results:", res["answer"])