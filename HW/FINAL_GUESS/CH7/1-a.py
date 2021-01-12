from nation import Nation
import pickle

# input
nation_obj_list = []
infile = open ("UN.txt", 'r')
for line in iter (infile):
	nation_data_list = line.strip ().split (',')
	nation_obj_list.append (Nation (nation_data_list))
infile.close ()

# construct dictionary
nation_dict = {x._nation : x for x in nation_obj_list}

# output
outfile = open ("nationsDict.dat", 'wb')
pickle.dump (nation_dict, outfile, pickle.HIGHEST_PROTOCOL)
outfile.close ()



