jk_smallgraph
==========

Introduction
------------

This python module is a directed graph implementation where each node and edges is represented as an individual object.

This implementation is not intended to represent large graphs. For this purpose, this implementation may not
be good enough. This is not the purpose of this module. This module provides objects for nodes and edges for
you to attach data to. The focus is on intuitive representation and management of your data,
not on maximum possible performance.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_smallgraph)

Limitations of this module
--------------------------

This module provides convenient support for smaller graphs but might not be usable for larger amounts of data.
This is not its purpose.

How to use this module
----------------------

### Importing this module

Please include this module into your application using the following code:

```python
import jk_smallgraph
import jk_smallgraph.io
```

Module `jk_smallgraph` holds all graph components while `jk_smallgraph.io` assists with I/O related functions.

### Creating a graph

To create a graph use the methods provided. Example:

```python
g = DirectedGraph()
nodeFoo = g.createNode("foo")
nodeBar = g.createNode("bar")
nodeBaz = g.createNode("baz")
g.createLink(nodeFoo, nodeBar)
g.createLink("bar", "baz")
```

### Selecting nodes

Example:

```python
listOfNodes = list(g.iterateConnectedNodes("bar"))
for node in listOfNodes:
	node.color = "yellow"
```

Example:

```python
listOfNodes = list(g.iterateStartNodes("bar"))
for node in listOfNodes:
	node.color = "green"
```

Example:

```python
listOfNodes = list(g.iterateOutgoingNodes("bar"))
for node in listOfNodes:
	node.color = "blue"
```

### Rendering as PNG

Rendering a graph is done with the help of `graphviz`:

```python
dot = jk_smallgraph.io.GraphvizIO.convert(g, "some title")
dot.render(filename="sometitle.dot", format="png")
```

This will create the PNG files `sometitle.dot` and `sometitle.dot.png`.

Contact Information
-------------------

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



