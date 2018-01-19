---
UID : NC:wdfcompanion.EVT_WDF_COMPANION_PRE_D0_ENTRY
title : EVT_WDF_COMPANION_PRE_D0_ENTRY
author : windows-driver-content
description : For internal use only.
old-location : wdf\evt_wdf_companion_pre_d0_entry.htm
old-project : wdf
ms.assetid : 18d55cf3-62c3-42e8-8c33-f61ea80ff680
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : _WDF_COMMON_BUFFER_CONFIG, *PWDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : callback
req.header : wdfcompanion.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 2.23
req.alt-api : EVT_WDF_COMPANION_PRE_D0_ENTRY
req.alt-loc : wdfcompanion.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : "*PWDF_COMMON_BUFFER_CONFIG, WDF_COMMON_BUFFER_CONFIG"
req.product : Windows 10 or later.
---


# EVT_WDF_COMPANION_PRE_D0_ENTRY function
For internal use only.

## Syntax

```
EVT_WDF_COMPANION_PRE_D0_ENTRY EvtWdfCompanionPreD0Entry;

NTSTATUS EvtWdfCompanionPreD0Entry(
  WDFCOMPANION Companion,
  WDF_POWER_DEVICE_STATE PreviousState
)
{...}
```

## Parameters

`Companion`



`PreviousState`




## Return Value

None


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Windows |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** | 2.23 |
| **Header** | wdfcompanion.h |
| **Library** |  |
| **IRQL** | PASSIVE_LEVEL |
| **DDI compliance rules** |  |