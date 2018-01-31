---
UID : NE:rilapitypes.RILREGSTATUSINFOPARAMMASK
title : RILREGSTATUSINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilregstatusinfoparammask_2.htm
old-project : netvista
ms.assetid : 22751b8b-f19c-4480-b8f4-6ee2322419ca
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_REGSI_REGREJECTREASON, rilapitypes/RIL_PARAM_REGSI_ALL, rilapitypes/RIL_PARAM_REGSI_VOICEDOMAIN, RILREGSTATUSINFOPARAMMASK, rilapitypes/RIL_PARAM_REGSI_SYSTEMCAPS, rilapitypes/RILREGSTATUSINFOPARAMMASK, netvista.rilregstatusinfoparammask_2, RIL_PARAM_REGSI_SYSTEMCAPS, RIL_PARAM_REGSI_VOICEDOMAIN, rilapitypes/RIL_PARAM_REGSI_ACCESSTECHNOLOGY, RIL_PARAM_REGSI_REGSTATUS, rilapitypes/RIL_PARAM_REGSI_NETWORKCODE, RIL_PARAM_REGSI_HUICCAPP, rilapitypes/RIL_PARAM_REGSI_REGREJECTREASON, RILREGSTATUSINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_REGSI_ALL, rilapitypes/RIL_PARAM_REGSI_REGSTATUS, RIL_PARAM_REGSI_CURRENTOPERATOR, rilapitypes/RIL_PARAM_REGSI_CURRENTOPERATOR, rilapitypes/RIL_PARAM_REGSI_HUICCAPP, RIL_PARAM_REGSI_NETWORKCODE, RIL_PARAM_REGSI_ACCESSTECHNOLOGY
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
req.typenames : RILREGSTATUSINFOPARAMMASK
req.product : Windows 10 or later.
---

# RILREGSTATUSINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILREGSTATUSINFOPARAMMASK { 
  RIL_PARAM_REGSI_HUICCAPP,
  RIL_PARAM_REGSI_REGSTATUS,
  RIL_PARAM_REGSI_ACCESSTECHNOLOGY,
  RIL_PARAM_REGSI_SYSTEMCAPS,
  RIL_PARAM_REGSI_REGREJECTREASON,
  RIL_PARAM_REGSI_CURRENTOPERATOR,
  RIL_PARAM_REGSI_VOICEDOMAIN,
  RIL_PARAM_REGSI_NETWORKCODE,
  RIL_PARAM_REGSI_ALL
} RILREGSTATUSINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_REGSI_ACCESSTECHNOLOGY</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_CURRENTOPERATOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_HUICCAPP</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_NETWORKCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_REGREJECTREASON</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_REGSTATUS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_SYSTEMCAPS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_REGSI_VOICEDOMAIN</td>
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