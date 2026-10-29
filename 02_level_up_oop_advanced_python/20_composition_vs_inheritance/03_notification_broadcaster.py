from abc import ABC, abstractmethod
from datetime import datetime

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass
    def format_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"[{timestamp}] {message}"
class EmailChannel(NotificationChannel):
    def send(self, message, recipient):
        formatted = self.format_message(message)
        print(f"[EMAIL] To: {recipient} — {formatted}")
class SMSChannel(NotificationChannel):
    def __init__(self, char_limit=160):
        self.char_limit = char_limit
    def send(self, message, recipient):
        formatted = self.format_message(message)
        if len(formatted) > self.char_limit:
            formatted = formatted[:self.char_limit]
        print(f"[SMS] To: {recipient} — {formatted}")
class SlackChannel(NotificationChannel):
    def __init__(self, workspace):
        self.workspace = workspace
    def send(self, message, recipient):
        formatted = self.format_message(message)
        print(
            f"[SLACK #{self.workspace}] "
            f"To: {recipient} — {formatted}"
        )
class NotificationService:
    def __init__(self):
        self.channels = []
    def add_channel(self, channel):
        if not isinstance(channel, NotificationChannel):
            raise TypeError("Channel must be a NotificationChannel")
        self.channels.append(channel)
    def remove_channel(self, channel_type):
        self.channels = [
            channel for channel in self.channels
            if not isinstance(channel, channel_type)
        ]
    def broadcast(self, message, recipient):
        print(f'Broadcasting: "{message}"')
        for channel in self.channels:
            channel.send(message, recipient)
    def send_via(self, channel_type, message, recipient):
        for channel in self.channels:
            if isinstance(channel, channel_type):
                channel.send(message, recipient)
class PriorityNotificationService(NotificationService):
    def __init__(self, priority):
        super().__init__()
        if priority not in ("low", "medium", "high"):
            raise ValueError("Priority must be low, medium, or high")
        self.priority = priority
    def broadcast(self, message, recipient):
        print(f'\nPriority: {self.priority.upper()} — "{message}"')
        if self.priority == "low":
            allowed_channels = (SlackChannel,)
        elif self.priority == "medium":
            allowed_channels = (SlackChannel, EmailChannel)
        else:
            allowed_channels = (
                SlackChannel, EmailChannel, SMSChannel
            )
        for channel in self.channels:
            if isinstance(channel, allowed_channels):
                channel.send(message, recipient)

email = EmailChannel()
sms = SMSChannel()
slack = SlackChannel("engineering")
print("=== Composition: NotificationService HAS channels ===")
service = NotificationService()
service.add_channel(email)
service.add_channel(sms)
service.add_channel(slack)
service.broadcast(
    "Server maintenance tonight",
    "team@company.com"
)
print("\nRemoving SMS channel...")
service.remove_channel(SMSChannel)
service.broadcast("Deploy complete", "team@company.com")
print("\n=== Inheritance: PriorityNotificationService IS-A "
      "NotificationService ===")
low_service = PriorityNotificationService("low")
medium_service = PriorityNotificationService("medium")
high_service = PriorityNotificationService("high")
for priority_service in (low_service, medium_service, high_service):
    priority_service.add_channel(EmailChannel())
    priority_service.add_channel(SMSChannel())
    priority_service.add_channel(SlackChannel("engineering"))
low_service.broadcast("Coffee machine fixed", "team")
medium_service.broadcast("New release available", "team")
high_service.broadcast("Production is down!", "team")

"""Notification Broadcaster
Composition AND inheritance together — channels are inherited, service composes channels
Build a notification system that uses BOTH composition and inheritance correctly.

Abstract class: NotificationChannel(ABC)
- Abstract method: send(message, recipient)
- Concrete method: format_message(message) — adds timestamp prefix

Concrete channels (inherit from NotificationChannel):
- EmailChannel — send() prints "[EMAIL] To: {recipient} — {message}"
- SMSChannel(char_limit=160) — truncates if needed, prints "[SMS] To: {recipient} — {message}"
- SlackChannel(workspace) — prints "[SLACK #{workspace}] To: {recipient} — {message}"

NotificationService (uses COMPOSITION — has channels, doesn't inherit):
- Holds a list of channels
- add_channel(channel) — adds a channel
- remove_channel(channel_type) — removes all channels of that type
- broadcast(message, recipient) — sends through ALL channels
- send_via(channel_type, message, recipient) — sends through only channels of that type

PriorityNotificationService(NotificationService) — INHERITS from NotificationService:
- Overrides broadcast() to only use channels appropriate for the priority:
  - priority "low" → only Slack
  - priority "medium" → Slack + Email
  - priority "high" → ALL channels (Slack + Email + SMS)

Demonstrate:
1. Create a NotificationService with all 3 channels, broadcast a message
2. Remove SMS channel, broadcast again — only 2 channels fire
3. Create a PriorityNotificationService with all 3 channels
4. Send low, medium, and high priority messages — show different channels used for each
5. Clearly label which relationships are composition (Service HAS channels) and which are inheritance (PriorityService IS-A Service, channels ARE NotificationChannels)

Example output:

Broadcasting: "Server maintenance tonight"
[EMAIL] To: team@company.com — [2024-01-15 14:30] Server maintenance tonight
[SMS] To: 9876543210 — [2024-01-15 14:30] Server maintenance tonight
[SLACK #engineering] To: team@company.com — [2024-01-15 14:30] Server maintenance tonight

Removing SMS channel...
Broadcasting: "Deploy complete"
[EMAIL] To: team@company.com — [2024-01-15 14:31] Deploy complete
[SLACK #engineering] To: team@company.com — [2024-01-15 14:31] Deploy complete

Priority: LOW — "Coffee machine fixed"
[SLACK #engineering] To: team — Coffee machine fixed

Priority: HIGH — "Production is down!"
[EMAIL] To: team — Production is down!
[SMS] To: 9876543210 — Production is down!
[SLACK #engineering] To: team — Production is down!
"""