
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

ParticipantResults=[]

Centre=psychopy.visual.Circle(win=Window, units="pix",
fillColor=[-1]*3, lineColor=[-1]*3, edges=128)
Centre.radius=12
CentreOffset=100
for Offset in [-1, +1]:
    Centre.pos=[CentreOffset * Offset, 0]

Context=

Centre.draw()



Radii=[21.6, 12, 2.4]
for Radius in Radii:
    Time=psychopy.core.Clock()
    Time.reset()
    
    Encircle=[0, 72, 144, 216, 288]
    EncircleOffset=random.choice([100, -100])
    Radius=random.choice(Radii)
    for Circles in range (len(Encircle)):
        [PosX, PosY]=psychopy.misc.pol2cart (
        Encircle[Circles], Radius)
        PosX=PosX+ EncircleOffset
        Circle.pos=[PosX, PosY]
        Circle.radius=25
        Circle.draw()
    Radii.remove(Radius)
    KeyPress=psychopy.event.waitKeys(keyList=['left', 'right', 'up'], 
    timeStamped=Time)
    print (KeyPress)
    ResponseTime=[Key.split()[1] for Key in KeyPress]
    for Keys in KeyPress:
        if KeyPress[0][0]=='left' or KeyPress[0][0]=='right':
            Response='IllusionPositive'
        else:
            Response='IlussionNegative'
        ParticipantResponse=[Response, ResponseTime]
    ParticipantResults.append(ParticipantResponse)
    Window.flip()
print(ParticipantResults)
Window.flip()
Window.close()

