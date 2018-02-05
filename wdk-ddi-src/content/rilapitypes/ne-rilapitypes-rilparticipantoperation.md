---
UID : NE:rilapitypes.RILPARTICIPANTOPERATION
title : RILPARTICIPANTOPERATION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilparticipantoperation_2.htm
old-project : netvista
ms.assetid : 74386760-95c8-4c69-99bf-542e7c58b8c8
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_PARTICIPANT_REMOVE, netvista.rilparticipantoperation_2, RILPARTICIPANTOPERATION enumeration [Network Drivers Starting with Windows Vista], rilapitypes/RIL_PARTICIPANT_MAX, RIL_PARTICIPANT_MAX, rilapitypes/RIL_PARTICIPANT_REMOVE, RILPARTICIPANTOPERATION, rilapitypes/RILPARTICIPANTOPERATION
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
req.typenames : RILPARTICIPANTOPERATION
req.product : Windows 10 or later.
---

# RILPARTICIPANTOPERATION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILPARTICIPANTOPERATION { 
  RIL_PARTICIPANT_REMOVE,
  RIL_PARTICIPANT_MAX
} RILPARTICIPANTOPERATION;
````

## Constants

<table>

<tr>
<td>RIL_PARTICIPANT_ADD</td>
<td></td>
</tr>

<tr>
<td>RIL_PARTICIPANT_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_PARTICIPANT_REMOVE</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h |