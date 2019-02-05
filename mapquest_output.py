# Richmond Horikawa
# ID: 18715219

class Steps:
    def __init__(self, directions: list) -> None:
        'Initialize the Steps object'
        self._steps = directions

    def add(self, directions: list) -> None:
        'Append additional directions to the current list of directions'
        for element in directions:
            self._steps.append(element)

    def peek(self) -> list:
        'Look at all of the directions stored in the current list'
        return self._steps

    def get_result(self) -> None:
        'Print out the directions'
        print('DIRECTIONS')
        for item in self._steps:
            print(item)

class TotalDistance:
    def __init__(self, distance: float) -> None:
        'Initialize the TotalDistance object'
        self._dist = distance
        
    def add(self, distance: float) -> None:
        'Add the distance to the current total'
        self._dist += distance

    def peek(self) -> float:
        'Look at current total for the distance of the trip'
        return self._dist
        
    def get_result(self) -> None:
        'Print out the total distance of the trip'
        print('TOTAL DISTANCE: ' + str(round(self._dist)) + ' miles')

class TotalTime:
    def __init__(self, time: float) -> None:
        'Initialize the TotalTime object'
        self._time = time
        
    def add(self, time: float) -> None:
        'Add the time to the current total'
        self._time += time

    def peek(self) -> float:
        'Look at the current total for the time of the trip'
        return self._time
        
    def get_result(self) -> None:
        'Print out the total time of the trip'
        print('TOTAL TIME: ' + str(round(self._time)) + ' minutes')

class LatLongs:
    def __init__(self, latlongs: list) -> None:
        'Initialize the LatLongs object'
        self._latlongs = latlongs
        
    def add(self, latlongs: list) -> None:
        'Add on the second coordinate to the list of coordinates'
        self._latlongs.append(latlongs[2])
        self._latlongs.append(latlongs[3])
        
    def peek(self) -> list:
        'Look at all of the coordinates stored in the current list'
        return self._latlongs
        
    def get_result(self) -> None:
        'Print out all of the coordinates'
        print('LATLONGS')
        count = 1
        while count < len(self._latlongs):
            print(self._latlongs[count-1] + ' ' + self._latlongs[count])
            count += 2

class Elevation:
    def __init__(self, elevations: int) -> None:
        'Initialize the Elevation object'
        self._elevations = [elevations]

    def add(self, elevations: int) -> None:
        'Add on the elevation measurement to the current list'
        self._elevations.append(elevations)

    def peek(self) -> list:
        'Look at the current list of elevations'
        return self._elevations

    def get_result(self) -> None:
        'Print out all of the elevations'
        print('ELEVATIONS')
        for element in self._elevations:
            print(element)
        
