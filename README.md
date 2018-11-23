# RequirementsTree

> An agent that uses Reeinforcement learning algorithms to solve a requirements dependency graph.

## Prerequisites

* `Python 3` and `pip`
* `numpy` and `binarytree` (can be installed with `pip`)
* `virtualenv`(optional)

## Dev setup

If desired, start the virtual environment:
```
source venv/bin/activate
```

Fetch the dependencies:
```
pip install -r requirements.txt
```

Run the Q-learning agent:
```
python QLearningAgent.py
```

## Idea

In the requirements graph, each requirement can have one or two dependent requirements. The type of dependency is either `AND` or `OR`. `AND` means that to implement the parent requirement both children need to be implemented. `OR` means that the parent requirement can be implemented by imlpementing on of the alternative children. Each requirement has a cost and value associated with it.

