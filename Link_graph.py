import psycopg2
import networkx as nx



conn = psycopg2.connect(host="localhost", user="postgres", password="root")
cur = conn.cursor()
cur.execute("SELECT * FROM crawldb.link")
edges =[]
for row in cur:
    edges.append((int(row[0]), int(row[1])))
conn.close()

#graph building
graph = nx.DiGraph()
graph.add_edges_from(edges)
print(len(graph.nodes))

nx.write_edgelist(graph, 'CrawlerLinksGraph.csv', data=False)

