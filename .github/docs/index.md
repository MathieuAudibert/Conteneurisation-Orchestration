---
icon: lucide/rocket
---

# Introduction

This project was made by Roméo AGOSTINO, Théo BIGAND, Moussa DRAME & Mathieu AUDIBERT for a [esilv project](https://www.esilv.fr/).

## Technical stack

* Python
* MongoDB
* Docker
* K8S
* Github Actions
* Zensical

---

## Plan

| Link                                    | Description                          |
| --------------------------------------- | ------------------------------------ |
| 1. **[Context](./context.md)**          | The context of this project          |
| 2. **[Objectives](./objectives.md)**    | The objectives of this project       |
| 3. **[Tasks](./tasks.md)**              | Our tasks w/ our current progression |
| 4. **[Optionnal tasks](./opt-task.md)** | Optionnal tasks w/ our progression   |
| 5. **[Links](./links.md)**              | All the important links              |

---

## Get Started

!!! info
    
    Python is required to run this project.

Clone the repo :

``` bash 
git clone https://github.com/MathieuAudibert/Conteneurisation-Orchestration.git
```

Then, setup your virtual env :

=== "Python & Windows "

    ``` cmd
    python -m venv venv
    venv\Scripts\activate
    
    ```

=== "Python & MacOS/Linux"

    ``` bash
    python -m venv venv
    source venv/bin/activate
    ```

=== "Uv"

    ``` bash
    uv init 
    ```

Once you've installed and setted your virtual env, you can install the necessary dependancies w/ [pip](https://pypi.org/project/pip/) or [uv](https://docs.astral.sh/uv/).

=== "pip"

    ``` bash
    pip install -r requirements.txt
    ```

=== "uv"

    ``` bash
    uv pip install -r requirements.txt 
    ```

You're all done now !