from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain

def get_summary(success_rate, age, retirement_age):
    prompt = PromptTemplate.from_template(
        "A client aged {age} wants to retire at {retirement_age}. The Monte Carlo simulation shows a success probability of {success_rate:.2f}%. Write a short, clear explanation of this result and suggest what the client can do to improve their chances."
    )

    llm = Ollama(model="mistral")  # Assumes Ollama is running
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(age=age, retirement_age=retirement_age, success_rate=success_rate)
