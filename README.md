## ORIE 6590 Project - queuing network

The uniformization method is adopted here to model the four class series queue as a discrete-time MDP. Let B = alpha + mu1 + mu2 + mu3 + mu4 be the potential event rate such that B is no less than any of the event rate. 

State space

s = (s1, s2, s3, s4)', where each entry s_i is the number of class i jobs in the buffer plus any that is in the processing, and thus being a non-negative integer.

Action space

a = (a1, a2, a3, a4)', where each entry a_i is a binary action variable, taking value 1 if the decision is to serve class i and 0 if it is idle.

Note that the state space is infinite so we have to truncate by level N, i.e., suppose at each class the capacity is N, still including any at service. Whenever the next transition is to make number of jobs exceed N, it is considered as a fake transition or self-transition, equivalently. With this assumption, the transitions are given as follows.

Transitions

If the arrival of a job is admissible, i.e., such new arrival is within the capacity of the first class, then it happens with probability alpha/B, no matter what actions and states would be.

If the service completion of class 1 is admissible, i.e., not serving an empty buffer, and also the arrival to class 2 is admissible, then such transition happens with probability mu1/B, given current action is to serve class 1.

If the service completion of class i, and the arrival to class i+1 are both admissible, then the transition happens with probability mu_i/B, i = 1, 2, 3, given current action is to serve class i.

If the service completion of the last class is admissible, then the transition happens with probability mu_4/B, given current action is to serve class 4.


```python

```
