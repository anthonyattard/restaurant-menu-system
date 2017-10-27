from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurant')
@app.route('/restaurants')
def showRestaurants():
    # return "This page will show all my restaurants"
    restaurants = session.query(Restaurant).all()
    return render_template('restaurants.html', restaurants=restaurants)

@app.route('/restaurant/new', methods=['GET','POST'])
def newRestaurant():
    # return "This page will be for making a new restaurant"
    if request.method == 'POST':
        newRest = Restaurant(name = request.form['name'])
        session.add(newRest)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newrestaurant.html')

@app.route('/restaurant/<int:restaurant_id>/edit', methods=['GET','POST'])
def editRestaurant(restaurant_id):
    # return "This page will be for editing restaurant %s" % restaurant_id
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            restaurant.name = request.form['name']
        session.add(restaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editrestaurant.html', restaurant=restaurant)

@app.route('/restaurant/<int:restaurant_id>/delete', methods=['GET','POST'])
def deleteRestaurant(restaurant_id):
    # return "This page will be for deleting restaurant %s" % restaurant_id
    restaurantToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(restaurantToDelete)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleterestaurant.html', restaurant=restaurantToDelete)

@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # return "This page is the menu for restaurant %s" % restaurant_id
    menu_items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('menu.html', restaurant_id=restaurant_id, menu_items=menu_items)

@app.route('/restaurant/<int:restaurant_id>/menu/new', methods=['GET','POST'])
def newMenuItem(restaurant_id):
    # return "This page is for making a new menu item for restaurant %s" % restaurant_id
    if request.method == 'POST':
        newItem = MenuItem(
                name=request.form['name'], description=request.form['description'], 
                price=request.form['price'], course=request.form['course'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    # return "This page is for editing menu item %s" % menu_id
    menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            menu_item.name = request.form['name']
        if request.form['description']:
            menu_item.description = request.form['description']
        if request.form['price']:
            menu_item.price = request.form['price']
        if request.form['course']:
            menu_item.course = request.form['course']
        session.add(menu_item)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', menu_item=menu_item, restaurant_id=restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    # return "This page is for deleting menu item %s" % menu_id
    menu_item = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(menu_item)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', menu_item=menu_item, restaurant_id=restaurant_id)

@app.route('/restaurants/JSON')
def restaurantsJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurants])

@app.route('/restaurant/<int:restaurant_id>/menu/JSON')
def menuItemsJSON(restaurant_id):
    menuItems = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in menuItems])

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    menuItem = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
    return jsonify(MenuItem=[menuItem.serialize])

if __name__ == '__main__':
    app.dubug = True
    print app.dubug
    app.run(host = '0.0.0.0', port = 5000)
