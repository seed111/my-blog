PROJECT NAME: MY BLOG 

Flask Blog on AWS Fargate with CloudFront HTTPS
This project documents the complete, production ready deployment of a Python Flask application onto a secure, scalable, and fully serverless infrastructure using Amazon Web Services AWS. I successfully integrated containerization, orchestration, global networking, and security principles.

Project Goal and Solution Summary
My primary objective was to deploy the Flask application to a production environment quickly and securely, without relying on traditional servers.

Challenge Faced: Serverless Operations
Solution: I deployed the application using AWS ECS Fargate so no server maintenance was needed.
Key Value: I saved time and avoided the cost of managing EC2 servers.

Challenge Faced: Security and Global Access
Solution: I used CloudFront for SSL termination and as a global CDN.
Key Value: I made the application accessible worldwide with HTTPS and kept it secure at the network edge.

Challenge Faced: Scalability
Solution: I built a fault-tolerant system using an Application Load Balancer across multiple Fargate tasks.
Key Value: I enabled automatic scaling and high availability to handle changing user traffic.



Core Architecture and Request Flow
I designed this architecture prioritizing security at the edge and cost efficiency through serverless compute.

| Component               | Description                    | Details                                  |
|-------------------------|--------------------------------|------------------------------------------|
| User Internet           | HTTPS Request                  |                                          |
| AWS CloudFront CDN      | CDN for distribution           | SSL Termination, Performance Caching     |
| Application Load Balancer | Routes traffic and checks health | Health Checks, Routing               |
| AWS ECS Fargate         | Serverless container cluster   | Scalable and auto healing                |
| Tasks 1 to N            | Individual container tasks     | Flask App listening on port 8000         |
| AWS CloudWatch          | Monitoring and logging         | Logging, Metrics                         |


Implementation Workflow What I Did

1. Application Containerization Docker and ECR
I updated the Python Flask application to listen on 0.0.0.0:8000 to ensure it was reachable within the container network. I created a lean Dockerfile, built the image, tagged it, and pushed it to a dedicated Amazon ECR repository my blog.

2. Serverless Deployment on ECS Fargate
I created an ECS Task Definition pointing to my ECR image. I also configured the task to send its logs directly to CloudWatch Logs. I deployed an ECS Service to manage the container lifecycle, ensuring that the desired number of application tasks are always running and healthy.

3. Load Balancing and Routing ALB
I set up an Application Load Balancer ALB as the front door for internal traffic. I configured a Target Group to check the health of my Fargate tasks and forward ALB traffic to the containers on port 8000. I attached the ECS Service to this ALB.

4. Global Security and Performance CloudFront
I created a CloudFront Distribution, setting the ALB's DNS name as the origin source. This was a critical security step: I configured the Viewer Protocol Policy to Redirect HTTP to HTTPS. This immediately secures all user connections using the CloudFront SSL certificate, maximizing performance via the global CDN edge network.

Key Achievements I Delivered

I successfully implemented HTTPS termination at the edge CloudFront, significantly minimizing the attack surface. I built an architecture ready for auto scaling through ECS Fargate and ALB, which can handle unexpected spikes in user traffic seamlessly. I established robust CloudWatch logging and metrics for continuous monitoring of container health and performance. I leveraged serverless services Fargate, CloudFront to achieve high availability while eliminating the operational burden and fixed cost of managing EC2 infrastructure.


