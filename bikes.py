""" CSC108 Assignment 2 Starter code """

from typing import List, TextIO

# A set of constants, each representing a list index for station information.
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
IS_RENTING = 7
IS_RETURNING = 8

####### BEGIN HELPER FUNCTIONS ####################

def is_number(value: str) -> bool:
    """Return True if and only if value represents a decimal number.

    >>> is_number('csc108')
    False
    >>> is_number('  108 ')
    True
    >>> is_number('+3.14159')
    True
    """

    return value.strip().lstrip('-+').replace('.', '', 1).isnumeric()


# It isn't necessary to call this function to implement your bikes.py
# functions, but you can use it to create larger lists for testing.
# See the main block below for an example of how to do that.
def csv_to_list(csv_file: TextIO) -> List[List[str]]:
    """Read and return the contents of the open CSV file csv_file as a list of
    lists, where each inner list contains the values from one line of csv_file.

    Docstring examples not given since results depend on data to be input.
    """

    # Read and discard header.
    csv_file.readline()

    data = []
    for line in csv_file:
        data.append(line.strip().split(','))
    return data


####### END HELPER FUNCTIONS ####################

### SAMPLE DATA TO USE IN DOCSTRING EXAMPLES ####

SAMPLE_STATIONS = [
    [7087, 'Danforth/Aldridge', 43.684371, -79.316756, 23, 9, 14, True, True],
    [7088, 'Danforth/Coxwell', 43.683378, -79.322961, 15, 13, 2, False, False]]

HANDOUT_STATIONS = [
    [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 20, 11, True, True],
    [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907,
     15, 5, 10, True, True]]

#########################################

def clean_data(data: List[list]) -> None:
    """Convert each string in data to an int if and only if it represents a
    whole number, a float if and only if it represents a number that is not a
    whole number, True if and only if it is 'True', False if and only if it is
    'False', and None if and only if it is either 'null' or the empty string.

    >>> d = [['abc', '123', '45.6', 'True', 'False']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, True, False]]
    >>> d = [['ab2'], ['-123'], ['False', '3.2']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], [False, 3.2]]
    """
    for i in range(len(data)):
        for j in range(len(data[i])):
            if is_number(data[i][j]):
                if '.' not in data[i][j]:
                    data[i][j] = int(data[i][j])
                else:
                    return_float(i, j, data)
                if int(data[i][j]) == data[i][j]:
                    data[i][j] = int(data[i][j]) 
            sign_sign(i, j, data)

def return_float(i: int, j: int, data: List[list]) -> None:
    """convert data[i][j] to a float
    Precondition: data[i][j] represents a number that is a float
    
    >>>i=0
    >>>j=0
    >>>data=[['2.3']]
    >>>return_float(i, j, data)
    >>>data[i][j]
    2.3
    """
    if signal_number(data[i][j]):
        data[i][j] = float_number(data[i][j])
    else:
        data[i][j] = float_number(data[i][j][1:])
        data[i][j] = -data[i][j]    


    
    
    

def float_number(ch: str) -> float:
    """convert ch to a float 
    Precondition: ch represents a nmber that is just a float without any '-'
    
    >>>float_number('1.23')
    1.23
    >>>float_number('2.34')
    2.34
    """
    i = 0
    i = int(ch[:ch.find('.')])
    i = i+int(ch[ch.find('.')+1:])*0.1**(len(ch)-len(ch[:ch.find('.')+1]))
    return i

def signal_number(ch: str) -> bool:
    """return if or not ch represent a number that is positive
    
    >>>signal_number('-1')
    False
    >>>signal_number('2')
    True
    """
    if ch[0] == '-':
        return False
    else:
        return True

