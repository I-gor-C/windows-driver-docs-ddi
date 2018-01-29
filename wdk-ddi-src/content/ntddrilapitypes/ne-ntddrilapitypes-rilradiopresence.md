---
UID : NE:ntddrilapitypes.RILRADIOPRESENCE
title : RILRADIOPRESENCE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilradiopresence.htm
old-project : netvista
ms.assetid : de67cf2e-1dd8-4b01-9a60-b8a2a01d326b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILRADIOPRESENCE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_RADIOPRESENCE_PRESENT, RIL_RADIOPRESENCE_MAX, RIL_RADIOPRESENCE_PRESENT, RILRADIOPRESENCE, ntddrilapitypes/RILRADIOPRESENCE, ntddrilapitypes/RIL_RADIOPRESENCE_MAX, netvista.rilradiopresence
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
req.typenames : RILRADIOPRESENCE
---

# RILRADIOPRESENCE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILRADIOPRESENCE { 
  RIL_RADIOPRESENCE_PRESENT,
  RIL_RADIOPRESENCE_MAX
} RILRADIOPRESENCE;
````

## Constants

<table>

<tr>
<td>RIL_RADIOPRESENCE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOPRESENCE_NOTPRESENT</td>
<td></td>
</tr>

<tr>
<td>RIL_RADIOPRESENCE_PRESENT</td>
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