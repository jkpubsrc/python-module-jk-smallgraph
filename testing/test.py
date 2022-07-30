#!/usr/bin/python3


import os

import jk_smallgraph
import jk_smallgraph.io





EXAMPLE_FILE_PATH = os.path.join("data", "example-graph.json")




g = jk_smallgraph.io.SimpleEdgeListIO.loadFromFile(EXAMPLE_FILE_PATH)


dot = jk_smallgraph.io.GraphvizIO.convert(g, "some title")
dot.render(filename=os.path.join("output", "sometitle1.dot"), format="png")


selectedNodes = set(g.iterateConnectedNodes("10", bIncludedStart=True))
for node in selectedNodes:
	node.color = "yellow"


dot = jk_smallgraph.io.GraphvizIO.convert(g, "some title")
dot.format = "png"
dot.render(filename=os.path.join("output", "sometitle2.dot"), format="png")


allNodes = set(g.iterateAllNodes())
nodesToRemove = allNodes - selectedNodes
g.removeNodes(nodesToRemove)


dot = jk_smallgraph.io.GraphvizIO.convert(g, "some title")
dot.format = "png"
dot.render(filename=os.path.join("output", "sometitle3.dot"), format="png")












