[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/tTztJ7yI)
# Wildcard Project

You have a cool idea for an algorithms project? Use this repository. Make sure
to explain what problem you're solving, how you're doing it, and that you test
your code.

# Task:
- ### **Objective**: 
  - Improving a previous project of mine, (initially focused on analyzing soccer passes and interceptions) by using algorithms to better understand the game's flow and tactics.

- ### **Approach**: 
  - Use Python’s graphing and algorithm libraries to create visual representations for in-depth analysis. Players are treated as points (vertices), and their passes to each other as lines (edges), to map out interactions and strategies during a match.

- ### **Purpose**: 
  - The goal is to apply algortihms such as Kruskal's MST, or Tarjan's SCC to show more detailed insights into team strategies and player roles, thus improving the overall understanding of soccer matches through visual and algorithmic analysis.

# Instructions to Directly Run Code (Dependencies)
### **Dependencies** - Anaconda Navigator: https://www.anaconda.com/download
- In Anaconda Navigator, run Jupyter Notebook 6.5.4
- In Jupyter Notebook, click the 'Upload' button at the top right 
- Upload the following files found in this GitHub repository:
  - CHELSEA.png
  - LUTON.png
  - Soccer Pitch.png
  - Chelsea vs Luton Town Gathered Data.xlsx
  - Chelsea vs Luton Town Wildcard Project Code - Algorithms.ipynb

Once uploaded, click on the "Chelsea vs Luton Town Wildcard Project Code - Algorithms.ipynb" file which should appear with a book icon now, then click run on each individual cell or click the 'Cell' tab and click on the 'Run All' option.

I used Python because it has built in libraries with some algorithms already available. Moreover, graphing is much easier in Python.

# Match Reference:
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/f538df15-6aa3-45f0-9727-032ddf57a4d2)


# Example Output


## Randomly Chosen Graphs from Time Interval 10-20:


![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/a39edfd6-d6e3-40f8-a8d4-067f3e647253)

![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/0e1a1949-5273-4efa-bba4-58be797b4ba5)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/e3145420-5ee3-46d1-b447-245e147972ba)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/e4210f7e-7067-4a41-a9fd-542507c55db9)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/82698e93-058c-4982-80e6-6a9897eec96c)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/177ba70b-0c4b-4817-b2aa-628b57dcf229)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/b98c6b8a-3b2c-4eb6-b923-df865c0417fe)



# Analysis/Reasoning
## Explaining Graph Types & Their Interpretation:
### •	Tarjan's Strongly Connected Components (SCC):

  - **Focus**: An SCC in a football network is a subset of players where every player is reachable from every other player through a sequence of passes. In simpler terms, it's a group where you can find a path       of passes from any player to any other player within the same group.
  
  - **Example in Football**: An SCC might include a set of players who are involved in a particular phase of play, like building out from the back. Here, the ball can be passed in a loop among these players           without involving others outside this component. 
  
  - **Relevance**: SCCs are crucial for understanding the team's internal connectivity and coherence. They can highlight key areas of the pitch where the team is particularly strong in maintaining possession and     can also identify potential weaknesses if certain players or areas are not well-included into the main play.

### •	Communities:

  - **Focus**: Communities in a football passing network identify groups of players who frequently interact more with each other than with players outside their group.
  
  - **Example in Football**: A community could be formed by attackers who often pass among themselves, a defensive unit that works closely to maintain possession, or midfielders who regularly exchange passes.
  
  - **Relevance**: Identifying communities helps in understanding the team's tactical sub-units and how they function together. For instance, it might reveal a strong partnership on the left flank between a           winger and a left-back, suggesting a tactical focus on attacking down that specific side.

### •	Eigenvector Centrality:

  - **Focus**: This metric indicates the influence of a player in a passing network. A player with high eigenvector centrality is not just connected to many others but is also connected to those who themselves       are well connected.
  
  - **Example in Football**: A midfielder who frequently exchanges passes with key players (like forwards and wingers) would have high eigenvector centrality.
  
  - **Relevance**: It highlights players crucial in linking various parts of the team, often pivotal in transitioning play from defense to attack or in maintaining possession effectively.

### •	Krusksal's Minimum Spanning Tree (MST):

  - **Focus** : MST is a network that connects all the nodes (players) with the minimum total edge weight (least number of passes), without creating any loops.
  
  - **Example in Football**: An MST can show the most direct connections between players needed to involve the entire team, often used for building from the back or quick counter-attacks.
    
  - **Relevance**: It shows the team's most efficient passing routes and can identify key players essential for maintaining team connectivity with minimal passes. 

