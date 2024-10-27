import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st

def research_industry(company_name):
    query = f"{company_name} AI industry overview"
    url = f"https://www.google.com/search?q={query}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    insights = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if "http" in href:
            insights.append(href)
    
    return insights[:5]  

def generate_use_cases(industry_insights):
    use_cases = []
    for insight in industry_insights:
        use_cases.append({
            "use_case": "AI-driven customer support",
            "description": "Using AI chatbots to enhance customer support services.",
            "source": insight
        })
        use_cases.append({
            "use_case": "Predictive maintenance",
            "description": "Leveraging machine learning models to predict equipment failures.",
            "source": insight
        })
    return use_cases

def find_datasets(use_cases):
    datasets = []
    for case in use_cases:
        datasets.append({
            "use_case": case['use_case'],
            "dataset_link": f"https://www.kaggle.com/search?q={case['use_case'].replace(' ', '+')}"
        })
    return datasets

import os

def generate_final_proposal(use_cases, datasets):
    os.makedirs("outputs", exist_ok=True)
    proposal = "## Final Proposal\n\n"
    proposal += "### AI/GenAI Use Cases\n\n"
    for case in use_cases:
        proposal += f"- **{case['use_case']}**: {case['description']} ([Source]({case['source']}))\n"
    
    proposal += "\n### Relevant Datasets\n\n"
    for dataset in datasets:
        proposal += f"- **{dataset['use_case']}**: [Dataset Link]({dataset['dataset_link']})\n"
    
    with open("outputs/final_proposal.md", "w") as file:
        file.write(proposal)

    df = pd.DataFrame(datasets)
    df.to_markdown("outputs/datasets.md", index=False)

    return proposal


st.title("Multi-Agent System for AI Use Case Generation")

company_name = st.text_input("Enter the Company Name", "Tesla")

if st.button("Generate Insights"):
    
    st.write("### Researching Industry...")
    industry_insights = research_industry(company_name)
    st.write("### Industry Insights", industry_insights)
    
    st.write("### Generating Use Cases...")
    use_cases = generate_use_cases(industry_insights)
    st.write("### Use Cases", use_cases)
    
    st.write("### Finding Datasets...")
    datasets = find_datasets(use_cases)
    st.write("### Relevant Datasets", datasets)
    
    st.write("### Generating Final Proposal...")
    final_proposal = generate_final_proposal(use_cases, datasets)
    st.markdown(final_proposal)

    st.success("Final proposal generated and saved as 'final_proposal.md' in the outputs folder.")
