from message import Message
class SignatureMessage:
    def __init__(self, sender, receiver, signature):
        """Initializes the class"""
        self.sender=sender
        self.receiver=receiver
        self.message=[]
        self.signature=signature
    def __str__(self):
        """Returns string to print"""
        messagestring=""
        for line in self.message:
            messagestring+=line+"\n"
        printstring = f"From: {self.sender}\nTo: {self.receiver}\n{messagestring}\n{self.signature}"
        return printstring
    def append(self, line:"str"):
        """adds line to email"""
        self.message.append(line)
    def __len__(self):
        """Calculates length of message"""
        length=0
        for line in self.message:
            length+=len(line)
        return length
    def __gt__(self, other:"Message"):
        """Checks if message is greater than another message"""
        if len(self)>len(other):
            return True
        else:
            return False
