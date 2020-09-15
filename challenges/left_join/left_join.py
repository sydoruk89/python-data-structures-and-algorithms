def left_join(t1, t2):
    """
    It combines the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
    The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
    """
    new_table = {}

    for key in t1:
        val  = None
        new_table[key] = [t1[key]]
        if key in t2:
            val = t2[key]
        new_table[key].append(val)
    return new_table
