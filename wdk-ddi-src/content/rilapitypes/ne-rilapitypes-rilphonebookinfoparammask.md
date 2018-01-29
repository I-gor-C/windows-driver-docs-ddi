---
UID : NE:rilapitypes.RILPHONEBOOKINFOPARAMMASK
title : RILPHONEBOOKINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilphonebookinfoparammask_2.htm
old-project : netvista
ms.assetid : 5c56186c-44a7-4948-a74a-9337dd47d0a7
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_PBI_MAXAASTEXTLENGTH, RILPHONEBOOKINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RILPHONEBOOKINFOPARAMMASK, RIL_PARAM_PBI_MAXGASLENGTH, rilapitypes/RIL_PARAM_PBI_MAXGASLENGTH, rilapitypes/RIL_PARAM_PBI_MAXANR, RIL_PARAM_PBI_MAXEMAILLENGTH, rilapitypes/RIL_PARAM_PBI_USEDAAS, netvista.rilphonebookinfoparammask_2, rilapitypes/RIL_PARAM_PBI_MAXANRLENGTH, RIL_PARAM_PBI_MAXGROUPS, RIL_PARAM_PBI_ALL, RIL_PARAM_PBI_MAXAASTEXTLENGTH, rilapitypes/RIL_PARAM_PBI_TOTALAAS, RILPHONEBOOKINFOPARAMMASK, rilapitypes/RIL_PARAM_PBI_MAXEMAILS, rilapitypes/RIL_PARAM_PBI_MAXGROUPS, RIL_PARAM_PBI_TOTAL, rilapitypes/RIL_PARAM_PBI_MAXSNELENGTH, RIL_PARAM_PBI_TOTALGAS, RIL_PARAM_PBI_USEDGAS, RIL_PARAM_PBI_MAXANR, RIL_PARAM_PBI_ADDRESSLENGTH, RIL_PARAM_PBI_MAXEMAILS, RIL_PARAM_PBI_USEDAAS, RIL_PARAM_PBI_TEXTLENGTH, rilapitypes/RIL_PARAM_PBI_TOTALGAS, rilapitypes/RIL_PARAM_PBI_USEDGAS, RIL_PARAM_PBI_MAXANRLENGTH, RIL_PARAM_PBI_MAXSNELENGTH, rilapitypes/RIL_PARAM_PBI_ALL, rilapitypes/RIL_PARAM_PBI_TEXTLENGTH, rilapitypes/RIL_PARAM_PBI_ADDRESSLENGTH, RIL_PARAM_PBI_TOTALAAS, rilapitypes/RIL_PARAM_PBI_MAXEMAILLENGTH, rilapitypes/RIL_PARAM_PBI_TOTAL
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
req.typenames : RILPHONEBOOKINFOPARAMMASK
req.product : Windows 10 or later.
---

# RILPHONEBOOKINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPHONEBOOKINFOPARAMMASK { 
  RIL_PARAM_PBI_TOTAL,
  RIL_PARAM_PBI_ADDRESSLENGTH,
  RIL_PARAM_PBI_TEXTLENGTH,
  RIL_PARAM_PBI_MAXANR,
  RIL_PARAM_PBI_MAXANRLENGTH,
  RIL_PARAM_PBI_MAXAASTEXTLENGTH,
  RIL_PARAM_PBI_USEDAAS,
  RIL_PARAM_PBI_TOTALAAS,
  RIL_PARAM_PBI_MAXEMAILS,
  RIL_PARAM_PBI_MAXEMAILLENGTH,
  RIL_PARAM_PBI_MAXGROUPS,
  RIL_PARAM_PBI_MAXGASLENGTH,
  RIL_PARAM_PBI_USEDGAS,
  RIL_PARAM_PBI_TOTALGAS,
  RIL_PARAM_PBI_MAXSNELENGTH,
  RIL_PARAM_PBI_ALL
} RILPHONEBOOKINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_PBI_ADDRESSLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXAASTEXTLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXANR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXANRLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXEMAILLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXEMAILS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXGASLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXGROUPS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_MAXSNELENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_TEXTLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_TOTAL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_TOTALAAS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_TOTALGAS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_USED</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_USEDAAS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_PBI_USEDGAS</td>
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