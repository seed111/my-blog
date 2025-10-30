PROJECT NAME: MY BLOG 

Flask Blog on AWS Fargate with CloudFront HTTPS
This project documents the complete, production ready deployment of a Python Flask application onto a secure, scalable, and fully serverless infrastructure using Amazon Web Services AWS. I successfully integrated containerization, orchestration, global networking, and security principles.

Project Goal and Solution Summary
My primary objective was to deploy the Flask application to a production environment quickly and securely, without relying on traditional servers.

| Challenge Faced           | Solution I Built                                                                 | Key Value Delivered                                                   |
|---------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Serverless Operations     | I achieved zero server maintenance by deploying the application using AWS ECS Fargate. | I avoided the time and cost of managing underlying EC2 virtual servers. |
| Security and Global Access| I used CloudFront for SSL termination and as a global CDN.                     | I ensured worldwide HTTPS access and security at the network edge.   |
| Scalability               | I built a fault tolerant system using an Application Load Balancer ALB across multiple Fargate tasks. | I delivered automatic scaling and high availability for variable user traffic. |



Core Architecture and Request Flow
I designed this architecture prioritizing security at the edge and cost efficiency through serverless compute.

+----------------+
|    User / Internet |
+-------+--------+
        |
      HTTPS Request
        v
+-----------------------+
|   AWS CloudFront CDN  |
| I configured it for SSL Termination |
| I enabled Performance Caching |
+-----------+-----------+
            |
            | Origin Fetch
            v
+-----------------------+
|   Application Load Balancer   |
| I configured Health Checks and Routing |
+-----------+-----------+
            |
            | Route to Port 8000
            v
+--------------------------------+
|       AWS ECS Fargate        |
| I deployed the Serverless Container Cluster |
+-----------------+--------------+
| Task 1 | Task N | Scalable, Auto healing
| +-------------+ |
| | Flask App| |
| | Listens on 8000 |
| +-------------+ |
+--------+--------+--------------+
         |
+--------+--------+
|   AWS CloudWatch  |
| I enabled Logging and Metrics |
+-----------------+


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
