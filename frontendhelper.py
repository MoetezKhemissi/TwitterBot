
def splitter(str):
    first_split = str.split(',')
    i=0
    
    email_list=[]
    for fragement in first_split:
        if i%2==0:
            email_template={}
            email_template["email"]=fragement
        if i%2==1:
            email_template["password"]=fragement
            email_list.append(email_template)
        i=i+1
    return email_list
