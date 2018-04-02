---
UID: NF:ucmtypes.UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG
title: UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG function
author: windows-driver-content
description: Initializes a UCM_PD_REQUEST_DATA_OBJECT structure by interpreting Request Data Object values and sets each field correctly.
old-location: buses\ucm_pd_request_data_object_init_ulong.htm
old-project: usbref
ms.assetid: 825AA3FC-1D2E-4D71-8F21-C89A249B3F1A
ms.author: windowsdriverdev
ms.date: 3/29/2018
ms.keywords: UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG, UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG function [Buses], buses.ucm_pd_request_data_object_init_ulong, ucmtypes/UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ucmtypes.h
req.include-header: Ucmcx.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	Ucmtypes.h
api_name:
-	UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG
product:
- Windows
targetos: Windows
req.typenames: UCM_TYPEC_PARTNER
req.product: Windows 10 or later.
---


# UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG function
Initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/mt187942">UCM_PD_REQUEST_DATA_OBJECT</a>  structure by interpreting Request Data Object values and sets each field correctly.

## Syntax

```
void UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG(
  PUCM_PD_REQUEST_DATA_OBJECT Rdo,
  ULONG                       UlongInLittleEndian
);
```

## Parameters

`Rdo`

TBD

`UlongInLittleEndian`

The ULONG value to set in the <b>Ul</b> member of   <a href="https://msdn.microsoft.com/library/windows/hardware/mt187942">UCM_PD_REQUEST_DATA_OBJECT</a>.


## Return Value

This function does not return a value.

## Remarks

For information about Request Data Objects, see the Power Delivery specification. There are different types of Request Data Objects and the type depends on the Power Data Object that is specified in the <b>ObjectPosition</b> member of <a href="https://msdn.microsoft.com/library/windows/hardware/mt187942">UCM_PD_REQUEST_DATA_OBJECT</a>. The  source buffer is little-endian format and the client driver can memcopy the Request Data Objects from the hardware into an array of <b>UCM_PD_REQUEST_DATA_OBJECT</b> structures.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 10 Windows Server 2016 |
| **Target Platform** | Windows |
| **Minimum KMDF version** | 1.15 |
| **Minimum UMDF version** | 2.15 |
| **Header** | ucmtypes.h (include Ucmcx.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/mt187942">UCM_PD_REQUEST_DATA_OBJECT</a>