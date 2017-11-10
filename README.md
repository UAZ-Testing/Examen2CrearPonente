# Examen 2 de Testing

Alta de ponentes

## Instrucciones:

### Para el proyecto de Django:

**Clonar el proyecto:**
```
git clone http://148.217.200.108:89/porfirioads/Examen2CrearPonente.git
```

**Crear virtualenv:**
```
cd Examen2CrearPonente
sudo apt-get install virtualenv 
virtualenv --python=/usr/bin/python3.5 venv
source venv/bin/activate
```

**Instalar requerimientos:**
```
pip install requirements_p3.txt
```

**Ejecutar pruebas unitarias:**
```
python manage.py test
```

### Para lettuce:
**Instalar requerimientos con pip2:**
```
pip2 install requirements_p2.txt
```

**Ejecutar pruebas funcionales:**
```
lettuce bdd/tests
```