from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from twittor import create_app

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand) #添加flask_migrate指令到flask_script manager之中

if __name__ == "__main__":
    manager.run()