print ("0123456789012345678901234567")

print ("Rank".ljust (5), "Player".ljust (20), "HR".rjust (3), sep = "")
print ('1'.center (5), "Barry Bonds".ljust (20), "762".rjust (3), sep = "")
print ('2'.center (5), "Hank Aaron".ljust (20), "755".rjust (3), sep = "")
print ('3'.center (5), "Babe Ruth".ljust (20), "714".rjust (3), sep = "")


barry_score = 762
hank_score = 755
babe_score = 714
print ("Rank".ljust (5), "Player".ljust (20), "HR".rjust (3), sep = "")
print ("{0:^5s}".format ('1'), "{0:<20s}".format ("Barry Bonds"), "{0:>3n}".format (barry_score), sep = "")
print ("{0:^5s}".format ('2'), "{0:<20s}".format ("Hank Aaron"), "{0:>3n}".format (hank_score) , sep = "")
print ("{0:^5s}".format ('3'), "{0:<20s}".format ("Babe Ruth"), "{0:>3n}".format (babe_score), sep = "")
