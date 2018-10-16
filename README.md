ZappyBackend
## Environment setup

### 1. Prerequisites

* Python v2.7
* PyPI v9.0.1
* Virtualenv v15.1.0

### 2. Clone project


```sh
$   git clone https://github.com/SmartMedicalServices/SMS.git SMS
```
    
### 3. Create Virtualenv

```sh
$   virtualenv env
 ```

### 4. Activate Virtualenv

```sh
$ source env/bin/activate
```

### 5. Install required packages inside virtualenv

```sh
$(env)  pip install -r requirements.txt
```

### 6. Verify

```sh
$(env)  manage.py runserver
```
