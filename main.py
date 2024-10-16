def createacc(name,user_name,passwd):
    zero=0
    with open('my_list.txt','a') as file:
        file.write(f'\n{name},{user_name},{passwd},{zero}')
    
def login(user_name,passwd):
    with open('my_list.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        parts = line.strip().split(',')
        if len(parts)>=3:
         if parts[2]==passwd and parts[1] == user_name:
            print(f'Welcome, {parts[0]}')
            global account_index
            account_index=(lines.index(line))
            return True

def deposit(deposite_amount):
    with open('my_list.txt','r') as f:
        lines=f.readlines()
    parts=(lines[account_index]).split(',')
    parts[-1]=int(parts[-1])+deposite_amount
    parts[-1]=str(parts[-1])+'\n'
    lines[account_index]=','.join(parts)

    with open('my_list.txt','w') as f:
        f.writelines(lines)
    print('your balance is : ',parts[-1])

def withdrawl(withdraw_amount):
    with open('my_list.txt','r') as f:
        lines=f.readlines()
    parts=(lines[account_index]).split(',')
    parts[-1]=int(parts[-1])-withdraw_amount
    parts[-1]=str(parts[-1])+'\n'
    lines[account_index]=','.join(parts)
    with open('my_list.txt','w') as f:
        f.writelines(lines)
    print('your balance is : ',parts[-1])

def balance():
    with open('my_list.txt','r') as f:
        lines=f.readlines()
    parts=(lines[account_index]).split(',')
    print('your balance is : ',parts[-1])

def admin(admin_passwd):
    with open('my_list.txt','r') as f:
        lines=f.readlines()
    if admin_passwd=='mominalimandal':
        print(f'there are total {len(lines)} accounts')
    else:
        print('access denied')
while True:
    print('created by >> momin\n.\n1.create account 2.log in(0 to stop) : ')
    f1=input('enter : ')
    if f1=='0':
        break
    elif f1=='1' or f1=='create account':
        name=input('enter name : ')
        username=input('create a username : ')
        passwd=input('create a passwd : ')
        createacc(name,username,passwd)
    elif f1=='3':
        passwd_admin=input('enter admin password : ')
        admin(passwd_admin)

    elif f1=='2' or f1=='log in':
        username=input('enter ur username: ')
        passwd=input('enter passwd : ')
        login(username,passwd)
        if login(username,passwd) is True:
            print('1.deposit   2.withdrawl   3.balance')
            f3=input('enter : ')
            if f3=='1' or f3=='deposit':
                deposit_amount=int(input('enter amount : '))
                deposit(deposit_amount)
            elif f3=='2' or f3=='withdrawl':
                withdraw_amount=int(input('enter withdraw amount : '))
                withdrawl(withdraw_amount)
            elif f3=='3' or f3=='balance':
                balance()
            else:
                print('please enter 1 or 2 or 3')
        else:
            print('login failed\nwrong password or wrong username maybe')
    else:
        print('please type 1 or 2 or 0 ')
