from store.schemas.product import ProductIn
from uuid import UUID
import pytest
from pydantic import ValidationError
from tests.factories import product_data


def test_schemas_return_sucess():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert product.name == "MacBook Pro M2"
    assert isinstance(product.id, UUID)


def test_schemas_return_raise():
    data = {"name": "MacBook Pro M2", "quantity": 5, "price": 12.000}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "MacBook Pro M2", "quantity": 5, "price": 12.0},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }
