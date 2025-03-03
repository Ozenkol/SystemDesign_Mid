<h1>Simple SAGA pattern microservices</h1>
<p>Simple SAGA pattern microservices using python and postgresql database. The code runned on Windows OS</p>

<p>The saga pattern help manage transaction across multiple servies. It acts like finite automata, with states "ok" and "error", and some transwer function that change state. The following diagramm represent saga pattern in terms of graph</p>

``` mermaid
flowchart LR;
    subgraph Saga
    Payment --Message--> Inventory --Message--> Shipping
    Shipping --Event--> Inventory --Event--> Payment
    end
```

<p>There are two ways of coordination sagas:<br>
Choreography - each local transaction publishes domain events that trigger local transactions in other services
Orchestration - an orchestrator (object) tells the participants what local transactions to execute</p>

<h2>Example: Orchestration</h2>

``` mermaid
graph LR;
    subgraph Payment
    PaymentService
    end
    subgraph Inventory
    InventoryService
    end
    subgraph Shipping
    ShippingService
    end
    subgraph Orchestrator
    
    end
    subgraph Client
    
    end
    Client --> Orchestrator
    Orchestrator --create payment-->Payment
    Orchestrator --create shipping-->Shipping
    Orchestrator --create inventory-->Inventory
    Payment -- success --> Orchestrator
    Shipping -- success --> Orchestrator
    Inventory  -- success --> Orchestrator

```

<h2>Example: Choreography-based saga</h2>

``` mermaid
graph TD;
    subgraph Payment
    PaymentService
    end
    subgraph Inventory
    InventoryService
    end
    subgraph Shipping
    ShippingService
    end
    EventBus:::wide
    classDef wide padding:500px
    subgraph Client
    
    end
    Client --> EventBus
    EventBus --create payment-->Payment
    EventBus --create shipping-->Shipping
    EventBus --create inventory-->Inventory
    Payment -- success --> EventBus
    Shipping -- success --> EventBus
    Inventory  -- success --> EventBus

```