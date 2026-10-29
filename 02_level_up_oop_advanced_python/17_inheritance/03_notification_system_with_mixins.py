import random
from datetime import datetime 

class Notification:
    def __init__(self,message,priority):
        self.message=message
        self.priority =max(1 ,min(5,priority))
    def send(self):
        print(f"Message: {self.message}")    
class EmailNotification(Notification):
    def __init__(self, message, priority,to_address,subject):
        super().__init__(message, priority)      
        self.to_address=to_address
        self.subject=subject
    def send(self):
        print(f"[EMAIL] To :{self.to_address}"
              f"Subject; {self.subject} | Priority: {self.priority}"
              )
        super().send()      
class SMSNotification(Notification):
    def __init__(self, message, priority,phone_number,char_limit=160):
        super().__init__(message, priority)
        self.phone_number=phone_number
        self.char_limit=char_limit
    def send(self):
        message=self.message
        if len(message) > self.char_limit:
            message =message[:self.char_limit -3] + "..."
        print(f"[SMS] TO: {self.phone_number} "
              f"Priority: {self.priority}")
        print(f"Message: {message}")
class PushNotification(Notification):
    def __init__(self, message, priority,device_id,ttl_sec):
        super().__init__(message, priority)        
        self.device_id=device_id
        self.ttl_sec=ttl_sec
    def send(self):
        print(f"[PUSH] To: {self.device_id} |"
              f"TTL :{self.ttl_sec}s |"
              f"Priority: {self.priority}")
        super().send()    
class LoggableMixin:
    def log(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        recipient = getattr(self, "to_address", "unknown")

        print(
            f"[{timestamp}] Sent: "
            f"{type(self).__name__} to {recipient}"
        )      
class RetryableMixin:
    def send_with_retry(self, max_attempts=3):
        for attempt in range(1, max_attempts + 1):
            print(f"Attempt {attempt}:", end=" ")
            if random.random() < 0.5:
                print("Failed. Retrying..." if attempt < max_attempts
                      else "Failed.")
            else:
                self.send()
                print(f"Attempt {attempt}: Success!")
                return True
        print("All attempts failed.")
        return False          
class UrgentEmail(EmailNotification, LoggableMixin, RetryableMixin):
    def send(self):
        print(f"[URGENT EMAIL] To: {self.to_address} | "
            f"Subject: {self.subject} | "
            f"Priority: {self.priority}")
        print(f"Message: {self.message}")   
email = EmailNotification(
    "Don't forget the standup at 10am",
    3,
    "prathmesh@email.com",
    "Meeting")
email.send()
print()         
sms = SMSNotification(
    "Your OTP is 4829. Do not share this code with anyone.",
    2,
    "8857035193",
    char_limit=40
)
sms.send()
print()
push = PushNotification(
    "New message received",
    4,
    "device_abc123",
    3600
)
push.send()
print()
urgent = UrgentEmail(
    "Production server is down!",
    5,
    "boss@company.com",
    "Server Down"
)

urgent.send()
urgent.log()
print()
urgent.send_with_retry(max_attempts=3)
print()
print("MRO:")
print(" → ".join(cls.__name__ for cls in UrgentEmail.__mro__))

"""Notification System with Mixins
Multiple inheritance, mixins, and understanding MRO
Build a notification system that uses both regular inheritance and mixins.

Base class: Notification
- Attributes: message, priority (1-5, where 5 is highest)
- Method: send() — prints the notification (simulated, not actual sending)

Subclasses:
- EmailNotification(Notification) — additional: to_address, subject
- SMSNotification(Notification) — additional: phone_number, char_limit=160. If message exceeds char_limit, truncate and add "..."
- PushNotification(Notification) — additional: device_id, ttl_seconds

Mixin classes (small utility classes, no __init__):
- LoggableMixin — adds a log() method that prints a timestamped log entry: "[2024-01-15 14:30:00] Sent: <notification type> to <recipient>"
- RetryableMixin — adds a send_with_retry(max_attempts=3) method that calls send() and simulates random failures (use random.random() < 0.5 to simulate failure). Retries up to max_attempts times, prints each attempt.

Combined class:
- UrgentEmail(EmailNotification, LoggableMixin, RetryableMixin) — inherits from all three

Demonstrate:
1. Send one of each basic notification type
2. Send an SMS that exceeds the character limit — verify truncation
3. Send an UrgentEmail — show logging and retry behavior
4. Print the MRO of UrgentEmail using UrgentEmail.__mro__ and explain the order

Example output:

[EMAIL] To: amit@email.com | Subject: Meeting | Priority: 3
Message: Don't forget the standup at 10am

[SMS] To: 9876543210 | Priority: 2
Message: Your OTP is 4829. Do not share thi...

[PUSH] To: device_abc123 | TTL: 3600s | Priority: 4
Message: New message received

[URGENT EMAIL] To: boss@company.com | Subject: Server Down | Priority: 5
[2024-01-15 14:30:00] Sent: UrgentEmail to boss@company.com
Attempt 1: Failed. Retrying...
Attempt 2: Success!

MRO: UrgentEmail → EmailNotification → Notification → LoggableMixin → RetryableMixin → object

"""