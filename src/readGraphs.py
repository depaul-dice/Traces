import json 
import sys

class node_t:
    def __init__(self, id, type, label = ""):
        self.id = id
        self.type = type
        self.label = label

    def __str__(self):
        return "id: " + self.id + ", type: " + self.type + ", label: " + self.label
        

class graph_t:
    def __init__(self, name, nodes, edges):
        self.name = name
        self.nodes = dict() # key is id, value is node itself
        self.edges = dict() # key is going to be the id of src, value is going to be the set of id of dsts
        for node in nodes: # this is a list of node, which has id, type, and label
            if "label" in node:
                self.nodes[node["id"]] = node_t(node["id"], node["type"], node["label"]) 
            else:
                self.nodes[node["id"]] = node_t(node["id"], node["type"]) 
            
        for edge in edges:
            if edge["src"] not in self.edges:
                self.edges[edge["src"]] = set()
            self.edges[edge["src"]].add(edge["dst"])
                
    def __str__(self):
        r = self.name + '\nNodes:\n'
        for key, value in self.nodes.items(): 
            r += str(value) + '\n'
        r += 'Edges:\n'
        for key, value in self.edges.items(): 
            for each in value:
                r += key + '->' + each + '\n'
        return r

    def __repr__(self):
        return self.__str__()
            

def main(filename):
    graphs = dict() # key is the function name, value is the graph itself
    with open(filename, 'r') as f:
        rawGraphs = json.load(f)

    for rawGraph in rawGraphs:
        funcname = rawGraph["function name"] 
        nodes = rawGraph["nodes"]
        if "edges" in rawGraph:
            edges = rawGraph["edges"]
        else:
            edges = dict()
        graphs[funcname] = graph_t(funcname, nodes, edges)
        print(graphs[funcname])


if __name__ == "__main__":
    main(sys.argv[1])
