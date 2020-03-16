# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_econ.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_econ.proto',
  package='',
  syntax='proto2',
  serialized_options=b'\220\001\001',
  serialized_pb=b'\n\x18steammessages_econ.proto\x1a steammessages_unified_base.proto\"D\n&CEcon_GetTradeOfferAccessToken_Request\x12\x1a\n\x12generate_new_token\x18\x01 \x01(\x08\"K\n\'CEcon_GetTradeOfferAccessToken_Response\x12 \n\x18trade_offer_access_token\x18\x01 \x01(\t\"C\n-CEcon_ClientGetItemShopOverlayAuthURL_Request\x12\x12\n\nreturn_url\x18\x01 \x01(\t\"=\n.CEcon_ClientGetItemShopOverlayAuthURL_Response\x12\x0b\n\x03url\x18\x01 \x01(\t\"\xa9\x01\n\x1f\x43\x45\x63on_GetAssetClassInfo_Request\x12\x10\n\x08language\x18\x01 \x01(\t\x12\r\n\x05\x61ppid\x18\x02 \x01(\r\x12\x37\n\x07\x63lasses\x18\x03 \x03(\x0b\x32&.CEcon_GetAssetClassInfo_Request.Class\x1a,\n\x05\x43lass\x12\x0f\n\x07\x63lassid\x18\x01 \x01(\x04\x12\x12\n\ninstanceid\x18\x02 \x01(\x04\"V\n\x19\x43\x45\x63onItem_DescriptionLine\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\".\n\x10\x43\x45\x63onItem_Action\x12\x0c\n\x04link\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"\x92\x06\n\x15\x43\x45\x63onItem_Description\x12\r\n\x05\x61ppid\x18\x01 \x01(\x05\x12\x0f\n\x07\x63lassid\x18\x02 \x01(\x04\x12\x12\n\ninstanceid\x18\x03 \x01(\x04\x12\x10\n\x08\x63urrency\x18\x04 \x01(\x08\x12\x18\n\x10\x62\x61\x63kground_color\x18\x05 \x01(\t\x12\x10\n\x08icon_url\x18\x06 \x01(\t\x12\x16\n\x0eicon_url_large\x18\x07 \x01(\t\x12\x30\n\x0c\x64\x65scriptions\x18\x08 \x03(\x0b\x32\x1a.CEconItem_DescriptionLine\x12\x10\n\x08tradable\x18\t \x01(\x08\x12\"\n\x07\x61\x63tions\x18\n \x03(\x0b\x32\x11.CEconItem_Action\x12\x36\n\x12owner_descriptions\x18\x0b \x03(\x0b\x32\x1a.CEconItem_DescriptionLine\x12(\n\rowner_actions\x18\x0c \x03(\x0b\x32\x11.CEconItem_Action\x12\x15\n\rfraudwarnings\x18\r \x03(\t\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x12\n\nname_color\x18\x0f \x01(\t\x12\x0c\n\x04type\x18\x10 \x01(\t\x12\x13\n\x0bmarket_name\x18\x11 \x01(\t\x12\x18\n\x10market_hash_name\x18\x12 \x01(\t\x12\x12\n\nmarket_fee\x18\x13 \x01(\t\x12\x16\n\x0emarket_fee_app\x18\x1c \x01(\x05\x12.\n\x0e\x63ontained_item\x18\x14 \x01(\x0b\x32\x16.CEconItem_Description\x12)\n\x0emarket_actions\x18\x15 \x03(\x0b\x32\x11.CEconItem_Action\x12\x11\n\tcommodity\x18\x16 \x01(\x08\x12#\n\x1bmarket_tradable_restriction\x18\x17 \x01(\x05\x12%\n\x1dmarket_marketable_restriction\x18\x18 \x01(\x05\x12\x12\n\nmarketable\x18\x19 \x01(\x08\x12\x1c\n\x04tags\x18\x1a \x03(\x0b\x32\x0e.CEconItem_Tag\x12\x17\n\x0fitem_expiration\x18\x1b \x01(\t\"\x98\x03\n\rCEconItem_Tag\x12\x31\n\x05\x61ppid\x18\x01 \x01(\rB\"\x82\xb5\x18\x1eThe app that contains the item\x12J\n\x08\x63\x61tegory\x18\x02 \x01(\tB8\x82\xb5\x18\x34The internal name of the category the tag belongs to\x12\x37\n\rinternal_name\x18\x03 \x01(\tB \x82\xb5\x18\x1cThe internal name of the tag\x12G\n\x17localized_category_name\x18\x04 \x01(\tB&\x82\xb5\x18\"The localized name of the category\x12=\n\x12localized_tag_name\x18\x05 \x01(\tB!\x82\xb5\x18\x1dThe localized name of the tag\x12G\n\x05\x63olor\x18\x06 \x01(\tB8\x82\xb5\x18\x34The color to use when displaying the tag to the user\"P\n CEcon_GetAssetClassInfo_Response\x12,\n\x0c\x64\x65scriptions\x18\x01 \x03(\x0b\x32\x16.CEconItem_Description2\xe2\x04\n\x04\x45\x63on\x12\x9a\x01\n\x18GetTradeOfferAccessToken\x12\'.CEcon_GetTradeOfferAccessToken_Request\x1a(.CEcon_GetTradeOfferAccessToken_Response\"+\x82\xb5\x18\'Get the user\'s trade offer access token\x12\xd9\x01\n\x1f\x43lientGetItemShopOverlayAuthURL\x12..CEcon_ClientGetItemShopOverlayAuthURL_Request\x1a/.CEcon_ClientGetItemShopOverlayAuthURL_Response\"U\x82\xb5\x18QGenerates a URL which sets a secure cookie for in-game-browser itemshop purchases\x12\x9f\x01\n\x11GetAssetClassInfo\x12 .CEcon_GetAssetClassInfo_Request\x1a!.CEcon_GetAssetClassInfo_Response\"E\x82\xb5\x18\x41Returns description information about the passed in asset classes\x1a?\x82\xb5\x18;A service that provides communication with the econ serversB\x03\x90\x01\x01'
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])




