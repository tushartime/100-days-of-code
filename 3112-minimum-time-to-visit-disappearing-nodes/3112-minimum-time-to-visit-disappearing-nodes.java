import java.util.*;

class Solution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) graph[i] = new ArrayList<>();
        for (int[] e : edges) {
            graph[e[0]].add(new int[]{e[1], e[2]});
            graph[e[1]].add(new int[]{e[0], e[2]});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0}); // {time, node}

        boolean[] visited = new boolean[n];

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int time = cur[0], u = cur[1];
            if (visited[u]) continue;
            visited[u] = true;
            if (time >= disappear[u]) continue;

            for (int[] nei : graph[u]) {
                int v = nei[0];
                int newTime = time + nei[1];
                if (!visited[v] && newTime < disappear[v] && newTime < dist[v]) {
                    dist[v] = newTime;
                    pq.offer(new int[]{newTime, v});
                }
            }
        }

        for (int i = 0; i < n; i++)
            if (dist[i] == Integer.MAX_VALUE) dist[i] = -1;

        return dist;
    }
}
