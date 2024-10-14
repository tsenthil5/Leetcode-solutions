import heapq as hq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Append each friend's index to their arrival-leave times
        for i in range(len(times)):
            times[i].append(i)
        
        # Sort by arrival time
        times.sort(key=lambda x: x[0])
        
        # Min-heap to track available chairs
        availableChairs = [i for i in range(len(times))]
        hq.heapify(availableChairs)
        
        # Min-heap to track exit times (based on leave time)
        currExit = []  # Elements will be (leave time, chair number)

        # Process each friend's arrival in chronological order
        for arr, leav, friend in times:
            # Release chairs for friends that have already left
            while currExit and currExit[0][0] <= arr:
                _, chair = hq.heappop(currExit)
                hq.heappush(availableChairs, chair)
            
            # Assign a chair to the current friend
            chair = hq.heappop(availableChairs)
            
            # If it's the target friend, return the assigned chair
            if friend == targetFriend:
                return chair
            
            # Add the friend's leave time to the exit heap
            hq.heappush(currExit, (leav, chair))