_CECON_GETTRADEOFFERACCESSTOKEN_REQUEST = _descriptor.Descriptor(
  name='CEcon_GetTradeOfferAccessToken_Request',
  full_name='CEcon_GetTradeOfferAccessToken_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='generate_new_token', full_name='CEcon_GetTradeOfferAccessToken_Request.generate_new_token', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=130,
)


_CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE = _descriptor.Descriptor(
  name='CEcon_GetTradeOfferAccessToken_Response',
  full_name='CEcon_GetTradeOfferAccessToken_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trade_offer_access_token', full_name='CEcon_GetTradeOfferAccessToken_Response.trade_offer_access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=207,
)


_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST = _descriptor.Descriptor(
  name='CEcon_ClientGetItemShopOverlayAuthURL_Request',
  full_name='CEcon_ClientGetItemShopOverlayAuthURL_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_url', full_name='CEcon_ClientGetItemShopOverlayAuthURL_Request.return_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=276,
)


_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE = _descriptor.Descriptor(
  name='CEcon_ClientGetItemShopOverlayAuthURL_Response',
  full_name='CEcon_ClientGetItemShopOverlayAuthURL_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='CEcon_ClientGetItemShopOverlayAuthURL_Response.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=339,
)


_CECON_GETASSETCLASSINFO_REQUEST_CLASS = _descriptor.Descriptor(
  name='Class',
  full_name='CEcon_GetAssetClassInfo_Request.Class',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='classid', full_name='CEcon_GetAssetClassInfo_Request.Class.classid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceid', full_name='CEcon_GetAssetClassInfo_Request.Class.instanceid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=511,
)

_CECON_GETASSETCLASSINFO_REQUEST = _descriptor.Descriptor(
  name='CEcon_GetAssetClassInfo_Request',
  full_name='CEcon_GetAssetClassInfo_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='CEcon_GetAssetClassInfo_Request.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='appid', full_name='CEcon_GetAssetClassInfo_Request.appid', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classes', full_name='CEcon_GetAssetClassInfo_Request.classes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CECON_GETASSETCLASSINFO_REQUEST_CLASS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=511,
)


_CECONITEM_DESCRIPTIONLINE = _descriptor.Descriptor(
  name='CEconItem_DescriptionLine',
  full_name='CEconItem_DescriptionLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CEconItem_DescriptionLine.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CEconItem_DescriptionLine.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='CEconItem_DescriptionLine.color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label', full_name='CEconItem_DescriptionLine.label', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=513,
  serialized_end=599,
)


