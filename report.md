### **Learning Behaviour Depends More on Objective Than Algorithm**



**I implemented a simple grid-world reinforcement learning agent and trained the same algorithm under four reward definitions.**



**Despite identical learning procedure, the behaviour differed significantly:**



* **When only success was rewarded, the agent learned inefficient wandering policies.**
* **When a small step penalty was introduced, the agent learned structured shortest-path behaviour.**
* **When penalties increased, behaviour became risk-averse.**
* **When the reward sign was reversed, the agent actively avoided the goal state.**



**This shows the agent consistently optimized the reward specification rather than the intended task.**



**The experiment highlights a key challenge in decision-making AI systems:**

**performance depends more on how objectives are defined than on model capability.**



**Even a correct learning algorithm can produce undesirable behaviour if incentives are misaligned.**

