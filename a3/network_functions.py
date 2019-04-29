""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    lines = profiles_file.readlines()
    i = 0
    while i < len(lines):
        j = i
        while j < len(lines) and lines[j] != '\n':
            name = reverse(lines[j])
            j = j+1
            while j < len(lines) and not(',' in lines[j]) and lines[j] != '\n':
                help_function1(name, person_to_networks, lines, j)
                j = j+1
            while j < len(lines) and lines[j] != '\n':
                help_function2(name, person_to_friends, lines, j)
                j = j+1
        i = j+1
    arrange(person_to_friends)
    arrange(person_to_networks)

def help_function1(name: str, person_to_networks: Dict[str, List[str]], \
                   lines: List, j: int) -> None:
    """add the information of networks of the person name to person_to_networks
    Docstring examples not given since result depends on input data.
    """
    if name not in person_to_networks:
        person_to_networks[name] = []                             
    if lines[j].strip() not in person_to_networks[name]:
        person_to_networks[name].append(lines[j].strip()) 

def help_function2(name: str, person_to_friends: Dict[str, List[str]],\
                   lines: List, j: int) -> None:
    """add the information of friends of the person name to person_to_friends
    Docstring examples not given since result depends on input data.
    """
    if name not in person_to_friends:
        person_to_friends[name] = []                        
    if reverse(lines[j]) not in person_to_friends[name]:
        person_to_friends[name].append(reverse(lines[j]))    
    


def reverse(line: str) -> str:
    """ reverse "LastName, FirstName(s)" format to "FirstName(s) LastName" 
    format
    >>> reverse('a, j\\n')
    'j a'
    """
    
    line1 = line.strip()
    x = line1.find(',')
    a = line1[: x]
    b = line1[x+2:]
    return b+' '+a

def arrange(l: Dict[str, List[str]]) -> None:
    """arrange the list in the dictionary l in alphabetical order
    >>> d= {'a':['a','s'], 'b':['f','d']}
    >>> arrange(d)
    >>> d
    {'a': ['a', 's'], 'b': ['d', 'f']}
    """
    for key in l:
        l[key].sort()
       
            

def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """
    Return the average number of friends that people who appear as keys 
    in the given "person to friends" dictionary have. 
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy', \
    'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': \
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'],\
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'],\
    'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett',\
    'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money',\
    'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],\
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'],\
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'],\
    'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett'\
    , 'Phil Dunphy']} 
    >>> get_average_friend_count(person_to_friends) == 28/11
    True
    """
    n = 0
    m = 0
    for key in person_to_friends:
        n = n+1
        m = m+len(person_to_friends[key])
    if n == 0:
        return 0.0
    return m/n

    
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "last name to first names" dictionary based on the given
    "person to friends" dictionary. The returned dictionary should contain
    every person whose name appears in the given dictionary (as a key or in
    a value list). The keys in the returned dictionary should be the last names
    of people in the given dictionary. The values are lists of the first names
    (in alphabetical order) of people with a given last name
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy',\
    'Gloria Pritchett'], 'Claire Dunphy': \
    ['Jay Pritchett','Mitchell Pritchett', 'Phil Dunphy']}
    >>> get_families(person_to_friends)
    {'Pritchett': ['Gloria', 'Jay', 'Mitchell'], 'Dunphy': ['Claire', 'Phil']}
    """
    family = {}
    for key in person_to_friends:
        if key[last_name(key)+1:] not in family:
            family[key[last_name(key)+1:]] = [key[:last_name(key)]]
        elif key[:last_name(key)] not in family[key[last_name(key)+1:]]:
            family[key[last_name(key)+1:]].append(key[:last_name(key)])
        for value in person_to_friends[key]:
            if value[last_name(value)+1:] not in family:
                family[value[last_name(value)+1:]] = [value[:last_name(value)]]
            elif value[:last_name(value)] not in family[value[last_name(value)+1:]]:
                family[value[last_name(value)+1:]].append(value[:last_name(value)])
    arrange(family)
    return family

def last_name(element: str) -> int:
    """get the place of the white space before last name from the element given
    >>> last_name('Manny Delgado')
    5
    >>> last_name('Man Yi Wang')
    6
    """
    i = len(element)-1
    while element[i] != ' ':
        i = i-1
    return i


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    Return a "network to people" dictionary based on the given
    "person to networks" dictionary. The values in the dictionary 
    are sorted alphabetically.
    >>> person_to_networks={'C D': ['P T A'], \
    'M D': ['C C'], 'M P': ['L A'],\
    'G P': ['P T A']} 
    >>> invert_network(person_to_networks)
    {'P T A': ['C D', 'G P'], 'C C': ['M D'], 'L A': ['M P']}


    """
    invert = {}
    for key in person_to_networks:
        for value in person_to_networks[key]:
            if value not in invert:
                invert[value] = [key]
            else:
                invert[value].append(key)
    arrange(invert)
    return invert


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """
    Given a "person to friends" dictionary and the name of a person
    (in the same format as the dictionary keys), return the list of
    names of people who are friends of the named person's friends.
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy', \
    'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
    'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett',\
    'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', \
    'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
    'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], \
    'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], \
    'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': \
    ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett':\
    ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy':\
    ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']} 
    >>> get_friends_of_friends(person_to_friends, 'Alex Dunphy')
    ['Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']
    """
    friends_of_friends = []
    for value in person_to_friends[person]:
        if value in person_to_friends:
            for value2 in person_to_friends[value]:
                if value2 != person:
                    friends_of_friends.append(value2)
    friends_of_friends.sort()
    return friends_of_friends
        
        
