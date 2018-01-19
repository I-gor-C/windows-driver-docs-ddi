---
UID : NA:dxapi
ms.assetid : e45b4941-1567-3e35-b90e-c4b63e233061
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# dxapi.h header



dxapi.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [DxApi](nf-dxapi-dxapi.md) | The DxApi function accepts commands from the hardware decoder's video capture driver to access the DxApi interface functions that are implemented in a video miniport driver. |
| [DxApiGetVersion](nf-dxapi-dxapigetversion.md) | Do not use the DxApiGetVersion function; use the DxApi function along with the DD_DXAPI_GETVERSIONNUMBER function identifier instead.The DxApiGetVersion function returns a Direct Sound version number of 4.02. |