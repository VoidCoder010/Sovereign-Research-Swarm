from src.orchestrator.engine import Orchestrator

def main():
    # Initialize the new Star-architecture engine
    gideon_swarm = Orchestrator()
    
    print("--- Gideon Swarm Online ---")
    while True:
        user_query = input("User: ")
        if user_query.lower() in ["exit", "quit"]:
            break
            
        # The Orchestrator handles all internal routing (Supervisor -> Worker -> Supervisor)
        result = gideon_swarm.execute(user_query)
        
        # Pull the final response from the message history
        final_msg = result["messages"][-1].content
        print(f"\nGideon: {final_msg}\n")

if __name__ == "__main__":
    main()















    
