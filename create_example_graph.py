import logging
import sys

from visualisation.graph import Node, Edge
from visualisation import template_renderer

logging.basicConfig(
    format='%(asctime)s %(levelname)-5s %(filename)-12s %(message)s',
    level=logging.DEBUG, stream=sys.stdout)


def create_graph():
    upload1 = Node("cloud-upload", "id:1", "Title1",
                     properties={'prop1': 'value1'})
    upload2 = Node("cloud-upload", "id:2",
                   "Title2")
    cloud = Node("cloud", "id:5",
                   "Title2")
    edges = []
    edges.append(Edge(upload1, cloud, role='Upload1'))
    edges.append(Edge(upload2, cloud, role='Upload2'))
    nodes = [upload1, upload2, cloud]
    return nodes, edges


if __name__ == '__main__':
    nodes, edges = create_graph()
    template_renderer.render(nodes, edges, 'graph.html')
