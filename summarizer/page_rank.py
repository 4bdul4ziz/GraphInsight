from .graph import Undirected_Graph

def page_rank_algorithm(graph, damping_factor = 0.85, num_iter = 1000):
    """Implement the classic Page Rank algorithm of Google"""
    # The list of web pages to be ranked
    webpages = graph.get_vertices()

    probs = {}
    for webpage in webpages:
        probs[webpage] = 1 / len(webpages)

    for iter in range(num_iter):
        next_probs = {}
        for webpage in probs:
            next_probs[webpage] = 0

        for (cur_webpage, prob) in probs.items():
            neighbours = graph.get_neighbours(cur_webpage)

            if (neighbours != []):
                for (neighbour, weight) in neighbours:
                    next_probs[neighbour] += prob * damping_factor * weight
                for webpage in next_probs:
                    next_probs[webpage] += prob * (1 - damping_factor) * (1 / len(webpages))
            
            else:
                for webpage in next_probs:
                    next_probs[webpage] += prob * (1 / len(webpages))

        probs = next_probs

    ranked_webpages = list(sorted(probs.items(), key = lambda kvp: kvp[1], reverse = True))

    return ranked_webpages
