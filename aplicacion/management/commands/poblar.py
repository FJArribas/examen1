# Populate Database
# This file has to be placed within the
# core/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py populate


from django.core.management.base import BaseCommand
from aplicacion.models import usuario, tweet, retweet

import datetime
import psycopg2


PSI_DB = "dbname=examen user=alumnodb password=alumnodb"


# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#
# Teachers, groups and constraints
# will be hardcoded in this file.
# Students will be read from a cvs file
# last year grade will be obtained from another cvs file
class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):
    #     parser.add_argument('model', type=str, help="""
    #     model to  update:
    #     all -> all models
    #     teacher
    #     labgroup
    #     theorygroup
    #     groupconstraints
    #     otherconstrains
    #     student (require csv file)
    #     studentgrade (require different csv file,
    #     update only existing students)
    #     pair
    #     """)
    #     parser.add_argument('studentinfo', type=str, help="""CSV file with student information
    #     header= NIE, DNI, Apellidos, Nombre, Teoría
    #     if NIE or DNI == 0 skip this entry and print a warning""")
    #     parser.add_argument('studentinfolastyear', type=str, help="""CSV file with student information
    #     header= NIE,DNI,Apellidos,Nombre,Teoría, grade lab, grade the
    #     if NIE or DNI == 0 skip this entry and print a warning""")

    # handle is another compulsory name, do not change it"
    def handle(self, *args, **kwargs):
        usuario.objects.all().delete()
        tweet.objects.all().delete()
        retweet.objects.all().delete()
                
        # Poblar la base de datos
        self.add_usuario()

        self.add_tweet()

        self.add_retweet()

    def add_usuario(self): 
        usuarios = [(1001, 'usuario_01'),
                    (1002, 'usuario_02'),
                    (1003, 'usuario_03')]

        for usu in usuarios:
            u = usuario.objects.get_or_create(id=usu[0],
                                              username=usu[1])[0]
            u.save()


    def add_tweet(self):
        tweets = [(1001, 'texto de mensaje 01', 1002, '05-01-2021'),
                  (1002, 'texto de mensaje 02', 1001, '10-01-2021'),
                  (1003, 'texto de mensaje 03', 1002, '12-01-2021'),
                  (1004, 'texto de mensaje 04', 1002, '15-01-2021')]

        for twe in tweets:
            t = tweet.objects.get_or_create(id=twe[0],
                                            texto=twe[1],
                                            usuario=usuario.objects.get(pk=twe[2]),
                                            fecha=twe[3])[0] 
            t.save()

    def add_retweet(self): 
        retweets = [(1001, 1001, 1003, '05-01-2021'),
                    (1002, 1001, 1001, '11-01-2021'),
                    (1003, 1002, 1003, '12-01-2021'),
                    (1004, 1003, 1003, '16-01-2021')]

        for ret in retweets:
            r = retweet.objects.get_or_create(id=ret[0],
                                            tweet=tweet.objects.get(pk=ret[1]),
                                            usuario=usuario.objects.get(pk=ret[2]),
                                            fechaDeRetweet=ret[3])[0] 
            r.save()
