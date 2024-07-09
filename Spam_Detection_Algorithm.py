class SpamDetector:
    def __init__(self):
        # List of common spam keywords
        self.spam_keywords = [
            "congratulations", "winner", "free", "prize", "click here", "urgent",
            "limited time offer", "act now", "guaranteed", "risk-free"
        ]
        # List of suspicious sender addresses
        self.suspicious_senders = [
            "noreply@spam.com", "offers@freemoney.com", "winbig@lottery.com"
        ]

    def detect_spam(self, email):
        # Check if the email contains any spam keywords
        for keyword in self.spam_keywords:
            if keyword in email["subject"].lower() or keyword in email["body"].lower():
                return True

        # Check if the sender is in the list of suspicious senders
        if email["sender"].lower() in self.suspicious_senders:
            return True

        return False


# Example usage
spam_detector = SpamDetector()

# Example email
email = {
    "sender": "noreply@spam.com",
    "subject": "Congratulations! You've won a free prize!",
    "body": "Click here to claim your guaranteed risk-free prize now."
}

# Detect if the email is spam
is_spam = spam_detector.detect_spam(email)

if is_spam:
    print("This email is spam.")
else:
    print("This email is not spam.")