_CECONITEM_ACTION = _descriptor.Descriptor(
  name='CEconItem_Action',
  full_name='CEconItem_Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='CEconItem_Action.link', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='CEconItem_Action.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=601,
  serialized_end=647,
)


_CECONITEM_DESCRIPTION = _descriptor.Descriptor(
  name='CEconItem_Description',
  full_name='CEconItem_Description',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CEconItem_Description.appid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='classid', full_name='CEconItem_Description.classid', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instanceid', full_name='CEconItem_Description.instanceid', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='CEconItem_Description.currency', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_color', full_name='CEconItem_Description.background_color', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_url', full_name='CEconItem_Description.icon_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_url_large', full_name='CEconItem_Description.icon_url_large', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descriptions', full_name='CEconItem_Description.descriptions', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradable', full_name='CEconItem_Description.tradable', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actions', full_name='CEconItem_Description.actions', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner_descriptions', full_name='CEconItem_Description.owner_descriptions', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner_actions', full_name='CEconItem_Description.owner_actions', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fraudwarnings', full_name='CEconItem_Description.fraudwarnings', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='CEconItem_Description.name', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_color', full_name='CEconItem_Description.name_color', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='CEconItem_Description.type', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_name', full_name='CEconItem_Description.market_name', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_hash_name', full_name='CEconItem_Description.market_hash_name', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_fee', full_name='CEconItem_Description.market_fee', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_fee_app', full_name='CEconItem_Description.market_fee_app', index=19,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contained_item', full_name='CEconItem_Description.contained_item', index=20,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_actions', full_name='CEconItem_Description.market_actions', index=21,
      number=21, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commodity', full_name='CEconItem_Description.commodity', index=22,
      number=22, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_tradable_restriction', full_name='CEconItem_Description.market_tradable_restriction', index=23,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='market_marketable_restriction', full_name='CEconItem_Description.market_marketable_restriction', index=24,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketable', full_name='CEconItem_Description.marketable', index=25,
      number=25, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='CEconItem_Description.tags', index=26,
      number=26, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_expiration', full_name='CEconItem_Description.item_expiration', index=27,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=650,
  serialized_end=1436,
)


_CECONITEM_TAG = _descriptor.Descriptor(
  name='CEconItem_Tag',
  full_name='CEconItem_Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appid', full_name='CEconItem_Tag.appid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\036The app that contains the item', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='CEconItem_Tag.category', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\0304The internal name of the category the tag belongs to', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_name', full_name='CEconItem_Tag.internal_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\034The internal name of the tag', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localized_category_name', full_name='CEconItem_Tag.localized_category_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\"The localized name of the category', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localized_tag_name', full_name='CEconItem_Tag.localized_tag_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\030\035The localized name of the tag', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='CEconItem_Tag.color', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\202\265\0304The color to use when displaying the tag to the user', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1439,
  serialized_end=1847,
)


_CECON_GETASSETCLASSINFO_RESPONSE = _descriptor.Descriptor(
  name='CEcon_GetAssetClassInfo_Response',
  full_name='CEcon_GetAssetClassInfo_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descriptions', full_name='CEcon_GetAssetClassInfo_Response.descriptions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1849,
  serialized_end=1929,
)

