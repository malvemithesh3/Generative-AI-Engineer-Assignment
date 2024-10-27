## Overview

The **Generative AI Engineering Steps** application is a multi-agent system designed to generate AI and GenAI use cases for specific companies or industries. This application consists of three main agents that work together to research an industry, analyze trends, propose relevant AI use cases, and compile a final proposal with the necessary datasets.

## Table of Contents

1. [Problem Definition](#problem-definition)
2. [Architecture](#architecture)
3. [Prerequisites](#prerequisites)
4. [Setup Instructions](#setup-instructions)
5. [Running the Application](#running-the-application)
6. [File Structure](#file-structure)
7. [Output Files](#output-files)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)

## Problem Definition

The goal of this application is to:

- Research the industry or company to understand its market, key offerings, and strategic focus.
- Analyze trends in AI, ML, and automation within the industry.
- Propose relevant AI use cases.
- Collect datasets for implementing these use cases.
- Compile a final proposal, including references.

## Architecture

The application is composed of three primary agents:

- **Research Agent:** Gathers information about the industry and company.
- **Use Case Agent:** Analyzes market trends and generates AI/GenAI use cases.
- **Resource Agent:** Finds datasets for each use case and prepares the final report.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python (3.7 or later): [Download here](https://www.python.org/downloads/)
- Streamlit
- Other required libraries: `requests`, `beautifulsoup4`, `pandas`

You can install the required libraries using pip:

```bash
pip install streamlit requests beautifulsoup4 pandas
```
