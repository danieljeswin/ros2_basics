import rclpy
from rclpy.node import Node
from my_service.srv import Add
import random

class Client(Node):
    def __init__(self):
        super().__init__('client')
        self.client = self.create_client(Add, 'add_floats')
        self.request = Add.Request()
        while not self.client.wait_for_service(timeout_sec = 10.0):
            self.get_logger().info('Waiting for service')

    def send_request(self):
        self.request.a = random.uniform(2043, 343294)
        self.request.b = random.uniform(3234, 45849054)
        wait = self.client.call_async(self.request)

        rclpy.spin_until_future_complete(self, wait)
        if wait.result() is not None:
            self.get_logger().info("Request was '%f' '%f'. Response is '%f'" %(self.request.a, self.request.b, wait.result().sum))
        else:
            self.get_logger().info("Request failed")

def main(args = None):
    rclpy.init(args = args)
    node = Client()
    while rclpy.ok():
        node.send_request()
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()