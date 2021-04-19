The uniformization method is adopted here to model the four class series queue as a discrete-time MDP. Let $B = \alpha + \sum_{i=1}^4 \mu_i$ be the potential event rate such that $B$ is no less than any of the event rate. Define state variable $s_i\in \mathbb{N}$ to be the number of class $i$ jobs in the buffer plus any that is in the processing, such that the state vector is given by $s = \big(s_1, s_2, s_3, s_4 \big)^T\in \mathbb{N}^4$. The decision to be made is for each class whether to serve the job, and thus the action is defined by a binary variable $a_i$ for class $i$, $i = 1,2,3,4$ respectively,

\begin{align*}
    a_i & = \begin{cases}
        1 & \text{serve class $i$,}\\
        0 & \text{set class $i$ idle.}
    \end{cases}
\end{align*}

The action vector is $a = \big(a_1, a_2, a_3, a_4 \big)^T \in \{0,1\}^4$. Note that the state space is infinite so we have to truncate by level $N$, i.e., suppose at each class the capacity is $N$, still including any at service. Whenever the next transition is to make number of jobs exceed $N$, it is considered as a fake transition or self-transition, equivalently. With this assumption, the transitions are given as follows:

\begin{align*}
  \mathbb{P}(s_1+1,s_2,s_3,s_4|s,a) &= \frac{\alpha \cdot \mathbb{I} \{s_1<N\}}{B}\\
  \mathbb{P}(s_1-1,s_2+1,s_3,s_4|s,(a_1=1,a_2,a_3,a_4)) &= \frac{\mu_1 \cdot \mathbb{I}\{s_1>0\} \mathbb{I}\{s_2<N\}}{B}\\
  \mathbb{P}(s_1,s_2-1,s_3+1,s_4|s,(a_1,a_2=1,a_3,a_4)) &= \frac{\mu_2 \cdot \mathbb{I}\{s_2>0\} \mathbb{I}\{s_3<N\}}{B}\\
  \mathbb{P}(s_1,s_2,s_3-1,s_4+1|s,(a_1,a_2,a_3=1,a_4)) &= \frac{\mu_3 \cdot \mathbb{I}\{s_3>0\} \mathbb{I}\{s_4<N\}}{B}\\
  \mathbb{P}(s_1,s_2,s_3,s_4-1|s,(a_1,a_2,a_3,a_4=1)) &= \frac{\mu_4 \cdot \mathbb{I}\{s_4>0\}}{B}\\
\end{align*}

The expression of self-transition is $\mathbb{P}(s|s,a) = 1 - \sum_{s' \neq s} \mathbb{P}(s'|s,a)$ for $\forall s,a$. The normalized cost function is $c^Ts/B$.


```python

```
