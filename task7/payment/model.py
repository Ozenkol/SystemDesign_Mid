from db import Base

class PaymentService:
    def process_payment(self, order_id, payment_data):
        # Здесь реализация обработки платежа
        pass

    def rollback_payment(self, order_id):
        # Здесь реализация отмены платежа и компенсирующих действий
        pass