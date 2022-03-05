# Basic Moon Weight Function

def moon_weight(your_weight, moon=0.165):
    for year in range(1, 6):
        weight_on_moon = your_weight * moon
        weight_on_moon += year
        # print("Year {0} = {1}".format(year, weight_on_moon))
        # print("Year %s =  %s" % (year, weight_on_moon))
        print(f"Year {year} = {weight_on_moon}")


moon_weight(210)
