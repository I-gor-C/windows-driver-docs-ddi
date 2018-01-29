---
UID : NE:ntddrilapitypes.RILIMSSUBSCRIBETYPE
title : RILIMSSUBSCRIBETYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimssubscribetype.htm
old-project : netvista
ms.assetid : 347b42c1-7585-471c-af42-44218da48fa3
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_CONFERENCE, RIL_IMSSUBSCRIBETYPE_MAX, RILIMSSUBSCRIBETYPE, RILIMSSUBSCRIBETYPE enumeration [Network Drivers Starting with Windows Vista], RIL_IMSSUBSCRIBETYPE_CONFERENCE, RIL_IMSSUBSCRIBETYPE_MWI, netvista.rilimssubscribetype, ntddrilapitypes/RILIMSSUBSCRIBETYPE, ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_MAX, ntddrilapitypes/RIL_IMSSUBSCRIBETYPE_MWI
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
req.typenames : RILIMSSUBSCRIBETYPE
---

# RILIMSSUBSCRIBETYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSSUBSCRIBETYPE { 
  RIL_IMSSUBSCRIBETYPE_MWI,
  RIL_IMSSUBSCRIBETYPE_CONFERENCE,
  RIL_IMSSUBSCRIBETYPE_MAX
} RILIMSSUBSCRIBETYPE;
````

## Constants

<table>

<tr>
<td>RIL_IMSSUBSCRIBETYPE_CONFERENCE</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSSUBSCRIBETYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSSUBSCRIBETYPE_MWI</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSSUBSCRIBETYPE_REG</td>
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