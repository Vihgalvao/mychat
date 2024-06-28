from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
import traceback
import os

# Create your views here.

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')


def espera(request):
    # Lógica para recuperar informações do usuário, como nome e tempo de espera, se necessário
    nome_usuario = request.GET.get('name', 'Teste')   # Exemplo de nome de usuário

    # Renderiza a página de espera, passando dados opcionais para o template
    return render(request, r'E:\mychat\mychat\base\templates\base\espera.html', {'nome_usuario': nome_usuario})

def getToken(request):
    appId = "b8da20f1fcaa45b097f6ff1573dea136"
    appCertificate = "a809a63ba7954ac89babbd08ba2f9b64"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)

@csrf_exempt
def salvar_no_json(request):
    if request.method == 'POST':
        try:
            # Decodifica o JSON do corpo da requisição
            dados = json.loads(request.body)

            # Caminho do arquivo JSON
            caminho_arquivo = r'E:\mychat\mychat\base\Requests\history.json'

            if os.path.exists(caminho_arquivo):
                with open(caminho_arquivo, 'r+') as arquivo:
                    # Carrega o conteúdo existente do arquivo JSON
                    try:
                        conteudo = json.load(arquivo)
                    except json.decoder.JSONDecodeError:
                        conteudo = []
                    
                    # Adiciona os novos dados à lista existente
                    conteudo.append(dados)

                    # Retorna o cursor para o início do arquivo
                    arquivo.seek(0)

                    # Escreve a lista JSON de volta no arquivo
                    json.dump(conteudo, arquivo, indent=4)
            else:
                # Se o arquivo não existir, cria um novo e escreve os dados
                with open(caminho_arquivo, 'w') as arquivo:
                    json.dump([dados], arquivo, indent=4)

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=500)

    else:
        return JsonResponse({'status': 'error'}, status=400)
    

def listar_pessoas_em_espera(request):
    # Caminho para o arquivo JSON
    caminho_arquivo = r'E:\mychat\mychat\base\Requests\history.json'

    # Abra o arquivo JSON e carregue os dados
    with open(caminho_arquivo, 'r') as arquivo:
        dados_json = json.load(arquivo)

    # Lista para armazenar as informações de pessoas em espera
    pessoas_em_espera = []

    # Iterar sobre cada item no JSON
    for item in dados_json:
        # Extrair os detalhes relevantes de cada item
        nome = item.get('name')
        data_sessao = item.get('dataSessao')
        estado = item.get('estado')
        cidade = item.get('cidade')
        # Adicionar os detalhes à lista de pessoas em espera
        pessoas_em_espera.append({'nome': nome, 'data_sessao': data_sessao, 'estado':estado,'cidade':cidade})

    # Retorna a lista de pessoas em espera como uma resposta JSON
    return render(request, r'E:\mychat\mychat\base\templates\base\lista_espera.html', {'pessoas_em_espera': pessoas_em_espera})

