---
UID : NE:ntddrilapitypes.RILCALLRTTACTION
title : RILCALLRTTACTION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallrttaction.htm
old-project : netvista
ms.assetid : c080c4da-097d-4ae3-b1ca-96d9b5b6e8c9
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_CALLRTTACTION_ACCEPT, ntddrilapitypes/RIL_CALLRTTACTION_MAX, RIL_CALLRTTACTION_MAX, netvista.rilcallrttaction, ntddrilapitypes/RILCALLRTTACTION, ntddrilapitypes/RIL_CALLRTTACTION_ASK, RIL_CALLRTTACTION_ACCEPT, RIL_CALLRTTACTION_REJECT, ntddrilapitypes/RIL_CALLRTTACTION_REJECT, RILCALLRTTACTION enumeration [Network Drivers Starting with Windows Vista], RILCALLRTTACTION, RIL_CALLRTTACTION_ASK
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
req.typenames : RILCALLRTTACTION
---

# RILCALLRTTACTION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLRTTACTION { 
  RIL_CALLRTTACTION_REJECT,
  RIL_CALLRTTACTION_ASK,
  RIL_CALLRTTACTION_ACCEPT,
  RIL_CALLRTTACTION_MAX
} RILCALLRTTACTION;
````

## Constants

<table>

<tr>
<td>RIL_CALLRTTACTION_ACCEPT</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLRTTACTION_ASK</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLRTTACTION_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLRTTACTION_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLRTTACTION_REJECT</td>
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