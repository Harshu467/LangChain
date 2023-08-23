from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os
import secrete  

llm = OpenAI(openai_api_key=secrete.OPEN_API_KEY ,temperature=0.7)

def get_restaurant_name_and_menu_items(cuisine):
    # Define the prompt template for Restaurant Name
    prompt_template_name =  PromptTemplate(
        input_variables=['cuisine'] ,
        template="I want to open a restaurant for {cuisine} food. Please suggest me a fancy and creative name for my restaurant."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Define the prompt template for Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="""Suggest some menu items for {restaurant_name}. Return the 5 menu items as comma-separated values."""
    )
    food_item_chain = LLMChain( llm=llm, prompt=prompt_template_items ,output_key="menu_items")

    # Define the sequential chain
    chain = SequentialChain(
        chains=[name_chain, food_item_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "menu_items"],
    )

    # Generate the response
    response = chain({"cuisine": cuisine})
    # print(response)
    return response
# if __name__ == "__main__":
#     result=get_restaurant_name_and_menu_items("Indian")
print(get_restaurant_name_and_menu_items("Indian"))