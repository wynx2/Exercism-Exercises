"""Module for scoring darts"""
import math

def score(x_coordinate, y_coordinate):
    """Function to score a dart throw"""
    
    if check_in_circle(x_coordinate, y_coordinate, 0, 0, 1):        
        return 10      
    if check_in_circle(x_coordinate, y_coordinate, 0, 0, 5):
        return 5
    if check_in_circle(x_coordinate, y_coordinate, 0, 0, 10):
        return 1
    return 0
    
        
def check_in_circle(x_coordinate,y_coordinate, center_x, center_y, radius):
    distance = math.sqrt((x_coordinate - center_x)**2 + (y_coordinate - center_y)**2)
    return distance <= radius