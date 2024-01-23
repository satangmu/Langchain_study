from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True) # chat model을 사용하고 싶으면 True 아니면 False

memory.save_context({"input": "Hi!"}, {"output": "How are you?"})

memory.load_memory_variables({})
