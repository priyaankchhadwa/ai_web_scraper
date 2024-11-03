from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model='llama3.2')

template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_llm(chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm

    parsed_result = []

    for i, chunk in enumerate(chunks):
        print(f'parsing chunk {i} of {len(chunks)}')
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_description})
        print(f'parsed chunk {i} of {len(chunks)}')
        parsed_result.append(response)

    return '\n'.join(parsed_result)