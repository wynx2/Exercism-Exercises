def check_tolerance(color):
    tolerance_band = {'violet':'0.1%',
                      'grey':'0.05%',
                      'blue':'0.25%',
                      'green':'0.5%',
                      'brown':'1%',
                      'red':'2%',
                      'gold':'5%',
                      'silver':'10%'}

    
    return f" ±{tolerance_band[color]}"

def resistor_label(colors):
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




    if len(colors) == 5:
        first_two = str(band_lookup[colors[0]]) + str(band_lookup[colors[1]])
        zero_sum = band_lookup[colors[3]]
        first_two += str(band_lookup[colors[2]])
    elif len(colors) == 1:
        return "0 ohms"
    else:
        first_two = str(band_lookup[colors[0]]) + str(band_lookup[colors[1]])
        zero_sum = band_lookup[colors[2]]

    converted_number = int(first_two) * (10 ** zero_sum)
    print(colors[-1])
    if converted_number >= 1e9:
        return f"{converted_number / 1000000000:.3g} gigaohms{check_tolerance(colors[-1])}"
    if converted_number >= 1e6:
        return f"{converted_number / 1000000:.3g} megaohms{check_tolerance(colors[-1])}"
    if converted_number >= 1e3:
        return f"{converted_number / 1000:.3g} kiloohms{check_tolerance(colors[-1])}"
    return f"{converted_number} ohms{check_tolerance(colors[-1])}"

