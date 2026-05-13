"""Module to test for aliquot sum"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or isinstance(number, float):
        raise ValueError("Classification is only possible for positive integers.")
        
    aliquot_factors = [potential_factor for potential_factor in range(1,number) if number % potential_factor == 0]
    aliquot_sum = sum(aliquot_factors)
    if aliquot_sum == number:
        return "perfect"
    if aliquot_sum > number:
        return "abundant"
    return "deficient"
        
        
