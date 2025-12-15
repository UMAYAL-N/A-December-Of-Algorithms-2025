# AquaNet – Minimum Time to Fill All Reservoirs
from collections import deque
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
adj = [[] for _ in range(V)]

for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

state = list(map(int, input().split()))
q = deque()
dist = [-1]*V

for i in range(V):
    if state[i] == 1:
        q.append(i)
        dist[i] = 0

while q:
    node = q.popleft()
    for nb in adj[node]:
        if dist[nb] == -1:
            dist[nb] = dist[node] + 1
            q.append(nb)

if -1 in dist:
    print(-1)
else:
    print(max(dist))
