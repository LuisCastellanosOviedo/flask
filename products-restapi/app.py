from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})


@app.route('/products')
def get_products():
    return jsonify({"products": products, "message": "ProductList"})


@app.route('/products/<string:product_name>')
def get_product(product_name):
    products_found = [
        product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        return jsonify({"product": products_found[0]})
    else:
        return jsonify({"message": "Product not found"})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)

    return jsonify({'message': 'Product added successfully', 'products': products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def edit_product(product_name):
    products_found = [
        product for product in products if product['name'] == product_name]
    if (len(products_found) > 0):
        products_found[0]['name'] = request.json['name']
        products_found[0]['price'] = request.json['price']
        products_found[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product Updated',
            'product': products_found[0]
        })
    return jsonify({
        'message': 'Product not found'
    })


@app.route('/products/<string:product_name>', methods=['DELETE'])
def delete_product(product_name):
     products_found = [
        product for product in products if product['name'] == product_name]

     if (len(products_found) > 0):
        products.remove(products_found[0])
        return jsonify({
                    'message': 'Product deleted successfully',
                    'products': products
                })

     return jsonify({'message': 'Product Not Found'})
    

if __name__ == '__main__':
    app.run(debug=True, port=4000)
