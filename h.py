# class employee():
#     name=""
#     id=""
#     time_period=""
#     def info(self):
#         print(f"Name:{self.name},ID:{self.id}\nThank you for {self.time_period} years, you have been with us .")   
# ankit=employee()
# ankit.name='ankit'
# ankit.id='2022084'
# ankit.time_period=2
# ankit.info()

class employee():
    def __init__(self,name,id,time):
        self.name=name
        self.id=id
        self.time=time
    
    def info(self):
        print(f"Name:{self.name},ID:{self.id}\nThank you, from {self.time} years you have been with us .")
ankit=employee('ankit','2022084',2)
ankit.info()