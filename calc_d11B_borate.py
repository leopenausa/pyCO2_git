def calc_d11B_borate(d11B_f, c, m):
    ''' Function that calculates d11B borate from d11B calcite
    If slope (m) > 1 then intercept (c) should be negative
    If slope (m) < 1 then intercept (c) should be possitive'''
    
    return (d11B_f - c) / m