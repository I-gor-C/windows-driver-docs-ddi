---
UID: NA:
---

# Hidpddi.h header

## -description

This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Hidpddi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [HidP_GetCollectionDescription function](nf-hidpddi-hidp_getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_HIDP_COLLECTION_DESC structure](ns-hidpddi-_hidp_collection_desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_DEVICE_DESC structure](ns-hidpddi-_hidp_device_desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
| [_HIDP_GETCOLDESC_DBG structure](ns-hidpddi-_hidp_getcoldesc_dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_REPORT_IDS structure](ns-hidpddi-_hidp_report_ids.md) | Contains report ID information for a top-level collection. |
