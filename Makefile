include .env
export $(shell sed 's/=.*//' .env)

sh-%:
	docker-compose exec $* bash

down:
	docker-compose down --volumes

# use run if you want to override the up command
up-%:
	docker-compose up $*

image-dev: 
	docker-compose down --volumes --rmi all
	docker-compose up

dev:
	docker-compose down --volumes	
	docker-compose up

psql:
	@echo ${DB_NAME}
	docker-compose exec db bash -c "clear && psql --username postgres --dbname ${DB_NAME} -P linestyle=unicode \
		-P border=2 \
		-P null=¤ \
		-P expanded=auto \
		-P footer=on \
		-v COMP_KEYWORD_CASE=upper \
		-v PROMPT1='%[%033[33;1m%]%x%[%033[0m%]%[%033[1m%]%n%[%033[0m%]%R%# ' \
		"
