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
import pandas as p


userDict = {}
songList = ()
songmatrix = []
songdataframe = p.DataFrame()
top5similarsongs = []
tasteProfile = 'D:/Personal/tempKia/MachineLearning/data/train_triplets_1M'

#def InitSimilarityCalculator:

"""
- Initilaizes the variables used by SongSimilarityCalculator program
- Gets the userDict, songList and songmatrix from the Dataparser program

------
For now, this program generates a random 300X300 song data matrix 
should be replaced once the input is available from the Dataparser program
------

"""
def InitSimilarityCalculator():
	userDict, songList = df.parse_TasteProfile(tasteProfile)
	songmatrix = np.random.random((len(songList), len(songList)))
	songdataframe = p.DataFrame(songmatrix, index = songList, columns = songList)
	

#def CalcSimilarSongs(userid):

"""
- Calculates the top 5 similar songs for a given user
- Input: 1. userid
- Output 2. Array of top 5 songs(array of 5 songids) similar to the most frequently played song (by user = userid) 
"""
def CalcSimilarSongs(userid):
	totalplaycount,meanplaycount = 0,0;
	usersongs = userDict[userid]
	totalnumofsongs = len(usersongs)

	for songid,pc in usersongs.iteritems():
		totalplaycount = totalplaycount + pc

	meanplaycount = totalplaycount/totalnumofsongs
	highestnormalizedpc = 0.00

	for songid, pc in usersongs.iteritems():
		usersongs[songid] = pc/meanplaycount
		if(usersongs[songid] > highestnormalizedpc):
			highestnormalizedpc = usersongs[songid]
			highnormpcsongid = songid




	top5similarsongs = songdataframe.loc[highnormpcsongid][bn.argpartsort(-songdataframe.loc[highnormpcsongid], 5)[:5]].index.values
	return top5similarsongs

#def CalcSimilarUsersSongs(userid):

"""
- Calculates the top 5 similar songs for a given user
- Input: 1. userid
- Output 2. Array of top 5 songs(array of 5 songids) that are played by a most similar user
"""
def CalcSimilarUsersSongs(userid):
	usersongsset = userDict[userid].keys()
	usersongintersection = p.DataFrame(index = [userid])
	top5similarusers = []
	for otheruserid in userDict.iteritems():
		otherusersongsset = userDict[otheruserid].keys()
		usersongintersection.insert(0, otheruserid, len(np.intersect1d(usersongsset,otherusersongsset, False)), False)
		top5similarusers = usersongintersection.loc[userid][bn.argpartsort(-usersongintersection.loc[userid], 5)[:5]].index.values
	unlistenedsongs = np.array([])
	for userid in top5similarusers:
		otherusersongsset = userDict[otheruserid].keys()
		np.union1d(unlistenedsongs, np.setdiff1d(otherusersongsset, usersongsset))
		if(len(unlistenedsongs) >= 5):
			break
	return unlistenedsongs

"""
Some sample user ids
>>> userDict.keys()[1]
'85c1f87fea955d09b4bec2e36aee110927aedf9a'
>>> userDict.keys()[2]
'a308e9cb88a72f2260526863f83ec6b9a65a6845'
>>> userDict.keys()[3]
'1b0bb9f249026df9c9620501188aa18af0bc6a78'
"""
def Test(userid):
        initsimilaritycalculator()
        print CalcSimilarSongs('85c1f87fea955d09b4bec2e36aee110927aedf9a')
