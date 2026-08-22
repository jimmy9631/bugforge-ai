import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("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")
)


def generate_report(vuln_type, scope, steps, impact, fix):

    prompt = f"""
You are an experienced bug bounty hunter.

Create a professional and concise vulnerability report.

Vulnerability Type:
{vuln_type}

Affected Asset:
{scope}

Steps to Reproduce:
{steps}

Impact:
{impact}

Suggested Fix:
{fix}

Use this format:

Title:
Summary:
Steps to Reproduce:
Impact:
Remediation:

Do not invent information that was not provided.
"""

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return response.output_text.strip()
