from langchain.memory import ConversationSummaryBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(temperature=0.1)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=120,
    memory_key="chat_history",
    return_messages=True,
    
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI talking to a human"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}"),
])


chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True, # log 출력
    
)
chain.predict(question="My name is Jaeyeon")
chain.predict(question="I live in Iksan")
chain.predict(question="What is my name?")