_CECON_GETASSETCLASSINFO_REQUEST_CLASS.containing_type = _CECON_GETASSETCLASSINFO_REQUEST
_CECON_GETASSETCLASSINFO_REQUEST.fields_by_name['classes'].message_type = _CECON_GETASSETCLASSINFO_REQUEST_CLASS
_CECONITEM_DESCRIPTION.fields_by_name['descriptions'].message_type = _CECONITEM_DESCRIPTIONLINE
_CECONITEM_DESCRIPTION.fields_by_name['actions'].message_type = _CECONITEM_ACTION
_CECONITEM_DESCRIPTION.fields_by_name['owner_descriptions'].message_type = _CECONITEM_DESCRIPTIONLINE
_CECONITEM_DESCRIPTION.fields_by_name['owner_actions'].message_type = _CECONITEM_ACTION
_CECONITEM_DESCRIPTION.fields_by_name['contained_item'].message_type = _CECONITEM_DESCRIPTION
_CECONITEM_DESCRIPTION.fields_by_name['market_actions'].message_type = _CECONITEM_ACTION
_CECONITEM_DESCRIPTION.fields_by_name['tags'].message_type = _CECONITEM_TAG
_CECON_GETASSETCLASSINFO_RESPONSE.fields_by_name['descriptions'].message_type = _CECONITEM_DESCRIPTION
DESCRIPTOR.message_types_by_name['CEcon_GetTradeOfferAccessToken_Request'] = _CECON_GETTRADEOFFERACCESSTOKEN_REQUEST
DESCRIPTOR.message_types_by_name['CEcon_GetTradeOfferAccessToken_Response'] = _CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE
DESCRIPTOR.message_types_by_name['CEcon_ClientGetItemShopOverlayAuthURL_Request'] = _CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST
DESCRIPTOR.message_types_by_name['CEcon_ClientGetItemShopOverlayAuthURL_Response'] = _CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE
DESCRIPTOR.message_types_by_name['CEcon_GetAssetClassInfo_Request'] = _CECON_GETASSETCLASSINFO_REQUEST
DESCRIPTOR.message_types_by_name['CEconItem_DescriptionLine'] = _CECONITEM_DESCRIPTIONLINE
DESCRIPTOR.message_types_by_name['CEconItem_Action'] = _CECONITEM_ACTION
DESCRIPTOR.message_types_by_name['CEconItem_Description'] = _CECONITEM_DESCRIPTION
DESCRIPTOR.message_types_by_name['CEconItem_Tag'] = _CECONITEM_TAG
DESCRIPTOR.message_types_by_name['CEcon_GetAssetClassInfo_Response'] = _CECON_GETASSETCLASSINFO_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CEcon_GetTradeOfferAccessToken_Request = _reflection.GeneratedProtocolMessageType('CEcon_GetTradeOfferAccessToken_Request', (_message.Message,), {
  'DESCRIPTOR' : _CECON_GETTRADEOFFERACCESSTOKEN_REQUEST,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_GetTradeOfferAccessToken_Request)
  })
_sym_db.RegisterMessage(CEcon_GetTradeOfferAccessToken_Request)

CEcon_GetTradeOfferAccessToken_Response = _reflection.GeneratedProtocolMessageType('CEcon_GetTradeOfferAccessToken_Response', (_message.Message,), {
  'DESCRIPTOR' : _CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_GetTradeOfferAccessToken_Response)
  })
_sym_db.RegisterMessage(CEcon_GetTradeOfferAccessToken_Response)

CEcon_ClientGetItemShopOverlayAuthURL_Request = _reflection.GeneratedProtocolMessageType('CEcon_ClientGetItemShopOverlayAuthURL_Request', (_message.Message,), {
  'DESCRIPTOR' : _CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_ClientGetItemShopOverlayAuthURL_Request)
  })
_sym_db.RegisterMessage(CEcon_ClientGetItemShopOverlayAuthURL_Request)

CEcon_ClientGetItemShopOverlayAuthURL_Response = _reflection.GeneratedProtocolMessageType('CEcon_ClientGetItemShopOverlayAuthURL_Response', (_message.Message,), {
  'DESCRIPTOR' : _CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_ClientGetItemShopOverlayAuthURL_Response)
  })
_sym_db.RegisterMessage(CEcon_ClientGetItemShopOverlayAuthURL_Response)

CEcon_GetAssetClassInfo_Request = _reflection.GeneratedProtocolMessageType('CEcon_GetAssetClassInfo_Request', (_message.Message,), {

  'Class' : _reflection.GeneratedProtocolMessageType('Class', (_message.Message,), {
    'DESCRIPTOR' : _CECON_GETASSETCLASSINFO_REQUEST_CLASS,
    '__module__' : 'steammessages_econ_pb2'
    # @@protoc_insertion_point(class_scope:CEcon_GetAssetClassInfo_Request.Class)
    })
  ,
  'DESCRIPTOR' : _CECON_GETASSETCLASSINFO_REQUEST,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_GetAssetClassInfo_Request)
  })
_sym_db.RegisterMessage(CEcon_GetAssetClassInfo_Request)
_sym_db.RegisterMessage(CEcon_GetAssetClassInfo_Request.Class)

