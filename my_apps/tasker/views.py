from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, ListView

from my_apps.tasker.forms import SubTaskForm, TaskForm
from my_apps.tasker.models import SubTask, Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = Task.objects.filter(owner=self.request.user).prefetch_related(
            "subtasks"
        )

        status = self.request.GET.get("status")

        valid_statuses = {
            Task.StatusChoices.PENDING,
            Task.StatusChoices.IN_PROGRESS,
            Task.StatusChoices.COMPLETED,
            Task.StatusChoices.CANCELLED,
        }

        if status in valid_statuses:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # -----------------------------------------------------
        # ALL USER TASKS
        # -----------------------------------------------------

        user_tasks = Task.objects.filter(owner=self.request.user)

        # -----------------------------------------------------
        # STATISTICS
        # -----------------------------------------------------

        context["total_tasks"] = user_tasks.count()

        context["pending_tasks"] = user_tasks.filter(
            status=Task.StatusChoices.PENDING
        ).count()

        context["in_progress_tasks"] = user_tasks.filter(
            status=Task.StatusChoices.IN_PROGRESS
        ).count()

        context["completed_tasks"] = user_tasks.filter(
            status=Task.StatusChoices.COMPLETED
        ).count()

        context["cancelled_tasks"] = user_tasks.filter(
            status=Task.StatusChoices.CANCELLED
        ).count()

        # -----------------------------------------------------
        # ACTIVE FILTER
        # -----------------------------------------------------

        context["active_status"] = self.request.GET.get("status", "ALL")

        return context


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = Task.StatusChoices.PENDING

        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "tasker:create_subtask",
            kwargs={"task_id": self.object.pk},
        )


class CreateSubTaskView(LoginRequiredMixin, CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "./subtask/create.html"

    def dispatch(self, request, *args, **kwargs):
        self.task = get_object_or_404(
            Task,
            pk=self.kwargs["task_id"],
            owner=request.user,
        )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = self.task
        return context

    def form_valid(self, form):
        form.instance.task = self.task
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "tasker:list",
            # kwargs={"pk": self.task.pk},
        )
