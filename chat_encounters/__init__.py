from datetime import datetime
import json
from time import time

from .core.base import BASE_PATH, BasePlugin
from .core.utils import command


class Plugin(BasePlugin):
    log_file = BASE_PATH / 'log.json'
    logs = {}

    def init(self):
        super().init()
        self.load()

    def load(self):
        if not self.log_file.is_file():
            self.log_file.write_text('{}')

        self.logs = json.loads(self.log_file.read_text())

    def save(self):
        self.log_file.write_text(json.dumps(self.logs))

    def strftime(self, time):
        return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d, %H:%M:%S')

    def incoming_public_chat_notification(self, room, user, _):
        self.logs[user] = (int(time()), '#' + room)
        self.save()

    def incoming_private_chat_notification(self, user, _):
        self.logs[user] = (int(time()), 'private')
        self.save()

    @command
    def encounters(self, args=[]):
        msg = ''
        total = 15
        if args and isinstance(args[0], int):
            total = args[0]
        elif args and args[0] == 'all':
            total = None
        elif args:
            time, place = self.logs.get(args[0], (None, None))
            if time:
                msg = f'You met {args[0]} at {self.strftime(time)} in {place}'
            else:
                msg = f'You haven\'t met {args[0]} yet'
        if not msg:
            encounters = sorted(self.logs.items(), key=lambda i: i[1][0], reverse=True)[:total]
            msg = f'Last Encounters [{len(encounters)}]:\nTime - Place - User\n' + '\n'.join(
                [f'- {self.strftime(v[0])} - {v[1]} - {u}'
                 for u, v in encounters])
        if msg:
            self.info_window(msg, with_prefix=False)

    __privatecommands__ = __publiccommands__ = [
        ('', encounters)
    ]
