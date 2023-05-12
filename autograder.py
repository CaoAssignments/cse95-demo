from pa1 import pa1_sum
import json

def test1():
    return pa1_sum(1, 2) == 3

def test2():
    return pa1_sum(0, 0) == 0

def test3():
    return pa1_sum(-1, -1) == 0

with open("/autograder/results/results.json", "w") as f:
    results = [
        {
            "name": "Sanity Test",
            "score": 2.0 if test1() else 0.0,
            "max_score": 2.0,
            "visibility": "visible"
        },
        {
            "name": "Edge Test",
            "score": 3.0 if test2() else 0.0,
            "max_score": 3.0,
            "visibility": "visible"
        },
        {
            "name": "Normal Test",
            "score": 3.0 if test3() else 0.0,
            "max_score": 3.0,
            "visibility": "after_published"
        },
    ]
    json.dump({
        "tests": results
    }, f)


