from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    class PriorityChoices(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        URGENT = "URGENT", "Urgent"

    title = models.CharField(
        max_length=150,
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    description = models.TextField(
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.MEDIUM,
    )

    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    # ---------------------------------------------------------
    # SUBTASKS
    # ---------------------------------------------------------

    @property
    def total_subtasks(self):
        return self.subtasks.count()

    @property
    def completed_subtasks(self):
        return self.subtasks.filter(is_completed=True).count()

    @property
    def pending_subtasks(self):
        return self.subtasks.filter(is_completed=False).count()

    # ---------------------------------------------------------
    # PROGRESS
    # ---------------------------------------------------------

    @property
    def progress(self):
        """
        Returns the task progress as a percentage.

        Example:
            2 completed subtasks out of 4 = 50%
        """

        total = self.total_subtasks

        if total == 0:
            return 0

        completed = self.completed_subtasks

        return round((completed / total) * 100)

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------

    def update_status_from_subtasks(self):
        """
        Updates the task status according to its subtasks.

        Rules:

        - No subtasks:
            Keep current status.

        - All subtasks completed:
            COMPLETED

        - Some subtasks completed:
            IN_PROGRESS

        - No subtasks completed:
            PENDING

        - CANCELLED:
            Remains CANCELLED.
        """

        if self.status == self.StatusChoices.CANCELLED:
            return

        total = self.total_subtasks

        if total == 0:
            return

        completed = self.completed_subtasks

        if completed == total:
            new_status = self.StatusChoices.COMPLETED

        elif completed > 0:
            new_status = self.StatusChoices.IN_PROGRESS

        else:
            new_status = self.StatusChoices.PENDING

        if self.status != new_status:
            self.status = new_status

            self.save(
                update_fields=[
                    "status",
                    "updated_at",
                ]
            )

    # ---------------------------------------------------------
    # HELPERS
    # ---------------------------------------------------------

    @property
    def is_completed(self):
        return self.status == self.StatusChoices.COMPLETED

    @property
    def is_cancelled(self):
        return self.status == self.StatusChoices.CANCELLED

    @property
    def has_subtasks(self):
        return self.total_subtasks > 0


class SubTask(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="subtasks",
    )

    title = models.CharField(
        max_length=150,
    )

    description = models.TextField(
        blank=True,
    )

    is_completed = models.BooleanField(
        default=False,
    )

    due_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @property
    def status(self):
        return self.task.status

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.task.update_status_from_subtasks()

    def delete(self, *args, **kwargs):
        task = self.task

        result = super().delete(*args, **kwargs)

        task.update_status_from_subtasks()

        return result

    @property
    def is_pending(self):
        return not self.is_completed

    @property
    def is_task_completed(self):
        return self.task.status == Task.StatusChoices.COMPLETED
