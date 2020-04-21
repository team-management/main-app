all:
	git rev-parse HEAD > commit
	docker build --tag pre -t rugby-dev .
	docker build --tag pre2 -t rugby-dev2 .
	docker build --tag prod -t rugby-prod .


dev:
	docker stop rugby-dev || echo "rugby-dev container not stopped"
	docker rm rugby-dev || echo "rugby-dev container not removed"
	docker run -it --rm \
	    -p 5000:5000 \
	    -v ${PWD}/app:/usr/src/app \
	    --name rugby-dev \
	    --link mongo-dev:mongo \
	    rugby-dev


dev2:
	docker stop rugby-dev2 || echo "rugby-dev2 container not stopped"
	docker rm rugby-dev2 || echo "rugby-dev2 container not removed"
	docker run -it --rm \
		-p 5000:5000 \
	    -v ${PWD}/app:/usr/src/app \
	    --name rugby-dev2 \
	    rugby-dev2


prod:
	docker stop rugby-prod || echo "rugby-prod container not stopped"
	docker rm rugby-prod || echo "rugby-prod container not removed"
	docker run --restart unless-stopped -d \
	    -p 5000:5000 \
	    --name rugby-prod \
	    --link mongo-prod:mongo \
	    rugby-prod/api

clean:
	docker stop rugby-prod || echo "stop back container not stopped"
	docker rm rugby-prod || echo "stop back container not removed"
	docker rmi rugby-prod

