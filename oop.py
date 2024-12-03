class fruits:
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print("Destructor called")
ob1=fruits("Apple")
print(ob1.name)
del ob1