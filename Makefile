docker-build: 
	docker build --rm --no-cache -t family-tree-api:1.0 .

docker-run:
	docker run -it --rm -p 5000:5000 family-tree-api:1.0