def sign_sign(i: int, j: int, data: List[list]) -> None:
    """return data[i][j] True if and only if it is 'True'.
    return data[i][j] False if and only if it is 'False'
    return data[i][j] None if and only if it is 'null' or the empty string
    
    >>>i=0
    >>>j=0
    >>>data=[['True']]
    >>>sign_sign(i, j, data)
    >>>data[i][j]
    True
    >>>i=0
    >>>j=0
    >>>data=[['False']]
    >>>sign_sign(i, j, data)
    >>>data[i][j]
    False
    """
    if data[i][j] == 'True':
        data[i][j] = True
    elif data[i][j] == 'False':
        data[i][j] = False
    elif data[i][j] == 'null' or data[i][j] == '':
        data[i][j] = None    

                        
                
           
                
                    


def get_station_info(station_id: int, stations: List[list]) -> list:
    """Return a list containing the following information from stations
    about the station with id number station_id:
        - station name
        - number of bikes available
        - number of docks available
    (in this order)

    Precondition: station_id will appear in stations.

    >>> get_station_info(7087, SAMPLE_STATIONS)
    ['Danforth/Aldridge', 9, 14]
    >>> get_station_info(7088, SAMPLE_STATIONS) 
    ['Danforth/Coxwell', 13, 2]
    """
    return_list = []
    for station in stations:
        if station[ID] == station_id:
            return_list.append(station[NAME])
            return_list.append(station[BIKES_AVAILABLE])
            return_list.append(station[DOCKS_AVAILABLE])
    return return_list


def get_total(index: int, stations: List[list]) -> int:
    """Return the sum of the column in stations given by index.

    Precondition: the items in stations at the position
                  that index refers to are ints.

    >>> get_total(BIKES_AVAILABLE, SAMPLE_STATIONS)
    22
    >>> get_total(DOCKS_AVAILABLE, SAMPLE_STATIONS)
    16
    """
    summ = 0
    for station in stations:
        summ = summ+station[index]
    return summ


def get_station_with_max_bikes(stations: List[list]) -> int:
    """Return the station ID of the station that has the most bikes available.
    If there is a tie for the most available, return the station ID that appears
    first in stations.

    Precondition: len(stations) > 0

    >>> get_station_with_max_bikes(SAMPLE_STATIONS)
    7088
    """
    the_id = stations[0][ID]
    max_bike_available = stations[0][BIKES_AVAILABLE]
    for station in stations:
        if station[BIKES_AVAILABLE] > max_bike_available:
            the_id = station[ID]
            max_bike_available = station[BIKES_AVAILABLE]
    return the_id


def get_stations_with_n_docks(n: int, stations: List[list]) -> List[int]:
    """Return a list containing the station IDs for the stations in stations
    that have at least n docks available, in the same order as they appear
    in stations.

    Precondition: n >= 0

    >>> get_stations_with_n_docks(2, SAMPLE_STATIONS)
    [7087, 7088]
    >>> get_stations_with_n_docks(5, SAMPLE_STATIONS)
    [7087]
    """
    id_list = []
    for station in stations:
        if station[DOCKS_AVAILABLE] >= n:
            id_list.append(station[ID])
    return id_list


def get_direction(start_id: int, end_id: int, stations: List[list]) -> str:
    """ Return a string that contains the direction to travel to get from
    station start_id to station end_id according to data in stations.

    Precondition: start_id and end_id will appear in stations.

    >>> get_direction(7087, 7088, SAMPLE_STATIONS)
    'SOUTHWEST'
    """
    for station in stations:
        if station[ID] == start_id:
            lat1 = station[LATITUDE]
            long1 = station[LONGITUDE]
        if station[ID] == end_id:
            lat2 = station[LATITUDE]
            long2 = station[LONGITUDE]     
    if lat1 < lat2:
        direction = 'NORTH'
    elif lat1 > lat2:
        direction = 'SOUTH'
    else:
        direction = ''
    if long1 < long2:
        direction = direction+'EAST'
    elif long1 > long2:
        direction = direction+'WEST'
    else:
        direction = direction+''
    return direction


