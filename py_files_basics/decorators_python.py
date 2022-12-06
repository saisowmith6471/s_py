def div(a,b):
    print(a/b)

def smart_div(function): # smart_div is a decorator which accepts functions
    def inner(a,b):
        if a < b:
            a,b = b,a
        return function(a,b) # means return div(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)
