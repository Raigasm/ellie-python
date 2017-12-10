
# Import PsychoPy libraries
import psychopy.visual
import psychopy.event
import psychopy.misc
import psychopy.core
import random
import psychopy.data
# Create a window
Window=psychopy.visual.Window(size=[600, 400], units="pix",
    fullscr=False, color=[1, 1, 1])
Instructions=psychopy.visual.TextStim(win=Window, color=[-1, -1, -1], 
wrapWidth=600)

Instructions.text="You will be presented with two centre-surround circles. \n\
Press the up-arrow if the centre circles are the same size. \n\
Press the left-arrow if the centre circle on the left is larger. \n\
Press the right-arrow if the centre circle on the right is larger. \n\
Press any key when you are ready to begin."
Instructions.draw()
Window.flip()
psychopy.event.waitKeys()
#Create list of responses
Responses=[]
#Create a circle
Target=psychopy.visual.Circle(win=Window, units="pix",
    fillColor=[-1]*3, lineColor=[-1]*3, edges=128)
Target.radius=12
TestOffset=100
for Offset in [-1, +1]:
    Target.pos=[TestOffset * Offset, 0]
    Target.draw()
#Create surrounding circles
LargeSurroundCircle=[0, 33, 66, 99, 132, 165, 198, 231, 264, 297, 330]
LargeSurroundRadius=18
for LargeSurround in range (len(LargeSurroundCircle)):
    [SurroundPosX, SurroundPosY]=psychopy.misc.pol2cart (
    LargeSurroundCircle[LargeSurround], LargeSurroundRadius)
    SurroundPosX=SurroundPosX+TestOffset
    Target.pos=[SurroundPosX, SurroundPosY]
    Target.radius=2
    Target.draw()
SmallSurroundCircle=[0, 45, 90, 135, 180, 225, 270, 315]
SmallSurroundRadius=18
for SmallSurround in range (len(SmallSurroundCircle)):
    [SurroundPosX, SurroundPosY]=psychopy.misc.pol2cart (
    SmallSurroundCircle[SmallSurround], SmallSurroundRadius)
    SurroundPosX=SurroundPosX-TestOffset
    Target.pos=[SurroundPosX, SurroundPosY]
    Target.radius=2
    Target.draw()
Window.flip()
#Start stopwatch
Stopwatch=psychopy.core.Clock()
Stopwatch.reset()

Response=psychopy.event.waitKeys(keyList=['left', 'right', 'up'], 
         timeStamped=Stopwatch)


for keys in Response:
    if Response[0]=='left':
        Response.append(IllusionPositive)
    if Response[0]=='right':
        Response[0]=IllusionReverse
    if Response[0]=='up':
        Response[0]=IlussionNegative
Responses.append(Response)
print(Responses)
Window.flip()
Window.getMovieFrame()
psychopy.event.waitKeys()
Window.close()

