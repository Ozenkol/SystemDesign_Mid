class SagaCoordinator:
    def execute_saga(self, order_data, payment_data, notification_data):
        order_service = OrderService()
        payment_service = PaymentService()
        notification_service = NotificationService()

        try:
            # Шаг 1: Создание заказа
            order_id = order_service.create_order(order_data)

            # Шаг 2: Выполнение платежа
            payment_service.process_payment(order_id, payment_data)

            # Шаг 3: Отправка уведомления
            notification_service.send_notification(order_id, notification_data)

            # Все успешно выполнено, завершаем сагу
            print("Сага успешно завершена!")
        except Exception as e:
            # Обработка ошибки и выполнение компенсирующих действий
            print(f"Произошла ошибка: {e}")
            self.rollback_saga(order_id)

    def rollback_saga(self, order_id):
        # Вызываем компенсирующие действия для отмены всех предыдущих операций
        order_service = OrderService()
        payment_service = PaymentService()
        notification_service = NotificationService()

        try:
            # Шаг 1: Отмена платежа
            payment_service.rollback_payment(order_id)

            # Шаг 2: Отмена уведомления
            notification_service.rollback_notification(order_id)

            # Шаг 3: Отмена создания заказа
            order_service.cancel_order(order_id)

            print("Сага успешно отменена!")
        except Exception as e:
            # Обработка ошибки во время отката
            print(f"Ошибка при откате саги: {e}")