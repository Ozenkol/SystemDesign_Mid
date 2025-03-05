from orchestra import SagaCoordinator

if __name__ == "__main__":
    saga_coordinator = SagaCoordinator()
    order_data = {"customer_id": 123, "products": [1, 2, 3]}
    payment_data = {"amount": 100.0, "payment_method": "credit_card"}
    notification_data = {"message": "Ваш заказ успешно оформлен!"}
    saga_coordinator.execute_saga(order_data, payment_data, notification_data)