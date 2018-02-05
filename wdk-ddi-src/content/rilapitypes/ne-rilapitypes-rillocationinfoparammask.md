---
UID : NE:rilapitypes.RILLOCATIONINFOPARAMMASK
title : RILLOCATIONINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rillocationinfoparammask_2.htm
old-project : netvista
ms.assetid : a7ce7aaf-fd98-4ba6-8c9e-d15419c658f1
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_LU_LAC, rilapitypes/RIL_PARAM_LU_LAC, rilapitypes/RIL_PARAM_LU_CELLID, RIL_PARAM_LU_HUICCAPP, rilapitypes/RILLOCATIONINFOPARAMMASK, rilapitypes/RIL_PARAM_LU_HUICCAPP, RIL_PARAM_LU_CELLID, RILLOCATIONINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], netvista.rillocationinfoparammask_2, RIL_PARAM_LU_ALL, RIL_PARAM_LU_TAC, rilapitypes/RIL_PARAM_LU_TAC, rilapitypes/RIL_PARAM_LU_ALL, RILLOCATIONINFOPARAMMASK
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
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : NtosKrnl.exe
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
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
<td>RIL_PARAM_LU_EXECUTOR</td>
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
| **Header** | rilapitypes.h |