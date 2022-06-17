from blog.models import Article
#injection des donnees aleatoires 
def run():
    for i in range(7,22):
        article = Article()
        article.title ="Article  N° %d" %i
        article.description ="Le lorem ipsum est, en imprimerie, une suite de mots sans signification utilisée à titre provisoire pour calibrer une mise en page. N°%d " %i
        article.image = "http://default" 
        article.save()
    
    print("opération reussie!")

#terminal :python3 manage.py runscript import_data