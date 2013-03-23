# -*- coding: utf-8 -*-
import os
from elixir import *
from datetime import date

# Diretório onde o arquivo do banco será armazenado e caminho do arquivo
dbdir = os.path.join(os.path.expanduser("~"), ".frequenza")
dbfile = os.path.join(dbdir, "frequenza.sqlite")

class Aluno(Entity):
    """Classe que representa um aluno na aplicação"""
    
    using_options(tablename='alunos')
    
    nome = Field(Unicode, required=True)
    matricula = Field(Unicode, primary_key=True)
    rfid_card = Field(Unicode, unique=True)
    turmas = ManyToMany('Turma')
    aluno_aula = OneToMany('AlunoAula')
    
    def __repr__(self):
        return u'%s - %s' %(unicode(self.matricula), unicode(self.nome))

class Turma(Entity):
    """Classe que representa uma turma na aplicação"""
    
    using_options(tablename='turmas')
    
    disciplina = Field(Unicode, required=True)
    ano = Field(Integer, required=True)
    semestre = Field(Integer, required=True)
    alunos = ManyToMany('Aluno')
    aulas = OneToMany('Aula')
    def __repr__(self):
        return u'%s - %d.%d' %(self.disciplina, self.ano, self.semestre)
    
class AlunoAula(Entity):
    """Classe que representa a relação entre um aluno e uma aula, necessário
    para saber a frequência do aluno
    """
    using_options(tablename='aluno_aulas')
    
    aluno = ManyToOne('Aluno')
    aula = ManyToOne('Aula')
    presente = Field(Boolean, default=False, required=True)
    
    def __repr__(self):
        return u"Aluno: %s - Aula: %s - Frequência: %s" %(unicode(self.aluno),
                unicode(self.aula), unicode(self.presente))

class Aula(Entity):
    """Classe que representa uma Aula na aplicação
    """
    using_options(tablename='aulas')
    
    conteudo = Field(Unicode, required=False)
    data = Field(Date)
    turma = ManyToOne('Turma')
    aluno_aula = OneToMany('AlunoAula')
 
    def __repr__(self):
        return u"Turma: %s - %s - %s"%(unicode(self.turma),
                                       unicode(self.conteudo),
                                       self.data.strftime("%d/%m/%y"))

saveData=None
rollBack=None

def initDB():
    
    if not os.path.isdir(dbdir):
        os.mkdir(dbdir)
    
    metadata.bind = "sqlite:///%s"%dbfile
    #metadata.bind.echo = True
    setup_all()
    
    if not os.path.exists(dbfile):
        create_all()
        
    global saveData
    saveData = session.commit
    
    global rollBack
    rollBack = session.rollback

def main():
    initDB()
    
    fulano = Aluno(nome=u"Fulano", matricula=u"1", rfid_card=u"1")
    ciclano = Aluno(nome=u"Ciclano", matricula=u"2", rfid_card=u"2")
    beltrano = Aluno(nome=u"Beltrano", matricula=u"3", rfid_card=u"3")
    
    
    turmaA = Turma(
                    disciplina=u"Disciplina A", ano=2012, semestre=1, alunos=[
                    fulano, ciclano]
                   )
    turmaB = Turma(disciplina=u"Disciplina B", ano=2011, semestre=2, alunos=[
                    fulano, ciclano]
                   )
    saveData()
    
    turmaC = Turma(disciplina=u"Disciplina C", ano=2011, semestre=2, alunos=[
                    ciclano, beltrano]
                   )
    turmaB.delete()
    
    aula1 = Aula(conteudo=u"Essa é a aula 1", data=date.today(), turma=turmaA)
    aula2 = Aula(conteudo=u"Essa é a aula 2", data=date.today(), turma=turmaC)
    
    
    saveData()
    
    print 'Alunos da Turma A:'
    print turmaA.alunos
    print
    print 'Alunos da Turma B'
    print turmaB.alunos
    print
    print 'Alunos da Turma C'
    print turmaC.alunos
    print

if __name__=='__main__':
    main()
        
    
        
    