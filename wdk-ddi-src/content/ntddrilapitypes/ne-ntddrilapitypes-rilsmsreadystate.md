---
UID : NE:ntddrilapitypes.RILSMSREADYSTATE
title : RILSMSREADYSTATE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsmsreadystate.htm
old-project : netvista
ms.assetid : f37b1e31-d0fa-4b0a-bab6-131b3bf1bdcd
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RILSMSREADYSTATE, ntddrilapitypes/RIL_SMSREADY_SERVICEREADY_3GPP2, RIL_SMSREADY_UICCREADY, RILSMSREADYSTATE enumeration [Network Drivers Starting with Windows Vista], RIL_SMSREADYSTATE_ALL, netvista.rilsmsreadystate, RILSMSREADYSTATE, RIL_SMSREADY_SERVICEREADY_3GPP2, ntddrilapitypes/RIL_SMSREADY_UICCREADY, ntddrilapitypes/RIL_SMSREADYSTATE_ALL
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
req.typenames : RILSMSREADYSTATE
---

# RILSMSREADYSTATE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSMSREADYSTATE { 
  RIL_SMSREADY_SERVICEREADY_3GPP2,
  RIL_SMSREADY_UICCREADY,
  RIL_SMSREADYSTATE_ALL
} RILSMSREADYSTATE;
````

## Constants

<table>

<tr>
<td>RIL_SMSREADY_SERVICEREADY_3GPP</td>
<td></td>
</tr>

<tr>
<td>RIL_SMSREADY_SERVICEREADY_3GPP2</td>
<td></td>
</tr>

<tr>
<td>RIL_SMSREADY_UICCREADY</td>
<td></td>
</tr>

<tr>
<td>RIL_SMSREADYSTATE_ALL</td>
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