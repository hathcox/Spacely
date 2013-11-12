from spacely.libs.Singleton import Singleton

@Singleton
class WebsocketManager(object):
	''' This is the Manager of websocket connections that we get '''

	def __init__(self):
		self.connections = {}
		pass

	def add_socket(self, socket):
		''' Add the socket into the manager '''
		if socket != None:
			self.connections[str(socket.socket.session.session_id)] = socket

	def get_socket(self, session_id):
		''' Attempt to find a socket from the manager map'''
		if session_id != None:
			return self.connections[str(session_id)]