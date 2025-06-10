# methods for various utility functions

def limit_m2m_field(m2m_field, limit=10):
    current_items = list(m2m_field.all())
    if len(current_items) > limit:
        m2m_field.remove(current_items[0])
        m2m_field.save()