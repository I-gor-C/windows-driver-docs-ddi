---
UID: NA:wiamindr_lh
ms.assetid: 8bb4455b-7b9a-3281-8f57-256069118040
ms.author: windowsdriverdev
ms.date: 03/13/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# Wiamindr_Lh.h header



This header is used by Imaging devices. For more information, see
- [Imaging devices](../_image/index.md)

Wiamindr_Lh.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_MINIDRV_TRANSFER_CONTEXT structure](ns-wiamindr_lh-_minidrv_transfer_context.md) | The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer. |
| [_WIAS_CHANGED_VALUE_INFO structure](ns-wiamindr_lh-_wias_changed_value_info.md) | The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property. |
| [_WIAS_DOWN_SAMPLE_INFO structure](ns-wiamindr_lh-_wias_down_sample_info.md) | The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer. |
| [_WIAS_ENDORSER_INFO structure](ns-wiamindr_lh-_wias_endorser_info.md) | The WIAS_ENDORSER_INFO structure holds custom endorser token/value pairs. |
| [_WIAS_ENDORSER_VALUE structure](ns-wiamindr_lh-_wias_endorser_value.md) | The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings. |
| [_WIA_DEV_CAP_DRV structure](ns-wiamindr_lh-_wia_dev_cap_drv.md) | The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports. |
| [_WIA_PROPERTY_CONTEXT structure](ns-wiamindr_lh-_wia_property_context.md) | The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. |
| [_WIA_PROPERTY_INFO structure](ns-wiamindr_lh-_wia_property_info.md) | The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type. |

## Interfaces

| Title   | Description   |
| ---- |:---- |
| [IWiaDrvItem interface](nn-wiamindr_lh-iwiadrvitem.md) | The IWiaDrvItem interface provides methods that a WIA minidriver can use to manage a tree of IWiaDrvItem items. |
| [IWiaMiniDrv interface](nn-wiamindr_lh-iwiaminidrv.md) | The IWiaMiniDrv interface provides the methods that are the entry points for all communication between the minidriver and the WIA service. These methods allow the WIA service to control the device. |
| [IWiaMiniDrvCallBack interface](nn-wiamindr_lh-iwiaminidrvcallback.md) | The IWiaMiniDrvCallBack interface provides the MiniDrvCallback method, which enables minidrivers to transfer image header data and image data from the imaging device to the WIA service. |
| [IWiaMiniDrvTransferCallback interface](nn-wiamindr_lh-iwiaminidrvtransfercallback.md) | This is a Callback interface that is called by the WIA mini-driver for stream-based transfers. |

## Methods

| Title   | Description   |
| ---- |:----

# wiamindr_lh.h header



wiamindr_lh.h contains the following programming interfaces:



## Interfaces
| Title | Description |
| ---- |:---- |
| [IWiaDrvItem](nn-wiamindr_lh-iwiadrvitem.md) | The IWiaDrvItem interface provides methods that a WIA minidriver can use to manage a tree of IWiaDrvItem items. |
| [IWiaMiniDrv](nn-wiamindr_lh-iwiaminidrv.md) | The IWiaMiniDrv interface provides the methods that are the entry points for all communication between the minidriver and the WIA service. These methods allow the WIA service to control the device. |
| [IWiaMiniDrvCallBack](nn-wiamindr_lh-iwiaminidrvcallback.md) | The IWiaMiniDrvCallBack interface provides the MiniDrvCallback method, which enables minidrivers to transfer image header data and image data from the imaging device to the WIA service. |
| [IWiaMiniDrvTransferCallback](nn-wiamindr_lh-iwiaminidrvtransfercallback.md) | This is a Callback interface that is called by the WIA mini-driver for stream-based transfers. |





## Structures
| Title | Description |
| ---- |:---- |
| [_MINIDRV_TRANSFER_CONTEXT](ns-wiamindr_lh-_minidrv_transfer_context.md) | The MINIDRV_TRANSFER_CONTEXT structure is used to store image and other information needed for a memory-callback data transfer or a file data transfer. |
| [_WIA_DEV_CAP_DRV](ns-wiamindr_lh-_wia_dev_cap_drv.md) | The WIA_DEV_CAP_DRV structure is used to enumerate device capabilities. A device capability is defined by an event or command that the device supports. |
| [_WIA_PROPERTY_CONTEXT](ns-wiamindr_lh-_wia_property_context.md) | The WIA_PROPERTY_CONTEXT structure stores property identifiers and their context. |
| [_WIA_PROPERTY_INFO](ns-wiamindr_lh-_wia_property_info.md) | The WIA_PROPERTY_INFO structure is used to store default access and valid value information for an item property of arbitrary type. |
| [_WIAS_CHANGED_VALUE_INFO](ns-wiamindr_lh-_wias_changed_value_info.md) | The WIAS_CHANGED_VALUE_INFO structure is used to store the current and previous values of a property. |
| [_WIAS_DOWN_SAMPLE_INFO](ns-wiamindr_lh-_wias_down_sample_info.md) | The WIAS_DOWN_SAMPLE_INFO structure stores information used by the downsampling helper function, wiasDownSampleBuffer. |
| [_WIAS_ENDORSER_INFO](ns-wiamindr_lh-_wias_endorser_info.md) | The WIAS_ENDORSER_INFO structure holds custom endorser token/value pairs. |
| [_WIAS_ENDORSER_VALUE](ns-wiamindr_lh-_wias_endorser_value.md) | The WIAS_ENDORSER_VALUE structure stores token/value pairs for endorser strings. |