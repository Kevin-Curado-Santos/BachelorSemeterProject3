# Class to handle network topology
class network():
    def __init__(self) -> None:
        self.node_list = []
        self.switch_list = []
        self.link_list = []
    
    #add a node to the network
    def add_node(self, node):
        self.node_list.append(node)
        
    #add multiple nodes to the network
    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)
    
    #add a switch to the network
    def add_switch(self, switch):
        self.switch_list.append(switch)
        
    #add multiple switches to the network
    def add_switches(self, switches):
        for switch in switches:
            self.add_switch(switch)
        
    #add a link to the network
    def add_link(self, link):
        self.link_list.append(link)
        
    #remove a node from the network
    def remove_node(self, node):
        self.node_list.remove(node)
    
    #remove a switch from the network
    def remove_switch(self, switch):
        self.switch_list.remove(switch)
    
    #remove a link from the network
    def remove_link(self, link):
        self.link_list.remove(link)
        
    # get the node list
    def get_node_list(self):
        return self.node_list
    
    #get the switch list
    def get_switch_list(self):
        return self.switch_list
    
    #get the link list
    def get_link_list(self):
        return self.link_list
        
    #print the network
    def __str__(self) -> str:
        string = "Network topology:\n"
        for node in self.node_list:
            string += str(node) + "\n"
        for switch in self.switch_list:
            string += str(switch) + "\n"
        for link in self.link_list:
            string += str(link) + "\n"
        return string
      
        
# Class to handle nodes
class node():
    def __init__(self, name) -> None:
        self.name = name
        self.isSource = False
        self.isDestination = False
        self.neighbors = []
    
    #get the name of the node
    def get_name(self):
        return self.name
    
    #get the type of the node
    def get_type(self):
        return self.type
    
    def set_source(self):
        self.isSource = True
    
    def set_destination(self):
        self.isDestination = True
        
    def get_neighbors(self):
        return self.neighbors
    
    #print the node
    def __str__(self) -> str:
        return "Node: " + self.name
        
        
# Class to handle switches
class switch():
    def __init__(self, name) -> None:
        self.name = name
        self.neighbors = []
    
    #get the name of the switch
    def get_name(self):
        return self.name
    
    def get_neighbors(self):
        return self.neighbors
    
    #print the switch  
    def __str__(self) -> str:
        return "Switch: " + self.name
    
    
#Class to handle links
class link():
    def __init__(self, node1, node2) -> None:
        self.node1 = node1
        self.node2 = node2
        self.node1.neighbors.append(node2)
        self.node2.neighbors.append(node1)
    
    #get the first node of the link
    def get_node1(self):
        return self.node1
    
    #get the second node of the link
    def get_node2(self):
        return self.node2
    
    #print the link
    def __str__(self) -> str:
        return "Link: " + self.node1 + " -> " + self.node2