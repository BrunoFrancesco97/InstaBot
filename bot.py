import instaloader
import numpy as np
import sys


TYPE_OF_WRITING = 'w'
NAME_OF_FILE_FOLLOWING_DONT_FOLLOW_YOU_BACK = 'follower.txt'
if len(sys.argv) == 3:
    L = instaloader.Instaloader()
    # Login
    try:
        L.login(sys.argv[1], sys.argv[2]) #It doesn't support 2FA
    except:
        print("Invalid username or password!")
    else:
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, sys.argv[1]) 
        follow_list = [] #List of followers
        following_list = [] #List of following
        for followee in profile.get_followers():
            follow_list.append(followee.username)
        
        print("Follower detected: "+str(len(follow_list)))
        for following in profile.get_followees():
            following_list.append(following.username)

        print("Number of following detected: "+str(len(following_list)))
        no_follower = np.setdiff1d(following_list,follow_list)
        print("Number of people that aren't following you back: "+str(len(no_follower)))
        file = open(NAME_OF_FILE_FOLLOWING_DONT_FOLLOW_YOU_BACK,TYPE_OF_WRITING) 
        count = 0
        for person in no_follower:
            file.write(no_follower[count])
            count = count + 1
            file.write("\n")
        file.close()
        print("You can find list of people who don't follow you back inside file follower.txt!")
        print("End")
else:
    print("Invalid number of arguments!\nProgram expects a number of 3 arguments, you can follow this format:\npython nomefile.py usernameInsta passwordInsta")