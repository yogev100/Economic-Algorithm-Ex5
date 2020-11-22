from typing import List

# Class that represent an agent which has a 'all_item' variable as a list,
# so that the index of the list represents the item i and the value in this index is the value of the agent in this item
class Agent:

    # Argument constructor that gets a list of values and assign it to the agent
    def __init__(self, items:List[float]):
        self.all_items = items
        self.agent_items = []
        self.envy_list = []
        self.list_value_agent = []
        self.total_value = 0

    # A function that gets an item_index and return the value of the agent for this item
    def item_value(self,item_index:int)->float:
        return self.all_items[item_index]

# A function that receives a list of agents and a bundle and initializes all the values of each agent
def init_agents(agents:List[Agent], bundles: List[List[int]]):
    for i in range(0, len(agents)):
        list_value_for_agent(agents[i], bundles)

    for i in range(0,len(agents)):
        agents[i].agent_items = bundles[i]
        agents[i].total_value = agents[i].list_value_agent[i]

    for i in range(0, len(agents)):
        for j in range(0,len(agents)):
            if i != j:
                if agents[i].total_value < agents[i].list_value_agent[j]:
                    agents[i].envy_list.append(j)
# A function that receives an agent and a bundle and initializes 'list_value_agent' variable of this agent
def list_value_for_agent(agent:Agent, bundles: List[List[int]])->List[float]:
    for i in range (0,len(bundles)):
        sum = 0
        for j in range(0, len(bundles[i])):
            sum += agent.item_value(bundles[i][j])
        agent.list_value_agent.append(sum)

# A function that receives two indexes of agents and a list of agents
# and checks whether in removing one item from agent 2, agent 1 will still be jealous of it
def is_no_envy(agent_1:int, agent_2:int, agents:List[Agent])->bool:
    if agent_2 not in agents[agent_1].envy_list:
        return True
    else:
        for item in range(0,len(agents[agent_2].agent_items)):
            agent2_value_minus_one_item = agents[agent_1].list_value_agent[agent_2] - agents[agent_1].all_items[item]
            if agents[agent_1].total_value >= agent2_value_minus_one_item:
                return True
        return False

# A function that receives a list of agents and a bundle and checks whether the distribution of items to the agents is EF1
def is_EF1(agents:List[Agent], bundles:List[List[int]])->bool:
    init_agents(agents, bundles)
    for agent_1 in range(0,len(agents)):
        for agent_2 in range(0,len(agents)):
            if agent_1 !=agent_2:
                if not is_no_envy(agent_1,agent_2, agents):
                    return False
    return True

def example_1():
    agent1, agent2, agent3 = Agent([3, 2, 4, 2, 1]), Agent([4, 3, 2, 2, 3]), Agent([1, 4, 2, 4, 2])
    agents = [agent1, agent2, agent3]
    # bundles = [[0, 2], [1], [3, 4]]
    bundles = [[0, 1, 2], [4], [3]]
    return agents, bundles

def example_2():
    agent1, agent2, agent3 = Agent([3, 2, 4, 2, 1]), Agent([4, 3, 2, 2, 3]), Agent([1, 4, 2, 4, 2])
    agents = [agent1, agent2, agent3]
    bundles = [[0, 2], [1], [3, 4]]
    return agents, bundles

def example_3():
    agent1, agent2, agent3, agent4 = Agent([3,6,5,1,2,1]), Agent([4,7,5,3,2,2]), Agent([2,4,6,4,4,3]), Agent([1,5,6,4,5,3])
    agents = [agent1, agent2, agent3, agent4]
    bundles = [[2],[3,5],[0,1],[4]]
    return agents, bundles

def print_data(agents:List[Agent], bundles:List[List[int]]):
    for i in range(0,len(agents)):
        print("Agent"+str(i+1)+" items value: ",agents[i].all_items, "Agent"+str(i+1)+" items: ", bundles[i])

def main():
    agents, bundles = example_1()
    print_data(agents, bundles)
    print("example 1 is EF1 ? ", is_EF1(agents, bundles))
    agents, bundles = example_2()
    print_data(agents, bundles)
    print("example 2 is EF1 ? ", is_EF1(agents, bundles))
    agents, bundles = example_3()
    print_data(agents, bundles)
    print("example 3 is EF1 ? ", is_EF1(agents, bundles))

if __name__ == '__main__':
    main()