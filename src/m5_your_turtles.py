"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Jaclyn Setina.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg  # why is it doing this?

import rosegraphics as rg

window = rg.TurtleWindow()

elvis = rg.SimpleTurtle('turtle')
elvis.pen = rg.Pen('red', 3)
elvis.speed = 10  # Fast

size = 300

for k in range(3):
    elvis.pen_up()
    elvis.right(100)

    elvis.pen_down()
    elvis.draw_circle(100)


miley = rg.SimpleTurtle('turtle')
miley.pen = rg.Pen('green', 6)
miley.speed = 10

size = 300

for k in range(4):
    miley.pen_up()
    miley.left(100)

    miley.pen_down()
    miley.draw_square(100)



