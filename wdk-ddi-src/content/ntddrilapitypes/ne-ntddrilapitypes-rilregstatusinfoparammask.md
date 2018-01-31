---
UID : NE:ntddrilapitypes.RILREGSTATUSINFOPARAMMASK
title : RILREGSTATUSINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilregstatusinfoparammask.htm
old-project : netvista
ms.assetid : 7857f845-d695-4b0f-9e52-8871c0140a74
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARAM_REGSI_REGREJECTREASON, ntddrilapitypes/RIL_PARAM_REGSI_HUICCAPP, ntddrilapitypes/RIL_PARAM_REGSI_SYSTEMCAPS, RILREGSTATUSINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_REGSI_VOICEDOMAIN, ntddrilapitypes/RILREGSTATUSINFOPARAMMASK, ntddrilapitypes/RIL_PARAM_REGSI_ALL, ntddrilapitypes/RIL_PARAM_REGSI_REGSTATUS, RIL_PARAM_REGSI_SYSTEMCAPS, RIL_PARAM_REGSI_VOICEDOMAIN, RIL_PARAM_REGSI_REGSTATUS, netvista.rilregstatusinfoparammask, ntddrilapitypes/RIL_PARAM_REGSI_NETWORKCODE, RIL_PARAM_REGSI_HUICCAPP, RILREGSTATUSINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_REGSI_ACCESSTECHNOLOGY, RIL_PARAM_REGSI_ALL, ntddrilapitypes/RIL_PARAM_REGSI_CURRENTOPERATOR, RIL_PARAM_REGSI_CURRENTOPERATOR, RIL_PARAM_REGSI_NETWORKCODE, RIL_PARAM_REGSI_ACCESSTECHNOLOGY, ntddrilapitypes/RIL_PARAM_REGSI_REGREJECTREASON
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
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : RILREGSTATUSINFOPARAMMASK
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
| **Header** | ntddrilapitypes.h |