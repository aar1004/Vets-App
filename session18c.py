from session18a import Customer
from session18b import MongoDBHelper
from bson.objectid import ObjectId


def main():
    db = MongoDBHelper()

    # customer = Customer()
    # customer.read_customer_data()

    # document = vars(customer)
    # db.insert(document)

    #  customer = Customer()
    # customer.read_customer_data()

    # document = vars(customer)

    # db.insert(document)

    # query = {"phone": "+91 99999 111111"}
    query = {"_id": ObjectId("64c36fc617851284a9d2f143")}
    # db.delete(query)

    db.fetch(query=query)
    document_data_to_update = {
        "name": "George w",
        "phone": "+91 64567 63673",
        "age": 33,
    }

    db.update(document_data_to_update, query)


if __name__ == "__main__":
    main()
