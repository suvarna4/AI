"""docstring"""
import sys
import time
from queue import Queue, PriorityQueue, LifoQueue

STIME = time.time()


def bfs(start):
    """breadth-first-search"""
    search = Queue(maxsize=0)
    visited = set()
    nodes = []
    parents = []
    search.put((start, 0))
    max_fringe_size = 1
    max_search_depth = 0
    nodecount = 0
    while not search.empty():
        state = search.get()
        if state[1] > max_search_depth:
            max_search_depth = state[1]
        visited.add(state[0])
        nodecount += 1
        if state[0] == ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
            fil = open('output', 'w')
            path = []
            ind = nodes.index(('0', '1', '2', '3', '4', '5', '6', '7', '8'))
            dif = parents[ind].index('0') - nodes[ind].index('0')
            if dif == 1:
                path.append("LEFT")
            if dif == -1:
                path.append("RIGHT")
            if dif == 3:
                path.append("UP")
            if dif == -3:
                path.append("DOWN")
            while parents[ind] != start:
                ind = nodes.index(parents[ind])
                dif = parents[ind].index('0') - nodes[ind].index('0')
                if dif == 1:
                    path.append("LEFT")
                if dif == -1:
                    path.append("RIGHT")
                if dif == 3:
                    path.append("UP")
                if dif == -3:
                    path.append("DOWN")
            path.reverse()
            fil.write("path_to_goal: "+str(path))
            fil.write("\ncost_of_path: "+str(state[1]))
            fil.write("\nnodes_expanded: "+str(nodecount - 1))
            fil.write("\nfringe_size: "+str(search.qsize()))
            fil.write("\nmax_fringe_size: "+str(max_fringe_size))
            fil.write("\nsearch_depth: "+str(state[1]))
            fil.write("\nmax_search_depth: "+str(max_search_depth))
            fil.write("\nrunning_time: "+str(time.process_time()))
            return
        for i in neighbors(state[0]):
            if not i in visited:
                search.put((i, state[1]+1))
                nodes.append(i)
                parents.append(state[0])
                visited.add(i)
        if search.qsize() > max_fringe_size:
            max_fringe_size = search.qsize()

def dfs(start):
    """depth-first-search"""
    search = LifoQueue(maxsize=0)
    visited = set()
    max_fringe_size = 1
    max_search_depth = 0
    nodecount = 0
    nodes = []
    parents = []
    search.put((start, 0))
    while not search.empty():
        state = search.get()
        nodecount += 1
        if state[1] > max_search_depth:
            max_search_depth = state[1]
        visited.add(state[0])
        if state[0] == ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
            fil = open('output', 'w')
            path = []
            ind = nodes.index(('0', '1', '2', '3', '4', '5', '6', '7', '8'))
            dif = parents[ind].index('0') - nodes[ind].index('0')
            if dif == 1:
                path.append("LEFT")
            if dif == -1:
                path.append("RIGHT")
            if dif == 3:
                path.append("UP")
            if dif == -3:
                path.append("DOWN")
            while parents[ind] != start:
                ind = nodes.index(parents[ind])
                dif = parents[ind].index('0') - nodes[ind].index('0')
                if dif == 1:
                    path.append("LEFT")
                if dif == -1:
                    path.append("RIGHT")
                if dif == 3:
                    path.append("UP")
                if dif == -3:
                    path.append("DOWN")
            path.reverse()
            fil.write("path_to_goal: "+str(path))
            fil.write("\ncost_of_path: "+str(state[1]))
            fil.write("\nnodes_expanded: "+str(nodecount-1))
            fil.write("\nfringe_size: "+str(search.qsize()))
            fil.write("\nmax_fringe_size: "+str(max_fringe_size))
            fil.write("\nsearch_depth: "+str(state[1]))
            fil.write("\nmax_search_depth: "+str(max_search_depth))
            fil.write("\nrunning_time: "+str(time.process_time()))
            return
        for i in reversed(neighbors(state[0])):
            if not i in visited:
                search.put((i, state[1]+1))
                nodes.append(i)
                parents.append(state[0])
                visited.add(i)
        if search.qsize() > max_fringe_size:
            max_fringe_size = search.qsize()

def ast(start):
    """a-star-search"""
    search = PriorityQueue(maxsize=0)
    visited = set()
    nodecount = 0
    nodes = []
    parents = []
    max_search_depth = 0
    max_fringe_size = 1
    search.put((dist(start), (start, 0)))
    while not search.empty():
        sdist = search.get()
        nodecount += 1
        state = sdist[1]
        if state[1] > max_search_depth:
            max_search_depth = state[1]
        visited.add(state[0])
        if state[0] == ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
            fil = open('output', 'w')
            path = []
            ind = nodes.index(('0', '1', '2', '3', '4', '5', '6', '7', '8'))
            dif = parents[ind].index('0') - nodes[ind].index('0')
            if dif == 1:
                path.append("LEFT")
            if dif == -1:
                path.append("RIGHT")
            if dif == 3:
                path.append("UP")
            if dif == -3:
                path.append("DOWN")
            while parents[ind] != start:
                ind = nodes.index(parents[ind])
                dif = parents[ind].index('0') - nodes[ind].index('0')
                if dif == 1:
                    path.append("LEFT")
                if dif == -1:
                    path.append("RIGHT")
                if dif == 3:
                    path.append("UP")
                if dif == -3:
                    path.append("DOWN")
            path.reverse()
            fil.write("path_to_goal: "+str(path))
            fil.write("\ncost_of_path: "+str(state[1]))
            fil.write("\nnodes_expanded: "+str(nodecount-1))
            fil.write("\nfringe_size: "+str(search.qsize()))
            fil.write("\nmax_fringe_size: "+str(max_fringe_size))
            fil.write("\nsearch_depth: "+str(state[1]))
            fil.write("\nmax_search_depth: "+str(max_search_depth))
            fil.write("\nrunning_time: "+str(time.process_time()))
            return
        for i in neighbors(state[0]):
            if not i in visited:
                search.put((dist(i), (i, state[1]+1)))
                nodes.append(i)
                parents.append(state[0])
                visited.add(i)
        if search.qsize() > max_fringe_size:
            max_fringe_size = search.qsize()

