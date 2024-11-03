from song_functions import *

the_menu = {
'L' : 'List',
'A' : 'Add',
'E' : 'Edit',
'D' : 'Delete',
'M' : 'Show statistical data on',
'S' : 'Save the data to file',
'R' : 'Restore data from file',
'Q' : 'Quit this program'
}

opt = None

all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
}

list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

#list of all keys in the song dictionary 
allkeys = list(all_songs.keys())

while True:
    print_main_menu(the_menu) # TODO 2: define the function, uncomment, and call with the menu as an argument
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu: # TODO 3: check of the character stored in opt is in the_menu dictionary
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q': # TODO 4: quit the program
        print("Goodbye!\n")
        break # exit the main `while` loop

    # Pause before going back to the main menu
        input("::: Press Enter to continue")


    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_songs(all_songs, rating_map, showid = True)
            input("::: Press Enter to continue")

        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
            input("::: Press Enter to continue")

        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
            input("::: Press Enter to continue")

        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)
            input("::: Press Enter to continue")

      # ----------------------------------------------------------------

    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            # TODO: Get user inputs for all 9 song info fields (i.e. keys). 
            # Get *all* inputs as strings.
            title =  input("Title: ")
            artist =  input("Artist: ") 
            length =  input("Length (00:00 format): ")
            album =  input("Album: ")
            genre =  input("Genres (separate them with commas): ")
            rating =  int(input("Rating (1-5): "))
            released =  input("Release Date (MM/DD/YYYY format): ")
            favorite =  input("Favorite (T/F): ")
            uid =  input("Unique ID: ")
            ######APPEND TO SONG_INFO######
            song_info.append(title)  #index0
            song_info.append(artist) #index1
            song_info.append(length) #index2
            song_info.append(album)  #index3
            song_info.append(genre)  #index4
            song_info.append(rating) #index5
            song_info.append(released) #index6
            song_info.append(favorite) #index7
            song_info.append(uid)      #index 8
            song_info_keys = list(all_songs.keys())
            
            result = get_new_song(song_info, all_songs, song_info_keys) # TODO: attempt to create a new song
            if type(result) == dict:
                get_new_song(song_info, all_songs, song_info_keys)# TODO: add a new song to the list of songs
                print(f"Successfully added a new song!")
                print_songs(all_songs, rating_map, title_only = False, showid = False)
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

        print("::: Would you like to add another song?", end=" ")
        continue_action = input("Enter 'y' to continue.\n> ")
        continue_action = continue_action.lower()
        # ----------------------------------------------------------------
        
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: # TODO
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if user_option in allkeys: # TODO - check to see if that ID is in the song dictionary
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, allkeys) #TODO
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_song(result, rating_map, title_only = True, showid = True )  # TODO
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  # TODO

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------
                 
    elif opt == 'D':
       continue_action = 'y'
       while continue_action == 'y':
           print("Which song would you like to delete?")
           print_songs(all_songs, rating_map, title_only = True, showid = True)
           print("X - Delete all songs at once")
           print("::: OR Enter the number corresponding to the song ID")
           print("::: OR press 'M' to cancel and return to the main menu.")
           
           user_option = input("> ")
           result = delete_song(all_songs, user_option)
               
           if user_option == "X": 
               print("::: WARNING! Are you sure you want to delete ALL songs?")
               print("::: Type Yes to continue the deletion.")
               user_option_again = input("> ")
               if user_option_again == "Yes":
                   for song in list(all_songs):
                       delete_song(all_songs, song)
               print("Deleted all songs.")
               input("::: Press Enter to continue")
               continue_action = 'n'
               
           elif user_option == "M" or "m": # if the user changed their mind
               input("::: Press Enter to continue")
               break
               continue_action = 'n'
                
           elif user_option in allkeys:
               print("Success!")
               print(f"Deleted the song |{result}|")
           elif len(all_songs) == 0: # empty input list 
               print(f"WARNING: There is nothing to delete!")
               
           elif user_option not in allkeys: # songid not valid, returned False
               print(f"WARNING: |{user_option}| is an invalid song ID!")
               print("::: Would you like to delete another song? Enter 'y' to continue.")
               user_option = input("> ")
    # ----------------------------------------------------------------
    elif opt == 'M':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: What would you like to show statistical data on?")
            print("A - Mean value of all song ratings")
            print("B - Median value of all song ratings")
            print("C - Standard Deviation value of all song ratings")
            print("D - Histogram of all song ratings")
            input("::: Enter your selection")
            user_option = input("> ")
            if user_option == "A": #shows the mean value
                print(f"You selected |{user_option}| to show statistical data on |mean value of all song ratings|.")
                do_stats(all_songs,user_option)
                continue_action = 'n'

            if user_option == "B": # shows the median value
                print(f"You selected |{user_option}| to show statistical data on |median value of all song ratings|.")
                do_stats(all_songs,user_option)
                continue_action = 'n'

            if user_option == "C": #shows the standard deviation value 
                print(f"You selected |{user_option}| to show statistical data on |standard deviation value of all song ratings|.")
                do_stats(all_songs,user_option)
                continue_action = 'n'

            if user_option == "D": # displays histogram
                print(f"You selected |{user_option}| to show statistical data on |histogram of all song ratings|.")
                do_stats(all_songs,user_option)
                continue_action = 'n'

            print("::: Would you like to get different statistics?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      

    #--------------------------------------------------------------------------
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = save_to_csv(all_songs, filename) # TODO: Call the function with appropriate inputs and capture the output
            if result == -1: # if last 4 characters in file name are not '.csv'
                print(f"WARNING: |{filename}| is an invalid file name!") 
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else: # successully stores save 
                print(f"Successfully stored all the songs to |{filename}|")
                input("::: Press Enter to continue")

                continue_action = 'n'
     #--------------------------------------------------------------------------

                  
    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = load_from_csv(all_songs, filename, rating_map, allkeys)# TODO: Call the function with appropriate inputs and capture the output
            if result == -1: # TODO
                print(f"WARNING: invalid input - must end with '.csv'") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
                
            elif result == None:
                print(f"WARNING: |{filename}| was not found!")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
                
            elif len(result) >=1: 
                print(f"WARNING: |{filename}| contains invalid data!")
                print(f"The following rows from the file were not loaded:")
                print(result)

            else:
                print(f"Successfully stored all the songs to |{filename}|")
                
            print("::: Would you like to try again?", end=" ")
            continue_action = input("Enter 'y' to try again.\n> ")

            continue_action = 'n'
        # ----------------------------------------------------------------
                    

print("Have a nice day!")
