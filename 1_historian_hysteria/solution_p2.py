def generate_location_id_lists():
    file = open("location_ids.txt")
    location_list1 = []
    location_list2 = []

    location_list2_map = {}

    for line in file:
        location1, location2 = line.strip().split("   ")
        location_list1.append(int(location1))
        location_list2.append(int(location2))
        if int(location2) in location_list2_map.keys():
            location_list2_map[int(location2)] += 1
        else:
            location_list2_map[int(location2)] = 1

    location_list1.sort()
    location_list2.sort()
    total_location_distance = 0
    index = 0
    while index <= len(location_list1) - 1:
        distance1 = location_list1[index]
        distance2 = location_list2[index]
        total_location_distance += abs(distance1 - distance2)
        index += 1
    print(total_location_distance)

    total_similarity_score = 0
    for location_id in location_list1:
        if location_id in location_list2_map.keys():
            total_similarity_score += location_id * location_list2_map[location_id]
    print(total_similarity_score)


def main():
    generate_location_id_lists()


main()
