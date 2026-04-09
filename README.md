# AWS-satelliteImg-Processing-pipeline
A scalable AWS-based , event-driven image processing system that processes uploaded images using s3 triggers, Lambda functions and EC2 and displays results through a real-time dashboard.
# Architecure Diagram / Workflow

[aws_pipeline_flowchart.html](https://github.com/user-attachments/files/26589826/aws_pipeline_flowchart.html)

# AWS Services Used-
1. AWS Lambda
2. Amazon S3
3. Amazon EC2
4. Amazon DynamoDB
5. Amazon API Gateway

# Key Features

### 1.Direct Image Upload via Pre-signed URLs
Images are uploaded directly from the frontend to Amazon S3 using pre-signed URLs, eliminating backend load and improving scalability.

### 2. Event-Driven Processing Pipeline
The system automatically triggers processing as soon as an image is uploaded to S3, enabling a fully automated and asynchronous workflow.

### 3. Automated EC2 Lifecycle Management
An Amazon EC2 instance is dynamically started for image processing and stopped after completion, optimizing cost and resource utilization.

### 4. Real-Time Dashboard for Processed Images
Users can view processed images instantly through a dashboard powered by backend APIs, ensuring a seamless user experience.

### 5. Metadata Storage and Retrieval
Image metadata (such as processed image URLs and timestamps) is stored in Amazon DynamoDB for fast and efficient access.

# UI screenshots
<img width="1884" height="725" alt="Image" src="https://github.com/user-attachments/assets/934c7fb9-ffdc-4026-bbd4-56893364004a" />

# Setup Instructions
# Key Learnings

### 1.Understanding Event-Driven Architecture
Learned how to design a system where actions are automatically triggered (S3 upload → Lambda → EC2), reducing manual intervention and enabling asynchronous workflows.

### 2.Working with Pre-signed URLs for Efficient Uploads
Understood how to upload files directly to Amazon S3 without routing them through the backend, improving performance and scalability.

### 3.Integrating Multiple AWS Services
Gained hands-on experience connecting AWS Lambda, Amazon API Gateway, Amazon EC2, and Amazon DynamoDB into a complete working pipeline.

### 4.Managing Compute Resources Efficiently
Learned how to start and stop EC2 instances dynamically based on workload, helping optimize cloud costs and avoid unnecessary resource usage.

### 5.Handling Data Storage and Retrieval
Understood how to store and fetch metadata from DynamoDB, and realized the limitations of scan() vs query() for ordered and efficient data retrieval.

### 6.Debugging Real-World Cloud Issues
Faced and resolved issues related to IAM permissions, service integration, and event triggers, improving problem-solving and debugging skills in a cloud environment.

# Challenges Faced

### 1.Multiple Lambda Triggers (Duplicate Processing)

Problem:
A single image upload triggered multiple Lambda executions, resulting in duplicate processed images.

Cause:
S3 event notifications were configured without filters, causing triggers for both input and processed files.

Fix:
Added a prefix filter (input/) to ensure Lambda is triggered only for new uploads.

### 2.EC2 Instance Shutting Down During Debugging
 
Problem:
The EC2 instance shut down immediately after execution, preventing debugging.

Cause:
A shutdown command was included in the SSM execution script.

Fix:
Temporarily removed the shutdown command to allow debugging and log inspection.

### 3.SSM Connectivity Issues
   
Problem:
Unable to connect to the EC2 instance using AWS Systems Manager (SSM).

Cause:
Missing or incorrectly configured IAM role and/or SSM agent issues.

Fix:
Attached the appropriate IAM role and ensured the SSM agent was installed and running.


### 4.Permission Errors in EC2
   
Problem:
Encountered permission denied errors while accessing directories on EC2.

Cause:
Commands were executed under a user with insufficient permissions.

Fix:
Switched to the correct user context with appropriate privileges.

### 5.AWS Region Configuration Error
 
Problem:
AWS SDK operations failed with region-related errors.

Cause:
Region was not specified in boto3 client/resource initialization.

Fix:
Explicitly defined the AWS region in all boto3 configurations.

### 6.Missing Dependencies in EC2 Environment
    
Problem:
Image processing script failed due to missing libraries.

Cause:
Required Python packages (e.g., OpenCV, NumPy) were not installed on the EC2 instance.

Fix:
Installed necessary dependencies using pip.

### 7.DynamoDB Not Updating
    
Problem:
No records were stored in DynamoDB despite successful execution.

Cause:
Incorrect table name and lack of proper execution verification.

Fix:
Corrected the table reference and ensured the pipeline was triggered correctly.

### 8.Overwriting of Processed Images
    
Problem:
Processed images were overwritten instead of being stored uniquely.

Cause:
Static output file naming.

Fix:
Generated unique filenames using timestamps.

### 9.CORS Configuration Issues

Problem:
Frontend requests to API Gateway and S3 were blocked due to CORS errors.

Cause:
Missing or incomplete CORS configuration across services.

Fix:
Configured CORS properly in:
API Gateway (allowed origin and methods)
Lambda responses (added headers)
S3 bucket (defined CORS policy)

# Future Improvements and scope
This project was my first implementation involving multiple AWS services in an end-to-end pipeline. The primary focus was on understanding cloud architecture, service integration, and building an event-driven workflow. As a result, less emphasis was placed on frontend design and advanced image processing.
Currently, the image processing step is limited to a basic grayscale and threshold (black-and-white) transformation. However, this can be significantly enhanced in future iterations
