m1 = '13x^3'
m2 = '0.43x^5.63'
def parse_monomial(m):
    co = 0
    var = ''
    expo = 0
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for val in m:
        if val in alph:
            var = val
            m = m.replace(val, '')
    poly = m.split('^')
    
    co = poly[0]
    expo = poly[1]
    
    if co.isdigit():
        co = int(co)
    else:
        co = float(co)

    if expo.isdigit():
        expo = int(expo)
    else:
        expo = float(expo)

    return co, var, expo

print(parse_monomial(m1))
print(parse_monomial(m2))