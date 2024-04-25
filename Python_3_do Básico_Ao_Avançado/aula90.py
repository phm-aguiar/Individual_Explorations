# generator expression, iteradores, iteráveis
import sys

iterable = ['Spring', 'Summer', 'Fall', 'Winter'];
iterator = iter(iterable);
lista = [n for n in range(10000)];
generator =(n for n in range(10000));

print(sys.getsizeof(lista));
print(sys.getsizeof((generator))); 