### •	Influence Graph (using PageRank):

  - **Focus**: This graph uses the PageRank algorithm to identify the most influential players in the network based on their involvement in the play.
  
  - **Example in Football**: A player who is often involved in critical plays, like initiating attacks or breaking down opposition plays, will have a higher PageRank score.
  
  - **Relevance**: It helps in pinpointing players who are pivotal in the team’s gameplay, often dictating the tempo or being the focal point in critical situations.

## Using the Graphs to Tell a Story:
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/003fd004-23a8-4104-b318-3f6ce1850e99)

**Eigenvector Centrality Graph**:

- This graph highlights the key role of central defender Thiago Silva in Chelsea's ball distribution and possession maintenance. Moreover, it shows that Chelsea's defenders were crucial in transitioning the ball from defense to attack and in retaining possession, with Silva playing a pivotal role (highest eigenvector centrality in the time interval). The three highest eigenvector centralities were achieved by the central defenders.

**Community Modularity Graph**:

- This graph shows that Chelsea's right-hand side players interacted much more frequently than those on the left. Thus suggesting a tactical emphasis on attacking through the right side, likely targeting vulnerabilities in Luton's left-side defense.

To better understand the specific contributions of Thiago Silva and his defensive colleagues during the time frame, we can examine Chelsea's Minimum Spanning Tree and Influence Graphs for more tactical insights.

![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/368333a3-f2ae-4282-a8e1-887a0e057338)

**Prominent Roles of Gallagher and Silva**:

- Gallagher and Silva are consistently central in both the Minimum Spanning Tree and Player Influence Graph, indicating their crucial roles in Chelsea's game strategy.

**Thiago Silva's Influence**:

- The Influence Graph highlights Thiago Silva due to his high number of passes, backed up by match data that notes him as a key distributor of the ball (highest number of passes in the interval).

**Defense as a Starting Point**:

- The Minimum Spanning Tree shows three paths beginning with central defenders, emphasizing their importance in initiating plays and controlling the game from the back.

**Connor Gallagher's Linkage Role**:

- Gallagher's involvement in four paths within the Minimum Spanning Tree, along with his prominent node size in the Influence Graph, signifies his essential role in linking defense and attack.

Based on these findings from the graphs, we can begin to piece together Chelsea's general gameplan and strategy. Attempting to build-up play from the back through Thiago Silva, then centrally through Connor Gallagher, with the majority of play ending up on the right side of Chelsea's formation.

### Comparing Chelsea's and Luton's Strongly Connected Components:



![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/20feb696-95bd-4806-8bab-b30816f9455f)

**Chelsea's SCC Analysis**:

- The graph shows all Chelsea players connected, indicating excellent team coordination and ball movement. The high connectivity suggests high possession and effective use of the ball across the team, contributing to a dominant period for Chelsea.

**Luton's SCC Analysis**:

Luton's graph displays only four players, significantly spaced apart. This sparse connectivity highlights several tactical challenges:

- **Reliance on Individual Efforts**: The considerable distances between the connected players suggests a dependence on individual skills rather than collective team play.

- **Challenges in Building Attacks**: The graph indicates difficulty in forming cohesive attacking moves, with the majority of the passes being long distance.

- **Weakness in Maintaining Possession**: The limited connections suggest that Luton struggled to keep the ball and build offensive pressure.

Luton's SCC graph shows us the areas where Luton's gameplay was lacking, thus impacting their overall performance in the interval.


### Summary:

Based on the specific graphs we chose, here's a tactical summary for the 10-20 Minute Interval of the match:

- **Key Players**: Thiago Silva and Connor Gallagher were crucial in ball distribution and linking defense to attack.

- **Tactical Focus**: The majority of play was directed through Chelsea's right side, exploiting weaknesses in Luton's left defense.

- **Team Dynamics**: Chelsea showed strong coordination with all players connected, indicating effective ball control. In contrast, Luton struggled with limited player connections and cohesion.

- **Overall Strategy**: Chelsea put together attacks from the back to the right flank, maintaining dominance and control during this interval.


## Conclusion

The analysis I provided using these graphs is just an example of the insights we can gather by applying algorithms to match-gathered data. These graphs help us understand key player roles, team strategies, overall game dynamics and many more insights. Therefore, we can demonstrate the application of data analysis with algorithms to help reveal important patterns and tactics in sports, giving us a valuable, deeper understanding of how any game is played.



# References:
### Specific Match:

https://www.chelseafc.com/en/video/full-match-chelsea-3-0-luton-town

### Algorithms taken from:

https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

https://www.geeksforgeeks.org/eigenvector-centrality-centrality-measure/

https://www.geeksforgeeks.org/community-detection-in-social-networks-using-brute-force-method/

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

https://www.geeksforgeeks.org/page-rank-algorithm-implementation/

### Debugging Assistance:

https://chat.openai.com/
