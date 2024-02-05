push:
	git commit -a
	git push

build:
	mongod --port 41231 --dbpath db/ &

test:
	python3 load-json.py 10.json 41231
	python3 main.py 41231

test100:
	python3 load-json.py ../farmers-protest-tweets-2021-03-5.json 41231
	python3 main.py 41231