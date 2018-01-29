---
UID : NE:rilapitypes.RILSERVICESETTINGSSTATUS
title : RILSERVICESETTINGSSTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilservicesettingsstatus_2.htm
old-project : netvista
ms.assetid : 4d193398-752f-4aef-8ae6-59c9afabd79a
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_SVCSTAT_MAX, rilapitypes/RILSERVICESETTINGSSTATUS, rilapitypes/RIL_SVCSTAT_MAX, RIL_SVCSTAT_DISABLED, RILSERVICESETTINGSSTATUS enumeration [Network Drivers Starting with Windows Vista], RIL_SVCSTAT_DEFAULT, rilapitypes/RIL_SVCSTAT_ENABLED, rilapitypes/RIL_SVCSTAT_DISABLED, netvista.rilservicesettingsstatus_2, RIL_SVCSTAT_ENABLED, rilapitypes/RIL_SVCSTAT_DEFAULT, RILSERVICESETTINGSSTATUS
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
req.typenames : RILSERVICESETTINGSSTATUS
req.product : Windows 10 or later.
---

# RILSERVICESETTINGSSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSERVICESETTINGSSTATUS { 
  RIL_SVCSTAT_DISABLED,
  RIL_SVCSTAT_ENABLED,
  RIL_SVCSTAT_DEFAULT,
  RIL_SVCSTAT_MAX
} RILSERVICESETTINGSSTATUS;
````

## Constants

<table>

<tr>
<td>RIL_SVCSTAT_DEFAULT</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCSTAT_DISABLED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCSTAT_ENABLED</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCSTAT_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_SVCSTAT_UNKNOWN</td>
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