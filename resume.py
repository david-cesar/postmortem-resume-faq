import os
from docling.document_converter import DocumentConverter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Initialize the LLM model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

prompt = (
    "Extraia do texto a seguir somente o problema e a solução adotada de modo detalhado com objetivo de criar uma base de dados para uma FAQ. Responda no formato markdown.\n\nTexto:\n{resume_document}"
)

input_folder = 'postmortem-original-docs'
output_folder = 'docs/postmortems'

# create docling converter
converter = DocumentConverter()

# search for all path and name files in the input folder
for root, dirs, files in os.walk(input_folder):
    for index, file in enumerate(files):
        rel_dir = os.path.relpath(root, '.')
        name, ext = os.path.splitext(file)
        file_path = os.path.join(rel_dir, file)
        print(f"File: {index+1} \nName: {name}")

        # parse files to .md with docling
        docling_result = converter.convert(file_path)
        markdown_content = docling_result.document.export_to_markdown()

        # llm invoke to resume
        full_prompt = prompt.format(resume_document=markdown_content)
        response = llm.invoke([HumanMessage(content=full_prompt)])

        # write llm result to new file .md with same name from original file
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, f"{name}.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(response.content)

        print(f"File {index+1} resumed with success.\n")