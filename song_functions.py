def print_main_menu(the_menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    """
    print("==========================")
    print("What would you like to do?")
    for key in the_menu.keys():
        print(key, '-', the_menu[key])
    print("==========================")

def get_written_date(date_list):
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY] format 
    and returns the resulting date (in the US format) as a string.
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    date = ''
    date += month_names[int(date_list[0])]
    date += (f' {str(int(date_list[1]))}, ')
    date += (f'{str(int(date_list[2]))}') 
    
    return date

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_song(song, rating_map, title_only = False, showid = False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If False, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'duedate' field
        You created a similar function in a previous lab.
    """
    for song_key, val in song.items():
        if title_only == True and showid == False: #if title_only = True and show_id = False, print only title
            if song_key == "title":
                print(f'{song_key.upper():>8}: {val}')
                
        elif title_only == True and showid == True: #if title_only = True and show_id = True, print title, including the unique id.
            if song_key == "uid":
                continue
            if song_key == "title":
                print(f'      ID: {song["uid"]} |{song_key.upper():>8}: {val}')

        elif title_only == False and showid == False: # if title_only and show_id = False, print everything except the uid
            if song_key == "uid":
                continue
            if song_key == "title":
                print(f'{song_key.upper():>8}: {val}')
            if song_key == "artist":
                print(f'{song_key.upper():>8}: {val}')
            if song_key == "length":
                if len(song["length"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {val}')
            if song_key == "album":
                if len(song["album"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {val}')
            if song_key == "genre":
                seperator = ", "
                i = seperator.join(song["genre"])
                if len(song["genre"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {i.title()}')
            if song_key == "rating":
                if song["rating"] == 1:
                    val = rating_map["1"]
                elif song["rating"] == 2:
                    val = rating_map["2"]
                elif song["rating"] == 3:
                    val = rating_map["3"]
                elif song["rating"] == 4:
                    val = rating_map["4"]
                else:
                    val = rating_map["5"]
                print(f'{song_key.upper():>8}: {val}')
            if song_key == "released":
                if len(song["released"]) == 0:
                    continue
                else:
                    date1 = song["released"].split("/")
                    revised_date = get_written_date(date1)
                    print(f'{song_key.upper():>8}: {revised_date}')
            if song_key == "favorite":
                print(f'{song_key.upper():>8}: {val}')
                print("*"*42)

        elif title_only == False and showid == True: #if title_only = False and show_id = True, print everything.
            if song_key == "uid":
                continue
            if song_key == "title":
                print(f'      ID: {song["uid"]} |{song_key.upper():>8}: {val}')
            if song_key == "artist":
                print(f'{song_key.upper():>8}: {val}')
            if song_key == "length":
                if len(song["length"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {val}')
            if song_key == "album":
                if len(song["album"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {val}')
            if song_key == "genre":
                seperator = ", "
                i = seperator.join(song["genre"])
                if len(song["genre"]) == 0:
                    continue
                else:
                    print(f'{song_key.upper():>8}: {i.title()}')
            if song_key == "rating":
                if song["rating"] == 1:
                    val = rating_map["1"]
                elif song["rating"] == 2:
                    val = rating_map["2"]
                elif song["rating"] == 3:
                    val = rating_map["3"]
                elif song["rating"] == 4:
                    val = rating_map["4"]
                else:
                    val = rating_map["5"]
                print(f'{song_key.upper():>8}: {val}')
            if song_key == "released":
                if len(song["released"]) == 0:
                    continue
                else:
                    date1 = song["released"].split("/")
                    revised_date = get_written_date(date1)
                    print(f'{song_key.upper():>8}: {revised_date}')
            if song_key == "favorite":
                print(f'{song_key.upper():>8}: {val}')
                print("*"*42)

def print_songs(song_dict, rating_map, title_only = False, showid = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    
    
    # Check to see if get_genre is True, so that you can ask for the genre keyword
   # Go through all the songs in the song dictionary:
    """
    print("*"*42)
    if get_genre == False:
        for song in song_dict.keys():
            if title_only == True and showid == False: #prints only title
                print_song(song_dict[song], rating_map, title_only = True, showid = False)
                
            elif title_only == True and showid == True: # prints only title and id 
                print_song(song_dict[song], rating_map, title_only = True, showid = True)

            elif fave == True and get_genre == False: 
                if song_dict[song]['favorite'] == True:
                    print_song(song_dict[song], rating_map, title_only = False, showid = False)
                    
            elif fave == False and get_genre == False and title_only == False:
                print_song(song_dict[song], rating_map, title_only = False, showid = False)
            

    elif get_genre == True: # only ask for user input if get_genre == True
        user_input = input('Enter genre:: ') # if asking specific genres: print those
        for song in song_dict.keys():
            if user_input in str((song_dict[song]["genre"])):
                print_song(song_dict[song], rating_map, title= only == False, showid = False)
            

                     
def is_valid_addlist(song_info):
    """
    param: song_info (list) - a list of user input strings
    The function checks if the entire input list (song_info) is made up of strings.
    Is called by get_new_song().
    """
    if len(song_info) == 9:
        for key in song_info:
            if type(key) == str:
                continue
            else:
                return False
                break      
        return True
    else:
        return False
   
              

def is_valid_title(song_info):
    """
    param: song_info (list) - a list of user-input strings.
    The function checks if the "title" value in song_info is a string that's at least 2 characaters long
    and at most 40 characters long.
    Is called by get_new_song().
    """
    
    if type(song_info) == str:
        if 2 <= len(song_info) <= 40: #checks if title value is between at least 2 and at most 40 characters
            return True
        else:
            return False
    else:
        return False

def is_valid_time(song_info):
    """
    param: song_info (list) - a list of user-input strings.
    The function checks if the "length" value is in 00:00 format, that is, a string that has 2
    digits, followed by a colon, followed by 2 digits.
    Is called by get_new_song().
    """
    if type(song_info) == str:
        if len(song_info) == 5:
            if song_info[0:2].isdigit() and song_info[3:5].isdigit():
                if song_info[2] == ":":
                    return True
                    
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False




def is_valid_month(song_info): #function from 7.19 LAB
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY] format 
    and returns True if the provided month number is a possible month in the U.S. (i.e., an integer between 1 and 12 inclusive).

    """
    new_date = song_info.split("/")
    if type(new_date[0]) == str:
        if '01' <= new_date[0] <= '12':
            return True
        else:
            return False
    else: 
        return False
    
def is_valid_day(song_info): #function from 7.19 LAB
    """
    The function takes as a parameter a list of strings in the [MM, DD, YYYY] format 
    and returns True if the provided day is a possible day for the given month.
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    new_date = song_info.split("/")
   
    if is_valid_month(new_date[0]) == True:
        if type(new_date[1]) == str:
            if int(new_date[1]) >= 1 and int(new_date[1]) < num_days[1]: 
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
def is_valid_year(song_info): #function from 7.19 LAB
    new_date = song_info.split("/")
    ##[0] = mm
    ##[1] == /
    ##[2] == dd
    ##[3] == /
    ##[4] == yyyy
    # new_date = ['07', '27', '2020']
    if type(new_date[2]) == str:
        if new_date[2] > '1000':
            return True
        else:
            return False
    else:
        return False
      

    
def is_valid_date(song_info):
    """
    param: song_info (list) - a list of user-input strings.
    The function checks if the "released" value in song_info is in MM/DD/YYYY format.
    Is called by get_new_song().
    """

    #mm = index 0
    ##/ = index 1
    #dd = index 2
    ##/ = index 4
    #yyyy = index 5
    new_date = song_info.split("/")
    
    if is_valid_month(song_info) == True:   #call to check the month i valid
        if is_valid_day(song_info) == True: #call to check if day is valid
            if is_valid_year(song_info) == True: #call to check if year is valid
                return True
            else:
                return False
        else:
            return False
    else:
        return False
   
def is_valid_uid(song_info, allkeys):
    """
    param: song_info (list) - list of user-input strings
    param: key_list (list) - a list of all keys in the song dictionary 
    The function checks if the "uid" value is a string that has to be made up of exactly 5 digits.
    The range of these digits can only be "10000" to "99999".
    Value has to be unique to any other uid value in all_songs(song dictionary).
    Is called by get_new_song().
    """
    if type(song_info) == str:
        if len(song_info) == 5 and song_info.isdigit():
            if "10000" <= song_info <= "99999":
                if song_info not in allkeys:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False    
    

def get_new_song(song_info,rating_map, allkeys):
    """
    param: song_info (list) - list of user-input strings
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: key_list (list) - a list of all keys in the song dictionary
    
    The function calls upon the 5 helper functions (is_valid_addlist(), is_valid_title(),
    is_valid_time(), is_valid_date(), and is_valid_uid() to check.
    
    Helper function: is_valid_addlist() - The function checks if the entire input list (song_info) is made up of strings.
        Is called by get_new_song().
    Helper function: is_valid_title() - The function checks if the "title" value in song_info is a string that's at least 2 characaters long
        and at most 40 characters long.
    Helper function: is_valid_time() - The function checks if the "length" value is in 00:00 format, that is, a string that has 2
        digits, followed by a colon, followed by 2 digits.
    Helper function: is_valid_date() - The function checks if the "released" value in song_info is in MM/DD/YYYY format.
    Helper function: is_valid_uid () - The function checks if the "uid" value is a string that has to be made up of exactly 5 digits.
        The range of these digits can only be "10000" to "99999".
        Value has to be unique to any other uid value in all_songs(song dictionary).
    """

    if is_valid_addlist(song_info) == True: 
        if is_valid_time(song_info[2]) == True:
            if "1" <= song_info[5] <= "5":
                if is_valid_date(song_info[6]) == True:
                    if song_info[7].startswith('T') == True:
                        if is_valid_uid(song_info[8], allkeys) == True:
                            if is_valid_title(song_info[0]) == True: 
                                new_song = {} ##new dictionary
                                new_song["title"] = song_info[0] #str
                                new_song["artist"] = song_info[1]  #str
                                new_song["length"] = song_info[2]#str
                                new_song["album"] = song_info[3]   #str
                                new_song["genre"] = song_info[4].split(",")  #list
                                new_song["rating"] = int(song_info[5])
                                new_song["released"] = song_info[6] #str
                                new_song["favorite"] = True #bool
                                new_song["uid"] = int(song_info[8])  #int
                                return new_song
                            
                            else:
                                return ("Bad Title length", -1)
                        else:
                            return("Unique ID is invalid or non-unique", -6)
                    elif song_info[7].startswith('t') == True:
                            if is_valid_uid(song_info[8], allkeys) == True:
                                if is_valid_title(song_info[0]) == True: 
                                    new_song = {} ##new dictionary
                                    new_song["title"] = song_info[0] #str
                                    new_song["artist"] = song_info[1]  #str
                                    new_song["length"] = song_info[2]#str
                                    new_song["album"] = song_info[3]   #str
                                    new_song["genre"] = song_info[4].split(",")  #list
                                    new_song["rating"] = int(song_info[5])
                                    new_song["released"] = song_info[6] #str
                                    new_song["favorite"] = True #bool
                                    new_song["uid"] = int(song_info[8])  #int
                                    return new_song
                                
                                else:
                                    return("Bad Title length", -1)
                            else:
                                return("Unique ID is invalid or non-unique", -6)
                                

                    elif song_info[7].startswith('F') == True:
                        if is_valid_uid(song_info[8], allkeys) == True:
                            if is_valid_title(song_info[0]) == True: 
                                new_song = {} ##new dictionary
                                new_song["title"] = song_info[0] #str
                                new_song["artist"] = song_info[1]  #str
                                new_song["length"] = song_info[2]#str
                                new_song["album"] = song_info[3]   #str
                                new_song["genre"] = song_info[4].split(",")  #list
                                new_song["rating"] = int(song_info[5])
                                new_song["released"] = song_info[6] #str
                                new_song["favorite"] = False #bool
                                new_song["uid"] = int(song_info[8])  #int
                                return new_song
                            
                            else:
                                return("Bad Title length", -1)
                        else:
                            return("Unique ID is invalid or non-unique", int-6)
                            
                    elif song_info[7].startswith('f') == True:
                        if is_valid_uid(song_info[8], allkeys) == True:
                            if is_valid_title(song_info[0]) == True: 
                                new_song = {} ##new dictionary
                                new_song["title"] = song_info[0] #str
                                new_song["artist"] = song_info[1]  #str
                                new_song["length"] = song_info[2]#str
                                new_song["album"] = song_info[3]   #str
                                new_song["genre"] = song_info[4].split(",")  #list
                                new_song["rating"] = int(song_info[5])
                                new_song["released"] = song_info[6] #str
                                new_song["favorite"] = False #bool
                                new_song["uid"] = int(song_info[8])  #int
                                return new_song
                            
                            else:
                                return("Bad Title length", -1)
                        else:
                            return("Unique ID is invalid or non-unique", -6)
                    else:
                        return("Invalid value for Favorite", -5)
                else: 
                    return("Invalid date format for Release Date", -4)
            else:
                return("Invalid Rating value", -3)
        else:
            return("Invalid time format for Length", -2)
    else:
        return("Bad list. Found non-string, or bad length", 0)
    
def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    if len(song_dict) == 0:
        return 0
    
    elif type(field_key) != str:
        return -1
    else:
        if field_key == "title":
            if is_valid_title(field_info) == True:
                song_dict[songid]["title"] = field_info
                return song_dict[songid]
            else:
                return field_key
        if field_key == "rating":
            if "1" <= field_info <= "5":
                song_dict[songid]["rating"] = field_info
                return song_dict[songid]
            else:
                return field_key
        if field_key == "length":
            if is_valid_time(field_info) == True:
                song_dict[songid]["length"] = field_info
                return song_dict[songid]
            else:
                return field_key
            
        if field_key == "favorite":
            if field_info[7].startswith('t') == True or field_info[7].startswith('T')== True or field_info[7].startswith('F') == True or field_info[7].startswith('f') == True:
                song_dict[songid]["favorite"] = field_info
                return song_dict[songid]
            else:
                return field_key
            
        if field_key == "released":
            if is_valid_date(field_info) == True:
                song_dict[songid]["released"] = field_info
                return song_dict[songid]
            else:
                return field_key

        if field_key == "uid":
            if is_valid_uid(field_info) == True:
                song_dict[songid]["uid"] = field_info
                return song_dict[songid]
            else:
                return field_key

        else:
            return field_key
       


def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the items title from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """

    if len(song_dict) == 0: # if input list is empty, return 0 
        return 0
    else:
        if songid in song_dict: #checks if songid is valid
            title_name = song_dict[songid]["title"]
            del song_dict[songid]
            return title_name
        else:
            return -1

def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """

    rating_list = []
    for song_key, val in song_dict.items():
        rating_list.append(val["rating"])

     # Calculate the arithmetic mean
    mean = sum(rating_list)/len(rating_list)

    rating_list.sort() #sorts list
    count = 0

    for rate in rating_list:
        count += (rate - mean)**2
    std_dev = (count/(len(rating_list)))**0.5
    
    if len(rating_list) % 2 == 0:  #if numbers in list add up to even amount
        middle = (len(rating_list))//2
        song_median = ((rating_list[middle] + rating_list[middle-1])/2)
    elif len(rating_list) %2 == 1: #for odd amt of numbers
        middle = (len(rating_list)/2)
        song_median = rating_list[middle]


    if opt == "A":
        print(f"The mean value of all ratings is: {mean:.2f}")

    elif opt == "B":
        print(f"The median value of all ratings is: {song_median:.2f}")
        
    elif opt == "C":
        print(f"The standard deviation value of all ratings is: {std_dev:.2f}")

    elif opt == "D":
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for item in rating_list:
            if item == 5:
                count5 += 1
            elif item == 4:
                count4 += 1
            elif item == 3:
                count3 += 1
            elif item == 2:
                count2 += 1
            elif item == 1:
                count1 += 1
        print(f"1 {count1*'*'}")
        print(f"2 {count2*'*'}")
        print(f"3 {count3*'*'}")
        print(f"4 {count4*'*'}")
        print(f"5 {count5*'*'}")
        
            
def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
    joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid
    
    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    
    import csv
    if filename[-4:] != '.csv':
        return -1
    else:
        with open(filename, 'w', newline="") as myfile:
                writer= csv.writer(myfile)
                for song, val in song_dict.items():
                    new_list = []
                    for song_key, val_key in val.items():
                        if type(val_key) == list:
                            join_item = ','.join(val_key)
                            new_list.append(join_item)
                        else: 
                            type(val_key) == str
                            new_list.append(val_key)
                    writer.writerow(new_list)
  


def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """
    import csv
    import os

    
    if filename[-4:] != '.csv':
        return -1

    else:
        if os.path.exists(filename):  #checks if filename exists
            with open(filename, 'r') as myfile:
                list_fail = []
                row_count = 0
                reader = csv.reader(myfile, delimiter=",")          
                for row in reader: #goes through each row in the csv file
                    row_count += 1
                    call_song = get_new_song(row, in_dict, allkeys)
                    if type(call_song) == tuple: # return rows that are 
                        list_fail.append(row_count)  
                    else:
                        song = str(call_song["uid"])
                        in_dict[song]= call_song
                              
                return list_fail 
        else:
            return None
   


       


