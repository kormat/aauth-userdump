To use this module:
- Install it using `python setup.py install` inside your venv envrionment.
- Edit your aauth settings file:
  - Add `'aauthuserdump',` to the `INSTALLED_APPS` section.
  - Add `USERDUMP_PATH = /path/to/export/userdump.json` to control where the
    JSON is exported to. If not specified, it will write to `/tmp/userdump.json`.
  - Add a scheduled task to run the export regularly:
  ```
  CELERYBEAT_SCHEDULE['aauthuserdump_update'] = {
      'task': 'aauthuserdump.update_all_users',
      'schedule': crontab(minute="*"),
  }
  ```
  - To see debug log messages from aauthuserdump:
  ```
  LOGGING['loggers']['aauthuserdump'] = {
      'handlers': ['log_file', 'console', 'notifications'],
      'level': 'DEBUG',
      'propagate': False,
  }
  ```
- Restart aauth and its celery workers: `supervisorctl restart aauth:`
