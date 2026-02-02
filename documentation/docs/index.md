---
icon: lucide/rocket
---

# :lucide-diamond: Introduction

This project was made by Roméo AGOSTINO, Théo BIGAND, Moussa DRAME & Mathieu AUDIBERT for a [ESILV project](https://www.esilv.fr/).

```mermaid
graph TB
    subgraph "Data Source"
        A[Kaggle Dataset<br/>Cars India Pre-Owned]
    end

    subgraph "ETL Pipeline"
        B[Extract Phase<br/>CSV Data Extraction]
        C[Transform Phase<br/>Data Cleaning & Enrichment]
        D[Load Phase<br/>MongoDB Insertion]
    end

    subgraph "Database"
        E[(MongoDB<br/>Cars Collection)]
    end

    subgraph "API Layer"
        F[FastAPI Backend<br/>Endpoints]
        F1["/api/v1/etl/extract"]
        F2["/api/v1/etl/transform"]
        F3["/api/v1/etl/load"]
        F4["/api/v1/etl/workflow"]
    end

    subgraph "Containerization"
        G[Docker Images<br/>Backend & Frontend]
        H[Docker Compose<br/>Orchestration]
    end

    subgraph "CI/CD Pipeline"
        I[GitHub Actions]
        J[Build Workflow<br/>Docker Images]
        K[Promote Workflow<br/>GitHub Artifactory]
    end

    subgraph "Documentation"
        L[Zensical Docs<br/>Project Documentation]
    end

    A -->|CSV File| B
    B -->|Extracted Data| C
    C -->|Transformed Data| D
    D -->|Insert Records| E
    
    E -->|Query Data| F
    F --> F1
    F --> F2
    F --> F3
    F --> F4
    
    F -->|Containerized| G
    G -->|Defined in| H
    
    H -->|Deployed via| I
    I --> J
    I --> K
    
    K -->|Registry| G
    
    L -.->|Documents| A
    L -.->|Documents| B
    L -.->|Documents| F
    L -.->|Documents| G

    style A fill:#e1f5ff
    style E fill:#ffe1e1
    style F fill:#e1ffe1
    style G fill:#fff4e1
    style I fill:#f0e1ff
    style L fill:#ffe1f5
```

## Technical stack :lucide-braces:

* Python :simple-python:
* MongoDB :simple-mongodb:
* Docker :simple-docker:
* K8S :simple-kubernetes:
* Git/GitHub :simple-git:
* Github Actions :simple-githubactions:
* Zensical 

---

## Doc Plan :lucide-drafting-compass:

| Link                                    | Description                          |
| --------------------------------------- | ------------------------------------ |
| 1. **[Context](./context.md)**          | The context of this project          |
| 2. **[Objectives](./objectives.md)**    | The objectives of this project       |
| 3. **[Tasks](./tasks.md)**              | Our tasks w/ our current progression |
| 4. **[Optionnal tasks](./opt-task.md)** | Optionnal tasks w/ our progression   |
| 5. **[Links](./link.md)**               | All the important links              |
| 6. **[Useful commands](./usfl-cmd.md)** | List of useful commands              |

---

## Get Started :lucide-arrow-up-right: 

!!! info
    
    Python is required to run this project.

Clone the repo :

``` bash 
git clone https://github.com/MathieuAudibert/Conteneurisation-Orchestration.git
```

Then, setup your virtual env :

=== "Python :simple-python: / Windows :fontawesome-brands-windows:"

    ``` cmd
    python -m venv venv
    venv\Scripts\activate
    
    ```

=== "Python :simple-python: / MacOS :simple-apple:/Linux :simple-linux:"

    ``` bash
    python -m venv venv
    source venv/bin/activate
    ```

=== "Uv :simple-uv:"

    ``` bash
    uv init 
    ```

Once you've installed and setted your virtual env, you can install the necessary dependancies w/ [pip](https://pypi.org/project/pip/) or [uv](https://docs.astral.sh/uv/).

=== "pip :simple-pypi:"

    ``` bash
    pip install -e .
    ```

=== "uv :simple-uv:"

    ``` bash
    uv pip install -e .
    ```

You're all done now !