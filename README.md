## install Steamlit on Lunix

* On Ubantu install `python 3`

```
sudo apt-get install python3-pip
```
* install `pipenv`
pipenv - Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. 

```
pip3 install pipenv
```
* Create a new environment with Steamlit
    
    - Navigate to your project folder
    ```
    cd myproject
    ```
    - Create a new Pipenv environment in that folder and activate that environment:
    ```
    pipenv shell
    ```
    `pipefile` will appear in `myprojects/`<br>
    environment and its dependencies are declare in this file.

    - Install Streamlit in your environment 
    ```
    pip install streamlit 
    or
    pipenv install streamlit
    ```
    - Test that the installation worked <br>this  will open in your browser
    ```
    streamlit hello
    ```

## Use your new environment

- Any time you want to use the new environment, you first need to go to your project folder (where the Pipenv file lives) and run:

```
pipenv shell
```
- Now you can use Python and Streamlit as usual:
```
streamlit run myfile.py
```