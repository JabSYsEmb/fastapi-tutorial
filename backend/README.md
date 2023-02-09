# Backend

```shell
$ python -m venv name_for_the_virtual_environment
$ source {name_for_the_virtual_environment}/bin/activate # source the binaries of the virtual environment
$ pip install -r requirement.txt
$ ./runner.sh (you can send parameters here)
```

``` bash
# contents of runner.sh
uvicorn main:app --reload "$@"
# $@ : look for https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
```
