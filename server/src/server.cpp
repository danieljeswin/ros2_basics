#include "my_service/srv/add.hpp"
#include "rclcpp/rclcpp.hpp"
#include <iostream>
#include <memory>

class Server : public rclcpp::Node {
public:
  Server() : Node("my_server") {
    auto handle_add =
        [this](
            const std::shared_ptr<rmw_request_id_t> request_header,
            const std::shared_ptr<my_service::srv::Add::Request> request,
            std::shared_ptr<my_service::srv::Add::Response> response) -> void {
      (void)request_header;

      response->sum = request->a + request->b;
      RCLCPP_INFO(this->get_logger(), "Incoming request %f %f. Response is %f",
                  request->a, request->b, response->sum);
    };

    srv_ = this->create_service<my_service::srv::Add>("add_floats", handle_add);
  }

private:
  rclcpp::Service<my_service::srv::Add>::SharedPtr srv_;
};

int main(int argc, char *argv[]) {
  rclcpp::init(argc, argv);
  auto node = std::make_shared<Server>();
  rclcpp::spin(node);
  return 0;
}