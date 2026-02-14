### **Reward Design and Reliability in Learning Agents**



**I implemented a grid-world reinforcement learning agent and trained the same algorithm under multiple reward definitions.**



**Initially, different incentives produced very different behaviours — efficient navigation, risk-averse movement, and even avoidance of the goal when the reward was incorrect.**



**To study reliability, I introduced environment noise where the agent’s action sometimes changed randomly.**



**Under uncertainty, well-defined rewards degraded gradually, but incorrect rewards caused complete failure. The agent did not become less intelligent — the objective simply became unstable.**



**This suggests that behaviour reliability depends more on incentive design than on learning capability. Noise exposes misalignment rather than causing it.**



**The experiment highlights a key challenge in responsible AI systems: correctness of learning does not guarantee correctness of behaviour.**



