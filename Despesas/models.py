from django.db import models

class Despesas_Ana(models.Model):
    data_criacao = models.DateField()
    descrição=models.CharField(max_length=89)
    vencimento = models.DateField()
    quitado = models.CharField(max_length=50)

    teste = (('Remédio','Remédio'),( 'Roupas','Roupas'),('Alimentação','Alimentação'),( 'educação','educação'),('Transporte','Transporte'),('Outros','Outros'))
    Tipo_Despesa=models.CharField(max_length=200,choices=teste,default="Remedío")

    teste1=(('Dinheiro','Dinheiro'),('Cartão de Crédito', 'Cartão de Crédito'),('Cartão de Débito', 'Cartão de Débito'),('Cartão Crediário', 'Cartão Crediário'),('Cheque', 'Cheque'))
    Forma_Pagamento=models.CharField(max_length=200,choices=teste1,default="Dinheiro")


