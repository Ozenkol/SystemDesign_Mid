from inventory.controller import InventoryService
from payment.controller import PaymentService
from shipping.controller import ShippingService

class SagaCoordinator:
    def execute_saga(self, order_data, payment_data, notification_data):
        inventory_service = InventoryService()
        payment_service = PaymentService()
        shipping_service = ShippingService()

        try:
            payment_id = payment_service.crea(order_data)

            shipping_service.process_payment(payment_id, payment_data)

            print("Сага успешно завершена!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            self.rollback_saga(payment_id)

    def rollback_saga(self, order_id):
        order_service = PaymentService()
        payment_service = InventoryService()
        notification_service = ShippingService()

        try:
            payment_service.rollback_payment(order_id)

            notification_service.rollback_notification(order_id)

            order_service.cancel_order(order_id)

            print("Сага успешно отменена!")
        except Exception as e:
            print(f"Ошибка при откате саги: {e}")