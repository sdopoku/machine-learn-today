"""
Author: David Selassie Opoku
@DataFormat.py

DataFormat program formats the files into the appropriate structure 
for user by the similarity classes 
"""

from subprocess import check_output
import hdf5_getters as hdf5
import os
import pandas as pd


def parse_taste_profile(taste_profile):
    """
    -Creates a user dictionary of songs and play counts and a list of songs from the 
    Echo Nest Taste Profile dataset
    -Input: Echo Nest Taste Profile dataset
    -Output: 1)Nested dictionary --> {userID:{songID:playCount},...}
             2)List of unique SongID in Taste Profile dataset
    """

    tp = open(taste_profile, 'r')
    user_dict = {} #Nested dictionary to store userID and songID:playCount mapping
    song_dict = {} #Dictionary to store unique songIDs in Echo Nest Taste Profile dataset
    
    #create nested dictionary of userID to songID,playcount
    for taste in tp:
        user_id, song_id,play_count = taste.split()
        play_count = int(play_count)

        if( not user_dict.has_key(user_id)): #if user_id not key of user_dict 
            user_dict[user_id] = {song_id:play_count} #create new userID key
        else:
            user_dict[user_id][song_id] =play_count
            
        if(not song_dict.has_key(song_id)): 
            song_dict[song_id]=0 #Store a dummy value

    #song_list = song_dict.keys()  #Save unique song_id into list
    tp.close()
    return user_dict, song_dict


def get_track_filenames(root_dir):#,dest_filename):
    #mssf=open(dest_filename,'w')
    mssf_test = []
    
    for root, dirs, files in os.walk(root_dir,topdown=False):
        for name in files:
            filename = root+"/"+name
            #mssf.write(filename)
            mssf_test.append(filename)
    return list(set(mssf_test))



def create_songfeature_file(trhdf5,song_dict,output_file):
    song_features = open(output_file,'w')
    header_str = "sid, samprt, danc, dur, end_fad_in,energy, bars_conf, bars_st, beats_conf, beats_st, sec_conf, sec_st, seg_conf, seg_ld_max, seg_ld_maxtm, seg_ld_st, seg_pch, seg_st, seg_tmb, tat_conf, tat_st, key, key_conf, ld, mode, mode_conf, st_fd_out, tempo, tm_sig, tm_sig_conf, art_fam, art_hot, song_hot\n"  
    song_features.write(header_str)

    for hdf5_path in trhdf5:
        try:
            hdf5_file = pd.HDFStore(hdf5_path)
            
            song_id = hdf5_file["/metadata/songs"].values[0][-3]
            if song_dict.has_key(song_id):
                analysis = hdf5_file["/analysis/songs"].values[0]
                analist = list(analysis[2:30])
                analist.insert(0,analysis[0])
                metadata = hdf5_file["/metadata/songs"].values[0]
                metalist = [metadata[2],metadata[3], metadata[-4]]
                analist.extend(metalist)
                analist.insert(0,song_id)
                feature_str = str(analist).strip('[]') +"\n"
                song_features.write(feature_str)
            

        except:
            print "Cannot open file: %s" %(hdf5_path)
            pass
        hdf5_file.close()
    song_features.close()
        
    

