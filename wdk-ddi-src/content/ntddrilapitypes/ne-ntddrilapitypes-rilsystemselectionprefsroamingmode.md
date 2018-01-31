---
UID : NE:ntddrilapitypes.RILSYSTEMSELECTIONPREFSROAMINGMODE
title : RILSYSTEMSELECTIONPREFSROAMINGMODE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsystemselectionprefsroamingmode.htm
old-project : netvista
ms.assetid : aa9e1a92-e175-46ce-9f2e-3794e8d96636
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_ROAMMODE_DOMESTIC, netvista.rilsystemselectionprefsroamingmode, RILSYSTEMSELECTIONPREFSROAMINGMODE, RILSYSTEMSELECTIONPREFSROAMINGMODE enumeration [Network Drivers Starting with Windows Vista], RIL_ROAMMODE_MAX, ntddrilapitypes/RILSYSTEMSELECTIONPREFSROAMINGMODE, RIL_ROAMMODE_AUTOMATIC, RIL_ROAMMODE_DOMESTIC, ntddrilapitypes/RIL_ROAMMODE_MAX, ntddrilapitypes/RIL_ROAMMODE_AUTOMATIC
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
req.typenames : RILSYSTEMSELECTIONPREFSROAMINGMODE
---

# RILSYSTEMSELECTIONPREFSROAMINGMODE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSYSTEMSELECTIONPREFSROAMINGMODE { 
  RIL_ROAMMODE_AUTOMATIC,
  RIL_ROAMMODE_DOMESTIC,
  RIL_ROAMMODE_MAX
} RILSYSTEMSELECTIONPREFSROAMINGMODE;
````

## Constants

<table>

<tr>
<td>RIL_ROAMMODE_AUTOMATIC</td>
<td></td>
</tr>

<tr>
<td>RIL_ROAMMODE_DOMESTIC</td>
<td></td>
</tr>

<tr>
<td>RIL_ROAMMODE_HOMEONLY</td>
<td></td>
</tr>

<tr>
<td>RIL_ROAMMODE_MAX</td>
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