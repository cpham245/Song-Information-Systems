from song_functions import*

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

allkeys = list(all_songs.keys())

#### ASSERT FOR GET_WRITTEN_DATE()####
assert get_written_date(["01", "01", "1970"]) == "January 1, 1970"
assert get_written_date(["02", "03", "2000"]) == "February 3, 2000"
assert get_written_date(["10", "15", "2022"]) == "October 15, 2022"
assert get_written_date(["12", "31", "2021"]) == "December 31, 2021"

##### DELETE OPTION #####
assert delete_song(all_songs, '14567') == "Soul Meets Body"
assert delete_song(all_songs, '12332') == "Cardigan"
assert delete_song(all_songs, '55555') == -1

addlist1 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "12333"]
addlist2 = ["Cardigan - Extended Version", "Taylor Swift", "07:59", "Folklore", "folk,indie rock", 3, "07/27/2020", True, "12333"]
addlist3 = ["Cardigan - Extended Version", "Taylor Swift", "b7:59", "Folklore"]

#### GET_NEW_SONG ####
addlist4 = ["Perfect Pair", "Beabadoobee", "02:50", "Beatopia", "indie rock", "5", "07/20/2022", "True", "12444"]
addlist5 = ["A", "Dominic Fike", "03:39", "indie rock"]

assert(get_new_song(addlist4, rating_map, allkeys)) == {'title': 'Perfect Pair', 'artist': 'Beabadoobee', 'length': '02:50', 'album': 'Beatopia', 'genre': ['indie rock'], 'rating': 5, 'released': '07/20/2022', 'favorite': True, 'uid': 12444}
assert(get_new_song(addlist5, rating_map, allkeys)) == ('Bad list. Found non-string, or bad length', 0)

#### VALID_ADDLIST HELPER FUNCTION ####
assert is_valid_addlist(addlist1) == True
assert is_valid_addlist(addlist2) == False
assert is_valid_addlist(addlist3) == False

title1 = "perfect"
title2 = "b"
title3 = 23433
                   
#### VALID_TITLE HELPER FUNCTION ####
assert is_valid_title(title1) == True
assert is_valid_title(title2) == False
assert is_valid_title(title3) == False

time1 = "3:59"
time2 = "30:55"
time3 = "123:44"

#### VALID_TIME HELPER FUNCTION ####
assert is_valid_time(time1) == False
assert is_valid_time(time2) == True
assert is_valid_time(time3) == False

date1 = "07/27/2020"
date2 = "11/5/1000"
date3 = "July 20, 2011"

#### VALID_DATE HELPER FUNCTION ####
assert is_valid_date(date1) == True
assert is_valid_date(date2) == False
assert is_valid_date(date3) == False

uid1 = "2344"
uid2 = "12332"
uid3 = "1000000"

#### VALID_UID HELPER FUNCTION ####
assert is_valid_uid(allkeys, uid1) == False
assert is_valid_uid(allkeys, uid2) == False
assert is_valid_uid(allkeys, uid3) == False

#### VALIDMONTH, VALIDDAY, VALID YEAR ####

# test the correct input
assert is_valid_month("01/01/1970") == True
assert is_valid_day("02/03/2001") == True
assert is_valid_day("05/05/2005") == True
assert is_valid_year("10/15/2022") == True

#### test the edge cases ####
assert is_valid_month("21/01/1970") == False
assert is_valid_month("-2/31/2021") == False
assert is_valid_day("02/33/2000") == False
assert is_valid_day("02/31/2021") == False
assert is_valid_year("12/31/-21") == False

#### EDIT SONG ####
uid = "14567"
subopt = "title"
field_info = "B"

uid2 = "12332"
subopt2 = "rating"
field_info2 = "A"

assert edit_song(all_songs, uid, rating_map, subopt, field_info, allkeys) == "title"
assert edit_song(all_songs, uid2, rating_map, subopt2, field_info2, allkeys) == "rating"

#### save to CSV ####
filename1 = "goodmat_songs"
filename2 = "badmat_songs"
b = "Hello World"
c = "Cook food"
assert save_to_csv(all_songs, filename1) == -1
assert save_to_csv(all_songs, filename2) == -1

#### Load to CSV ####
assert load_from_csv(b, all_songs, rating_map, allkeys) == -1
assert load_from_csv(c, all_songs, rating_map, allkeys) == -1


