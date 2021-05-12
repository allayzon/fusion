import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):  # Função para mudar os nomes dos arquivos de imagem
    ext = filename.split('.')[-1]  # Pega o nome, separa a partir do ponto (pra pegar a extensão)
    filename = f'{uuid.uuid4()}.{ext}'  # Estamos reescrevendo o nome do arquivo com uuid e reconectando à extensão
    return filename


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)  # auto_now_add é quando o objt for criado, ele adiciona
    # a data automaticamente
    modificado = models.DateField('Modificado', auto_now=True)  # auto_now é ativado sempre que o objt é modif.
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Adicionais(Base):
    ICONE_CHOICES2 = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Laptop'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Layers'),
        ('lni-leaf', 'Folha2'),
    )
    nome = models.CharField('Adicional', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=16, choices=ICONE_CHOICES2)

    class Meta:
        verbose_name = 'Adicional'
        verbose_name_plural = 'Adicionais'

    def __str__(self):
        return self.nome


class Servico(Base):
    ICONE_CHOICES = (  # Estamos iniciando uma tupla com o chamamento dos ícones css
        ('lni-cog', 'Engrenagem'),  # Esses são os nomes dos ícones no css
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES)  # choices vai criar uma
    # caixa de escolha com os elementos da tupla

    class Meta:  # Área administrativa
        verbose_name = 'Serviço'  # Nome de apresentação naquela tabela de adm
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):  # Será chave estrangeira de Equipe
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Equipe(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    # cargo é uma chave estrangeira (class Cargo da aplicação Core), o on_delete é para remoção em cascata, ou seja
    # se o cargo for removido da empresa, todos que o tem, o perderão
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'cropy': True}})
    # Estamos passando o arquivo de imagem para receber o tratamento da função get_file_path que criamos
    # Variations serve para qualquer img fora do padrão, será redimencionada nas dimenções passadas, se precisar cortar
    # 'cropy', corta.
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionários'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome