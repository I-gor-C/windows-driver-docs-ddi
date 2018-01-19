---
UID : NE:rilapitypes.RILCONFPARTICIPANTSTATUSPARAMMASK
title : RILCONFPARTICIPANTSTATUSPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilconfparticipantstatusparammask_2.htm
old-project : netvista
ms.assetid : 1194f333-7422-4dc2-9110-3fca067430a8
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCONFPARTICIPANTSTATUSPARAMMASK, RILCONFPARTICIPANTSTATUSPARAMMASK
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
req.alt-api : RILCONFPARTICIPANTSTATUSPARAMMASK
req.alt-loc : rilapitypes.h
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
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |