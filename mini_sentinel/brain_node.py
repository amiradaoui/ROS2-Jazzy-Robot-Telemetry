import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker

class TelemetryNode(Node):
    def __init__(self):
        super().__init__('telemetry_node')
        self.publisher = self.create_publisher(Marker, '/robot_status', 10)
        self.timer = self.create_timer(0.5, self.publish_marker)

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = "base_link" # مهم جداً!
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position.z = 0.5  # ستظهر فوق المكعب بنصف متر
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0 # لون أحمر
        self.publisher.publish(marker)

def main():
    rclpy.init()
    node = TelemetryNode()
    rclpy.spin(node)
    rclpy.shutdown()
