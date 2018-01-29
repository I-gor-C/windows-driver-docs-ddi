---
UID : NE:rilapitypes.RILMESSAGEFLAGS
title : RILMESSAGEFLAGS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmessageflags_2.htm
old-project : netvista
ms.assetid : 49f8bd1b-5c8a-47d3-a5d5-817216562559
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_MSGFLAG_STATUSREPORTREQUESTED, RIL_MSGFLAG_STATUSREPORTRETURNED, rilapitypes/RIL_MSGFLAG_ALL, rilapitypes/RILMESSAGEFLAGS, netvista.rilmessageflags_2, RILMESSAGEFLAGS enumeration [Network Drivers Starting with Windows Vista], RIL_MSGFLAG_CAUSEDBYCOMMAND, RIL_MSGFLAG_ALL, RIL_MSGFLAG_REPLYPATH, rilapitypes/RIL_MSGFLAG_REPLYPATH, RIL_MSGFLAG_HEADER, RIL_MSGFLAG_REJECTDUPS, rilapitypes/RIL_MSGFLAG_MORETOSEND, rilapitypes/RIL_MSGFLAG_HEADER, RIL_MSGFLAG_MORETOSEND, RILMESSAGEFLAGS, rilapitypes/RIL_MSGFLAG_REJECTDUPS, rilapitypes/RIL_MSGFLAG_STATUSREPORTRETURNED, RIL_MSGFLAG_STATUSREPORTREQUESTED, rilapitypes/RIL_MSGFLAG_CAUSEDBYCOMMAND
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
req.typenames : RILMESSAGEFLAGS
req.product : Windows 10 or later.
---

# RILMESSAGEFLAGS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMESSAGEFLAGS { 
  RIL_MSGFLAG_MORETOSEND,
  RIL_MSGFLAG_REPLYPATH,
  RIL_MSGFLAG_HEADER,
  RIL_MSGFLAG_REJECTDUPS,
  RIL_MSGFLAG_STATUSREPORTRETURNED,
  RIL_MSGFLAG_STATUSREPORTREQUESTED,
  RIL_MSGFLAG_CAUSEDBYCOMMAND,
  RIL_MSGFLAG_ALL
} RILMESSAGEFLAGS;
````

## Constants

<table>

<tr>
<td>RIL_MSGFLAG_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_CAUSEDBYCOMMAND</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_HEADER</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_MORETOSEND</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_NONE</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_REJECTDUPS</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_REPLYPATH</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_STATUSREPORTREQUESTED</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGFLAG_STATUSREPORTRETURNED</td>
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