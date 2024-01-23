from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.1)

memory = ConversationSummaryBufferMemory(llm=llm,
                                         max_token_limit=150,
                                         return_messages=True)

def add_message(input, output):
    return memory.save_context({'input': input}, {'output': output})

def get_history():
    return memory.load_memory_variables({}) 

add_message("Hi I'm Jaeyeon, I live in South Korea", "Wow that is so cool!")
add_message("South Korea is so pretty", "I wish I could go!!!")

get_history()
