s = {"Always", "up.", "give", "Never"}
s.discard ("Always")
print (" ".join (sorted (s, key = len, reverse = True)))


#### OUTPUT LOG ####
#Never give up.
