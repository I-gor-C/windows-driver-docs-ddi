---
UID : NE:rilapitypes.RILMESSAGETYPE
title : RILMESSAGETYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmessagetype_2.htm
old-project : netvista
ms.assetid : 5f167bd5-a2b8-48a1-b403-e9ac68122ae4
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_MSGTYPE_IN_IS637STATUS, rilapitypes/RIL_MSGTYPE_BC_GENERAL, RIL_MSGTYPE_OUT_SUBMIT, rilapitypes/RIL_MSGTYPE_IN_STATUS, RIL_MSGTYPE_OUT_CDMASUBMIT, rilapitypes/RILMESSAGETYPE, RIL_MSGTYPE_BC_GENERAL, RIL_MSGTYPE_IN_IS637STATUS, netvista.rilmessagetype_2, rilapitypes/RIL_MSGTYPE_OUT_SUBMIT, rilapitypes/RIL_MSGTYPE_OUT_CDMASUBMIT, RILMESSAGETYPE enumeration [Network Drivers Starting with Windows Vista], RILMESSAGETYPE, RIL_MSGTYPE_IN_CDMADELIVER, RIL_MSGTYPE_IN_STATUS, rilapitypes/RIL_MSGTYPE_IN_CDMADELIVER
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
req.typenames : RILMESSAGETYPE
req.product : Windows 10 or later.
---

# RILMESSAGETYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMESSAGETYPE { 
  RIL_MSGTYPE_IN_STATUS,
  RIL_MSGTYPE_IN_IS637STATUS,
  RIL_MSGTYPE_IN_CDMADELIVER,
  RIL_MSGTYPE_OUT_SUBMIT,
  RIL_MSGTYPE_OUT_CDMASUBMIT,
  RIL_MSGTYPE_BC_GENERAL
} RILMESSAGETYPE;
````

## Constants

<table>

<tr>
<td>RIL_MSGTYPE_BC_GENERAL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_IN_CDMADELIVER</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_IN_DELIVER</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_IN_IS637STATUS</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_IN_STATUS</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_OUT_CDMASUBMIT</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGTYPE_OUT_SUBMIT</td>
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