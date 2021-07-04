# **REPORT**
## TASK 1:
* The agent is not trying to planning to stay in the centre and east square. Its quite a safe option beacause we are getting a reward of -40 up on hitting by the MM.

* It took nearly 126 iterations for our stepcost (-20) to converge

* In the **east** square the agent is only trying to **hit or shoot** the target most of times, as there are high chances for getting a reward.

* The utility values for hit is lower than shoot

* The agent is taking chances by choosing to **shoot** when MM has health of 25, even from the west square 

* When the agent is out of arrows  and there is a possibility of crafting,  the agent is choosing to craft arrows in the north. But if he already has the arrows he is travelling down to the centre.  

* Agent is trying to end the game as soon as possible by travelling towards east as there is a stepcost factor.

* Agent is not trying to hit MM from centre due to the very little probablity. But he took chances to hit from east may be due to the greater decrease in the health of MM.

* As expected the agent is **not** trying to shoot more **frequently** from the **west** as there is a low probablity of a strike.  And also that will cost an arrow.


### SIMULATION
* START STATE = (W,0,0,D,100)
    
        1. (W,0,0,D,100); RIGHT

        2. (C,0,0,D,100); RIGHT

        3. (E,0,0,D,100); HIT

        4. (E,0,0,R,50 ); hit (fails; MM strikes)

        5. (E,0,0,D,75 ); HIT (fails; low probablity)

        6. (E,0,0,D,75 ); HIT 

        7. (E,0,0,R,25 ); HIT (fails; low probablity)

        8. (E,0,0,R,25 ); hit (fails; MM Strikes)

        9. (E,0,0,D,50 ); Hit

        10. (E,0,0,D,0  ); NONE


* START STATE = (C,2,0,R,100)
    
        1. (C,2,0,R,100); UP

        2. (N,2,0,R,100); CRAFT

        3. (N,1,2,D,100); DOWN (fails; => east)

        4. (E,1,2,D,100); HIT (fails; low probablity)

        5. (E,1,2,D,100); HIT 

        6. (E,1,2,D,50 ); SHOOT 

        7. (E,1,1,R,25 ); shoot (fails; MM Strikes) 

        8. (E,1,0,D,50 ); HIT (fails; low probablity)

        9. (E,1,0,D,50 ); HIT (fails; low probablity)

        10.(E,1,0,R,50); HIT
        
        11.(E,1,0,R,0); NONE

* COMMENTS         
    * IN **EAST** square the agent is always trying to hit and shoot.

    * Not planning on moving away from **East**. As it only increases cost. As you can see in the first example, the agent only choose to move right towards the east square.

    * Agent is trying to move towards east direction from  each square.
***

## TASK 2:

### Case 1:
    * There is no significant change in the approach of the agent.

    * Initially the agent is not moving away from the **East** square may be due to the increasing negative cost. After change, **LEFT** action takes agent to the **West** square where the probablity of completing the game is low compared to that of in the **centre** square. It only makes the situation worse by further increase in the total negative cost. So agent is not choosing left action here.

    * The number of iterations here were same as that of the original case.  


### Case 2:

    * Agent is choosing the **stay** action more frequent than before.

    * Since there is no stepcost for stay action, indirectly there is no need for agent to complete the game ASAP.

    * Theoritically speaking, the agent can stay in the **west, north and south** squares for longer time or to hide from the attacks of MM, as MM cannot effect IJ in these positions.

    * If we run a simulation, from the start state as west square, the game will never end because the stay action dominates other actions which has a zero utility value.

    * It took 63 iterations for convergence



### Case 3:    
    * Low gamma value caused decrease in number of iterations as the difference value can be easlily maintained under 0.001 with reduced gamma. It took 9 iterations for convergence.

    * Left action in east square was choosen for some states; this was not the case earlier. This is because, earlier we have this stepcost building up with 0.999 as gamma, but here we have some relaxation wiht the decreased  negative contribution to the utility. We can say the agent is not trying to be hit by MM. 