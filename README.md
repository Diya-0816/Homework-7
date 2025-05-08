# QR Code Generator (Dockerized)

This project generates a QR code linking to your GitHub homepage using Python and Docker.

## How to Run

### 1. Clone this repository:
```bash
git clone https://github.com/user/qr-code-docker.git
cd qr-code-docker
```

### 2. Build Docker Image:
```bash
docker build -t qr-code-generator .
```

### 3. Run Docker Container:
```bash
docker run --rm -v $(pwd):/app qr-code-generator
```

### Output:
The file `github_qr_code.png` will be created in your current directory.

## Sample QR Code
![QR Code](github_qr_code.png)
