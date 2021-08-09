all:
		gunicorn 'app:create_app()' -c app/gunicorn.py

clean:
	ps -eo pid,command | grep gunicorn.py | grep python | cut -d " " -f1


.PHONY: clean
