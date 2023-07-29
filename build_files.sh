
python manage.py loaddata ./products/fixtures/category.json
python manage.py loaddata ./products/fixtures/sub_category.json
python manage.py loaddata ./products/fixtures/article.json
python manage.py loaddata ./products/fixtures/gender.json
python manage.py loaddata ./products/fixtures/products.json
pip install Werkzeug==1.0.1
pip install --disable-pip-version-check --target . werkzeug==1.0.1
pip install -r requirements.txt
python manage.py collecstatic 0