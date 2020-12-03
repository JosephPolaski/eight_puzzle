**Eight Puzzle**
===

Joseph Polaski\
HW 8: Portfolio Project\
CS325 Algorithm Analysis\
Fall 2020

### **Overview**:

This 8-puzzle game uses Pygame for the GUI, I highly recommend checking it out! it was my first time working with Pygame and my first time doing anything front end with Python so it was definitely a learning experience that was alot of fun. 
- <a href="https://www.pygame.org/">Pygame.org</a>

Note: The project was developed with python 3.8.1 but mainly uses the python standard library so it should work with most recent versions of python 3.

### **8 - Puzzle Background**:

This is a number slider puzzle game with a size of n x n cells where where n = 3. There are (n<sup>2</sup> - 1) cells filled with numbers from (1...[n<sup>2</sup> - 1]). It can start out with any configuration other than the solved state. This game can be simply played by the user or it can determine whether or not the puzzle is solvable within a certain number of turns entered by the user. Below are examples of a solved and unsolved state.


|| unsolved| |        
|:--:| :--: |:--:| 
| 2 | 4 | 3 | 
| 7 | 5 |  | 
| 8| 6 | 1 |



|| solved | |
|:--:| :--: |:--:| 
| 1 | 2 | 3 | 
| 4 | 5 | 6 | 
| 7 | 8 |   | 

### **Controls for this game**:
- there are four possible move types. On any turn there may be 2 - 4 of them available.

    - Moves:
    1. up - click the tile above the white (blank space)
    2. down - click the tile below the white (blank space)
    3. left - click the tile to the left of the white (blank space)
    4. right - click the tile to the right of the white (blank space)

---
### **To Run on Windows (using cmd.exe)**:
* *this guide assumes you have some version of Python 3.x.x installed, as well as pip. if you do not you can find Python <a href="https://www.python.org"/>here</a> and some documentation on pip <a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">here</a>. You can also check if you have these with the following commands:*
    ```
    pip --version
    python --version
    ```

1. Ensure that all of the files in this package are all in the same directory. At minimum, the following need to be in within the same directory for this program to work properly:

    - requirements.txt
    - eight_puzzle.py
    - puzzle_board.py
    - verify_puzzle.py


2. Open cmd.exe in the directory where the files are located or navigate to the directory in the windows command line and create a virtual environment. Then activate it and upgrade pip:
    ```
    virtualenv venv
    .\venv\Scripts\activate
    python -m pip install --upgrade pip
    ```
    - this will create a new subdirectory for your virtual environment and activate the new environment. If you successfully activated your environment you sill see (venv) al lthe way to the left of your directory path in command prompt, like so:
    ```
    (venv) C:\Users\yourusername\Desktop\test_dir>
    ```
3. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Launch the game and enjoy!
    ```
    python eight_puzzle.py
    ```

### **To Run on Mac/Linux**:
* ### *Note to graders: This project will not run on OSU flip servers as Pygame cannot render a GUI there.*
* *this guide assumes you have some version of Python 3.x.x installed, as well as pip. if you do not you can find Python <a href="https://www.python.org"/>here</a> and some documentation on pip <a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">here</a>. You can also check if you have these with the following commands:*

1. Ensure that all of the files in this package are all in the same directory. At minimum, the following need to be in within the same directory for this program to work properly:

    - requirements.txt
    - eight_puzzle.py
    - puzzle_board.py
    - verify_puzzle.py


2. Open cmd.exe in the directory where the files are located or navigate to the directory in the windows command line and create a virtual environment. Then activate it and upgrade pip:
    ```
    virtualenv venv -p $(which python3)
    source ./venv/bin/activate
    pip3 install --upgrade pip
    ```
3. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Launch the game and enjoy!
    ```
    python3 eight_puzzle.py
    ```