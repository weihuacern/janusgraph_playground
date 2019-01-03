"""
Talking to JanusGraph from Python.
http://tinkerpop.apache.org/docs/current/reference/#gremlin-python
https://github.com/davebshow/aiogremlin
"""

#import asyncio
#from aiogremlin import DriverRemoteConnection, Graph
#from gremlin_python.structure.graph import Graph
#from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

#async def go(loop):
#    remote_connection = await DriverRemoteConnection.open('http://localhost:8182/gremlin', 'g')
#    g = Graph().traversal().withRemote(remote_connection)
#    vertices = await g.V().toList()
#    await remote_connection.close()
#    return vertices

from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

if __name__ == "__main__":
    #graph = Graph()
    #g = graph.traversal().withRemote(DriverRemoteConnection('http://localhost:8182/gremlin', 'g'))
    #print(type(g.V()))
    #vertices = g.V().toList()
    #print(vertices)

    #loop = asyncio.get_event_loop()
    #vertices = loop.run_until_complete(go(loop))
    #print(vertices)

    statics.load_statics(globals())
    graph = Graph()
    g = graph.traversal().withRemote(DriverRemoteConnection('ws://localhost:8182/gremlin','g'))
    # nested traversal with Python slicing and attribute interception extensions
    g.V().hasLabel("person").repeat(both()).times(2).name[0:2].toList()
    g = g.withComputer()
    g.V().hasLabel("person").repeat(both()).times(2).name[0:2].toList()
    # a complex, nested multi-line traversal
    g.V().match( \
        as_("a").out("created").as_("b"), \
        as_("b").in_("created").as_("c"), \
        as_("a").out("knows").as_("c")). \
      select("c"). \
      union(in_("knows"),out("created")). \
      name.toList()
