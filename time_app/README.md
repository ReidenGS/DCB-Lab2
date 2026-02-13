# Lab 2 – Application Layer Protocols & Web Applications

**Student:** (Your Name)
**Course/Section:** (Course Name / Section)
**Semester:** (e.g., Spring 2026)

---

## Repository Overview

This repository contains my solutions for **Lab 2**.
For **Problem 2**, I implemented and deployed a simple Flask application that returns the current time at the `/time` endpoint. The final application is located in the **`time_app/`** folder as required.

---

## Problem 2 – Time Application (Required Folder: `time_app/`)

### Requirements (from the lab)

* Implement a Flask endpoint: **`GET /time`** → returns the current server time
* Containerize the application with Docker
* Push the image to Docker Hub
* Deploy to Kubernetes (Minikube) and expose it using a **NodePort** service
* Verify the endpoint works via **`http://<IP>:<NodePort>/time`**
* Commit the application code under **`time_app/`** including the **Dockerfile** and all files needed to build the image

### Folder Structure

```
time_app/
  Dockerfile
  requirements.txt
  run.py
  (other required files...)
```

### Endpoint

* **URL:** `/time`
* **Method:** `GET`
* **Response:** JSON with current UTC time

Example:

```json
{"time":"2026-02-13 22:31:46 UTC"}
```

---

## Build and Run Locally (Docker)

From the repository root:

```bash
cd time_app
docker build -t jackiewen02/sample-time-app:latest .
docker rm -f sample-time-app 2>/dev/null
docker run --name sample-time-app -p 8080:8080 -it jackiewen02/sample-time-app:latest
```

Verify:

```bash
curl http://localhost:8080/time
```

---

## Push Image to Docker Hub

```bash
docker login
docker push jackiewen02/sample-time-app:latest
```

**Docker Hub image:** `docker.io/jackiewen02/sample-time-app:latest`

---

## Deploy to Kubernetes (Minikube)

### 1) Start Minikube

```bash
minikube start
kubectl get nodes
```

### 2) Create a Deployment

```bash
kubectl create deployment sample-time-app --image=docker.io/jackiewen02/sample-time-app:latest
kubectl get pods
```

### 3) Expose as a NodePort Service

```bash
kubectl expose deployment sample-time-app --type=NodePort --port 8080 --target-port 8080
kubectl get services
```

In the `PORT(S)` column you will see something like:

* `8080:32687/TCP`

Here, **32687** is the NodePort.

### 4) Verify Access

Option A (recommended):

```bash
minikube service sample-time-app --url
curl <MINIKUBE_SERVICE_URL>/time
```

Option B (manual):

```bash
MINIKUBE_IP=$(minikube ip)
curl http://$MINIKUBE_IP:<NODEPORT>/time
```

---

## Submission Notes

* The required application code is located in **`time_app/`**.
* The Docker image used for Kubernetes deployment is **`jackiewen02/sample-time-app:latest`**.
* Screenshots (for the lab report) should include:

  1. Local `/time` test (localhost)
  2. Docker build success
  3. Docker Hub push and/or repo tag page
  4. `kubectl get pods` showing Running
  5. `kubectl get services` showing NodePort
  6. Successful `/time` response via Minikube IP/NodePort (or Minikube service URL)

---
