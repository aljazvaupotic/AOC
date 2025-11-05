from collections import defaultdict, deque


def parse_file(file_content):
    """Parse the rules and updates from the input."""
    sections = file_content.strip().split("\n\n")  # Split into sections by empty line
    rules_input = sections[0]  # First section contains rules
    updates_input = sections[1]
    rules = []
    updates = []

    # Parse rules
    for line in rules_input.strip().split('\n'):
        if '|' in line:
            x, y = map(int, line.split('|'))
            rules.append((x, y))

    # Parse updates
    for line in updates_input.strip().split('\n'):
        updates.append(list(map(int, line.split(','))))

    return rules, updates


def build_graph(rules):
    """Build a graph from the ordering rules."""
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph


def is_update_valid(update, graph):
    """Check if an update satisfies the ordering rules."""
    # Build a set of pages in the current update
    pages_in_update = set(update)

    # Filter the graph to only include relevant rules
    filtered_graph = {x: [y for y in graph[x] if y in pages_in_update] for x in pages_in_update}

    # Topological sort to check if ordering is valid
    in_degree = {page: 0 for page in pages_in_update}
    for x in filtered_graph:
        for y in filtered_graph[x]:
            in_degree[y] += 1

    # Perform topological sorting
    queue = deque([node for node in pages_in_update if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in filtered_graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If sorted_pages contains all pages, the update is valid
    return len(sorted_pages) == len(pages_in_update)


def find_middle_number(update):
    """Find the middle page number of an update."""
    n = len(update)
    return update[n // 2]  # 0-based indexing


def process_file(file_content):
    """Main function to process the file and compute the result."""
    rules, updates = parse_file(file_content)
    graph = build_graph(rules)
    middle_numbers = []

    for update in updates:
        if is_update_valid(update, graph):
            middle_numbers.append(find_middle_number(update))

    return sum(middle_numbers)


with open('demo5.txt', 'r') as file:
    file_content = file.read()

result = process_file(file_content)
print(result)