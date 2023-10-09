arr_title = []
arr_intructions = []
arr_stack = []
counter = 0
d = {}

isWork = True
while(isWork):
    
    n = input()
    arr_title.append(n)
    
    if n == "//down":
        counter += 1
        arr_stack.append("(")
        #d.add(counter: f"{counter - 1}")
        
    elif n == "//up":
        arr_stack.pop()
        if len(arr_stack) == 0:
            isWork = False
    elif n.find("//title") and n.index(""):
        pass
    else:
        continue

    
        

        
    