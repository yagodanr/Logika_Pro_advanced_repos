import django_startup
from blog.models import * 

    
def main():
    
    
    
    while True:
        print('''1 - create user
2 - create post
3 - comment post
0 - end programm
    ''')
        while True:
            user_inp = input("Enter code: ")
            
            try:
                user_inp = int(user_inp)
            except:
                print("Input should be number from 0 to 3")
                continue
            
            if user_inp not in range(0, 3+1):
                print("Input should be number from 0 to 3")
                continue
                
            break
    
        if user_inp == 1:
            login = input("Enter login: ")
            email = input("Enter email: ")
            
            User(
                login=login,
                email=email,
                role="user",
            ).save()
            
        elif user_inp == 2:
            title = input("Enter post's title: ")
            text = input("Enter text:\n")
            
            author_db = None
            while True:
                author = input("Enter author's login(0 -- cancel): ")
                
                try:
                    author_db = User.objects.get(login=author)
                except:
                    print("No such user in database")
                    continue
                
                print(author_db.email)
                break
            
              
            
            

if __name__ == "__main__":
    # main()
    user = User(
        login="g",
        email="nothing@gmail.com",
        role="user"
    )
    
    Post(
        title="asd",
        text="asd",
        author=user
    )

