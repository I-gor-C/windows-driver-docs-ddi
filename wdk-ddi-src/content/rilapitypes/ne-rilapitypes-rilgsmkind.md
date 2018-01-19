---
UID : NE:rilapitypes.RILGSMKIND
title : RILGSMKIND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgsmkind_2.htm
old-project : netvista
ms.assetid : ec02cb5a-78e4-411b-945c-2ded798720e6
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILGSMKIND, RILGSMKIND
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
req.alt-api : RILGSMKIND
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
req.typenames : RILGSMKIND
req.product : Windows 10 or later.
---

# RILGSMKIND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILGSMKIND { 
  RIL_GSMKIND_GPRS,
  RIL_GSMKIND_EDGE,
  RIL_GSMKIND_MAX
} RILGSMKIND;
````

## Constants

<table>

<tr>
<td>RIL_GSMKIND_EDGE</td>
<td></td>
</tr>

<tr>
<td>RIL_GSMKIND_GPRS</td>
<td></td>
</tr>

<tr>
<td>RIL_GSMKIND_MAX</td>
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