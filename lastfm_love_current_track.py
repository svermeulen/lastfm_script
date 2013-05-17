#!/usr/bin/python2 

import os
import pylast
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("settings.ini")

API_KEY = config.get("settings", "API_KEY")
API_SECRET = config.get("settings", "API_SECRET")
username = config.get("settings", "USERNAME")
password_hash = pylast.md5(config.get("settings", "PASSWORD"))

def loveLastTrack():

    print "Contacting last.fm...",
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

    user = network.get_user(username)

    # try now playing first
    currentTrack = user.get_now_playing()

    if not currentTrack:
        # Failing that just love the last track played instead 
        # this is necessary for some apps, like subsonic, which do not play nicely with the now playing feature for some reason
        lastPlayed = user.get_recent_tracks(1)[0]

        if not lastPlayed:
            print "Error: Could not find now playing track or last played track!"
            return

        currentTrack = lastPlayed.track

    currentTrack.love()

    # Make sure it was correct
    lastLovedTrack = str(user.get_loved_tracks(limit=1)[0][0])

    print "Done"
    print
    if str(currentTrack) == str(lastLovedTrack):
        print "'"+ str(currentTrack) + "' has been marked as loved"
    else:
        print "** Error ** '"+ str(currentTrack) + "' could not be marked as loved (most likely because it is already loved)"

if __name__ == "__main__":
    try:
        loveLastTrack()
    except Exception, e:
        print "Failed."
        print
        print "Errors occurred trying to contact last.fm.  Check your settings or network connection."
        print
    raw_input("Press any key to exit")
