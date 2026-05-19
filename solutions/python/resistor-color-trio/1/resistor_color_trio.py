def label(colors):
    band_lookup = {'black':0,
                   'brown':1,
                   'red':2,
                   'orange':3,
                   'yellow':4,
                   'green':5,
                   'blue':6,
                   'violet':7,
                   'grey':8,
                   'white':9}

    first_two = str(band_lookup[colors[0]]) + str(band_lookup[colors[1]]) 
    zero_sum = band_lookup[colors[2]]
    converted_number = int(first_two) * (10 ** zero_sum)
    if converted_number >= 1e9:
        return f"{converted_number//1000000000} gigaohms"
    if converted_number >= 1e6:
        return f"{converted_number//1000000} megaohms"
    if converted_number >= 1e3:
        return f"{converted_number//1000} kiloohms"
    return f"{converted_number} ohms"