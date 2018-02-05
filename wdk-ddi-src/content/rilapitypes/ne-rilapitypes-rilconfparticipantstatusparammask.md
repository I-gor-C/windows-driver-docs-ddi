---
UID : NE:rilapitypes.RILCONFPARTICIPANTSTATUSPARAMMASK
title : RILCONFPARTICIPANTSTATUSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilconfparticipantstatusparammask_2.htm
old-project : netvista
ms.assetid : 1194f333-7422-4dc2-9110-3fca067430a8
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_PARAM_CPS_ID, rilapitypes/RIL_PARAM_CPS_PARTICIPANTOP, rilapitypes/RIL_PARAM_CPS_ALL, RIL_PARAM_CPS_PARTICIPANTOP, rilapitypes/RILCONFPARTICIPANTSTATUSPARAMMASK, rilapitypes/RIL_PARAM_CPS_ADDRESS, RIL_PARAM_CPS_ADDRESS, RILCONFPARTICIPANTSTATUSPARAMMASK, RIL_PARAM_CPS_CALLTRANSFER, RILCONFPARTICIPANTSTATUSPARAMMASK enumeration [Network Drivers Starting with Windows Vista], RIL_PARAM_CPS_SIPSTATUS, rilapitypes/RIL_PARAM_CPS_SIPSTATUS, RIL_PARAM_CPS_ALL, netvista.rilconfparticipantstatusparammask_2, rilapitypes/RIL_PARAM_CPS_CALLTRANSFER, RIL_PARAM_CPS_ID
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
req.typenames : RILCONFPARTICIPANTSTATUSPARAMMASK
req.product : Windows 10 or later.
---

# RILCONFPARTICIPANTSTATUSPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCONFPARTICIPANTSTATUSPARAMMASK { 
  RIL_PARAM_CPS_ID,
  RIL_PARAM_CPS_CALLTRANSFER,
  RIL_PARAM_CPS_ADDRESS,
  RIL_PARAM_CPS_PARTICIPANTOP,
  RIL_PARAM_CPS_SIPSTATUS,
  RIL_PARAM_CPS_ALL
} RILCONFPARTICIPANTSTATUSPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_CPS_ADDRESS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_CALLTRANSFER</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_ID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_PARTICIPANTOP</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_CPS_SIPSTATUS</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |