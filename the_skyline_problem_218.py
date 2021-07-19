# add alias
import heapq
import itertools
from operator import itemgetter

pq = []  # list of entries arranged in a heap
entry_finder = {}  # mapping of tasks to entries
REMOVED = (-1,-1)  # placeholder for a removed task


def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)

    entry = [-priority, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)


def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED


def get_pq_max():
    """Get maximum"""
    while pq:
        priority, task = pq[0]
        # print(task)
        if task is REMOVED:
            # print("pop\\-/")
            heapq.heappop(pq)
            continue
        return -priority
    return 0


def sort_event(e):
    if e[2] == 'enter':
        return e[0], e[2], -e[1]
    return e[0], e[2], e[1]


List = list


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        corner_points = []
        counter = itertools.count()  # unique sequence count
        for bd in buildings:
            count = next(counter)
            corner_points.append((bd[0], bd[2], 'enter', count))
            corner_points.append((bd[1], bd[2], 'leave', count))
        corner_points = sorted(corner_points, key=sort_event)
        # print(corner_points)
        global pq
        for event in corner_points:
            # meet a new building
            if event[2] == 'enter':
                if len(pq) == 0 or event[1] > get_pq_max():
                    res.append([event[0], event[1]])
                # x coordinate as task, height as priority
                # use negative to achieve max heap
                add_task((event[1], event[3]), event[1])
            elif event[2] == 'leave':
                # print(entry_finder)
                remove_task((event[1], event[3]))
                if event[1] > get_pq_max():
                    res.append([event[0], get_pq_max()])
            # print(pq)
        return res
