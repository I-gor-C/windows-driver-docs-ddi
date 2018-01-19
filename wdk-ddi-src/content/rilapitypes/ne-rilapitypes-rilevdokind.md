---
UID : NE:rilapitypes.RILEVDOKIND
title : RILEVDOKIND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilevdokind_2.htm
old-project : netvista
ms.assetid : df59e0f7-6e78-4098-9a2a-9a3143d66152
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILEVDOKIND, RILEVDOKIND
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : rilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILEVDOKIND
req.alt-loc : rilapitypes.h
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
req.typenames : RILEVDOKIND
req.product : Windows 10 or later.
---

# RILEVDOKIND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEVDOKIND { 
  RIL_EVDOKIND_REVA,
  RIL_EVDOKIND_REVB,
  RIL_EVDOKIND_MAX
} RILEVDOKIND;
````

## Constants

<table>

<tr>
<td>RIL_EVDOKIND_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_EVDOKIND_REVA</td>
<td></td>
</tr>

<tr>
<td>RIL_EVDOKIND_REVB</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |