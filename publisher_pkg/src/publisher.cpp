#include <iostream>
#include <memory>

#include "my_msgs/msg/add.hpp"
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;

class MyPublisher : public rclcpp::Node {
public:
  MyPublisher() : Node("my_publisher") {
    publisher_ = this->create_publisher<my_msgs::msg::Add>("numbers");

    auto publishMsg = [this]() -> void {
      auto msg = std::make_shared<my_msgs::msg::Add>();
      msg->a = std::rand();
      msg->b = std::rand();

      RCLCPP_INFO(this->get_logger(), "Publishing: '%f' '%f' ", msg->a, msg->b);
      publisher_->publish(msg);
    };

    timer_ = this->create_wall_timer(1s, publishMsg);
  }

private:
  rclcpp::Publisher<my_msgs::msg::Add>::SharedPtr publisher_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  auto publisher_node = std::make_shared<MyPublisher>();
  rclcpp::spin(publisher_node);
  return 0;
}