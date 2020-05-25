from sqlalchemy.exc import IntegrityError
from .models import Property, PropertySelection
from .dbsession import Session


def _property_dict(prop):
    return {
        'id': prop.id,
        'fullAddress': prop.full_address,
        'classDescription': prop.class_description,
    }


def complete(text, limit):
    session = Session()
    results = (session.query(Property)
        .outerjoin(PropertySelection)
        .filter(PropertySelection.property_id == None)
        .filter(Property.full_address.startswith(text))
        .limit(limit))
    return [_property_dict(r) for r in results]


def selections(limit=10, offset=0):
    session = Session()
    results = (session.query(PropertySelection)
        .join(PropertySelection.property)
        .limit(limit)
        .offset(offset))
    return [_property_dict(r.property) for r in results]


def add_selection(property_id):
    session = Session()
    try:
        session.add(PropertySelection(property_id=property_id))
        session.commit()
        return True
    except IntegrityError:
        return False


def delete_selection(property_id):
    session = Session()
    selection = session.query(PropertySelection).filter_by(property_id=property_id)
    count = selection.delete()
    session.commit()
    return bool(count)

