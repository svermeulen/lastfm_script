#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#F12::
    Run python lastfm_love_current_track.py
    Return

