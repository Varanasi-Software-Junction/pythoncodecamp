class Currency:
    def __init__(self, rs, p):
        self.total = 100* rs + p

    def __str__(self):
        
        return "{}".format(self.total)
