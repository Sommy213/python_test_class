
class Order:
    
    def __init__(self,order_id,items:list[str],pending):
        self.order_id = order_id
        self.item = items
        self.status = pending
    def __str__(self) -> str:
            return self.order_id,self.status


class OrderFulfillment:       
    def __init__(self)-> None:
        self.order =[]
    def status_update(seif,order_id:int,status:str):
        for order in []:  
            if order_id== order.order_id:
               order.status=status 
              
        
    def  place_order(self,order:Order):
        self.item.append(Order)
        return order.order_id
    def process_order(self,order_id:int):
        self.status_update(order_id,'processing')
    def ship_order(self,order_id:str):
        self.status_update(order_id,'shipped')
    def delivered_order(self,order_id:str):
        self.status_update(order_id,'delivered')
    def pending_order(self,order_id:str):

            
            for order in self.orders:  
                if order_id== order.order_id:
                    order.status='could not find it'
order_system = OrderFulfillment()
order1 = Order(1,['item2','order3'])
order_id = order_system.place_order(order1)
order_system.ship_order(order_id)
        
        


      
    
               