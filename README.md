# django
Para aprendizado em django

### Ativar ambiente virtual
``` source path_to_env/bin/activate ```
## Constatntes:
* __MIDDLEWARE__ - Interceptam requisições, para autentificações <br>

### Para iniciar um projeto Django
```
django-admin startproject nome_do_projeto
```

### Para rodar o django
```
python manage.py runserver

```

### No servidor de produção, criar a pasta para arquivos staticos:
```
python manage.py collectstatic
```

### Para migração do banco de dados
```
python manage.py migrate
```

### Para Verificação de variaveis declaradas no Django
```
python manage.py shell
```
* Após instancia o local da variavél ```from django.conf import arq_da_var```
<br>

https://www.geeksforgeeks.org/datetimefield-django-models/

<br>
Verifica log
```sudo tail -f /var/log/apache2/access.log```
