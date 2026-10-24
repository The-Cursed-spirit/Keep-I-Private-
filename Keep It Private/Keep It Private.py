# CLass creation
class myClass:

    # private variable
    __privateVar = 27;

    # private method
    def __privMeth(self):
        print("I'm inside callass Myclass")

    #Function to print value of private variable
    def hello(self):
        print("Private Variable value : ", myClass.__privateVar)

# Object creation and mehod call
foo = myClass()
foo.hello()
foo.__privMeth