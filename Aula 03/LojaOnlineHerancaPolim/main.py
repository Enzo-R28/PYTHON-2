from classe import * 
#Criando instâncias dos itens
teclado = ProdutoFisico('Teclado Mecanico', 150.00, 0.8, '30x15x5 cm')
python_book = LivroDigital('Python Fluente', 80.00, 'PDF')
web_course = CursoOnline('Desenvolvimento Web Completo', 400.00, 30)
data_course = CursoOnline('Análise dos Dados com Python', 250.00, 15)

# Demonstrando herança e polimorfismo
intens = [teclado, python_book, web_course, data_course]

for item in intens:
    item.exibir_detalhes()
    preco_final = item.calcular_preco_final() # polimorfismo em ação
    print(f'Preço final: R$ {preco_final:.2f}')
    print('-' * 30)