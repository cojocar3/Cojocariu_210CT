class Node:
    def __init__(self,n):
        self.name = n
        self.relations = []
class Graph:
    vertices ={}

    def add_node(self,n):
        node = Node(n)
        self.vertices[n] = []
        return node

    def add_edge(self,relation1,relation2):
        self.vertices[relation1].append(relation2)
        self.vertices[relation2].append(relation1)

    def get_edge(self,n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None
        
    def print_nodes(self):
        print (self.vertices)
        
    def BFS (G,n):
        queue = []
        visited = []
        queue.insert(0,n)
        while queue != []:
            current = queue.pop()
            if current not in visited:
                visited.append(current)
            for i in g.get_edge(current):
                if i not in visited:
                    queue.insert(0,i)
        print ('BFS: ',visited)
        return visited
    def DFS(G,n):
        stack = []
        visited = []
        stack.append(n)
        while stack !=[]:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
            for i in g.get_edge(current):
                if i not in visited:
                    stack.append(i)
        print ('DFS: ',visited)
        return visited
        

if __name__ == '__main__':

    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_node('G')
    g.add_node('H')
    g.add_node('S')

    g.add_edge('A','B')
    g.add_edge('A','S')
    g.add_edge('S','C')
    g.add_edge('S','G')
    g.add_edge('G','F')
    g.add_edge('G','H')
    g.add_edge('C','D')
    g.add_edge('H','E')
    g.add_edge('E','C')
    g.add_edge('C','F')
    
    

    g.BFS('A')
    g.DFS('A')

    
    
        