CEconItem_DescriptionLine = _reflection.GeneratedProtocolMessageType('CEconItem_DescriptionLine', (_message.Message,), {
  'DESCRIPTOR' : _CECONITEM_DESCRIPTIONLINE,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEconItem_DescriptionLine)
  })
_sym_db.RegisterMessage(CEconItem_DescriptionLine)

CEconItem_Action = _reflection.GeneratedProtocolMessageType('CEconItem_Action', (_message.Message,), {
  'DESCRIPTOR' : _CECONITEM_ACTION,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEconItem_Action)
  })
_sym_db.RegisterMessage(CEconItem_Action)

CEconItem_Description = _reflection.GeneratedProtocolMessageType('CEconItem_Description', (_message.Message,), {
  'DESCRIPTOR' : _CECONITEM_DESCRIPTION,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEconItem_Description)
  })
_sym_db.RegisterMessage(CEconItem_Description)

CEconItem_Tag = _reflection.GeneratedProtocolMessageType('CEconItem_Tag', (_message.Message,), {
  'DESCRIPTOR' : _CECONITEM_TAG,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEconItem_Tag)
  })
_sym_db.RegisterMessage(CEconItem_Tag)

CEcon_GetAssetClassInfo_Response = _reflection.GeneratedProtocolMessageType('CEcon_GetAssetClassInfo_Response', (_message.Message,), {
  'DESCRIPTOR' : _CECON_GETASSETCLASSINFO_RESPONSE,
  '__module__' : 'steammessages_econ_pb2'
  # @@protoc_insertion_point(class_scope:CEcon_GetAssetClassInfo_Response)
  })
_sym_db.RegisterMessage(CEcon_GetAssetClassInfo_Response)


DESCRIPTOR._options = None
_CECONITEM_TAG.fields_by_name['appid']._options = None
_CECONITEM_TAG.fields_by_name['category']._options = None
_CECONITEM_TAG.fields_by_name['internal_name']._options = None
_CECONITEM_TAG.fields_by_name['localized_category_name']._options = None
_CECONITEM_TAG.fields_by_name['localized_tag_name']._options = None
_CECONITEM_TAG.fields_by_name['color']._options = None

_ECON = _descriptor.ServiceDescriptor(
  name='Econ',
  full_name='Econ',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\202\265\030;A service that provides communication with the econ servers',
  serialized_start=1932,
  serialized_end=2542,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTradeOfferAccessToken',
    full_name='Econ.GetTradeOfferAccessToken',
    index=0,
    containing_service=None,
    input_type=_CECON_GETTRADEOFFERACCESSTOKEN_REQUEST,
    output_type=_CECON_GETTRADEOFFERACCESSTOKEN_RESPONSE,
    serialized_options=b'\202\265\030\'Get the user\'s trade offer access token',
  ),
  _descriptor.MethodDescriptor(
    name='ClientGetItemShopOverlayAuthURL',
    full_name='Econ.ClientGetItemShopOverlayAuthURL',
    index=1,
    containing_service=None,
    input_type=_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_REQUEST,
    output_type=_CECON_CLIENTGETITEMSHOPOVERLAYAUTHURL_RESPONSE,
    serialized_options=b'\202\265\030QGenerates a URL which sets a secure cookie for in-game-browser itemshop purchases',
  ),
  _descriptor.MethodDescriptor(
    name='GetAssetClassInfo',
    full_name='Econ.GetAssetClassInfo',
    index=2,
    containing_service=None,
    input_type=_CECON_GETASSETCLASSINFO_REQUEST,
    output_type=_CECON_GETASSETCLASSINFO_RESPONSE,
    serialized_options=b'\202\265\030AReturns description information about the passed in asset classes',
  ),
])
_sym_db.RegisterServiceDescriptor(_ECON)

DESCRIPTOR.services_by_name['Econ'] = _ECON

Econ = service_reflection.GeneratedServiceType('Econ', (_service.Service,), dict(
  DESCRIPTOR = _ECON,
  __module__ = 'steammessages_econ_pb2'
  ))

Econ_Stub = service_reflection.GeneratedServiceStubType('Econ_Stub', (Econ,), dict(
  DESCRIPTOR = _ECON,
  __module__ = 'steammessages_econ_pb2'
  ))


# @@protoc_insertion_point(module_scope)
