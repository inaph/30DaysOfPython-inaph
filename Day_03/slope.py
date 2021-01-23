def slope_intercept(x1,y1,x2,y2):
    slope = (y2-y1)/(x2-x1)
    intercept = y1 - slope * x1
    return slope, intercept
print(" Slope and intercept of line with point (2,2) and (6,10) are ", slope_intercept(2,2,6,10)) 