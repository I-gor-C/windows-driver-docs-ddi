---
UID : NE:rilapitypes.RILEQUIPMENTSTATE
title : RILEQUIPMENTSTATE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilequipmentstate_2.htm
old-project : netvista
ms.assetid : fd3af191-aae8-4afa-b737-8c51029df0e4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RILEQUIPMENTSTATE enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_EQSTATE_FULL, RIL_EQSTATE_MAX, rilapitypes/RILEQUIPMENTSTATE, netvista.rilequipmentstate_2, RILEQUIPMENTSTATE, rilapitypes/RIL_EQSTATE_SHUTDOWN, rilapitypes/RIL_EQSTATE_MAX, RIL_EQSTATE_SHUTDOWN, RIL_EQSTATE_FULL
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
req.typenames : RILEQUIPMENTSTATE
req.product : Windows 10 or later.
---

# RILEQUIPMENTSTATE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILEQUIPMENTSTATE { 
  RIL_EQSTATE_FULL,
  RIL_EQSTATE_SHUTDOWN,
  RIL_EQSTATE_MAX
} RILEQUIPMENTSTATE;
````

## Constants

<table>

<tr>
<td>RIL_EQSTATE_FULL</td>
<td></td>
</tr>

<tr>
<td>RIL_EQSTATE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_EQSTATE_MINIMUM</td>
<td></td>
</tr>

<tr>
<td>RIL_EQSTATE_SHUTDOWN</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |