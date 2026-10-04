from tools.tavily_tool import search_results
from tools.flight_tool import search_flights


results = search_flights("Plan a 7 days Japan trip from India")
print(results)

# results = search_results("Best travel destinations in Europe")
# print("\n".join(results))