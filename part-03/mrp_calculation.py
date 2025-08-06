#!/usr/bin/env python3
"""
MRP Calculation for Aufgabe 3: Rollierende Planung
Calculates correct Material Requirements Planning with inventory consideration
"""

import pandas as pd
import numpy as np

def main():
    print("=== MRP Calculation for Aufgabe 3 ===\n")

    # Product data
    products = {
        'L1': {'lead_time': 1, 'initial_stock': 20, 'structure': 'end_product'},
        'S1': {'lead_time': 1, 'initial_stock': 50, 'structure': 'end_product'},
        'P1': {'lead_time': 2, 'initial_stock': 30, 'structure': 'component'},
        'W1': {'lead_time': 3, 'initial_stock': 100, 'structure': 'component'}
    }

    # BOM (Bill of Materials) - what components are needed for each product
    bom = {
        'L1': {'P1': 1, 'W1': 1},  # L1 needs 1 P1 and 1 W1
        'S1': {'W1': 1}            # S1 needs 1 W1
    }

    # Primary demand
    weeks = list(range(1, 7))
    primary_demand = {
        'L1': [0, 40, 0, 60, 0, 50],
        'S1': [30, 0, 80, 0, 70, 0]
    }

    print("Primary Demand:")
    demand_df = pd.DataFrame({
        'Week': weeks,
        'L1': primary_demand['L1'],
        'S1': primary_demand['S1']
    })
    print(demand_df.to_string(index=False))
    print()

    # Calculate MRP for end products
    print("=== STEP 1: End Products MRP ===")
    production_schedule = {'L1': {}, 'S1': {}}

    for product in ['L1', 'S1']:
        print(f"\n{product} (Lead time: {products[product]['lead_time']}, Initial stock: {products[product]['initial_stock']}):")
        current_stock = products[product]['initial_stock']

        for i, week in enumerate(weeks):
            gross_req = primary_demand[product][i]
            if gross_req > 0:
                net_req = max(gross_req - current_stock, 0)
                if net_req > 0:
                    production_week = week - products[product]['lead_time']
                    production_schedule[product][production_week] = net_req
                    print(f"  Week {week}: Gross req {gross_req}, Stock {current_stock} → Net req {net_req} → Production in week {production_week}")
                    current_stock = 0  # Stock is consumed
                else:
                    print(f"  Week {week}: Gross req {gross_req}, Stock {current_stock} → Net req 0 (sufficient stock)")
                    current_stock -= gross_req
            else:
                print(f"  Week {week}: No demand")

    print(f"\nProduction Schedule:")
    for product in ['L1', 'S1']:
        for week, qty in sorted(production_schedule[product].items()):
            print(f"  {product}: {qty} units in week {week}")

    # Calculate component requirements
    print("\n=== STEP 2: Component Requirements ===")
    component_requirements = {'P1': {}, 'W1': {}}

    # P1 requirements (only from L1)
    print("\nP1 Requirements (from L1 production):")
    for week, qty in production_schedule['L1'].items():
        component_requirements['P1'][week] = qty
        print(f"  Week {week}: {qty} units needed (from L1 production)")

    # W1 requirements (from both L1 and S1)
    print("\nW1 Requirements (from L1 and S1 production):")
    for product in ['L1', 'S1']:
        for week, qty in production_schedule[product].items():
            if week in component_requirements['W1']:
                component_requirements['W1'][week] += qty
            else:
                component_requirements['W1'][week] = qty
            print(f"  Week {week}: +{qty} units from {product} production")

    # Calculate component MRP
    print("\n=== STEP 3: Component MRP & Order Dates ===")
    order_schedule = {'P1': {}, 'W1': {}}

    for component in ['P1', 'W1']:
        print(f"\n{component} (Lead time: {products[component]['lead_time']}, Initial stock: {products[component]['initial_stock']}):")
        current_stock = products[component]['initial_stock']

        # Sort requirements by week
        req_weeks = sorted(component_requirements[component].keys())

        for week in req_weeks:
            gross_req = component_requirements[component][week]
            net_req = max(gross_req - current_stock, 0)
            if net_req > 0:
                order_week = week - products[component]['lead_time']
                order_schedule[component][order_week] = net_req
                print(f"  Week {week}: Gross req {gross_req}, Stock {current_stock} → Net req {net_req} → Order in week {order_week}")
                current_stock = 0  # Stock is consumed
            else:
                print(f"  Week {week}: Gross req {gross_req}, Stock {current_stock} → Net req 0 (sufficient stock)")
                current_stock -= gross_req

    # Summary of all orders/productions
    print("\n=== COMPLETE ORDER SCHEDULE ===")
    all_orders = []

    # End products
    for product in ['L1', 'S1']:
        for week, qty in sorted(production_schedule[product].items()):
            all_orders.append({
                'Product': product,
                'Type': 'Production',
                'Week': week,
                'Quantity': qty,
                'Frozen': week <= 2
            })

    # Components
    for component in ['P1', 'W1']:
        for week, qty in sorted(order_schedule[component].items()):
            all_orders.append({
                'Product': component,
                'Type': 'Order',
                'Week': week,
                'Quantity': qty,
                'Frozen': week <= 2
            })

    # Sort by week
    all_orders.sort(key=lambda x: x['Week'])

    orders_df = pd.DataFrame(all_orders)
    print(orders_df.to_string(index=False))

    # Frozen zone analysis
    print("\n=== FROZEN ZONE ANALYSIS ===")
    frozen_orders = [order for order in all_orders if order['Frozen']]
    print(f"Orders in Frozen Zone (Week <= 2):")
    for order in frozen_orders:
        print(f"  {order['Product']}: {order['Type']} of {order['Quantity']} units in week {order['Week']}")

    return all_orders, production_schedule, order_schedule

if __name__ == "__main__":
    main()
