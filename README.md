# Medida-experimental

## Forma de uso:
```python
from valorexp import ValorExp


valor1 = ValorExp(10, 0.1)  # cria um objeto com valor 10 e incerteza 0.1
valor2 = ValorExp(20, 0.001)  # cria um objeto com valor 20 e incerteza 0.001
valor3 = 100  # constante

"""A partir daqui qualquer operação entre as variáveis valor1, valor2 e valor3
propagará a incerteza nas operações. Note que valor3 é uma constante, portanto
qualquer valor número pode ser utilizado, mesmo sem a criaçãod e uma variável.
"""
```
