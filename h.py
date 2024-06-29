class employee():
    name=""
    id=""
    time_period=""
    def info(self):
        print(f"Name:{self.name},ID:{self.id}\nThank you for {self.time_period} years, you have been with us .")   
ankit=employee()
ankit.name='ankit'
ankit.id='2022084'
ankit.time_period=2
ankit.info()