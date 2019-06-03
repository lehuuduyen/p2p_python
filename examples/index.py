from TcpServerNode import Node
import time
from argparse import ArgumentParser
node = None # global variable
parser = ArgumentParser()
parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
args = parser.parse_args()
port = args.port



def callback_node_event(event, node, other, data):
   print("Event Node 1 (" + node.id + "): %s: %s" % (event, data))
   node.send_to_nodes({"thank": "you"})



print(port)

node = Node('localhost', port, callback_node_event)

node.start()

node.connect_with_node('localhost', port +10)

#node.terminate_flag.set() # Stopping the thread

node.send_to_nodes({"type": "message", "message": "test"})

while True:
   time.sleep(1)

node.stop()