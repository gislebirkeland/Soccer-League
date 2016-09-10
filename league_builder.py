# imports the csv 
import csv

# creates a list of dictionaries with info on all the players
def list_players(file):
	# opens the .csv file
	with open(file) as csvfile:
		# starts reading the csv.file...
		player_reader = csv.reader(csvfile)
		# ...row by row
		rows = list(player_reader)
		# creates an empty list to put the dictionary of each players
		player_list = []
		# iterates through all the rows in the csv file. starts at row 1, after the titles
		for row in rows[1:]:
			# creates an empty dictionary
			player_info = {}
			# creates a key called 'name' and stores the value from first item in the row
			player_info['name'] = row[0]
			# creates a key called 'height' and stores the value from second item in the row
			player_info['heigth (inches)'] = row[1]
			# creates a key called 'experience' and stores the value from third item in the row
			player_info['experience'] = row[2]
			# creates a key called 'guardian' and stores the value from fouth item in the row
			player_info['guardian'] = row[3]
			# appends the dictionary into the list called 'player_list'
			player_list.append(player_info)
		# returns the list
		return player_list


def assign_to_teams(list):
	# creates a list of the different teams
	teams = ["Dragons", "Sharks", "Raptors"]
	# creates an empty list to store players with experience
	experience = []
	# creates an empty list to store players with NO experience
	no_experience = []
	# starts iterating the list of players
	for player in list[0:]:
		# if the player has any experience...
		if player['experience'] == 'YES':
			# ...append the player to the 'experience' list
			experience.append(player)
		# if not...
		else:
			# ...append the player to the 'no_experience' list
			no_experience.append(player)
	# calculates how many experienced players should be on each team
	experienced_per_team = len(experience) / len(teams)
	# calculates how many INexperienced players should be on each team
	newplayers_per_team = len(no_experience) / len(teams)

	# starts a counter
	count = 0
	# while the counter is less than the number of experienced_per_team variable
	while count < experienced_per_team:
		# add a "team" key to the dictionary with the value "Dragons"
		experience[count]["team"] = "Dragons"
		# ...and a key called "practice" with the time/date for the first practice
		experience[count]["practice"] = "March 17, 1pm"
		# add 1 to the counter
		count += 1
	while count < experienced_per_team * 2:
		experience[count]["team"] = "Sharks"
		experience[count]["practice"] = "March 17, 3pm"
		count += 1
	while count < experienced_per_team * 3:
		experience[count]["team"] = "Raptors"
		experience[count]["practice"] = "March 17, 1pm"
		count += 1

	# starts a counter
	count = 0
	# while the counter is less than the number of inexperienced players per team variable
	while count < newplayers_per_team:
		# add a "team" key to the dictionary with the value "Dragons"
		no_experience[count]["team"] = "Dragons"
		# ...and a key called "practice" with the time/date for the first practice
		no_experience[count]["practice"] = "March 17, 1pm"
		# add 1 to the counter
		count += 1
	while count < newplayers_per_team * 2:
		no_experience[count]["team"] = "Sharks"
		no_experience[count]["practice"] = "March 17, 3pm"
		count += 1
	while count < newplayers_per_team * 3:
		no_experience[count]["team"] = "Raptors"
		no_experience[count]["practice"] = "March 18, 1pm"
		count += 1

	# concatenate the list of experienced and inexperienced players into a new list
	updated_list = experience + no_experience
	# returns the new_list
	return updated_list

# creates a function for writing letters to the guardians
def write_letters(list):
	# the text in the letter with the placeholders
	letter = "Dear {guardian},\n\nI'm writing this letter to inform you that {name} will be playing for the {team}. The first practice will be on {practice}.\n\n- Coach"
	# creates a counter to help access each dictionary in the list
	count = 0
	# a for loop to iterate through the list of dictioanries
	for dictionary in list:
		# stores the players name, and converts it to lowercase, plus splits first and last name
		player_name = list[count]['name'].lower().split()
		# creates the file name by joining the names from above, plus adding the .txt extension
		filename = "_".join(player_name) + ".txt"
		# merges the info from the dictionary with the letter text
		text = letter.format(**list[count])
		# opens a file with the name of the player
		file = open(filename, "w")
		# writes the text from the 'text' variable
		file.write(text)
		# adds 1 to the counter to be able to go through the list
		count += 1


# starts the whole script
if __name__ == "__main__":
	# runs the function (with the .csv file) that stores all the player info in a list/dictionary
	players = list_players('soccer_players.csv')
	# assigns the players to different teams
	team_list = assign_to_teams(players)
	# runs the final funtion that actually writes and stores the letters
	write_letters(team_list)