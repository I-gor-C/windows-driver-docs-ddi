---
UID : NE:rilapitypes.RILLOCATIONINFOPARAMMASK
title : RILLOCATIONINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rillocationinfoparammask_2.htm
old-project : netvista
ms.assetid : a7ce7aaf-fd98-4ba6-8c9e-d15419c658f1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILLOCATIONINFOPARAMMASK, RILLOCATIONINFOPARAMMASK
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
req.alt-api : RILLOCATIONINFOPARAMMASK
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
req.typenames : RILLOCATIONINFOPARAMMASK
req.product : Windows 10 or later.
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
| **Header** | rilapitypes.h |