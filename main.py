from functions import traveling_sales_person, gen_graph

graph = gen_graph(150, 1, 10)
cycles = traveling_sales_person(graph)
print(cycles)

