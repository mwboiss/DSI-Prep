def find_complement(event, sample):
    # Declare a new list to collect and return
    new_list = []

    # Iterate through the sample space
    for obj in sample:
        # If the object isn't in the event
        if obj not in event:
            # Add it to the new list
            new_list.append(obj)

    # Sort and return the list
    new_list.sort()

    return new_list

def find_complement(event, sample):
    # Convert the lists to sets
    event_set, sample_set = set(event), set(sample)

    # Find the difference between the two sets
    diff = sample_set.difference(event_set)

    # Return the new set
    return diff