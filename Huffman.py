# NAME : SURAJ SUBHASH DHAMAK
# ROLL NO : BECOA140


class Node:
    name = ""
    freq = 0
    left = None
    right = None
    def __init__(self, name, freq, left, right):
        self.name = name
        self.freq = freq
        self.left = left
        self.right = right
        

class huffman_tree:
    total_chars = 0
    nodelist = []
    codes = {}
    def __init__(self, *nodes):
        self.total_chars = 0
        for node in nodes:
            self.total_chars += node.freq
            self.nodelist.append([node.freq, node])
            self.nodelist.sort()
    
    def construct_huffman_tree(self):
        #first consider the first 2 nodes in the nodelist
        newnode=None
        node1 = self.nodelist[0][1]
        node2 = self.nodelist[1][1]
        counter = 1
        ptr = 2
        while(True):
            newname = "n" + str(counter)
            newnode = Node(newname, node1.freq+node2.freq, node1, node2)
            if(ptr>=len(self.nodelist)):
                break
            if(self.nodelist[ptr][0]<=newnode.freq):
                node1 = self.nodelist[ptr][1]
                node2 = newnode
            else:
                node1 = newnode
                node2 = self.nodelist[ptr][1]
            
            counter+=1
            ptr+=1
        
        return newnode 
        
    def generateCodes(self,n, code):
        if(not n.right and not n.left):
            self.codes[n.name] = code
        else:
            self.generateCodes(n.left, code+"0")
            self.generateCodes(n.right, code+"1")
            
def main():
    a = Node("a", 50, None, None)
    b = Node("b", 10, None, None)
    c = Node("c", 30, None, None)
    d = Node("d", 5, None, None)
    e = Node("e", 3, None, None)
    f = Node("f", 2, None, None)
    
    tree = huffman_tree(a,b,c,d,e,f)
    root = tree.construct_huffman_tree()
    tree.generateCodes(root,"")
    print(tree.codes)
    for i in tree.nodelist:
        print(i[1].name, i[0])
    
main()
            