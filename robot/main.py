import URsocket.UR as UR
import time
import numpy as np

ur=UR.control('172.20.10.9')
#Current_Joint
current_joint=ur.getActualJointPositions(False)
print('JOINT POSITIONS: ',current_joint)
current_pose=ur.getActualTCPPose()
print('TCP Pose: ',current_pose)
#Defining Relative and absolute points
start_joint=[0,-90,-100.77,-90,0,0]
entry_grab=[42,-49.76,-143.14,-189.59,0,-1.12]
grab_down=[28.64,-103.61,-147.51,-108.88,-13.36,18]
grip_pose=[0,-0.133,0,0,0,0]#relative
card_out=[0,0.352,0,0,0,0]#relative
card_push_pose=[0.45032,-0.165,0.115,1.595,0.339,0.816]
push1=[0,-0.02,0,0,0,0]
push=[0,0,0.002,0,0,0]#relative#ToolSpace
card_up=[0,0,0.1,0,0,0]
rotate_wrist=[0,0,0,0,-112,0]
insert_entry=[0.42288,0.42381,0.25451,0.803,2.002,2.152]
insert=[0,0.1,0,0,0,0]
slide_out=[0,-0.1,0,0,0,0]#relative
push_pose=[0.519,0.41286,0.25451,0.803,2.002,2.152]
push_cardIn=[0,0.064,0,0,0,0]#relative
push_clip_entry=[0.470,0.41286,0.25451,0.803,2.002,2.152]
push_clip=[0,0.064,0,0,0,0]#relative

#Function for calculating relative points
def Deg2Rad(deglist):
    radlist=[np.deg2rad(x) for x in deglist]
    return radlist
    
def rel2abs(pose=False,relPose=[],relPoseDeg=False):
    if pose==True:
        current=ur.getActualTCPPose()
    else:
        current=ur.getActualJointPositions(True)
        if relPoseDeg==True:
            relPose = [np.deg2rad(x) for x in relPose]
    target=[a + b for a, b in zip(current, relPose)]
    return target

                 #OPERATION

#MOVEJ to Starting Pose
ur.moveJ(Deg2Rad(start_joint),0.5,0.1,0,0)
#Open the gripper
ur.setToolDigitalOut(0,True)
ur.setToolDigitalOut(1,False)

ur.moveJ(Deg2Rad(entry_grab),0.5,0.1,0,0)
ur.moveJ(Deg2Rad(grab_down),0.5,0.1,0,0)
ur.moveL(rel2abs(True,grip_pose,False),0.5,0.1,0,0)

#Close the gripper
ur.setToolDigitalOut(0,False)
ur.setToolDigitalOut(1,True)

ur.moveL(rel2abs(True,card_out,False),0.5,0.1,0,0)#p5
ur.moveL(card_push_pose,0.5,0.1,0,0)#
ur.moveUntillcontact(push1,0.5)

ur.movelToolspace(push,True,0.1,0.1,0,0.0)#
ur.moveL(rel2abs(True,card_up,False),0.5,0.1,0,0)
ur.moveJ(Deg2Rad(rotate_wrist),0.5,0.1,0,0)

##INSERT##
ur.moveL(insert_entry,0.5,0.1,0,0)
ur.moveL(rel2abs(True,insert,False),0.5,0.1,0,0)
#Open the gripper
ur.setToolDigitalOut(0,True)
ur.setToolDigitalOut(1,False)

ur.moveL(rel2abs(True,slide_out,False),0.5,0.1,0,0)
ur.moveL(push_pose,0.5,0.1,0,0)
ur.moveL(rel2abs(True,push_cardIn,False),0.5,0.1,0,0)
ur.moveL(push_clip_entry,0.5,0.1,0,0)
ur.moveL(rel2abs(True,push_clip,False),0.5,0.1,0,0)
ur.moveJ(start_joint,0.5,0.1,0,0)
ur.disconnect()