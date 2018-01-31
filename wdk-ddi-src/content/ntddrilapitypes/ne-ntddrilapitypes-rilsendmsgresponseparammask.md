---
UID : NE:ntddrilapitypes.RILSENDMSGRESPONSEPARAMMASK
title : RILSENDMSGRESPONSEPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsendmsgresponseparammask.htm
old-project : netvista
ms.assetid : d3bf2b1a-22ac-4b37-a442-ecd8a2108b46
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RILSENDMSGRESPONSEPARAMMASK, RIL_PARAM_MSGRES_CDMAERRORCLASS, RIL_PARAM_MSGRES_GWLRELAYCODE, RILSENDMSGRESPONSEPARAMMASK, netvista.rilsendmsgresponseparammask, ntddrilapitypes/RIL_PARAM_MSGRES_CDMACAUSECODE, RIL_PARAM_MSGRES_MSGID, ntddrilapitypes/RIL_PARAM_MSGRES_GWLRELAYCODE, RIL_PARAM_MSGRES_GWLTRANSPORTCODE, ntddrilapitypes/RIL_PARAM_MSGRES_MSGID, RIL_PARAM_MSGRES_CDMACAUSECODE, ntddrilapitypes/RIL_PARAM_MSGRES_GWLTRANSPORTCODE, ntddrilapitypes/RIL_PARAM_MSGRES_ALL, RIL_PARAM_MSGRES_ALL, ntddrilapitypes/RIL_PARAM_MSGRES_CDMAERRORCLASS, RILSENDMSGRESPONSEPARAMMASK enumeration [Network Drivers Starting with Windows Vista]
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
req.typenames : RILSENDMSGRESPONSEPARAMMASK
---

# RILSENDMSGRESPONSEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSENDMSGRESPONSEPARAMMASK { 
  RIL_PARAM_MSGRES_CDMACAUSECODE,
  RIL_PARAM_MSGRES_CDMAERRORCLASS,
  RIL_PARAM_MSGRES_GWLTRANSPORTCODE,
  RIL_PARAM_MSGRES_GWLRELAYCODE,
  RIL_PARAM_MSGRES_MSGID,
  RIL_PARAM_MSGRES_ALL
} RILSENDMSGRESPONSEPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_MSGRES_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_CDMACAUSECODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_CDMAERRORCLASS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_GWLRELAYCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_GWLTRANSPORTCODE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_MSGID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSGRES_RETURN</td>
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