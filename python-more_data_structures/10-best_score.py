#!/usr/bin/python3

def best_score(a_dictionary):
    # Return the key with the highest value if the dictionary exists
    if a_dictionary:
        return max(a_dictionary, key=a_dictionary.get)
    return None


if __name__ == "__main__":
    # Test dictionary and retrieving the best score
    a_dictionary = {
        'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10
    }
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    # Test with None to see if it correctly returns None
    best_key = best_score(None)
    print("Best score: {}".format(best_key))
