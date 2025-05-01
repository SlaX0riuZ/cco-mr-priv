import cubelist as cl
import matconfig as mc
import seriesconfig as sc
import rarityconfig as rc
import math, random

''' Functions for Utility '''

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

''' Functions for Cube Rolling/Mats/Rarity, etc. '''

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
    oarr = create_empty_array(26) # fill with normal mat count of names
    for i in range(len(item) - 3):
        itemname = item[i+3] # itemname is a string, like "Resin" or "Shards"
        if itemname in mc.mat_called_name:
            oarr[mc.mat_called_name.index(itemname)] += 1 # increment the array's mat name
        else:
            raise ValueError('---FATAL ERROR---: Invalid Material Name Input. Check terminal.') # Raise error if invalid material name (won't get raised if something is right)
    return oarr

# Function to roll and pick a cube based off of roll chances from a given series
def roll_cube_from_series(series): # <<CHECKED AND WORKS AS INTENDED>>
    rollnumceiling, rolledcubeindex = 0, -1
    for cube in series:
        rollnumceiling += cube[2] # Add roll chance from cube (ex: 13.33, 27.28)
    rollnum = randfloat(0, rollnumceiling) # Random number from 0 to total roll ceiling (should be ~100)
    while rollnum > 0:
        rolledcubeindex += 1
        try:
            rollnum -= series[rolledcubeindex][2] # decreases rollnum by cube's roll chance
        except:
            rollnum = rolledcubeindex = -1
    return series[rolledcubeindex]

# Function to link 'get_mats_from_cuberarity' to 'get_matnames_from_cube', returning an array of materials given a cube
def matarray_from_cube(cube): # <<CHECKED AND WORKS AS INTENDED>>
    # cube is imported as cube's array, ex: ["no", "e", 2.20, "heavy", "hard"]
    oarr = create_empty_array(33) # start with an array of all zeroes
    mlist = get_matnames_from_cube(cube) # get matname array from cube
    print(mlist)
    for nmindex in range(0, 26):
        if mlist[nmindex] > 0: # if there's at least 1 iteration of a given mat
            oarr[nmindex] = get_mats_from_cuberarity(cube[1], mlist[nmindex], False) # add mat rolls to cube's array
    rmtick = 26 # set tick to 26, starting position of raremats in typical mat array
    for rmindex in [10, 1, 13, 2, 18, 14, 25]:
        if (mlist[rmindex] > 0) and (cube[1] not in ['c', 'u', 'r', 'e', 'sp']):
            oarr[rmtick] = get_mats_from_cuberarity(cube[1], mlist[rmindex], True) # add mat rolls to cube's array
    return oarr


