class ElectronicSign:
    def __init__(self):
        self.views = []

    def add_view(self, view):
        self.views.append(view)
        
    def print_views(self):
        for index, view in enumerate(self.views):
            print("```")
            for row in view:
                print("".join(row))
            print("```")
    def print_views1(self):
        for index, view in enumerate(self.views):
            print("```")
            for row in view:
                print(" ".join(row))
            print("```")

    def clear_memory(self):
        del self.views
