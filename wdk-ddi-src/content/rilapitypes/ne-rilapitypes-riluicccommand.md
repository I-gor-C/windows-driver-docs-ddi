---
UID : NE:rilapitypes.RILUICCCOMMAND
title : RILUICCCOMMAND
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riluicccommand_2.htm
old-project : netvista
ms.assetid : 13861810-91a6-4027-81a0-297b049e3ee4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_UICCCMD_READRECORD, rilapitypes/RIL_UICCCMD_UPDATERECORD, RIL_UICCCMD_UPDATERECORD, RIL_UICCCMD_READRECORD, rilapitypes/RIL_UICCCMD_UPDATEBINARY, RILUICCCOMMAND enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_UICCCMD_MAX, RIL_UICCCMD_MAX, RIL_UICCCMD_UPDATEBINARY, rilapitypes/RILUICCCOMMAND, netvista.riluicccommand_2, RILUICCCOMMAND
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
req.typenames : RILUICCCOMMAND
req.product : Windows 10 or later.
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
| **Header** | rilapitypes.h |