def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """
    return the friend recommendations for the given person as a list 
    of tuples where the first element of each tuple is a potential friend's 
    name (in the same format as the dictionary keys) and the second element 
    is that potential friend's score.
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy', \
    'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', \
    'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett',\
    'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', \
    'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], \
    'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'],\
    'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy'\
    : ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
    'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', \
    'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', \
    'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']} 
    >>> person_to_networks={'Claire Dunphy': ['Parent Teacher Association'],\
    'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'],\
    'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
    ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy':\
    ['Real Estate Association'], 'Gloria Pritchett': ['Parent Teacher Association']} 
    >>> make_recommendations('Jay Pritchett', person_to_friends, person_to_networks)
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), ('Phil Dunphy', 1)]
    >>> make_recommendations('Claire Dunphy', person_to_friends, person_to_networks)
    [('Luke Dunphy', 3), ('Gloria Pritchett', 2), ('Cameron Tucker', 1), ('Manny Delgado', 1)]
    """
    result = []
    b = []
    for key in person_to_friends:
        for value in person_to_friends[key]:
            if value != person and ((person not in person_to_friends) or \
                                    (value not in person_to_friends[person])) \
               and value not in b:
                a = mark(person, person_to_friends, person_to_networks, value)
                if a > 0:
                    result.append((value, a))
                b.append(value)
    get_sort(result)
    return result

def mark(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]], value1: str) -> int:
    """
    get the score for value1 depending on 
    For every mutual friend that the person and the potential friend have, 
    add 1 point to the potential friend's score
    For each network that the person and the potential friend both belong to, 
    add 1 point to the potential friend's score
    If the person has the same last name as the potential friend, 
    add 1 point to the potential friend's score, 
    but only if they have something else in common 
    (mutual friend(s), mutual network(s), or both).
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy', \
    'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett',\
    'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': \
    ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
    'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker':\
    ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy':\
    ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy',\
    'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
    'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', \
    'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', \
    'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']} 
    >>> person_to_networks={'Claire Dunphy': ['Parent Teacher Association'], \
    'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'],\
    'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker':\
    ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
    ['Real Estate Association'], 'Gloria Pritchett': ['Parent Teacher Association']} 
    >>> mark('Jay Pritchett', person_to_friends, person_to_networks, 'Mitchell Pritchett')
    2
    """
    last_score = 0
    friend_score = friend(person, person_to_friends, value1)
    network_score = network(person, person_to_networks, value1)
    if network_score > 0 or friend_score > 0:
        if person[person.find(' ')+1:] == value1[value1.find(' ')+1:]:
            last_score = last_score + 1
    last_score = last_score + friend_score + network_score
    return last_score


def friend(person: str, person_to_friends: Dict[str, List[str]], \
    value1: str) -> int:
    """ For every mutual friend that the person and the potential friend 
    have, add 1 point to the potential friend's score 
    >>> person_to_friends={'Jay Pritchett': ['Claire Dunphy', \
    'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': \
    ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], \
    'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], \
    'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'],\
    'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', \
    'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money',\
    'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'],\
    'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], \
    'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'],\
    'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', \
    'Phil Dunphy']} 
    >>> friend('Jay Pritchett', person_to_friends,'Mitchell Pritchett')
    1
    
    """
    frien_d = []
    for key in person_to_friends:
        for value in person_to_friends[key]:
            if value not in frien_d and value in person_to_friends and \
               value != person and value != value1:
                if person in person_to_friends and \
                   value in person_to_friends[person] and \
                   value1 in person_to_friends[value]:
                    frien_d.append(value)
                elif value1 in person_to_friends and \
                     value in person_to_friends[value1] and \
                     person in person_to_friends[value]:
                    frien_d.append(value)
    friend_score = len(frien_d)
    return friend_score


def network(person: str, \
    person_to_networks: Dict[str, List[str]], value1: str) -> int:
    """For each network that the person and the potential friend both 
    belong to, add 1 point to the potential friend's score
    >>> person_to_networks={'Claire Dunphy': ['Parent Teacher Association'], \
    'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'],\
    'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker':\
    ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy':\
    ['Real Estate Association'], 'Gloria Pritchett':\
    ['Parent Teacher Association']} 
    >>> network('Jay Pritchett', person_to_networks,'Mitchell Pritchett')
    0
    
    """
    networ_k = []
    networks_to_people = invert_network(person_to_networks)
    for key in networks_to_people:
        if value1 in networks_to_people[key] and person in networks_to_people[key]:
            networ_k.append(key)
    network_score = len(networ_k)
    return network_score


def get_sort(result: List[Tuple[str, int]]) -> None:
    """ The recommendations should be sorted from highest to lowest score. 
    If multiple people have the same score, they should be sorted 
    alphabetically.
    >>> result=[('Manny Delgado', 1), ('Luke Dunphy', 3), ('Cameron Tucker', 1)]
    >>> get_sort(result)
    >>> result
    [('Luke Dunphy', 3), ('Cameron Tucker', 1), ('Manny Delgado', 1)]
    
    """
    end = len(result)-1
    while end != 0:
        for i in range(end):
            if result[i][1] < result[i+1][1]:
                result[i], result[i+1] = result[i+1], result[i]
            elif result[i][1] == result[i+1][1]:
                if result[i][0] > result[i+1][0]:
                    result[i], result[i+1] = result[i+1], result[i]
        end = end - 1
        
                
                


if __name__ == '__main__':
    import doctest
    doctest.testmod()
