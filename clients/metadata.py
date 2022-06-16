from dataclasses import dataclass
from django import List
from allauth.account.forms import SignupForm



@dataclass
class ProductMetadata(object):
    """
    Metadata for a Stripe product.
    """
    stripe_id: str
    name: str
    features: List[str]
    description: str = ''
    is_default: bool = False


STARTER_PLAN = ProductMetadata(
    stripe_id='prod_LKq59hozqYcK7I',
    name='Starter plan',
    description='1 person',
    is_default=False,
    features=[
      
    ],
)
# other plans go here