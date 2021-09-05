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
        self.logs.setdefault('#' + room, {})
        self.logs['#' + room][user] = time()
        self.save()

    def incoming_private_chat_notification(self, user, _):
        self.logs.setdefault('private', {})
        self.logs['private'][user] = time()
        self.save()

    @command
    def encounters(self, args=[]):
        msg = 'Last Encounters'
        encounters = []
        key = None

        tot = 15
        if len(args) > 1:
            key, tot = args[:2]
        elif args:
            tot = args[0]

        total = int(tot) if isinstance(tot, (int, float)) else None if tot == 'all' else -1
        if total == -1:
            if not key:
                key = tot
            total = 15

        if isinstance(key, str):
            if key == 'private' or key.startswith('#'):
                msg += f' in {key}'
                encounters = [(key, u, t) for u, t in self.logs.get(key, {}).items()]
            else:
                msg += f' with {key}'

        if not encounters:
            for place, users in self.logs.items():
                for user, time_ in users.items():
                    if key and key != user:
                        continue
                    encounters.append((place, user, time_))

        encounters = sorted(encounters, key=lambda i: i[2], reverse=True)[:total]
        msg += f' [{len(encounters)}]:\nTime - Place - User\n' + '\n'.join(
            [f'- {self.strftime(t)} - {p} - {u}'
             for p, u, t in encounters])

        self.info_window(msg, with_prefix=False)

    __privatecommands__ = __publiccommands__ = [
        ('', encounters)
    ]
