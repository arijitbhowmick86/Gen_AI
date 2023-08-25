import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain




input_template = """

Describe the person : {person}

"""

temp = PromptTemplate(input_variables='person', template=input_template)
#llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
#chain = LLMChain(llm=llm, prompt=temp)

print('Inside Langchain function!')
#print(chain.run(person='Elon Musk'))