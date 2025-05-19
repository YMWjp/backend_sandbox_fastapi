.PHONY: build run stop clean

# setup image name and container name
IMAGE_NAME = fastapi-backend
CONTAINER_NAME = fastapi-container

# port number
PORT = 80

# build an image
build:
	docker build -t $(IMAGE_NAME) .

# run a container
run:
	docker run -d --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

# delete a container and stop it
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# delete a image
clean:
	docker rmi $(IMAGE_NAME) || true

# restart a container (stop + run)
restart: stop run

# show logs of a container
logs:
	docker logs -f $(CONTAINER_NAME)

# check the status of a container
status:
	docker ps -a | grep $(CONTAINER_NAME) 