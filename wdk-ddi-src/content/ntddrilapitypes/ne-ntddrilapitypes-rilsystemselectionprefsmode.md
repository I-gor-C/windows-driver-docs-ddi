---
UID : NE:ntddrilapitypes.RILSYSTEMSELECTIONPREFSMODE
title : RILSYSTEMSELECTIONPREFSMODE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsystemselectionprefsmode.htm
old-project : netvista
ms.assetid : f2d9bb70-cb0c-4e4b-be7a-11a89df739be
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RILSYSTEMSELECTIONPREFSMODE, RILSYSTEMSELECTIONPREFSMODE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_OPSELMODE_MANUAL, RILSYSTEMSELECTIONPREFSMODE, ntddrilapitypes/RIL_OPSELMODE_MAX, RIL_OPSELMODE_MAX, netvista.rilsystemselectionprefsmode, RIL_OPSELMODE_MANUAL
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
req.typenames : RILSYSTEMSELECTIONPREFSMODE
---

# RILSYSTEMSELECTIONPREFSMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSYSTEMSELECTIONPREFSMODE { 
  RIL_OPSELMODE_MANUAL,
  RIL_OPSELMODE_MAX
} RILSYSTEMSELECTIONPREFSMODE;
````

## Constants

<table>

<tr>
<td>RIL_OPSELMODE_AUTOMATIC</td>
<td></td>
</tr>

<tr>
<td>RIL_OPSELMODE_MANUAL</td>
<td></td>
</tr>

<tr>
<td>RIL_OPSELMODE_MAX</td>
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