def rent_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for the station in stations with id station_id as if a single bike was
    removed, leaving an additional dock available. Return True if and only
    if the rental was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available - 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available + 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> rent_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    for station in stations:
        if station[ID] == station_id:
            if station[IS_RENTING]:
                if station[BIKES_AVAILABLE] <= 0:
                    return False
                else:
                    station[BIKES_AVAILABLE] = station[BIKES_AVAILABLE]-1
                    station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE]+1
                    return True
            else:
                return False


def return_bike(station_id: int, stations: List[list]) -> bool:
    """Update the available bike count and the docks available count
    for station in stations with id station_id as if a single bike was added,
    making an additional dock unavailable. Return True if and only if the
    return was successful.

    Precondition: station_id will appear in stations.

    >>> station_id = SAMPLE_STATIONS[0][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    True
    >>> original_bikes_available + 1 == SAMPLE_STATIONS[0][BIKES_AVAILABLE]
    True
    >>> original_docks_available - 1 == SAMPLE_STATIONS[0][DOCKS_AVAILABLE]
    True
    >>> station_id = SAMPLE_STATIONS[1][ID]
    >>> original_bikes_available = SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    >>> original_docks_available = SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    >>> return_bike(station_id, SAMPLE_STATIONS)
    False
    >>> original_bikes_available == SAMPLE_STATIONS[1][BIKES_AVAILABLE]
    True
    >>> original_docks_available == SAMPLE_STATIONS[1][DOCKS_AVAILABLE]
    True
    """
    for station in stations:
        if station[ID] == station_id:
            if station[IS_RETURNING]:
                if station[DOCKS_AVAILABLE] <= 0:
                    return False
                else:
                    station[BIKES_AVAILABLE] = station[BIKES_AVAILABLE]+1
                    station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE]-1
                    return True
            else:
                return False    


def balance_all_bikes(stations: List[list]) -> int:
    """Calculate the percentage of bikes available across all stations
    and evenly distribute the bikes so that each station has as close to the
    overall percentage of bikes available as possible. Remove bikes from a
    station if and only if the station is renting and there is a bike
    available to rent, and return a bike if and only if the station is
    allowing returns and there is a dock available. Return the difference
    between the number of bikes rented and the number of bikes returned.

    >>> balance_all_bikes(HANDOUT_STATIONS)
    0
    >>> HANDOUT_STATIONS == [\
     [7000, 'Ft. York / Capreol Crt.', 43.639832, -79.395954, 31, 17, 14, True, True], \
     [7001, 'Lower Jarvis St / The Esplanade', 43.647992, -79.370907, \
     15, 8, 7, True, True]]
    True
    """
    average = 0
    i = 0
    number = 0
    number_return = 0
    number_rent = 0
    for station in stations:
        average = average+station[BIKES_AVAILABLE]
        i = i+station[CAPACITY]
    average = average/i
    for station in stations:
        number = round(station[CAPACITY]*average)
        if number > station[BIKES_AVAILABLE]:
            if station[IS_RETURNING]:
                number_return = number_return+(number-station[BIKES_AVAILABLE])
                station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE]\
                    -(number-station[BIKES_AVAILABLE])
                station[BIKES_AVAILABLE] = number
        if number < station[BIKES_AVAILABLE]:
            if station[IS_RENTING]:
                number_rent = number_rent+(station[BIKES_AVAILABLE]-number)
                station[DOCKS_AVAILABLE] = station[DOCKS_AVAILABLE]\
                    +(station[BIKES_AVAILABLE]-number)
                station[BIKES_AVAILABLE] = number
    return number_rent-number_return

if __name__ == '__main__':
    pass  

    # # To test your code with larger lists, you can uncomment the code below to
    # # read data from the provided CSV file.
    # stations_file = open('stations.csv')
    # bike_stations = csv_to_list(stations_file)
    # clean_data(bike_stations)

    # # For example,
    # print('Testing get_station_with_max_bikes: ', \
    #     get_station_with_max_bikes(bike_stations) == 7033)
