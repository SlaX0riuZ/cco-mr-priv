import matconfig as mc
import seriesconfig as sc
import rarityconfig as rc
import random

''' Functions for Utility '''

# Function for returning series off of text input
def text_to_series(txt, reverse=False):
    if reverse: # Series -> Text
        for s in range(len(sc.series_true_list)):
            if txt == sc.series_true_list[s]: return sc.series_text_list[s]
    else: # text -> Series
        for s in range(len(sc.series_text_list)):
            if txt == sc.series_text_list[s]: return sc.series_true_list[s]
    raise ValueError('---FATAL ERROR---: Invalid Series Input. Check terminal.')

# Function to create an empty array with specific length, and specific items to fill it with
def create_empty_array(alength, emptyfill=0):
    n = []
    for _ in range(alength): n.append(emptyfill)
    return n

# Function to return a random fload value, given start and end positions
def randfloat(a, b): return a + ((b - a) * random.random())

''' Functions for Cube Rolling/Mats/Rarity, etc. '''

# Function to get number of dropped items, given the rarity.
def get_mats_from_cuberarity(rarity, iterations, nrbool=False):
    dropchance = lcount = hcount = 0
    for n in range(len(rc.raritylist)):
        if rarity == rc.raritylist[n][0]:
            if nrbool: dropchance = rc.raritylist[n][2]
            else: dropchance = rc.raritylist[n][1]
            lcount, hcount = rc.raritylist[n][3] * iterations, rc.raritylist[n][4] * iterations
    if randfloat(0, 100) < dropchance: return random.randint(lcount, hcount)
    else: return 0

# Function to get array of all counts of mat's name inside of a specific cube
def get_matnames_from_cube(item):
    oarr = create_empty_array(26)
    for i in range(len(item) - 3):
        itemname = item[i+3]
        if itemname in mc.mat_called_name: oarr[mc.mat_called_name.index(itemname)] += 1
        else: raise ValueError('---FATAL ERROR---: Invalid Material Name Input. Check terminal.')
    return oarr

# Function to roll and pick a cube based off of roll chances from a given series
def roll_cube_from_series(series): #
    rollnumceiling, rolledcubeindex = 0, -1
    for cube in series: rollnumceiling += cube[2]
    rollnum = randfloat(0, rollnumceiling)
    while rollnum > 0:
        rolledcubeindex += 1
        try: rollnum -= series[rolledcubeindex][2]
        except: rollnum = rolledcubeindex = -1
    return series[rolledcubeindex]

# Function to link 'get_mats_from_cuberarity' to 'get_matnames_from_cube', returning an array of materials given a cube
def matarray_from_cube(cube):
    oarr = create_empty_array(33)
    mlist = get_matnames_from_cube(cube)
    for nmindex in range(0, 26):
        if mlist[nmindex] > 0: oarr[nmindex] = get_mats_from_cuberarity(cube[1], mlist[nmindex], False)
    rmtick = 26
    for rmindex in [10, 1, 13, 2, 18, 14, 25]:
        if (mlist[rmindex] > 0) and (cube[1] not in ['c', 'u', 'r', 'e', 'sp']): oarr[rmtick] = get_mats_from_cuberarity(cube[1], mlist[rmindex], True)
    return oarr

# Function to spin a certain amount of a series, returning the final material array
def spin_with_count(series, count):
    oarr = create_empty_array(33)
    for _ in range(count):
        spuncubematlist = matarray_from_cube(roll_cube_from_series(series))
        for j in range(33): oarr[j] += spuncubematlist[j]
    oarr.append(text_to_series(series, True))
    return oarr

# Function to rank top 5 series based off of highest count of material
def material_rank_with_spincount(material, spincount):
    oarr = create_empty_array(5, ['0', 0])
    sarray = []
    try: mindex = mc.mat_display_name.index(material)
    except ValueError: raise ValueError("Invalid material name.")
    for series in sc.series_true_list:
        sinparray = spin_with_count(series, spincount)
        sarray.append([sinparray[-1], sinparray[mindex]])
    for series in range(len(sarray)):
        for pos in range(5):
            if sarray[series][1] > oarr[pos][1]:
                oarr.pop(4)
                oarr.insert(pos, [sarray[series][0], sarray[series][1]])
                break
    print(f'Ranked Material: {material}')
    for p2 in range(5): print(f'Rank #{p2+1}: {oarr[p2][0]} - {oarr[p2][1]}')