from system_monitor import scheduler, app
from system_monitor.docker.docker import running_containers
from system_monitor.system.systeminfo.c_system import system


if __name__ == '__main__':
    scheduler.add_job(id='Scheduled Task1', func=system, trigger="interval", seconds=3)
    scheduler.add_job(id='Scheduled Task2', func=running_containers, trigger="interval", seconds=3)
    scheduler.start()
    app.run(host='localhost', port=5000, debug=True)
