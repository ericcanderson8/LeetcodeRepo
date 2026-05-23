class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # MIN STOPS ARRAY
        min_stops = [float('inf')] * n
        min_stops[src] = 0

        # TRIPS ADJACENCY LIST
        adj = [[] for _ in range(n)]

        for fr, to, price in flights:
            adj[fr].append((to, price))
        # adj[i] = list of flights to (to, price)

        # QUEUE GETS THE CHEAPEST FLIGHT
        # (Cost, node, stops)
        heap = []
        heapq.heappush(heap, (0, src, 0))


        # print(heap)
        # print(adj)
        # print(min_stops)
        # EXPLORE THE ROUTES
        while len(heap) > 0:
            # print(heap)
            price, node, stops = heapq.heappop(heap)
            
            min_stops[node] = min(stops, min_stops[node])
            # print("Node:" + str(price) + ", " + str(node) + ", " + str(stops))
            # print(min_stops)
            if node == dst:
                return price
            if stops < k+1:
                # Add all items in the adjency list to the heap
                for nextNode, nextPrice in adj[node]:
                    # check if new stops would be less than the current
                    if stops + 1 < min_stops[nextNode]:
                        # add it to the queue
                        heapq.heappush(heap, (price + nextPrice, nextNode, stops + 1))

        return -1