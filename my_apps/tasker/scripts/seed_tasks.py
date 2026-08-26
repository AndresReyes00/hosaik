from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone

from my_apps.tasker.models import SubTask, Task


def run():
    # =========================================================
    # USER
    # =========================================================

    user = User.objects.first()

    if not user:
        print("❌ No users found.")
        print("Create a user first:")
        print("py manage.py createsuperuser")
        return

    # =========================================================
    # CLEAR EXISTING DATA
    # =========================================================

    SubTask.objects.all().delete()
    Task.objects.all().delete()

    print("🧹 Existing tasks and subtasks deleted.")

    # =========================================================
    # BASE DATE
    # =========================================================

    now = timezone.now()

    # =========================================================
    # TASKS
    # =========================================================

    tasks_data = [
        {
            "title": "Build Hosaik portfolio",
            "description": (
                "Complete the main Hosaik portfolio using Django and Bootstrap."
            ),
            "priority": Task.PriorityChoices.HIGH,
            "due_date": now + timedelta(days=7),
            "subtasks": [
                ("Create hero section", True, 0),
                ("Create technologies section", True, 1),
                ("Create projects section", True, 2),
                ("Create blog section", False, 4),
                ("Create contact section", False, 6),
                ("Optimize responsive design", False, 7),
            ],
        },
        {
            "title": "Learn Python fundamentals",
            "description": (
                "Strengthen Python fundamentals through theory and practical exercises."
            ),
            "priority": Task.PriorityChoices.HIGH,
            "due_date": now + timedelta(days=5),
            "subtasks": [
                ("Review variables and data types", True, 0),
                ("Practice conditionals", True, 1),
                ("Practice loops", True, 2),
                ("Practice lists and dictionaries", True, 3),
                ("Practice functions", False, 4),
                ("Solve 10 programming exercises", False, 5),
            ],
        },
        {
            "title": "Study computer networks",
            "description": (
                "Study networking fundamentals and practice "
                "configuration in Packet Tracer."
            ),
            "priority": Task.PriorityChoices.URGENT,
            "due_date": now + timedelta(days=3),
            "subtasks": [
                ("Review OSI model", True, 0),
                ("Study TCP/IP model", True, 1),
                ("Study IPv4 addressing", False, 1),
                ("Practice subnetting", False, 2),
                ("Configure a switch in Packet Tracer", False, 2),
                ("Configure a basic router", False, 3),
            ],
        },
        {
            "title": "Create Hosaik branding guidelines",
            "description": (
                "Define the visual rules used throughout the Hosaik ecosystem."
            ),
            "priority": Task.PriorityChoices.MEDIUM,
            "due_date": now + timedelta(days=14),
            "subtasks": [
                ("Define primary colors", True, 2),
                ("Define typography", True, 3),
                ("Define spacing system", False, 5),
                ("Define button styles", False, 7),
                ("Document brand guidelines", False, 14),
            ],
        },
        {
            "title": "Build Taskedo dashboard",
            "description": (
                "Create the main dashboard where users can "
                "visualize and manage their tasks."
            ),
            "priority": Task.PriorityChoices.URGENT,
            "due_date": now + timedelta(days=10),
            "subtasks": [
                ("Create dashboard layout", True, 0),
                ("Create task statistics", True, 1),
                ("Create progress cards", False, 3),
                ("Create upcoming tasks section", False, 5),
                ("Create task filters", False, 7),
                ("Add responsive design", False, 10),
            ],
        },
        {
            "title": "Study databases",
            "description": (
                "Learn relational databases and SQL fundamentals "
                "for backend development."
            ),
            "priority": Task.PriorityChoices.MEDIUM,
            "due_date": now + timedelta(days=20),
            "subtasks": [
                ("Learn database concepts", False, 2),
                ("Study primary keys", False, 4),
                ("Study foreign keys", False, 6),
                ("Learn SQL SELECT", False, 9),
                ("Practice JOIN queries", False, 14),
                ("Design a small database", False, 20),
            ],
        },
        {
            "title": "Improve Django skills",
            "description": (
                "Deepen Django knowledge by building features for real projects."
            ),
            "priority": Task.PriorityChoices.HIGH,
            "due_date": now + timedelta(days=12),
            "subtasks": [
                ("Review Django models", True, 0),
                ("Review Django forms", True, 1),
                ("Practice class based views", True, 2),
                ("Study Django authentication", False, 5),
                ("Study permissions", False, 8),
                ("Build a CRUD application", False, 12),
            ],
        },
        {
            "title": "Create Python automation scripts",
            "description": ("Build small Python scripts to automate repetitive tasks."),
            "priority": Task.PriorityChoices.MEDIUM,
            "due_date": now + timedelta(days=15),
            "subtasks": [
                ("Create file organizer", False, 2),
                ("Create folder backup script", False, 5),
                ("Read and write CSV files", False, 8),
                ("Process JSON data", False, 11),
                ("Create command line interface", False, 15),
            ],
        },
        {
            "title": "Study cybersecurity fundamentals",
            "description": (
                "Build a strong foundation in cybersecurity, "
                "covering threats, vulnerabilities and defenses."
            ),
            "priority": Task.PriorityChoices.HIGH,
            "due_date": now + timedelta(days=30),
            "subtasks": [
                ("Study CIA triad", False, 3),
                ("Study common vulnerabilities", False, 7),
                ("Study authentication", False, 12),
                ("Study authorization", False, 17),
                ("Study encryption basics", False, 23),
                ("Practice security concepts", False, 30),
            ],
        },
        {
            "title": "Plan Hosaik content",
            "description": (
                "Prepare technical content for Hosaik social media "
                "and professional platforms."
            ),
            "priority": Task.PriorityChoices.LOW,
            "due_date": now + timedelta(days=18),
            "subtasks": [
                ("Define content categories", True, 1),
                ("Create Python post idea", True, 3),
                ("Create networking post idea", False, 7),
                ("Create Django post idea", False, 11),
                ("Create cybersecurity post idea", False, 18),
            ],
        },
        {
            "title": "Read technical documentation",
            "description": (
                "Read official documentation regularly to improve technical knowledge."
            ),
            "priority": Task.PriorityChoices.LOW,
            "due_date": now + timedelta(days=30),
            "subtasks": [
                ("Read Python documentation", False, 7),
                ("Read Django documentation", False, 14),
                ("Read Bootstrap documentation", False, 21),
                ("Read Git documentation", False, 30),
            ],
        },
        {
            "title": "Deploy Hosaik project",
            "description": ("Prepare the Hosaik project for production deployment."),
            "priority": Task.PriorityChoices.URGENT,
            "due_date": now + timedelta(days=21),
            "subtasks": [
                ("Configure production settings", False, 3),
                ("Configure environment variables", False, 6),
                ("Configure static files", False, 9),
                ("Configure database", False, 12),
                ("Configure domain", False, 16),
                ("Deploy application", False, 19),
                ("Test production environment", False, 21),
            ],
        },
        {
            "title": "Practice Git and GitHub",
            "description": (
                "Improve Git workflow and repository management "
                "for software development."
            ),
            "priority": Task.PriorityChoices.MEDIUM,
            "due_date": now + timedelta(days=8),
            "subtasks": [
                ("Review Git basics", True, 1),
                ("Practice branches", True, 2),
                ("Practice merge conflicts", False, 4),
                ("Learn pull requests", False, 6),
                ("Improve repository README", False, 8),
            ],
        },
        {
            "title": "Build a Python data project",
            "description": (
                "Create a small project focused on data processing "
                "and analysis with Python."
            ),
            "priority": Task.PriorityChoices.HIGH,
            "due_date": now + timedelta(days=16),
            "subtasks": [
                ("Find a dataset", False, 2),
                ("Load CSV data", False, 4),
                ("Clean the data", False, 7),
                ("Calculate statistics", False, 10),
                ("Create visualizations", False, 13),
                ("Document the project", False, 16),
            ],
        },
        {
            "title": "Prepare Taskedo MVP",
            "description": (
                "Define and implement the essential functionality "
                "for the first Taskedo MVP."
            ),
            "priority": Task.PriorityChoices.URGENT,
            "due_date": now + timedelta(days=25),
            "subtasks": [
                ("Create Task model", True, 1),
                ("Create SubTask model", True, 2),
                ("Create task list", False, 5),
                ("Create task detail", False, 8),
                ("Create task creation form", False, 12),
                ("Create task editing", False, 16),
                ("Create task deletion", False, 20),
                ("Create dashboard", False, 25),
            ],
        },
    ]

    # =========================================================
    # CREATE
    # =========================================================

    task_count = 0
    subtask_count = 0

    for data in tasks_data:
        subtasks = data.pop("subtasks")

        task = Task.objects.create(
            owner=user,
            **data,
        )

        task_count += 1

        for title, is_completed, days_after_now in subtasks:
            SubTask.objects.create(
                task=task,
                title=title,
                is_completed=is_completed,
                due_date=now + timedelta(days=days_after_now),
            )

            subtask_count += 1

        # Synchronize status with subtasks.
        task.update_status_from_subtasks()

    # =========================================================
    # RESULT
    # =========================================================

    print("")
    print("✅ Taskedo seed completed successfully!")
    print(f"📋 Tasks created: {task_count}")
    print(f"☑️ SubTasks created: {subtask_count}")
    print(f"👤 Owner: {user.username}")
    print("")

    # =========================================================
    # SUMMARY
    # =========================================================

    pending = Task.objects.filter(
        owner=user,
        status=Task.StatusChoices.PENDING,
    ).count()

    in_progress = Task.objects.filter(
        owner=user,
        status=Task.StatusChoices.IN_PROGRESS,
    ).count()

    completed = Task.objects.filter(
        owner=user,
        status=Task.StatusChoices.COMPLETED,
    ).count()

    cancelled = Task.objects.filter(
        owner=user,
        status=Task.StatusChoices.CANCELLED,
    ).count()

    print("📊 Task status:")
    print(f"   Pending: {pending}")
    print(f"   In progress: {in_progress}")
    print(f"   Completed: {completed}")
    print(f"   Cancelled: {cancelled}")
    print("")
