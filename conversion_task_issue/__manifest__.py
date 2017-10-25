# -*- coding: utf-8 -*-
{
    'name': "Convert Task to Issue, vice-versa",
    'summary': """
        Provide an option to a task to be converted into issue, as well as the issue to be converted into task.""",
    'description': """
Convert Task to Issue and Issue to Task
=======================================

Normally incoming mails are converted to Issues, and it's good that way.

Once in a while, we wish to treat an incoming mail as a Task (ex. if it is a Feature Request).

Provide an Action on Issues for converting Issue to Task.

Similarly, provide an Action on Tasks to convert_task_issue them into Issues.
    """,
    'author': "Dajana S.",
    'category': 'Project',
    'application': True,
    'version': '0.1',
    'depends': ['base', 'project', 'project_issue'],
    'data': [
        'views/issue_to_task.xml',
        'views/task_to_issue.xml'
    ],
}