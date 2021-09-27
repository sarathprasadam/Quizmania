from background import quizmania
def home():
	print("--------QUIZMANIA--------")	
	tst=False
	while(tst==False):
		print("BUTTON        FUNCTION")
		print("   1          Super user login")
		print("   2          User login")
		print("   3          New user registration")
		print("   4          Exit the application")
		tst1=False
		while(tst1==False):
			hometst=input("Enter the Button: ")
			if hometst not in ['1','2','3','4']:
				print("Ener correct button")
			else:
				tst1=True
				if hometst=='1':
					quizmania.superUsersPage()					
				elif hometst=='2':
					quizmania.user()					
				elif hometst=='3':
					quizmania.register()					
				else:
					tst=True
def main():
    foo = home()
    

if __name__ == "__main__":
    main()
