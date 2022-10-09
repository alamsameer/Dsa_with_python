# At least 4 characters -Y
# At least one numeric digit -Y
# At least one Capital letter -y
# Must not have space or slash (/) 
# Starting character must not be a number 
import re
def passwordValidation(pwd):
    if(len(pwd)<=4):
        return 0
        # 
    pattern='.*[0-9].*[A-Z].'
    if(re.search(pattern,pwd)):
        if not" " or'/' in pwd:
            print("suucess")
        else:
            print("not matched inside")
    else:
        print("not matched")

passwordValidation("sdfksdlj34Azdfksldfj2")
passwordValidation("2dfksdlj34z dfks/ldfj Abgfb")
passwordValidation("sdfksdlj87ADz/dfdgd12ksldfj")
passwordValidation("sdu23yADij")