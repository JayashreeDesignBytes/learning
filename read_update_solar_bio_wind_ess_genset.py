import mysql.connector


def fetch_parameters(cursor, table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    return cursor.fetchall()


def print_parameters(parameters):
    for param in parameters:
        print(
            f"id: {param[0]}, created_at: {param[1]}, updated_at: {param[2]}, maintainance_last_date: {param[3]}, next_due: {param[4]}, utilisation: {param[5]}, power_factor: {param[6]}, notification_alarms: {param[7]}, shutdowns: {param[8]}, frequency: {param[9]}, breaker_status: {param[10]}, operating_hours: {param[11]}, total_generation: {param[12]}, total_utilisation: {param[13]}, total_savings: {param[14]}, voltagel: {param[15]}, voltagen: {param[16]}, current: {param[17]}, kW: {param[18]}, kVA: {param[19]}, hours_operated: {param[20]}, power_generated: {param[21]}")
        print("\n")


def update(cursor, table_name, id, column, value):
    query = f"UPDATE {table_name} SET {column} = %s WHERE id = %s"
    cursor.execute(query, (value, id))


def print_parameters_ess(parameters):
    for param in parameters:
        print(
            f"id: {param[0]}, coolant_temp: {param[1]}, frequency: {param[2]}, battery_charged: {param[3]}, hours_operated_yesterday: {param[4]}, utilisation_factot: {param[5]}, alerts_shutdown: {param[6]}, power_gen_yesterday: {param[7]}, power_factor: {param[8]}, critical_load: {param[9]}, non_critical_load: {param[10]}, operating_hours: {param[11]}, total_gen: {param[12]}, total_consumption: {param[13]}, total_savings: {param[14]}, last_maintainance_date: {param[15]}, next_maintainance_date: {param[16]}, voltagei: {param[17]}, voltagen: {param[18]}, kw: {param[19]}, kva: {param[20]}, current: {param[21]}, level: {param[22]}")


def print_parameters_genset(parameters):
    for param in parameters:
        print(
            f"id: {param[0]}, coolant_temp: {param[1]}, frequency: {param[2]}, battery_charged: {param[3]}, oil_pressure: {param[4]}, hours_operated_yesterday: {param[5]}, utilisation_factot: {param[6]}, alerts_shutdown: {param[7]}, power_gen_yesterday: {param[8]}, power_factor: {param[9]}, critical_load: {param[10]}, non_critical_load: {param[11]}, operating_hours: {param[12]}, total_gen: {param[13]}, total_consumption: {param[14]}, total_savings: {param[15]}, last_maintainance_date: {param[16]}, next_maintainance_date: {param[17]}, voltagei: {param[18]}, voltagen: {param[19]}, kw: {param[20]}, kva: {param[21]}, current: {param[22]}")


def main():
    # Establish the database connection
    cnn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="J@yashreevj30",
        database="microgrid"
    )

    cursor = cnn.cursor()

    table_name = input("Enter Table name: ")
    if table_name in ["solar", "wind", "biogas", "mains"]:
        parameters = fetch_parameters(cursor, table_name)
        print_parameters(parameters)

        table_name = input("Enter table name to update: ")
        id = int(input("Enter ID to update: "))

        columns = [
            "created_at", "updated_at", "maintainance_last_date", "next_due",
            "utilisation", "power_factor", "notification_alarms", "shutdowns",
            "frequency", "breaker_status", "operating_hours", "total_generation",
            "total_utilisation", "total_savings", "voltagel", "voltagen",
            "current", "kW", "kVA", "hours_operated", "power_generated"
        ]

        for i, col in enumerate(columns, 1):
            print(f"({i}) {col}")

        action = int(input("Select what you want to update: "))

        if 1 <= action <= len(columns):
            column = columns[action - 1]
            value = input(f"Enter new value for {column}: ")
            update(cursor, table_name, id, column, value)
        else:
            print("Invalid action selected.")

        cnn.commit()
        parameters = fetch_parameters(cursor, table_name)
        print("Updated parameters:")
        print_parameters(parameters)

    elif table_name == "ess":
        parameters = fetch_parameters(cursor, table_name)
        print_parameters_ess(parameters)

        table_name = input("Enter table name to update: ")
        id = int(input("Enter ID to update: "))

        columns = [
            "coolant_temp", "frequency", "battery_charged", "hours_operated_yesterday", "utilisation_factor",
            "alerts_shutdown", "power_gen_yesterday", "power_factor", "critical_load", "non_critical_load",
            "operating_hours", "total_gen", "total_consumption", "total_savings", "last_maintainance_date",
            "next_maintainance_date", "voltagel", "voltagen", "kW", "kVA", "current", "level"
        ]

        for i, col in enumerate(columns, 1):
            print(f"({i}) {col}")

        action = int(input("Select what you want to update: "))

        if 1 <= action <= len(columns):
            column = columns[action - 1]
            value = input(f"Enter new value for {column}: ")
            update(cursor, table_name, id, column, value)
        else:
            print("Invalid action selected.")

        cnn.commit()
        parameters = fetch_parameters(cursor, table_name)
        print("Updated parameters:")
        print_parameters(parameters)

    elif table_name == "genset":
        parameters = fetch_parameters(cursor, table_name)
        print_parameters_genset(parameters)

        table_name = input("Enter table name to update: ")
        id = int(input("Enter ID to update: "))

        columns = [
            "coolant_temp", "frequency", "battery_charged","oil pressure" "hours_operated_yesterday", "utilisation_factor",
            "alerts_shutdown", "power_gen_yesterday", "power_factor", "critical_load", "non_critical_load",
            "operating_hours", "total_gen", "total_consumption", "total_savings", "last_maintainance_date",
            "next_maintainance_date", "voltagel", "voltagen", "kW", "kVA", "current", "level"
        ]

        for i, col in enumerate(columns, 1):
            print(f"({i}) {col}")

        action = int(input("Select what you want to update: "))

        if 1 <= action <= len(columns):
            column = columns[action - 1]
            value = input(f"Enter new value for {column}: ")
            update(cursor, table_name, id, column, value)
        else:
            print("Invalid action selected.")

        cnn.commit()
        parameters = fetch_parameters(cursor, table_name)
        print("Updated parameters:")
        print_parameters(parameters)


    else:
        print("Invalid table name.")

    cursor.close()
    cnn.close()


if __name__ == "__main__":
    main()