def ida(start):
    """iterative-deepening-search"""
    nodecount = 0
    max_search_depth = 0
    max_fringe_size = 0
    limit = 1
    while True:
        ans = dlst(start, limit)
        if not ans:
            return
        else:
            nodecount += ans[0]
            if ans[1] > max_search_depth:
                max_search_depth = ans[1]
            if ans[2] > max_fringe_size:
                max_fringe_size = ans[2]
            if len(ans) > 3:
                fil = open('output', 'w')
                fil.write("path_to_goal: "+str(ans[5]))
                fil.write("\ncost_of_path: "+str(ans[3]))
                fil.write("\nnodes_expanded: "+str(nodecount))
                fil.write("\nfringe_size: "+str(ans[4]))
                fil.write("\nmax_fringe_size: "+str(max_fringe_size))
                fil.write("\nsearch_depth: "+str(ans[3]))
                fil.write("\nmax_search_depth: "+str(max_search_depth))
                fil.write("\nrunning_time: "+str(time.process_time()))
                return
            limit += 1

def dlst(start, limit):
    """depth-limited-search"""
    search = PriorityQueue(maxsize=0)
    visited = set()
    nodecount = 0
    nodes = []
    parents = []
    max_search_depth = 0
    max_fringe_size = 1
    search.put((dist(start), (start, 0)))
    while not search.empty():
        sdist = search.get()
        state = sdist[1]
        nodecount += 1
        if state[1] > max_search_depth:
            max_search_depth = state[1]
        visited.add(state[0])
        if state[0] == ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
            path = []
            ind = nodes.index(('0', '1', '2', '3', '4', '5', '6', '7', '8'))
            dif = parents[ind].index('0') - nodes[ind].index('0')
            if dif == 1:
                path.append("LEFT")
            if dif == -1:
                path.append("RIGHT")
            if dif == 3:
                path.append("UP")
            if dif == -3:
                path.append("DOWN")
            while parents[ind] != start:
                ind = nodes.index(parents[ind])
                dif = parents[ind].index('0') - nodes[ind].index('0')
                if dif == 1:
                    path.append("LEFT")
                if dif == -1:
                    path.append("RIGHT")
                if dif == 3:
                    path.append("UP")
                if dif == -3:
                    path.append("DOWN")
            path.reverse()
            return (nodecount-1, max_search_depth, max_fringe_size, state[1], search.qsize(), path)
        if state[1] < limit:
            for i in neighbors(state[0]):
                if not i in visited:
                    search.put((dist(i), (i, state[1]+1)))
                    visited.add(i)
                    nodes.append(i)
                    parents.append(state[0])
        if search.qsize() > max_fringe_size:
            max_fringe_size = search.qsize()
        if nodecount >= 181440:
            return False
    return (nodecount - 1, max_search_depth, max_fringe_size)

def dist(confi):
    """computes priority for each node"""
    count = 0
    for i in range(9):
        j = int(confi[i])
        count += abs((j%3) - (i%3))
        count += abs((j//3) - (i//3))
    return count


def neighbors(pos):
    """neighbor finding function"""
    nlist = []
    ind = pos.index("0")
    if ind > 2:
        slist = list(pos)
        slist[ind] = slist[ind-3]
        slist[ind-3] = "0"
        nlist.append(tuple(slist))
    if ind < 6:
        slist = list(pos)
        slist[ind] = slist[ind+3]
        slist[ind+3] = "0"
        nlist.append(tuple(slist))
    if (ind % 3) != 0:
        slist = list(pos)
        slist[ind] = slist[ind-1]
        slist[ind-1] = "0"
        nlist.append(tuple(slist))
    if (ind % 3) != 2:
        slist = list(pos)
        slist[ind] = slist[ind+1]
        slist[ind+1] = "0"
        nlist.append(tuple(slist))
    return nlist

if sys.argv[1] == "bfs":
    bfs(tuple(sys.argv[2].split(",")))
if sys.argv[1] == "dfs":
    dfs(tuple(sys.argv[2].split(",")))
if sys.argv[1] == "ast":
    ast(tuple(sys.argv[2].split(",")))
if sys.argv[1] == "ida":
    ida(tuple(sys.argv[2].split(",")))
