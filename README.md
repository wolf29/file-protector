file-protector
==============

Protects Downloadable Files from Screen Scraping
If you have a lot of pdf files behind a pay-wall, and don't want them to be sucked out by a spidering program like Google.com or Bing!, then you need to set up something like what this application creates.  This is written in python to make developing the structure easier, even if you do not have UNIX on your desktop.  The first version may only work on Linux/UNIX.

What this script is supposed to do:
1.) create a randomly-named folder for each paid download
2.) put a payload of an index.htm and the paid download into its own folder
3.) send an email to you with the paths in which every file have been placed.  It is easy to forget a series of paths with 32-char random folder names. Most people will appreciate the help.
4.) display to standard output, the paths to the files.

