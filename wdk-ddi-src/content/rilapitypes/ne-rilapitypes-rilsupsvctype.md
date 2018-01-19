---
UID : NE:rilapitypes.RILSUPSVCTYPE
title : RILSUPSVCTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsupsvctype_2.htm
old-project : netvista
ms.assetid : 4aec39d6-3e12-4393-b477-24ea2036c227
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSUPSVCTYPE, RILSUPSVCTYPE
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
req.alt-api : RILSUPSVCTYPE
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
req.typenames : RILSUPSVCTYPE
req.product : Windows 10 or later.
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
| **Header** | rilapitypes.h |