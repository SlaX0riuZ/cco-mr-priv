import cubelist as cl
import matconfig as mc
import seriesconfig as sc
import rarityconfig as rc
import math, random

# Function for returning series off of text input
def text_to_series(txt): # <<CHECKED AND WORKS AS INTENDED>>
    for s in range(len(sc.series_text_list)):
        if txt == sc.series_text_list[s]: return sc.series_true_list[s] # Match positions of stextlist vs struelist
    raise ValueError('---FATAL ERROR---: Invalid Series Input. Check terminal.') # Raise error if invalid series

# Function to create an empty array with specific length, and specific items to fill it with
def create_empty_array(alength, emptyfill): # <<CHECKED AND WORKS AS INTENDED>>
    n = []
    for _ in range(alength): n.append(emptyfill) # add text to array alength times
    return n # return array back to user

# Function to get materials from a specific item
def get_mats_from_item(item):
    irarity = item[1] # get item rarity from item
    ndrop = rdrop = lcount = hcount = currentdrop = 0 # base counting items, /by0 error will be raised if they aren't filled (purposeful)
    for n in range(len(rc.raritylist)):
        if irarity == rc.raritylist[n][0]:
            ndrop, rdrop = rc.raritylist[n][1], rc.raritylist[n][2]
            lcount, hcount = rc.raritylist[n][3], rc.raritylist[n][4]
    # Finish function:
        # Add random values to pick if mats drop or not (ndrop and rdrop%)
        # If ndrop and rdrop pass, randint between lcount and hcount
        # Return value
    # Other things to do:
        # Add a way to count for multiple iterations of something (ie, a cube has two "Hot" tags)
        # This bumps min by +(minval) and max by +(maxval) (ie, 1-32 --> 2-64)
    
