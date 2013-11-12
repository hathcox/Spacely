# -*- coding: utf-8 -*-
from django_socketio.events import on_message
from django_socketio.events import on_connect
from spacely.libs.WebsocketManager import WebsocketManager
from spacely.physics.Vector import Vector
import logging, json, jsonpickle

logger = logging.getLogger(__name__)

class Event():
	def __init__(self):
		self.type = 'UPDATE'
		self.value = {}
		pass


@on_message(channel="^zone-")
def my_message_handler(request, socket, context, message):
    print 'Got Message'
    event_type = message['type']
    event_value = message['value']
    socket_id = socket.socket.session.session_id
    SPEED = 8
    my_vector = Vector(int(event_value['current_x']), int(event_value['current_y']))
    target_vector = Vector(int(event_value['x']), int(event_value['y']))
    new_x_y = move_towards_point(my_vector, target_vector, SPEED)
    if event_type == 'MOVE':
    	new_event = Event()
    	new_event.value['x'] = new_x_y.x
    	new_event.value['y'] = new_x_y.y
            
        socket.send(jsonpickle.encode(new_event))
    	

def move_towards_point(vector, target_vector, speed):
    ''' This returns the new x and y as a tuple for the my_x and my_y variable '''
    # var des:Point = *destination*;
    # var loc:Point = *currentPosition*;
    # var speed:Number = *speed in pixels per frame*

    # var vel:Point = des.subtract(loc);
    # vel.normalize( speed );
    # myObj.x += vel.x;
    # myObj.y += vel.y;
    # //repeat every frame until to the destination
    distance = target_vector - vector
    velocity = distance.normalized() * speed
    vector += velocity
    return vector

@on_connect
def my_on_connect(request, socket, context):
    manager = WebsocketManager.Instance()
    manager.add_socket(socket)
    print 'Added socket [%s] to websocket manager.' % socket.socket.session.session_id
    print manager.connections

