from order import Porder
from calculate_shipping import CalculateShipping

calculate_shipping = CalculateShipping()

order = Porder(500)

calculate_shipping.execute_calculation(order,'Default')
calculate_shipping.execute_calculation(order,'Express')

