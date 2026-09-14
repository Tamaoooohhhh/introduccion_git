horas = float(input("Ingrese las horas que ha trabajado: "))
valor_de_hora = float(input("Ingrese el valor pagado por cada hora trabajada: "))

salario_bruto = horas * valor_de_hora
descuento = salario_bruto * 0.08
salario_neto = salario_bruto - (salario_bruto * 0.08)

print(f"""Salario bruto: {salario_bruto}
Valor descontado: {descuento}
Salario neto: {salario_neto}
""")

