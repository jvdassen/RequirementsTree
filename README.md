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
> The dependencies that the project uses are also attached locally in 'venv/lib/python3.7/site-packages' folder for completeness.

## Running an agent

### Q-Learning

Run the Q-learning agent:
```
python QLearningAgent.py
```

### Actor-critic learning

Run the AC-learning agent:
```
python ACLearningAgent.py
```
