from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
import asana
from pprint import pprint as p
from core.settings import ASANA_CONFIG
from todo.forms import AddTaskForm
from todo.utils import create_task, get_all_tasks, update_task, delete_task
from django.urls import reverse


headers = {
    "Asana-Enable": "new_user_task_lists"
}


class ListCreateTodoApiView(View):
    
    def get(self, request, *args, **kwargs):
        tasks = get_all_tasks()
        return render(request, 'todo/index.html', {'tasks': tasks})
    

    def post(self, request, *args, **kwargs):
        name = self.request.POST['name']
        notes = self.request.POST['notes']
        gid = self.request.POST.get('gid')
        print(gid)
        data = {
            "name": name,
            "notes": notes,
            "workspace": ASANA_CONFIG['WORKSPACE'],
            "assignee": ASANA_CONFIG['ASSIGNEE']
        }
        if not gid:
            post_status = create_task(data)
            print(post_status)
            return HttpResponseRedirect(reverse('todoAPI'))

        put_data = update_task(data, str(gid))
        print(put_data)
        return HttpResponseRedirect(reverse('todoAPI'))

class DeleteTodoApiView(View):

    def get(self, request, *args, **kwargs):
        gid = kwargs['gid']
        delete_data = delete_task(gid)
        return HttpResponse(delete_data, content_type='application/json', status=200)