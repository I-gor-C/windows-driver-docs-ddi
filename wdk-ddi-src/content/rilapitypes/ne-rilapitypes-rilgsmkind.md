---
UID : NE:rilapitypes.RILGSMKIND
title : RILGSMKIND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilgsmkind_2.htm
old-project : netvista
ms.assetid : ec02cb5a-78e4-411b-945c-2ded798720e6
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_GSMKIND_GPRS, rilapitypes/RIL_GSMKIND_MAX, rilapitypes/RILGSMKIND, RIL_GSMKIND_GPRS, rilapitypes/RIL_GSMKIND_EDGE, RIL_GSMKIND_EDGE, RILGSMKIND, RILGSMKIND enumeration [Network Drivers Starting with Windows Vista], RIL_GSMKIND_MAX, netvista.rilgsmkind_2
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
<td>RIL_GSMKIND_GSM</td>
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