## 加权图Weighted Graph

# Author: Aric Hagberg (hagberg@lanl.gov)
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

# 确定边
G.add_edge('a', 'b', weight=0.6)
G.add_edge('a', 'c', weight=0.2)
G.add_edge('c', 'd', weight=0.1)
G.add_edge('c', 'e', weight=0.7)
G.add_edge('c', 'f', weight=0.9)
G.add_edge('a', 'd', weight=0.3)

# 长边 权重大于0.5
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
# 短边 权重小于0.5
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

# 设置位置
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
# 画节点
nx.draw_networkx_nodes(G, pos, node_size=700)

# edges
# 画边
nx.draw_networkx_edges(G, pos, edgelist=elarge,width=6)
# style边的样式
nx.draw_networkx_edges(G, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b', style='dashed')

# labels
# 画标签
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
