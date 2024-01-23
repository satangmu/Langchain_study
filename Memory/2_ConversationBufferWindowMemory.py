from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    return_messages=True,
    k=4 # 크기 지정
)

def add_message(input, output):
    memory.save_context({'input': input}, {'output': output})

add_message(1, 1)
add_message(2, 2)
add_message(3, 3)
add_message(4, 4)
add_message(5, 5)

memory.load_memory_variables({})

# 출력 결과
# {'history': [HumanMessage(content='2'),
#   AIMessage(content='2'),
#   HumanMessage(content='3'),
#   AIMessage(content='3'),
#   HumanMessage(content='4'),
#   AIMessage(content='4'),
#   HumanMessage(content='5'),
#   AIMessage(content='5')]}
