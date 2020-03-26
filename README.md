# SmartFarmer

Against unpredictable external factors, such as rising climate change, farmers face much difficulty in efficiently managing their farms. Therefore, to increase yields and reduce waste, IoT technologies can be used to evaluate the conditions of their land and inform farmers of any discrepancies. 

In order to accomplish this, several nodes are designed to be placed around a farm in a mesh network to send data to a cloud server. Mesh networks allow all microcontrollers to share data and extend range much more significantly as they all can pass data long to each other. By having a root node act as a bridge between the mesh and the internet, cost savings can be implemented with data as cellular/mobile data only has to be integrated with one microcontroller, not several. 

The cloud server would provide analytics and feedback to users regarding the status of their farms/plants. Powered by AWS, the service provides a website that allows the usere to see the status of their farm at any time with graphs, analytics, and other useful information to maintain a healthy farm. 

## Project Details
For the website details, see the "django" directory.

For the microcontroller details, see the "esp_src" directory. 
