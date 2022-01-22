def find_complement(event, sample):
    event_set, sample_set = set(event), set(sample)
    diff = sample_set.difference(event_set)
    return diff

elst = set(range(0,10,2))
olst = set(range(1,10,2))
threelst = set(range(0,10,3))
totlst = set(range(0,10))

print(elst)
#print(olst)
print(threelst)
print(totlst)

#first of demorgan first law
onedemorgone = elst.union(threelst)
onedemorgone = find_complement(onedemorgone, totlst)
onedemorgtwo = find_complement(elst, totlst).intersection(find_complement(threelst, totlst))
print(onedemorgone)
print(onedemorgtwo)

twodemorgone = find_complement(elst.intersection(threelst), totlst)
twodemorgtwo = find_complement(elst, totlst).union(find_complement(threelst, totlst))

print(twodemorgone)
print(twodemorgtwo)
