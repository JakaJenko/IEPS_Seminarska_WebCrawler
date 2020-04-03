import psycopg2
import networkx as nx
from fa2 import ForceAtlas2
import matplotlib.pyplot as plt

conn = psycopg2.connect(host="localhost", user="postgres", password="root")
cur = conn.cursor()
cur.execute("""SELECT l.from_page, l.to_page
                FROM crawldb.link l
                INNER JOIN crawldb.page p ON p.id = l.from_page
                INNER JOIN crawldb.site s ON s.id = p.site_id""") #or s.id = 484
# cur.execute("SELECT * FROM crawldb.link l")

edges =[]
for row in cur:
    edges.append((int(row[0]), int(row[1])))
conn.close()

print("graph building...")
graph = nx.DiGraph()
graph.add_edges_from(edges)
# nx.write_edgelist(graph, 'CrawlerLinksGraph.csv', data=False)

print("graph plotting...")
forceatlas2 = ForceAtlas2(
                        # Behavior alternatives
                        outboundAttractionDistribution=True,  # Dissuade hubs
                        edgeWeightInfluence=1,
                        # Performance
                        jitterTolerance=1,  # Tolerance
                        barnesHutOptimize=True,
                        barnesHutTheta=1.2,
                        # Tuning
                        scalingRatio=2,
                        strongGravityMode=False,
                        gravity=1,
                        # Log
                        verbose=True)

positions = forceatlas2.forceatlas2_networkx_layout(graph, pos=None, iterations=200)
nx.draw_networkx_nodes(graph, positions, node_size=20, with_labels=False, node_color="blue", alpha=0.4)
nx.draw_networkx_edges(graph, positions, edge_color="green", alpha=0.05)
plt.axis('off')
plt.show()