---
UID : NE:ntddrilapitypes.RILLOCATIONINFOPARAMMASK
title : RILLOCATIONINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rillocationinfoparammask.htm
old-project : netvista
ms.assetid : 3d681026-7ccb-4dcb-bed1-505c13089177
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILLOCATIONINFOPARAMMASK, RILLOCATIONINFOPARAMMASK
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
req.alt-api : RILLOCATIONINFOPARAMMASK
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
req.typenames : RILLOCATIONINFOPARAMMASK
---

# RILLOCATIONINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILLOCATIONINFOPARAMMASK { 
  RIL_PARAM_LU_HUICCAPP,
  RIL_PARAM_LU_LAC,
  RIL_PARAM_LU_TAC,
  RIL_PARAM_LU_CELLID,
  RIL_PARAM_LU_ALL
} RILLOCATIONINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_LU_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_LU_CELLID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_LU_HUICCAPP</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_LU_LAC</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_LU_TAC</td>
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