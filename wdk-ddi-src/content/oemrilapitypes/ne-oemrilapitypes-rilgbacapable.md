---
UID : NE:oemrilapitypes.RILGBACAPABLE
title : RILGBACAPABLE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgbacapable.htm
old-project : netvista
ms.assetid : c1acc574-6e9e-40a1-8892-00572fcc545c
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_GBA_UNKNOWN, RILGBACAPABLE enumeration [Network Drivers Starting with Windows Vista], oemrilapitypes/RIL_GBA_UNKNOWN, oemrilapitypes/RIL_GBA_ME_SUPPORTED, RIL_GBA_U_SUPPORTED, RILGBACAPABLE, RIL_GBA_ME_SUPPORTED, oemrilapitypes/RIL_GBA_NOT_SUPPORTED, oemrilapitypes/RIL_GBA_U_SUPPORTED, RIL_GBA_NOT_SUPPORTED, netvista.rilgbacapable, oemrilapitypes/RILGBACAPABLE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : oemrilapitypes.h
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
req.lib : Ntstrsafe.lib
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILGBACAPABLE
---

# RILGBACAPABLE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILGBACAPABLE { 
  RIL_GBA_UNKNOWN,
  RIL_GBA_NOT_SUPPORTED,
  RIL_GBA_ME_SUPPORTED,
  RIL_GBA_U_SUPPORTED
} RILGBACAPABLE;
````

## Constants

<table>

<tr>
<td>RIL_GBA_ME_SUPPORTED</td>
<td></td>
</tr>

<tr>
<td>RIL_GBA_NOT_SUPPORTED</td>
<td></td>
</tr>

<tr>
<td>RIL_GBA_U_SUPPORTED</td>
<td></td>
</tr>

<tr>
<td>RIL_GBA_UNKNOWN</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | oemrilapitypes.h |