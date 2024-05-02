[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/tTztJ7yI)
# Wildcard Project

You have a cool idea for an algorithms project? Use this repository. Make sure
to explain what problem you're solving, how you're doing it, and that you test
your code.

# Task:
Applying algorithms to improve a project of mine which was originally centered around Passes and Interceptions to help tell the story of a soccer/football match. The primary motive for this project was to provide more insights and tactical analysis for match data by visually applying some of the algorithms we learned in class. Using Python's built in graphing and algorithm libraries, I hoped to visually demonstrate the purpose of some of these algorithms with vertices (which were players) and edges (which were passes).

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


# Output
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/f538df15-6aa3-45f0-9727-032ddf57a4d2)

## Randomly Chosen Graphs from Time Interval 10-20:


![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/25959447-0874-40e0-98d5-a236b12e0d28)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/0e1a1949-5273-4efa-bba4-58be797b4ba5)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/e3145420-5ee3-46d1-b447-245e147972ba)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/e4210f7e-7067-4a41-a9fd-542507c55db9)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/82698e93-058c-4982-80e6-6a9897eec96c)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/177ba70b-0c4b-4817-b2aa-628b57dcf229)
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/b98c6b8a-3b2c-4eb6-b923-df865c0417fe)



# Analysis/Reasoning
## Graph Types & Their Interpretation:
### •	Strongly Connected Components (SCC): (Tiki-Taka)

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

### •	Minimum Spanning Tree (MST):

  - **Focus** : MST is a network that connects all the nodes (players) with the minimum total edge weight (least number of passes), without creating any loops.
  
  - **Example in Football**: An MST can show the most direct connections between players needed to involve the entire team, often used for building from the back or quick counter-attacks.
    
  - **Relevance**: It shows the team's most efficient passing routes and can identify key players essential for maintaining team connectivity with minimal passes. 

### •	Influence Graph (using PageRank):

  - **Focus**: This graph uses the PageRank algorithm to identify the most influential players in the network based on their involvement in the play.
  
  - **Example in Football**: A player who is often involved in critical plays, like initiating attacks or breaking down opposition plays, will have a higher PageRank score.
  
  - **Relevance**: It helps in pinpointing players who are pivotal in the team’s gameplay, often dictating the tempo or being the focal point in critical situations.

## Using the Graphs to Tell a Story:
![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/003fd004-23a8-4104-b318-3f6ce1850e99)

Our eigenvector centrality and community modularity graphs paint a simple image of what exactly Chelsea utilized to build-up play and generate attacks. The community modularity graph suggests that players on the right hand side of Chelsea’s formation interacted with each other far more often than the player’s on the left hand side. This shows that Chelsea were consistently attempting to attack Luton’s left side. Moreover, through the Eigenvector centraility graph, we observe how vital the Central Defender Thiago Silva was for Chelsea's distribution of the ball and in maintaining possession. The Eigenvector graph emphasizes how important the Chelsea defenders were in transitioning the ball from defense to attack and how well they helped the team hold the ball.

But just how important was Thiago Silva and his defensive partners in the interval? We can further verify by specifically taking a look at Chelsea's Minimum Spanning Tree and Influence Graphs:

![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/368333a3-f2ae-4282-a8e1-887a0e057338)

Comparing Chelsea's and Luton's Strongly Connected Components:



![image](https://github.com/COSC3020/wildcard-project-Assel-Aljazwe/assets/157559559/20feb696-95bd-4806-8bab-b30816f9455f)




# References:
### Algorithms taken from:

https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

https://www.geeksforgeeks.org/eigenvector-centrality-centrality-measure/

https://www.geeksforgeeks.org/community-detection-in-social-networks-using-brute-force-method/

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

https://www.geeksforgeeks.org/page-rank-algorithm-implementation/

### Debugging Assistance:

https://chat.openai.com/
