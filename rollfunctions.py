import cubelist as cl
import matconfig as mc
import seriesconfig as sc
import rarityconfig as rc
import math, random

# Function for returning series off of text input
def text_to_series(txt): # <<CHECKED AND WORKS AS INTENDED>>
    for s in range(len(sc.series_text_list)):
        if txt == sc.series_text_list[s]:
            return sc.series_true_list[s] # Match positions of stextlist vs struelist
    raise ValueError('---FATAL ERROR---: Invalid Series Input. Check terminal.') # Raise error if invalid series (won't get raised if something is returned)

# Function to create an empty array with specific length, and specific items to fill it with
def create_empty_array(alength, emptyfill=0): # <<CHECKED AND WORKS AS INTENDED>>
    n = []
    for _ in range(alength):
        n.append(emptyfill) # add text to array alength times
    return n # return array back to user

def randfloat(a, b): # <<CHECKED AND WORKS AS INTENDED>>
    return a + ((b - a) * random.random()) # bypassing the random.randrange()'s integer limitations

# Function to get number of dropped items, given the rarity.
def get_mats_from_cuberarity(rarity, iterations, nrbool=False): # <<CHECKED AND WORKS AS INTENDED>>
    dropchance = lcount = hcount = 0 # base counting items, /by0 error will be raised if they aren't filled (purposeful)
    for n in range(len(rc.raritylist)):
        if rarity == rc.raritylist[n][0]: # set dropchance, lcount, hcount based off of rarity
            if nrbool:
                dropchance = rc.raritylist[n][2] # nrbool = true, so roll rare mats
            else:
                dropchance = rc.raritylist[n][1] # nrbool = false, so don't roll rare mats
            lcount, hcount = rc.raritylist[n][3] * iterations, rc.raritylist[n][4] * iterations
    if randfloat(0, 100) < dropchance:
        return random.randint(lcount, hcount) # return random integer between lowest count and highest count
    else:
        return 0

# Function to get array of all counts of mat's name inside of a specific cube
def get_matnames_from_cube(item): # <<CHECKED AND WORKS AS INTENDED>>
    oarr = create_empty_array(25) # fill with normal mat count of names
    for i in range(len(item) - 3):
        itemname = item[i+3] # itemname is a string, like "Resin" or "Shards"
        if itemname in mc.mat_called_name:
            oarr[mc.mat_called_name.index(itemname)] += 1 # increment the array's mat name
        else:
            raise ValueError('---FATAL ERROR---: Invalid Material Name Input. Check terminal.') # Raise error if invalid material name (won't get raised if something is right)
    return oarr
