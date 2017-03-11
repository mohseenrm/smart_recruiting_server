
sudo rm /etc/ndis/sites-enabled/default
sudo cp $PYTHONPATH/smart_recruiting_server/conf/smart_recruiting_server_nginx.conf /etc/nginx/sites-enabled/
pkill gunicorn
cd $PYTHONPATH/smart_recruiting_server/conf
echo $PWD
gunicorn -c gunicorn.py service_app:app
sudo service nginx restart


