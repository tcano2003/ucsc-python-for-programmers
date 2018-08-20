#!/usr/bin/env python
"""list_scopes.py - answers lab17_1.b Scope issue with lists.
""" 
tea = ['earl grey', 'camomile', 'chai']

def AppendTea():
    tea.append('green') # <-- Good because we don't assign 
                        #     (bind) the name, we use the
                        #     function of an existing name.
def AssignTea(): 
    global tea             # <- But for assignment, we need 
    tea += ['blackberry']  #    global because it will try
                           #    to bind the name to the 
def PlusAddTea():          #    local namespace and fail.
    tea += ['peppermint']  # <- No good

def main():
    AppendTea()
    print tea
    AssignTea()
    print tea
    PlusAddTea()
if __name__ == '__main__':
    main()
    
