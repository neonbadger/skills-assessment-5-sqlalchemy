"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries


# Get the brand with the **id** of 8.

Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Model.query.filter(Model.name == 'Corvette', 
                   Model.brand_name == 'Chevrolet'). all()

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter(Brand.founded == 1903, 
                   Brand.discontinued == None).all()

# Get all brands with that are either discontinued or founded before 1950.

a = Brand.query.filter( (Brand.discontinued != None) |
                    (Brand.founded < 1950) ).all()

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''


    all_cars_from_year = Model.query.filter(Model.year == year).all()

    for car in all_cars_from_year:
      print "Model %s from brand %s in %s came out in %d." % (car.name,
                                                              car.brand_name,
                                                              car.brands.headquarters,
                                                              year)
      print '\n'
    
    ### Solution before using db.ForeignKey & db.relationship
    ### join on Model.brand_name == Brand.name
    ### cars_from_year are NOT a list of objects, but a list
    ### of tuple with column info selected ( [(u'Model T'), (u'Ford') ...])
    ### print out without the objects

    # cars_from_year = db.session.query(Model.name, 
    #                                   Model.brand_name, 
    #                                   Brand.headquarters).join(
    #                                   Brand, Model.brand_name == Brand.name).filter(
    #                                   Model.year == year).all()
    
    # for name, brand_name, headquarters in cars_from_year:
    #     print "Model %s from brand %s in %s came out in %d." % (
    #                 name, brand_name, headquarters, year)

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    all_brands = Brand.query.all()

    for brand in all_brands:
      for model in brand.models:
        print "Brand %s has model %s %s." % (brand.name,
                                             model.year,
                                             model.name)
      print '\n'


    ### Solution before using db.ForeignKey and db.relationship

    # brand_model = db.session.query(Brand.name, 
    #                                Model.name,
    #                                Model.year).join(Model,
    #                                                 Brand.name == Model.brand_name).order_by(
    #                                                 Brand.name, Model.year).all()
    
    # # add year info as Brands issued same models for diff years
    # for brand, model, year in brand_model:
    #     print "Brand %s has model %s %s." % (brand, year, model)

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    matching_brands = Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()
    return matching_brands


def get_models_between(start_year, end_year):
    
    matching_models = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return matching_models

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

### My Answer ###

# The returned value is a BaseQuery object
# with a filtering criterion that Brand.name be equal to 'Ford' attached to 
# the object. The BaseQuery object subclasses from SQLAlchemy's Query class
# and has the standard query methods. The BaseQuery object is like a question that 
# can be trimmed down by adding more conditions and narrowing the scope, but on its own it does not
# return the answer directly. To get the answer, we should use a fetch method like all(), first(), one(),
# to execute on the question.

### End of My Answer ###

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

### My Answer ###

# The association table is an intermediary table that connects two tables that has
# a many-to-many relationship. The association table on its own does not have 
# interesting information other than storing primary keys from the other two tables and thus
# creating foreign keys in its own table that reference the other tables. 
# For the two tables connected by the association table, they can then build
# a relationship to each through the conduit of the association table, or via
# a "seconary" relationship with the association table.

### End of My Answer ###
