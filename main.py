import autogen

config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")

llm_config = {
    "seed": 2024,
    "config_list": config_list,
    "temperature": 0,
}

agent_assistant = autogen.AssistantAgent(
    name="agent_assistant",
    llm_config=llm_config,
)

agent_proxi = autogen.UserProxyAgent(
    name="agent_proxi",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "agent_output",
        "use_docker": False,
    },
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
                    Otherwise reply CONTINUE, or the reason why the task is not solved yet."""
)

agent_proxi.initiate_chat(
    agent_assistant,
    message="""I need to write a  python script that will the following:
    1. go to airbnb
    2. search for Mendoza, Argentina stay from March 10, 2024 - March 17, 2024
    3. gather the results, no more than 10. The class html div to search is "c4mnd7m" 
    4. create a Pandas DataFrame with the results.
    4. print the dataframe to the screen
"""
)

agent_proxi.send(
    recipient=agent_assistant,
    message="""Please save the python script file you created to air1.py"""
)