# Subsystem A: Payment System
class PaymentSystem:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}...")
        return True


# Subsystem B: SMS Notification System
class SMSNotificationSystem:
    def send_sms(self, phone_number, message):
        print(f"Sending SMS to {phone_number}: {message}")
        return True


# Subsystem C: Invoice System
class InvoiceSystem:
    def generate_invoice(self, amount, customer_name):
        print(f"Generating invoice for {customer_name} with amount ${amount}...")
        return f"Invoice #{hash(customer_name)}"


# Facade: E-commerce Workflow
class ECommerceFacade:
    def __init__(self):
        self.payment_system = PaymentSystem()
        self.sms_system = SMSNotificationSystem()
        self.invoice_system = InvoiceSystem()

    def complete_order(self, customer_name, phone_number, amount):
        print("Starting order process...")

        payment_success = self.payment_system.process_payment(amount)
        if not payment_success:
            print("Payment failed!")
            return False

        invoice = self.invoice_system.generate_invoice(amount, customer_name)
        sms_success = self.sms_system.send_sms(phone_number, f"Thank you! Your order is confirmed.\n{invoice}")

        print("Order successfully completed!")
        return sms_success


# Client Code: Using the Facade
def main():
    facade = ECommerceFacade()
    facade.complete_order(customer_name="Amir", phone_number="+989377966936", amount=100.0)


if __name__ == "__main__":
    main()
