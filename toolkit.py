# Scenario: Building a Smart Data Aggregator
# You have been hired by a startup working on a Smart Data Aggregator tool. The goal
# of the tool is to manage and analyze large sets of user data efficiently. The startup
# focuses on different types of collections (List, Tuple, Set, and Dictionary) to handle
# various tasks such as real-time analytics, tracking data, and reporting. Your task is to
# develop different modules for the aggregator using Python

# Part 01

def filter_users(lst):
    return [u[1] for u in lst if u[2] > 30 and u[3] in {'USA', 'Canada'}]

def top_10_oldest(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j][2] < lst[j+1][2]:  
                lst[j], lst[j+1] = lst[j+1], lst[j]  
    top_10 = []
    for i in range(10):
        top_10.append(lst[i])
    
    return top_10


def find_duplicates(lst):
    names = [u[1] for u in lst]
    return [n for n in set(names) if names.count(n) > 1]

# Part 2
def unique_users(trans):
    return len(set([t[1] for t in trans]))

def max_transaction(trans):
    return max(trans, key=lambda t: t[2])

def split_ids(trans):
    return [t[0] for t in trans], [t[1] for t in trans]

# Part 3
def both_visited(A, B):
    return A & B

def either_both(A, C):
    return (A | C) - (A & C)

def update_set(A, new_ids):
    A.update(new_ids)

def remove_set(B, ids):
    B.difference_update(ids)

# Part 4:

def filter_feedback(dic):
    return {k: v['rating'] for k, v in dic.items() if v['rating'] >= 4}


def top_5_feedback(dic):
    return dict(sorted(dic.items(), key=lambda x: x[1]['rating'], reverse=True)[:5])


def combine_feedback(dic_list):
    result = {}
    for dic in dic_list:
        for k, v in dic.items():
            if k in result:
                result[k]['rating'] = max(result[k]['rating'], v['rating'])
                result[k]['comments'] += " " + v['comments']
            else:
                result[k] = v
    return result



def dict_comp(dic):
    return {k: v['rating'] for k, v in dic.items() if v['rating'] > 3}
