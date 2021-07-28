# RL_dino_try
An RL agent attempts to play the google chrome dino game. I have created a gym enviroment for the same and have implemented the DQN model to tain the agent . The gym 
enviroment can be found [here](https://github.com/19-ade/gym-dino-game)


## Setting up the enviroment
------------------------------------------------------------------------
**Please make sure you have Google chrome installed*

1. Clone the RL_dino_try repo


```
git clone https://github.com/19-ade/RL_dino_try.git
```

2.Clone the gym-dino-game(gym enviroment for the given code)


```
git clone https://github.com/19-ade/gym-dino-game.git
```
3.Install the gym enviroment :
```cd``` your way to the gym-dino-game folder on your system . 


```
cd /path/to/gym-dino-game
pip install -e .

```

*If you are using an enviroment to open RL_dino_try (Anaconda etc..) please make sure you follow the above steps inside a terminal of the enviroment*

4.NOw that the enviroment is installed we come back to RL_dino_try . Run the *requirements.py* script in the repo . This will install all the necessary libraries 
for our program.
```cd``` your way to the gym-dino-game folder on your system . 

```
cd /path/to/RL_dino_try
python requirements.py

```


5.Now we will run the **test.py** script. It just creates the dino enviroment .This is to make sure that everything is working correctly.

```
python test.py

```

6.Now we are ready!  Run the  **ai_run.py** script. Here  can see the pre-trained agent playing the game using the pretrained model(vidw_model.h5).

```
python ai_run.py

```

7. One can train the model using the **main.py**. 

- uncomment the last few lines in main method.


- after than the **main.py** can be executed
```
python main.py

```




#### Troubleshooting:




















## Hitchhiker's Guide to Reinforcement Learning
----------------------------------------------------------------
This project is based on the application Of RL. Ill try to explain the basics the best i can but I'm  a beginner ,please forgive me if I miss few points. Also Ill be very grateful if you, the reader would help me improve this rudimentary effort of mine.

One of the main backbones of RL is the **Markov Principle**
Markov pronciple states that the probability of going to a State S at time t+1 depends only on the current state at time t. 


So basically in RL we never look back . We analyse the present , estimate the future and perform the action.


P[S<sub>_t+1_</sub>| S<sub>t</sub>]=P[S<sub>_t+1_</sub> |S<sub>1</sub>,S<sub>2</sub>,.....,S<sub>t</sub>]
  
The states which follow this Principle are called Markov states.

Based on this we make the MDP (Markov Decision Process) . 

The basic architecture of a Rl model consistes of an **Agent**, **Enviroment**, **Actions**, **Rewards**, **State**.


The Agent performs an action in the enviroment at time t while being in the state S<sub>t</sub> and obtains the next state S<sub>t+1</sub> and Reward R<sub>t</sub>


Lets go through them one by one:

**Agent**: This is the part which decides which action to take . In our case our Agent plays the game and decides whether the dino will jump or do nothing . 

**Action**: the activity which the agent performs in the enviroment . In our case its jump or do nothing . 

**Enviroment**:The enviroment with which the agent interacts to perform the action . In our case its the Dino game . 

**State**: its the situation at a given time. It could be the coordinates in which the agent is at the moment of time or as In our case its snap shot of the dino game at that moment t .

**Reward**: This is the reward which the agent gets for performing a specific action. The main goal of tha agent is to maximise this reward. 

##### Q Learning

some definitions first:
**G<sub>t</sub>**= return is the total discounted reward from the time-step t


G<sub>t</sub> =R<sub>t+1</sub> + 	γR<sub>t+2</sub> +.......=  Σ(k=0 -> ∞) γ<sup>k</sup>R<sub>t+k+1</sub>

Here the γ represents the discount factor . This lies between 0 and 1 and helps us regulate how important the subsequent future steps are going to be. A γ of 0.99 would indicate the subsequent future is very important while
0.001 would reflect the fact that the subsequent rewards are not that important for the model


**policy**(π): policy defines the behaviour of an agent . Its the distribution over actions given states . (def copied from [David_silver_lecs](https://youtu.be/lfHX2hHRMVQ)). 

π(a|s)=P[A<sub>t</sub>=a|S<sub>t</sub>=s]

NOw we are ready to define Q 

The action-value functions is the expected return(G) if we take ation a , following policy , starting at state s

q<sub>π</sub>(s,a)=E<sub>π</sub>[G<sub>t</sub>|S<sub>t</sub>=s, A<sub>t</sub>=a]

Now we know the main goal of an agent is to maximize the reward . Since Q is just the esimate of the return we can say that we need to find the max value of q for the best policy . This will gaurantee the most reward.

If we decopose the G(reward) definition 

q<sub>π</sub>(s,a)=E<sub>π</sub>[R<sub>t+1</sub> + γq<sub>π</sub>(S<sub>t+1</sub>,A<sub>t+1</sub>|S<sub>t</sub>=s,A<sub>t</sub>=a]

This is the **Bellman Equation**. This will help us estimate the future rewards 

Now to define the best possibel q for the best possible policy we Q<sub>*</sub>


Q<sub>*</sub>(s,a)=argmax<sub>π</sub>
q<sub>π</sub>(s,a)

This is the optimal Q

Now tweaking the Bellman equation a bit:

Q<sub>*</sub>(s,a)=R<sub>t+1</sub> + γQ<sub>*</sub>(s<sub>t+1</sub>,a<sub>t+1</sub>)


This is a very simplified version of the Bellman optimality equation which we will use in the program. Its a recursive statement which contimues until the episode is over and then traces back .


#### DQN

The Algorithm I implemented here is Deep Q Learning.

In a DQN we enter the state into the neural network as the input and we get the Q values for output . From the output I used np.max() to find the optimal Q value.


**sailent features** :
- The input: Applying RL techniques to teach the agent to play Atari games is a common practise. I have learnt that to produce a sense of motion in games we need to stack 3-4 snapshots of the game enviroment together . So each input state for the CNN(since its pixel data) will be 4 screenshots stacked together. The shape for the input in my program is (20,40,4). 


- Experience Replay: The big problem faced is if we send the outputs in a sequential manner the inputs maybe heavily correleated . This correleation will have a harmful effect on the model and we get a bad output . To counter this the agent plays the game for a specific number of times . All the observations(s,a,r , s') are then stored in memory. Then from this memory we randomly pick a fixed number of observations(batch_size=64 in our case) to train the CNN. This increases the speed , and reduces the danger of correlation.

- the exploitation-exploration balance:A delicate balance needs to be maintained between exploitation (performing the same action which has produced results) and exploration(performing random actions). For example: You visit Amul after dinner everyday and get the chocolate ice cream every time .You can choose only one flavor of ice cream at a time. There are other flavours avialable ; yet you keep choosing the same one . This is exploitation . Another scenario is you choose a different flavour of ice-cream every day of the week . This is exploration . After exploration you find out that you like vanilla and butterscotch too. NOw you can choose between chocolate , vanilla and butterscotch . Yes ou do lose some iterations(money) while trying to explore more flavors and they turned out to be not palatable; but in the end you have more optons to choose from . This is what the balance of exploration and exploitation . To achieve this epsilon is used. Epsilon can be fixed or can be decided using some kind of function. a random number is generated using np.rand.random() and if it turns out to be less than epsilon a random action is taken . 


## Resources:
- This [resource](https://www.advisori.de/a-headless-gym-enviroment-for-every-browser-game/) helped me a lot in making the gym enviroment for the dino game . It also teaches you how to interact with the game javascript something i have no idea about.
- This [resource](https://medium.com/acing-ai/how-i-build-an-ai-to-play-dino-run-e37f37bdf153) was a great help in understanding how to tackle the problem at hand. I did not implement his code but his reward function is fantastic. With each passing iteration the negative reward for crashing decreses while the reward for surviving increases giving the agent incentive to increase reward.
-  This [youtube](https://youtu.be/wYIiMH1cIis) gave a beginner like me an idea on how to implement the deep q .
- This [resource](https://lilianweng.github.io/lil-log/2018/02/19/a-long-peek-into-reinforcement-learning.html) for the picture of the mdp architecture.
- [David Silver Lectures](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLzuuYNsE1EZAXYR4FJ75jcJseBmo4KQ9-)






















