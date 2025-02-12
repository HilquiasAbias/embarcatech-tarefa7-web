from ninja import NinjaAPI
from django.http import HttpRequest
from django.contrib.admin.views.decorators import staff_member_required
from .models import Tarefa
import json

api = NinjaAPI(docs_decorator=staff_member_required, urls_namespace='matheus_api')


@api.get("/get/")
def api_get(request: HttpRequest):
    tarefas = list(Tarefa.objects.all().values())
    return tarefas if tarefas else []


@api.post("/post/")
def api_post(request: HttpRequest):
    body = json.loads(request.body)
    tarefa = Tarefa.objects.create(
        nome=body["nome"],
        descricao=body["descricao"]
    )
    return {
        "tarefa": tarefa.nome,
        "descricao": tarefa.descricao
    }