import rclpy
from rclpy.node import Node
from my_msgs.msg import Add

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscriber_ = self.create_subscription(Add, "numbers", self.add_callback)

    def add_callback(self, msg):
        sum = msg.a + msg.b
        self.get_logger().info("'%f' + '%f' = '%f'" %(msg.a, msg.b, sum))

def main(args = None):
    rclpy.init(args = args)
    node = Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()