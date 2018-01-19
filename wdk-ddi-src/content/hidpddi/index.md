---
UID : NA:hidpddi
ms.assetid : 4eebcc15-de7e-3d7d-b3d9-c8f7b86b35cb
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# hidpddi.h header



hidpddi.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [HidP_GetCollectionDescription](nf-hidpddi-hidp_getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |



## Structures
| Title | Description |
| ---- |:---- |
| [_HIDP_COLLECTION_DESC](ns-hidpddi-_hidp_collection_desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_DEVICE_DESC](ns-hidpddi-_hidp_device_desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
| [_HIDP_GETCOLDESC_DBG](ns-hidpddi-_hidp_getcoldesc_dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [_HIDP_REPORT_IDS](ns-hidpddi-_hidp_report_ids.md) | Contains report ID information for a top-level collection. |