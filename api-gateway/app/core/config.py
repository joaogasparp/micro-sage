import os

ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://order-service:8001")
INVENTORY_SERVICE_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory-service:8002")
BILLING_SERVICE_URL = os.getenv("BILLING_SERVICE_URL", "http://billing-service:8003")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8004")
LOGGER_SERVICE_URL = os.getenv("LOGGER_SERVICE_URL", "http://logger-service:8005")
