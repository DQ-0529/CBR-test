def compute_similarity(case, query, weights, ranges):
    sim = 0
    total_weight = 0
    for attr in weights:
        w = weights[attr]
        if attr in ranges:
            min_val, max_val = ranges[attr]
            range_val = max_val - min_val if max_val != min_val else 1
            diff = abs(case[attr] - query[attr])
            attr_sim = 1 - diff / range_val
        else:
            attr_sim = 1.0 if case[attr] == query[attr] else 0.0
        sim += w * attr_sim
        total_weight += w
    return sim / total_weight

def find_similar_cases(cases, query_case):
    weights = {"Cost": 0.2, "Duration": 0.2, "Year": 0.2, "Stories": 0.2, "Type": 0.2}
    ranges = {
        "Cost": (cases["Cost"].min(), cases["Cost"].max()),
        "Duration": (cases["Duration"].min(), cases["Duration"].max()),
        "Year": (cases["Year"].min(), cases["Year"].max()),
        "Stories": (cases["Stories"].min(), cases["Stories"].max())
    }
    cases["Similarity"] = cases.apply(lambda row: compute_similarity(row, query_case, weights, ranges), axis=1)
    return cases.sort_values(by="Similarity", ascending=False).head(5)
