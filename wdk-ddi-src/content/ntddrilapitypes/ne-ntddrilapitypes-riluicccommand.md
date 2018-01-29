---
UID : NE:ntddrilapitypes.RILUICCCOMMAND
title : RILUICCCOMMAND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluicccommand.htm
old-project : netvista
ms.assetid : 1c2ded31-9d2d-46e4-a23f-a48528fd448f
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_UICCCMD_UPDATERECORD, RIL_UICCCMD_READRECORD, RILUICCCOMMAND enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RILUICCCOMMAND, ntddrilapitypes/RIL_UICCCMD_MAX, RIL_UICCCMD_MAX, RIL_UICCCMD_UPDATEBINARY, ntddrilapitypes/RIL_UICCCMD_UPDATERECORD, ntddrilapitypes/RIL_UICCCMD_UPDATEBINARY, RILUICCCOMMAND, ntddrilapitypes/RIL_UICCCMD_READRECORD, netvista.riluicccommand
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
req.typenames : RILUICCCOMMAND
---

# RILUICCCOMMAND Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILUICCCOMMAND { 
  RIL_UICCCMD_READRECORD,
  RIL_UICCCMD_UPDATEBINARY,
  RIL_UICCCMD_UPDATERECORD,
  RIL_UICCCMD_MAX
} RILUICCCOMMAND;
````

## Constants

<table>

<tr>
<td>RIL_UICCCMD_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_UICCCMD_READBINARY</td>
<td></td>
</tr>

<tr>
<td>RIL_UICCCMD_READRECORD</td>
<td></td>
</tr>

<tr>
<td>RIL_UICCCMD_UPDATEBINARY</td>
<td></td>
</tr>

<tr>
<td>RIL_UICCCMD_UPDATERECORD</td>
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