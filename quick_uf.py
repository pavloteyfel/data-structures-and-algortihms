class QuickUF:
    """
        Quadtratic algorithm, we just update every p's component id to the q 
        component id
        init: N
        union: N
        find: 1
    """
    def __init__(self, N):
        self.id = list(range(N))

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        p_component_id, q_component_id = self.id[p], self.id[q]
        for i, component_id in enumerate(self.id):
            if (component_id == p_component_id): self.id[i] = q_component_id

###############################################################################

class QuickUnionUF:
    """
        init: N
        union: N
        find: N
    """
    def __init__(self, N):
        self.id = list(range(N))
    
    def root(self, i):
        while self.id[i] != i:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p == root_q:
            return

        self.id[root_p] = root_q

###############################################################################

class WeightedQuickUnionUF:
    """
        init: N
        union: lgN
        find: lgN
    """
    def __init__(self, N): 
        self.id = list(range(N))
        self.size = [1 for i in range(N)]
    
    def find(self, i):
        """
        We reach the root then index number equals to the value
        """
        while self.id[i] != i:
            # path compression
            # tbd i think it can be optimized, if size > 2
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        The algorithm makes sure that the smaller goes below
        """
        root_p, root_q = self.find(p), self.find(q)

        if root_p == root_q: return

        if self.size[root_p] > self.size[root_q]:
            self.id[root_p] = root_q
            self.size[root_p] += self.size[root_q]
        else:
            self.id[root_p] = root_q
            self.size[root_q] += self.size[root_p]
