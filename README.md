PROJECT NAME: MY BLOG

Flask Blog on AWS Fargate with CloudFront and HTTPS

I built this project to showcases a full production ready deployment of a Python Flask application using Amazon Web Services. The goal was to build, containerize, and deploy a secure and scalable web application without managing any servers. I used Docker for containerization, Amazon ECR for image hosting, ECS Fargate for orchestration, and an Application Load Balancer for routing and security. The project also demonstrates my understanding of DevOps concepts, serverless infrastructure, and cloud deployment automation.

My main objective was to deploy a Python Flask application to a production environment quickly, securely, and with minimal operational overhead. Instead of relying on EC2 servers, I used AWS Fargate to achieve a truly serverless deployment.

When I faced the challenge of operating without traditional servers, I solved it by deploying the application on AWS ECS Fargate. This allowed the containers to run without managing any virtual machines, which saved cost and simplified maintenance.

For security and global access, I used CloudFront and HTTPS through an Application Load Balancer. This ensured that users could access the application securely from anywhere in the world.

To make the system scalable, I connected multiple Fargate tasks behind a Load Balancer. This design made the application fault-tolerant and ready to handle any level of traffic automatically.

I designed the architecture with security and scalability in mind. The user sends an HTTPS request which first reaches CloudFront. CloudFront handles SSL termination and caching for faster delivery. Traffic then flows to the Application Load Balancer, which routes requests to healthy ECS Fargate tasks running the Flask container. Logs and metrics are continuously sent to CloudWatch for monitoring. Each task runs a containerized Flask app that listens on port 8000. The entire deployment is serverless, fully managed by AWS, and integrated with CloudWatch for observability.

I began by writing a simple Flask web application with routes for registration, greeting, and a homepage. The app was configured to listen on 0.0.0.0:8000 to make it accessible from within Docker and Fargate. After building the app, I created a Dockerfile using Python 3.12-slim. I installed dependencies through the requirements file, exposed port 8000, and set the startup command to run the Flask app. Once the Docker image was tested locally, I built and tagged it, then pushed it to my private Amazon ECR repository named flask-blog.

On ECS, I created a task definition pointing to this image and configured CloudWatch logging to monitor the application. I deployed the ECS service on Fargate, ensuring that one running task was always maintained and healthy. Next, I created an Application Load Balancer to manage incoming traffic. It was linked to a target group configured to monitor container health on port 8000. The ALB handled HTTP and HTTPS traffic, routing requests securely to the ECS containers. Finally, CloudFront was used to add another security layer and global distribution.

I successfully implemented HTTPS termination at the edge using the Application Load Balancer, ensuring encrypted communication and minimizing security risks. The architecture is fully scalable and fault-tolerant, automatically handling increases in traffic without manual intervention. Logging and performance metrics are centralized in CloudWatch, providing full visibility into container health. By combining Fargate, ECR, ALB, and CloudFront, I deployed a secure and efficient serverless web application with zero EC2 management.

The development process started locally in VS Code, where the Flask app was written and tested on port 8000. The Dockerfile defined how the application was containerized using Python 3.12-slim. After confirming it ran correctly, the image was built and pushed to a private Amazon ECR repository named flask-blog. The repository and image details are visible in the ECR dashboard, confirming successful upload.

Next, I created an ECS cluster called myblog. The ECS console shows the cluster as active, with one running service managed by AWS Fargate. The service automatically launched a task, and the task overview in ECS displays the container as running successfully with the desired status of running. This verifies that the Flask container was deployed and is functioning properly on AWS.

Infrastructure provisioning was done through AWS CloudFormation. The CloudFormation console shows both the ECS service stack and cluster stack in a CREATE COMPLETE state, proving that the infrastructure was created automatically through infrastructure as code.

The Application Load Balancer configuration shows the ALB as active with a public DNS name. It is internet-facing and distributed across multiple availability zones for high availability. The listener configuration confirms that both HTTP on port 80 and HTTPS on port 443 are active and forwarding traffic to the target group. The target group page shows that the registered target identified by IP address 10.0.36.68 on port 8000 has a health status of healthy, confirming that the load balancer can successfully route traffic to the ECS container.

Each of these screenshots, from the Flask app setup to Docker, ECR, ECS, CloudFormation, ALB, and the target group, demonstrates the complete lifecycle of building, containerizing, deploying, and securing a web application in AWS.

Live Application Link:https://myblog-alb-1742662327.us-east-1.elb.amazonaws.com

This project helped me strengthen both my cloud and security foundations. I applied secure architecture principles by implementing HTTPS encryption, container isolation, and centralized monitoring. It also improved my understanding of network traffic management, access control, and application delivery at scale. The combination of Flask, Docker, and AWS services demonstrates my ability to design, secure, and automate modern cloud solutions. This aligns directly with my professional path as a Cloud and Security Analyst, capable of building secure, scalable, and efficient infrastructures in AWS.

Below are screenshots from my project showing the complete process of building, containerizing, and deploying my Flask application on AWS Fargate with HTTPS enabled.
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 10 13 43" src="https://github.com/user-attachments/assets/eb2de93c-8039-48a0-a310-d28f15b2bcd2" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 10 13 04" src="https://github.com/user-attachments/assets/196a7957-1531-4e75-9768-0ebf02bfbf9e" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 10 12 43" src="https://github.com/user-attachments/assets/7fdf9fda-efde-4e3f-b37b-36da9d5a25a2" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 10 11 18" src="https://github.com/user-attachments/assets/9b0913be-e4b0-4f6b-b9cb-af6e40a79b69" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 14 45" src="https://github.com/user-attachments/assets/9eca48a8-6508-400f-aa1c-9533e164da36" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 13 21" src="https://github.com/user-attachments/assets/1cb3e104-8585-45ab-9960-dcea75a0f146" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 11 51" src="https://github.com/user-attachments/assets/1c7ef115-5aaf-454e-91d1-fdfe1b258a69" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 10 50" src="https://github.com/user-attachments/assets/38599a3e-e570-4edf-8160-a0e5247a78eb" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 09 04" src="https://github.com/user-attachments/assets/74f2e5d8-75a5-493d-81bd-dac419ca2a63" />
<img width="1440" height="900" alt="Screenshot 2025-11-02 at 09 06 11" src="https://github.com/user-attachments/assets/6e20c688-6f15-4cec-a8a0-aa56b3a130ca" />







