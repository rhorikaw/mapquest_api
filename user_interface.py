# Richmond Horikawa
# ID: 18715219

import mapquest
import mapquest_output
import urllib

def read_num_locations() -> int:
    'Read the number of locations the user will input'
    user_input = int(input())
    while user_input < 2:
        user_input = int(input())
    return user_input

def read_locations(num: int) -> list:
    'Read all of the locations input by the user'
    location_list = []
    while len(location_list) < num:
        location_input = input()
        location_list.append(location_input)
    return location_list

def read_num_outputs() -> int:
    'Read the number of outputs the user expects'
    user_input = int(input())
    while user_input < 1:
        user_input = int(input())
    return user_input

def read_outputs(num: int) -> list:
    'Read all of the type of outputs the user expects'
    output_list = []
    while len(output_list) < num:
        output_type = input()
        output_list.append(output_type)
    return output_list

def create_object(output: str, data: dict) -> object:
    'Create an object depending on the input given'
    if output == 'STEPS':
        return mapquest_output.Steps(mapquest.return_directions(data))
    elif output == 'TOTALDISTANCE':
        return mapquest_output.TotalDistance(mapquest.return_distance(data))
    elif output == 'TOTALTIME':
        return mapquest_output.TotalTime(mapquest.return_time(data))
    elif output == 'LATLONG':
        return mapquest_output.LatLongs(mapquest.return_latlongs(data))
    elif output == 'ELEVATION':
        return mapquest_output.Elevation(mapquest.return_elevations(data))

def initialize(output: str) -> object:
    if output == 'ELEVATION':
        initial_elevation = mapquest.check_result(mapquest.build_elevation_url(mapquest.return_first_latlongs(route_data)))
        initial_obj = create_object(output,initial_elevation)
        obj = create_object(output,elevation_data)
        initial_obj.add(obj.peek()[0])
        return initial_obj                        
    else:
        return create_object(output, route_data)
        
    
if __name__ == '__main__':
    num_location = read_num_locations()
    list_locations = read_locations(num_location)
    num_output = read_num_outputs()
    list_output = read_outputs(num_output)

    list_of_objects = []
    count1 = 0
    
    while count1 < num_location:
        if count1 == 0:
            start = list_locations[0]
            count1 += 1

        else:
            try:
                route_data = mapquest.check_result(mapquest.build_route_url(start, list_locations[count1]))
                elevation_data = mapquest.check_result(mapquest.build_elevation_url(mapquest.return_last_latlongs(route_data)))
                if list_of_objects == []:
                    for output in list_output:
                        obj = initialize(output)
                        list_of_objects.append(obj)

                else:
                    count2 = 0
                    while count2 < num_output:
                        if list_output[count2] == 'ELEVATION':
                            element = create_object(list_output[count2],elevation_data)
                            list_of_objects[count2].add(element.peek()[0])
                        else:
                            element = create_object(list_output[count2],route_data)
                            list_of_objects[count2].add(element.peek())
                        count2 += 1
                    
                if count1 == num_location -1:
                    for obj in list_of_objects:
                        print()
                        obj.get_result()

                else:
                    start = list_locations[count1]

                count1 += 1
            except KeyError:
                print()
                print('NO ROUTE FOUND')
                break
            except urllib.error.HTTPError:
                print()
                print('MAPQUEST ERROR')
                break
            except urllib.error.URLError:
                print()
                print('MAPQUEST ERROR')
                break
                                
    print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    print()
