with open("data\students.txt") as users:  # The with keyword automatically closes the file when you are done
	users = users.read().splitlines() 
def checkCredentials(username, password):
	for details in users:
		
		detail_split = details.strip().split(",")

		if(detail_split[0] == username and detail_split[1].strip() == password):
			show_frame(MenuPage)
