"""
Author: David Selassie Opoku
@DataFormat.py

DataFormat program formats the files into the appropriate structure 
for user by the similarity classes 
"""

from subprocess import check_output
import hdf5_getters as HDF5

    
"""
-Creates a user dictionary of songs and play counts and a list of songs from the 
Echo Nest Taste Profile dataset
-Input: Echo Nest Taste Profile dataset
-Output: 1)Nested dictionary --> {userID:{songID:playCount},...}
         2)List of unique SongID in Taste Profile dataset
"""
def parse_TasteProfile(tasteProfile):
    TP = open(tasteProfile, 'r')
    userDict = {} #Nested dictionary to store userID and songID:playCount mapping
    songDict = {} #Dictionary to store unique songIDs in Echo Nest Taste Profile dataset
    
    #create nested dictionary of userID to songID,playcount
    for taste in TP:
        userID, songID,playCount = taste.split()
        playCount = int(playCount)

        if( not userDict.has_key(userID)): #if userID not key of userDict 
            userDict[userID] = {songID:playCount} #create new userID key
        else:
            userDict[useIDr][songID] =playCount
            
        if(not songDict.has_key(songID)): 
            songDict[songID]=0 #Store a dummy value

    songList = songDict.keys()  #Save unique song ID into list
    return userDict, songList


#def rename_HDF5():

"""
-Creates a dictionary of a songID to features provided by the Million Song Dataset(MSD)
-Input: 1) path to root folder storing HDF5 MSD files: Ex './MillionSongSubset/data/'
        2) List of unique songIDs from Echo Nest Taste Profile dataset
-Output: A dictionary of songID to MSD feature mapping ---yet to decide on what features to 
         select 
"""
        
def create_song_dict(rootDir,songList):
    for songID in songList:
        songFilename = songID+".h5" #add .h5 extension to end of songID
        try:
            songPath = check_output("find rootDir -type f -name songFilename", shell=True).strip()
            songObject = HDF5.open_h5_file_read(songPath) #create HDF5 object
            songYear = HDF5.get_year(songObject)
            print "%s : %s" %(songID,songYear) #This is just a test print statement
        except: 
            pass #ignore system exit error from check_output command
    
        
    

