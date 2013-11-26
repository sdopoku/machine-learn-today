"""
Author: Krithika Raghavan
@SongSimilarityCalculator.py

This program finds the top 5 similar songs of a given user ID. 
It returns the 5 songs most similar to the user's most frequently listened song
Requires : - userDict and songList from the Dataparser program
		   - songmatrix which is the euclidean distance between the songs in the songList 
"""

import numpy as np
import DataFormat as df
import bottleneck as bn
import pandas p


userDict = {}
songList = ()
songmatrix
songdataframe
top5similarsongs

#def initsimilaritycalculator:

"""
- Initilaizes the variables used by SongSimilarityCalculator program
- Gets the userDict, songList and songmatrix from the Dataparser program

------
For now, this program generates a random 300X300 song data matrix 
should be replaced once the input is available from the Dataparser program
------

"""
def initsimilaritycalculator:
	songmatrix = np.random.random((300, 300))
	songdataframe = p.DataFrame(songmatrix, index = songList, column = songList)
	userDict, songList = df.parse_TasteProfile(tasteProfile)
	songmatrix

#def calcsimilarity(userid):

"""
- Calculates the top 5 similar songs for a given user
- Input: 1. userid
- Output 2. Array of top 5 songs(array of 5 songids) similar to the most frequently played song (by user = userid) 
"""
def calcsimilarity(userid):
	totalplaycount,meanplaycount = 0,0;
	usersongs = userDict[userid]
	totalnumofsongs = len(usersongs)

	for songid,pc in usersongs.iteritems():
		totalplaycount = totalplaycount + pc

	meanplaycount = totalplaycount/totalnumofsongs
	highestnormalizedpc = 0.00
	highnormpcsongid

	for songid, pc in usersongs.iteritems():
		usersongs[songid] = pc/meanplaycount
		if(usersongs[songid] > highestnormalizedpc):
			highestnormalizedpc = usersongs[songid]
			highnormpcsongid = songid




	return top5similarsongs = songdataframe.loc[highnormpcsongid][bn.argpartsort(-songdataframe.loc[highnormpcsongid], 5)[:5])].index.values

