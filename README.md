


### THE GAME

MACGYVER is a game build with PYTHON.

The purpose of the game is to move the main character in the labyrinth in order to pick up the objects. Once the objects have been picked up, the character must reach the guardian's position to end the game.

The objects are set randomly in the labyrinth. 


Main Goal:

Macgyver must collect all the objects from the labyrinth and take the guardian's position to earn the victory.

If Macgyver don't collect all the objects before reaching the guardian's position, the user loses the game.


### Installation

  ## Installation and execution in a virtual environment:

As part of the game installation, we proceed to set up through the Terminal a virtual environment, Virtualenv:

pip install virtualenv


We create and activate virtualenv :

  # Creation:

 '''virtualenv -p python3 env'''

  # Activation:

 '''source env/bin/activate'''

  # Finally we launch the game:

 '''python3 launch_game_macgyver.py'''

   ## Installation and execution of packages


In order to make the file executable we install the cx_Freeze module:


 '''python3 -m pip install cx_Freeze --upgrade'''

Then we create the setup.py file in which we make our game executable.

Then we generate a folder name build to execute the game:


 '''python3 setup.py build'''


In that folder we can find the the file (launchgame) we need to click on to actually launch the game.








