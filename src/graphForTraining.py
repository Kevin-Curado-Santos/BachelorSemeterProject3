import networkx as nx 
import matplotlib.pyplot as plt

def create_graph():
    graph = nx.Graph()

    # all nodes are from 1 to 100 
    for i in range(1, 101):
        graph.add_node(i)
        
    # all switches are from 101 to 130
    for i in range(101, 131):
        graph.add_node(i)
        
    # link some of the switches (creating a cycle)
    graph.add_edge(101, 102, weight=1)
    graph.add_edge(102, 103, weight=5)
    graph.add_edge(103, 104, weight=3)
    graph.add_edge(104, 105, weight=8)
    graph.add_edge(105, 106, weight=1)
    graph.add_edge(106, 107, weight=2)
    graph.add_edge(107, 108, weight=9)
    graph.add_edge(108, 109, weight=4)
    graph.add_edge(109, 110, weight=3)
    graph.add_edge(110, 111, weight=4)
    graph.add_edge(111, 101, weight=2)

    graph.add_edge(111, 112, weight=7)
    graph.add_edge(112, 113, weight=4)

    graph.add_edge(114, 101, weight=3)
    graph.add_edge(115, 103, weight=2)
    graph.add_edge(116, 105, weight=1)
    graph.add_edge(117, 107, weight=5)
    graph.add_edge(118, 109, weight=6)
    graph.add_edge(119, 111, weight=7)
    graph.add_edge(120, 118, weight=8)
    graph.add_edge(121, 118, weight=9)
    graph.add_edge(122, 118, weight=3)
    graph.add_edge(123, 111, weight=4)
    graph.add_edge(124, 123, weight=1)
    graph.add_edge(125, 124, weight=2)
    graph.add_edge(126, 121, weight=3)
    graph.add_edge(127, 126, weight=4)
    graph.add_edge(128, 103, weight=5)
    graph.add_edge(129, 120, weight=6)
    graph.add_edge(130, 129, weight=7)

    # connect nodes to switches
    graph.add_edge(1, 101, weight=1)
    graph.add_edge(2, 101, weight=2)
    graph.add_edge(3, 101, weight=3)
    graph.add_edge(4, 101, weight=4)
    graph.add_edge(5, 102, weight=1)
    graph.add_edge(6, 102, weight=7)
    graph.add_edge(7, 102, weight=3)
    graph.add_edge(8, 103, weight=4)
    graph.add_edge(9, 103, weight=5)
    graph.add_edge(10, 104, weight=6)
    graph.add_edge(11, 104, weight=7)
    graph.add_edge(12, 104, weight=8)
    graph.add_edge(13, 104, weight=9)
    graph.add_edge(14, 104, weight=1)
    graph.add_edge(15, 104, weight=5)
    graph.add_edge(16, 105, weight=3)
    graph.add_edge(17, 105, weight=1)
    graph.add_edge(18, 105, weight=5)
    graph.add_edge(19, 105, weight=3)
    graph.add_edge(20, 105, weight=7)
    graph.add_edge(21, 106, weight=1)   
    graph.add_edge(22, 106, weight=9)
    graph.add_edge(23, 106, weight=1)
    graph.add_edge(24, 106, weight=7)
    graph.add_edge(25, 107, weight=3)
    graph.add_edge(26, 107, weight=2)
    graph.add_edge(27, 107, weight=5)
    graph.add_edge(28, 107, weight=2)
    graph.add_edge(29, 107, weight=2)
    graph.add_edge(30, 107, weight=3)
    graph.add_edge(31, 107, weight=9)
    graph.add_edge(32, 107, weight=1)
    graph.add_edge(33, 108, weight=7)
    graph.add_edge(34, 108, weight=6)
    graph.add_edge(35, 108, weight=1)
    graph.add_edge(36, 108, weight=2)
    graph.add_edge(37, 108, weight=1)
    graph.add_edge(38, 109, weight=8)
    graph.add_edge(39, 109, weight=8)
    graph.add_edge(40, 109, weight=1)
    graph.add_edge(41, 109, weight=4)
    graph.add_edge(42, 109, weight=8)
    graph.add_edge(43, 110, weight=1)
    graph.add_edge(44, 110, weight=6)
    graph.add_edge(45, 110, weight=1)
    graph.add_edge(46, 110, weight=2)
    graph.add_edge(47, 110, weight=2)
    graph.add_edge(48, 110, weight=9)
    graph.add_edge(49, 110, weight=1)
    graph.add_edge(50, 110, weight=1)
    graph.add_edge(51, 110, weight=6)
    graph.add_edge(52, 111, weight=1)
    graph.add_edge(53, 111, weight=9)
    graph.add_edge(54, 111, weight=2)
    graph.add_edge(55, 111, weight=9)
    graph.add_edge(56, 111, weight=1)
    graph.add_edge(57, 112, weight=9)
    graph.add_edge(58, 112, weight=9)
    graph.add_edge(59, 112, weight=9)
    graph.add_edge(60, 112, weight=9)
    graph.add_edge(61, 113, weight=1)
    graph.add_edge(62, 113, weight=4)
    graph.add_edge(63, 113, weight=6)
    graph.add_edge(64, 113, weight=1)
    graph.add_edge(65, 113, weight=7)
    graph.add_edge(66, 114, weight=1)
    graph.add_edge(67, 114, weight=2)
    graph.add_edge(68, 114, weight=8)
    graph.add_edge(69, 114, weight=1)
    graph.add_edge(70, 114, weight=2)
    graph.add_edge(71, 114, weight=8)
    graph.add_edge(72, 114, weight=1)
    graph.add_edge(73, 114, weight=2)
    graph.add_edge(74, 115, weight=8)
    graph.add_edge(75, 116, weight=1)
    graph.add_edge(76, 117, weight=2)
    graph.add_edge(77, 118, weight=3) 
    graph.add_edge(78, 119, weight=4)
    graph.add_edge(79, 120, weight=5)
    graph.add_edge(80, 120, weight=6)
    graph.add_edge(81, 121, weight=7)
    graph.add_edge(82, 121, weight=8)
    graph.add_edge(83, 122, weight=9)
    graph.add_edge(84, 122, weight=1)
    graph.add_edge(85, 123, weight=2)
    graph.add_edge(86, 123, weight=3)
    graph.add_edge(87, 124, weight=4)
    graph.add_edge(88, 124, weight=5)
    graph.add_edge(89, 125, weight=2)
    graph.add_edge(90, 125, weight=7)
    graph.add_edge(91, 126, weight=4)
    graph.add_edge(92, 126, weight=1)
    graph.add_edge(93, 127, weight=2)
    graph.add_edge(94, 127, weight=1)
    graph.add_edge(95, 128, weight=1)
    graph.add_edge(96, 128, weight=4)
    graph.add_edge(97, 129, weight=9)
    graph.add_edge(98, 129, weight=9)
    graph.add_edge(99, 130, weight=1)
    graph.add_edge(100, 130, weight=4)

    nx.draw_spring(graph, with_labels=True)
    plt.show()
    
    return graph

G = create_graph()
