"""Module for scoring darts"""
import math

def score(x, y):
    """Function to score a dart throw"""
    
    if check_in_circle(x, y, 0, 0, 1):        
        return 10      
    if check_in_circle(x, y, 0, 0, 5):
        return 5
    if check_in_circle(x, y, 0, 0, 10):
        return 1
    return 0
    
        
def check_in_circle(x,y, center_x, center_y, radius):
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    return distance <= radius