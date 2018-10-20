import codecs

# PN : The assumption made here is that the input file contains entry direcions for both cities
# Eg : Arad Zerind 75
#    : Zerind Arad 75

# The input file is tab seperated. A reference input file used is attached along with the code.



def getInput():
    filepath = raw_input("Please enter the file path : ")
    filename = codecs.open(filepath,'r','UTF-8')
    #Create a distance list from Input File
    distance = list()
    for line in filename :
        inline = line.split("\t")
        distance.append(tuple(inline))

    #Create an adjacency graph and visited hashmap
    directed_graph = dict((value[0], []) for value in distance)
    for city1 in distance:
        directed_graph[city1[0]].append(city1[1])


    while (True):
        city1 = raw_input("Enter the start city : ")
        city2 = raw_input("Enter the destination city : ")
        traversal =int(raw_input("Enter the type of search you wold like to use. \n 1. DFS \n 2. BFS \n 3. Iterative Deepning. \n 4. Exit\n"))
        visited = dict((value[0], False) for value in distance)


        if (traversal == 1):
            traversed_path = dfs_search(directed_graph,city1,city2,visited,[city1])
            if (traversed_path and len(traversed_path) > 0) :
                path_cost = calculteCost(traversed_path,distance)
                print "The traversed path using DFS is : "
                for city in traversed_path:
                    print(city + " "),
                print
                print "The total cost of path is : " , path_cost
            else :
                print "The source or destination was not found"
            print


        elif (traversal == 2):
            traversed_path = bfs_search(directed_graph,city1,city2)
            if (traversed_path and len(traversed_path) > 0) :
                path_cost = calculteCost(traversed_path,distance)
                print "The traversed path using BFS is : "
                for city in traversed_path:
                    print(city + " "),
                print
                print "The total cost of path is : " , path_cost
            else :
                print "The source or destination was not found"
            print

        elif (traversal == 3):
            traversed_path = iterative_deepening_search(directed_graph,city1,city2,visited,[city1])
            if (traversed_path and len(traversed_path) > 0) :
                path_cost = calculteCost(traversed_path,distance)
                print "The traversed path using Iterative Deepening is : "
                for city in traversed_path:
                    print(city + " "),
                print
                print "The total cost of path is : " , path_cost
            else :
                print "Either the source or destination was not found or depth limit exceeded "
            print

        continue_exit = raw_input("Do you want to really want to exit (Y/N) : ")
        if (continue_exit == 'Y' or continue_exit == 'y'):
            break


def calculteCost(final_path,distance):
    totalcost = 0
    for city1,city2,dist in distance:
        for index in xrange(0,len(final_path)-1):
            if final_path[index] == city1 and final_path[index+1] == city2 :
                totalcost += int(dist)
    return totalcost



def dfs_search(directed_graph,city1,city2,visited,actual_path):
    # Mark the first city as visited
    visited[city1] = True

    # If destination city is found, return the path
    if city1 == city2:
        return actual_path

    # If destination city not found, return False

    if not directed_graph.has_key(city1) :
        return False

    # Traverse through the children of each city
    for city in directed_graph[city1]:
            if not visited[city]:
                actual_path.append(city)
                result = dfs_search(directed_graph,city,city2,visited,actual_path)
                if not result : actual_path.remove(city)
                else: return result

    return False

def bfs_search(directed_graph, city1, city2):


    if city1 not in directed_graph or city2 not in directed_graph :
        return False
    # Create a queue to store cities
    queue = []
    # Push the start city : city1 in queue
    queue.append([city1])
    while queue:
        # Get the first inserted city in FIFO manner
        path = queue.pop(0)
        # Get the mot recent city
        city = path[-1]
        # Reach Goal city
        if city == city2:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent_city in directed_graph[city]:
            new_path = list(path)
            new_path.append(adjacent_city)
            queue.append(new_path)

    return False

def iterative_deepening_search(directed_graph,city1,city2,visited,actual_path):
    depth_limit = int(raw_input("Please enter the depth till you want to find the nodes : ") or 15)

    for i in xrange(0,depth_limit):
        path_till_now = list(actual_path)
        new_visited = dict(visited)
        path_till_now = id_dfs_search(directed_graph,city1,city2,new_visited,actual_path,0,i)

        if path_till_now == False:
            continue
        elif path_till_now:
            print "Soln at depth : " +str(i)
            return path_till_now

def id_dfs_search(directed_graph,city1,city2,visited,actual_path,depth_traverse,depth_limit):
    # If the depth limit is not reached continue the following
    if (depth_traverse <= depth_limit):
        visited[city1] = True

        # If the destination city s found, return path
        if city1 == city2:
            return actual_path

        # If destination city not found return false
        if not directed_graph.has_key(city1) :
            return False

        # To Traverse through each child node:
        for city in directed_graph[city1]:
            if not visited[city]:
                actual_path.append(city)
                result = id_dfs_search(directed_graph,city,city2,visited,actual_path,depth_traverse+1,depth_limit)
                if not result :
                    actual_path.remove(city)
                else:
                    return result

    return False

def main():
    # parse command line options
    getInput()

if __name__ == "__main__":
main()
