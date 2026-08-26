from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from my_apps.tasker.forms import TaskForm
from my_apps.tasker.models import Task


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
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.status = Task.StatusChoices.PENDING

        return super().form_valid(form)
