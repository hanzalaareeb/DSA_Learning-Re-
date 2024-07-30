#--------------------- nested Vertex class ---------------------------------
class Vertex:
    """Lightweight vertex structure for a graph.
    """
    __slots__ = '_element'
    
    def __init__(self, x):
        """Do not use constructor directly. Use graph's insert.vertex(x).

        Args:
            x (val): node
        """
        self._element = x
    
    def element(self):
        """Return the element associated with this vertex."""
        return self._element
    def __hash__(self) :  # will allow vertex to be a map/set key
        return hash(id(self))

#--------------------- nested Edge class ----------------------------------------
class Edge:
    """Lightweight edge structure for grapg. """
    __slots__ = '_origin', '_destination', '_element'
    
    def __init__(self, u, v, x) -> None:
        """Do not call constructor directly. Use Graph's insert._edge(u, v, x)."""
        self._origin = u
        self._destination = v
        self._element = x
        
    def endpoints(self):
        """Return (u,v) pair for vertices associated with this edge."""
        return (self._origin, self._destination)
    
    def opposite(self, v):
        """Return vertex that this edge goes out from, if v is one of its vertices."""
        return self._destination if v in self._origin else self._origin
    
    def element(self):
        """Return the element associated with this edge."""
        return self._element
    
    def __hash__(self) -> int:
        return hash((self._origin, self._destination))
    
#--------------------- Graph class -------------------------------------------
class Graph:
    """Representation of a simple graph using an adjecency map."""
    
    def __init__(self, directed=False) -> None:
        """ Create an empty graph (undirected, by default)
        
        Graph is directed if oprional parameter is set to True.
        """
        self._outgoing = { }
        # Only create second map for directed Graph; use alias for undirected graph
        self._incoming = { } if directed else self._outgoing
        
    def is_directed(self):
        """Return True if graph is directed, False otherwise
        Property is based on the origin declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing # directed if maps are distenct
    
    def vertex_cont(self):
        """Return the number of vertices in this graph."""
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iterator of all vertices in this graph"""
        return self._outgoing.keys()
    
    def edge_count(self):
        """Return the number of edges in this graph"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.value())  # add edge to resulting set
        return result
    
    def get_edge(self, u, v):
        """Return edge associated with vertices u and v, if it exists."""
        return self._outgoing.get(u, {}).get(v)  #return None if v not adjecent
    
    def degree(self, v, outgoing=True):
        """ Return number of (outgoing) edges incident to vertex v in the graph.
        
        If graph is directed, optional parameter used to count incoming edges.
        """
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        """Retrun all (outgoing) edges incident to vertes v in the graph
        If graph is directed, optional parameter used to request incoming edges.

        Args:
            v (val): _description_
            outgoing (bool, optional): _description_. Defaults to True.
        """
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
        
    def insert_vertex(self, x=None):
        """Insert and return a new vertex with element x.

        Args:
            x (val, optional): element. Defaults to None.
        """
        v = self.Vertex(x)
        self._outgoing[v] = { }
        if self.is_directed():
            self._incoming[v] = {} # need distinct map for incoming edges
        return v
    
    