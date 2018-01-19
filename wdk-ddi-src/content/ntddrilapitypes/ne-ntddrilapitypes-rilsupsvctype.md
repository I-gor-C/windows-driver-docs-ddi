---
UID : NE:ntddrilapitypes.RILSUPSVCTYPE
title : RILSUPSVCTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsupsvctype.htm
old-project : netvista
ms.assetid : 3d9415f7-cc28-4e45-8d88-b8693aa57116
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSUPSVCTYPE, RILSUPSVCTYPE
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : ntddrilapitypes.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : RILSUPSVCTYPE
req.alt-loc : ntddrilapitypes.h
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
req.typenames : RILSUPSVCTYPE
---

# RILSUPSVCTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSUPSVCTYPE { 
  RIL_SUPSVCTYPE_CLIP,
  RIL_SUPSVCTYPE_CLIR,
  RIL_SUPSVCTYPE_COLP,
  RIL_SUPSVCTYPE_COLR,
  RIL_SUPSVCTYPE_CNAP,
  RIL_SUPSVCTYPE_MAX
} RILSUPSVCTYPE;
````

## Constants

<table>

<tr>
<td>RIL_SUPSVCTYPE_CLIP</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCTYPE_CLIR</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCTYPE_CNAP</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCTYPE_COLP</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCTYPE_COLR</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCTYPE_MAX</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntddrilapitypes.h |