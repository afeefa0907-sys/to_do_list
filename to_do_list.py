print("Hello and welcome to my to do list checker")
t=int(input("How many tasks you want to add? "))
to_do=dict()
for k in range(1,t+1):
    to=input(f"Enter your task no. {k}: ")
    to=to.upper().strip()
    to_do[to]=False
print(to_do)    
while True :
    print("Type 'done' to stop;")
    task_to_check=input("Enter to task you want to check :> ")
    if task_to_check.upper().strip() in to_do :
        to_do[task_to_check]=True
    elif task_to_check=="done":
        print(to_do)
        break
    else :
        print("Enter the task from the list below >>")
        print(to_do)
file=open("to_do_file.txt",'a')

with open('to_do_file.txt' , "w") as f:
    for key, value in to_do.items():
        f.write(f"{key}: {value}\n")        