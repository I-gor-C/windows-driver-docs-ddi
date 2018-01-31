---
UID : NE:rilapitypes.RILCALLWAITINGINFOPARAMMASK
title : RILCALLWAITINGINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallwaitinginfoparammask_2.htm
old-project : netvista
ms.assetid : ed6f3d54-face-43e3-a45f-820c2f8e99cf
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_CWI_ALL, rilapitypes/RILCALLWAITINGINFOPARAMMASK, RILCALLWAITINGINFOPARAMMASK, RIL_PARAM_CWI_CALLERINFO, rilapitypes/RIL_PARAM_CWI_CALLERINFO, RILCALLWAITINGINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], netvista.rilcallwaitinginfoparammask_2, RIL_PARAM_CWI_ALL, RIL_PARAM_CWI_CALLTYPE, rilapitypes/RIL_PARAM_CWI_CALLTYPE
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
req.typenames : RILCALLWAITINGINFOPARAMMASK
req.product : Windows 10 or later.
---

# RILCALLWAITINGINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLWAITINGINFOPARAMMASK { 
  RIL_PARAM_CWI_CALLTYPE,
  RIL_PARAM_CWI_CALLERINFO,
  RIL_PARAM_CWI_ALL
} RILCALLWAITINGINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CWI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CWI_CALLERINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CWI_CALLTYPE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CWI_EXECUTOR</td>
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