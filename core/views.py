from audioop import reverse
from django.shortcuts import redirect, render
from .models import Membro



# logica que pega os dados do formulario 
def home(request):
    nome      = request.POST.get('nome',      None)
    data      = request.POST.get('data',      None)
    curso     = request.POST.get('curso',     None)
    matricula = request.POST.get('matricula', None)
    email     = request.POST.get('email',     None)
    entrada   = request.POST.get('entrada',   None)
    saida     = request.POST.get('saida',     None)
    pontos    = request.POST.get('pontos',    None)
    cargo     = request.POST.get('cargo',     None)
    info      = request.POST.get('geral',     None)
    foto      = request.POST.get('foto',      None)

    
    # pega os valores das variáveis e cadastra no banco de dados
    if request.method == "POST":
        Membro.objects.create(nome=nome, data=data, curso=curso, matricula=matricula, email=email, entrada=entrada, saida=saida, pontos=pontos, cargo=cargo, info=info, foto=foto)
        return render(request, 'home.html')
    else:
        return render(request, 'home.html')


 



# botao que leva para area administrativa
def capitania(request):
    return redirect(reverse('capitania'))

    
     