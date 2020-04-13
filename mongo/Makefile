all:
	git rev-parse HEAD > commit

dev:
	docker stop mongo-dev || echo "mongo-dev container not stopped"
	docker rm mongo-dev || echo "mongo-dev container not removed"
	docker run -d \
		--name mongo-dev \
		-p 27017:27017 \
		-v ~/data/db-dev:/data/db \
		mongo

dev-rep:
	docker stop mongo-dev-rep || echo "mongo-dev-rep container not stopped"
	docker rm mongo-dev-rep || echo "mongo-dev-rep container not removed"
	docker run -d \
		--name mongo-dev-rep \
		-p 27018:27017 \
		-v ~/data/db-dev-rep:/data/db \
		mongo

prod:
	docker stop mongo-prod || echo "mongo-prod container not stopped"
	docker rm mongo-prod || echo "mongo-prod container not removed"
	docker run --restart unless-stopped -d \
		--name mongo-prod \
		-p 27017:27017 \
		-v ~/data:/data/db \
		mongo

clean:
	docker stop mongo-dev || echo "stop mongo-dev container not stopped"
	docker rm mongo-dev || echo "stop mongo-dev container not removed"
	docker stop mongo-prod || echo "stop mongo-prod container not stopped"
	docker rm mongo-prod || echo "stop mongo-prod container not removed"
	docker rmi mongo

