---
UID : NS:iddcx.IDDCX_MONITOR_DESCRIPTION
title : IDDCX_MONITOR_DESCRIPTION
author : windows-driver-content
description : Gives information about the current monitor description.
old-location : display\iddcx_monitor_description.htm
old-project : display
ms.assetid : 3ef7ffca-9192-4578-8397-c7fbb2ea2239
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : display.iddcx_monitor_description, iddcx/IDDCX_MONITOR_DESCRIPTION, IDDCX_MONITOR_DESCRIPTION, IDDCX_MONITOR_DESCRIPTION structure [Display Devices]
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : iddcx.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : 
---

# IDDCX_MONITOR_DESCRIPTION structure
Gives information about the current monitor description.

## Syntax
````
typedef struct IDDCX_MONITOR_DESCRIPTION {
  UINT                              Size;
  IDDCX_MONITOR_DESCRIPTION_TYPE    Type;
  UINT                              DataSize;
  _Field_size_full_(DataSize) PVOID pData;
} IDDCX_MONITOR_DESCRIPTION, *IDDCX_MONITOR_DESCRIPTION;
````

## Members


`DataSize`

The size of the monitor description data.

`pData`

Pointer to the monitor description data.

`Size`

Total size of the structure.

`Type`

Type of this monitor description.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | iddcx.h |