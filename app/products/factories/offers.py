from app.products.dtos.offers import OfferDTO
from app.products.models import Offer, OfferParam, OfferPicture, Product


class OfferFactory:
    def __init__(self):
        self.manager = Offer.objects
        self.offer_picture_manager = OfferPicture.objects
        self.offer_param_manager = OfferParam.objects

    def create(self, offer_dto: OfferDTO, product: Product) -> Offer:
        try:
            offer = self.manager.get(id=offer_dto.id)
            offer.name = offer_dto.name
            offer.simular = offer_dto.simular
            offer.price = offer_dto.price
            offer.price_begin = offer_dto.price_begin
            offer.percent = offer_dto.percent
            offer.vat = offer_dto.vat
            offer.vendor_code = offer_dto.vendor_code
            offer.description = offer_dto.description
            offer.barcode = offer_dto.barcode
            offer.product = product
            offer.save()
        except Offer.DoesNotExist:
            offer = self.manager.create(
                id=offer_dto.id,
                name=offer_dto.name,
                simular=offer_dto.simular,
                price=offer_dto.price,
                price_begin=offer_dto.price_begin,
                percent=offer_dto.percent,
                vat=offer_dto.vat,
                vendor_code=offer_dto.vendor_code,
                description=offer_dto.description,
                barcode=offer_dto.barcode,
                product=product,
            )
        for picture_url in offer_dto.pictures:
            self._create_picture(picture_url, offer)
        for param_key, param_value in offer_dto.params.items():
            self._create_param(param_key, param_value, offer)
        return offer

    def _create_picture(self, picture_url, offer):
        self.offer_picture_manager.get_or_create(offer=offer, url=picture_url)

    def _create_param(self, key, value, offer):
        try:
            offer_param = self.offer_param_manager.get(offer=offer, name=key)
            offer_param.value = value
            offer_param.save()
        except OfferParam.DoesNotExist:
            self.offer_param_manager.create(offer=offer, name=key, value=value)
