from collections import deque, defaultdict

class Solution:
    def minTime(self, root, target):
        def build_parent_map(node, parent, parent_map, val_to_node):
            if not node:
                return
            val_to_node[node.data] = node
            if parent:
                parent_map[node] = parent
            build_parent_map(node.left, node, parent_map, val_to_node)
            build_parent_map(node.right, node, parent_map, val_to_node)

        def bfs(start, parent_map):
            visited = set()
            queue = deque()
            queue.append(start)
            visited.add(start)
            time = -1 

            while queue:
                size = len(queue)
                time += 1
                for _ in range(size):
                    curr = queue.popleft()
                    for neighbor in [curr.left, curr.right, parent_map.get(curr)]:
                        if neighbor and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            return time

        parent_map = {}
        val_to_node = {}
        build_parent_map(root, None, parent_map, val_to_node)

        target_node = val_to_node[target]
        return bfs(target_node, parent_map)
