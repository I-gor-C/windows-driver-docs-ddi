# Hidpddi.h header


This header is used by unknown technology.

Hidpddi.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [HidP_GetCollectionDescription function](nf-hidpddi-hidp-getcollectiondescription.md) | Fills a device description block with collection description and the corresponding report ID information for the specified report descriptor. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [HIDP_COLLECTION_DESC structure](ns-hidpddi--hidp-collection-desc.md) | Contains the information of a top-level-collection. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_DEVICE_DESC structure](ns-hidpddi--hidp-device-desc.md) | Contains the device description block filled in collection descriptions as linked lists. This structure is used by HidP_GetCollectionDescription. |
| [HIDP_GETCOLDESC_DBG structure](ns-hidpddi--hidp-getcoldesc-dbg.md) | Contains the error code indicating the failure in parsing the report descriptor. This structure is used in the HidP_GetCollectionDescription call. |
| [HIDP_REPORT_IDS structure](ns-hidpddi--hidp-report-ids.md) | Contains report ID information for a top-level collection. |
