# YSA-presentation
Slide decks and example code for Jack's September YSA presentation


## Getting Started

### Step 1
If you're on Windows, it is highly recommended that you download the Git Bash Shell before starting. You can do some of the similar things in cmd, but it's just not the same. https://git-scm.com/downloads

If you're on Mac you can use the terminal. If you're on Linux, bonus cookies to you.

In bash, run

```shell
pip --version
```

to make sure you have pip installed. If not, you'll need to start by installing python. https://www.python.org/downloads/.
I'm using 3.6.5 as my global interpreter for this project. If you use an older one (like python 2) I can't guaruntee if it will work.

### Step 2
The next step is to clone this git repo, which you can do with:
```shell
git clone https://github.com/Novacer/YSA-presentation.git
cd YSA-presentation  # if the clone worked properly you should be able to go to this folder
```

Alternatively, you can fork it into your own github account as well.


### Step 3
To install the dependencies needed to run this project you can do 

```shell
pip install -r requirements.txt
```
which will install the python stuff globally. Some of you may want to make a virtual environment so that these new dependencies don't conflict with your current python installation. (This is purely optional, though in software development it is seen as a best practice.) [Here is how you can do it.](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv)


### Step 3.5
If you want to work on the Angular UI, you'll need to install the ```node_modules``` for it as well. To do this do

```shell
cd example-ui/angular-frontend
npm install
```

Once you have all the dependencies installed you are ready to go.

## Actually running the stuff.

I've conveniently written two bash scripts that will do most of the work for you. If you just want to run the APIs, do
```shell
# Method 1
source run_backend.sh

# Method 2
. run_backend.sh
```
The two methods are equivalent in bash.

You can run the angular in the same way, replacing ```run_backend.sh``` with ```run_frontend.sh```

Feel free to read the ```.sh``` files to understand how this actually works.
