---
UID : NE:ntddrilapitypes.RILADDITIONALCALLERINFOPARAMMASK
title : RILADDITIONALCALLERINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riladditionalcallerinfoparammask.htm
old-project : netvista
ms.assetid : b37246ed-37b8-4d5f-aace-41053ea839da
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : netvista.riladditionalcallerinfoparammask, RIL_PARAM_ADDTLCI_ALL, RIL_PARAM_ADDTLCI_CALLERINFO, ntddrilapitypes/RIL_PARAM_ADDTLCI_ALL, RILADDITIONALCALLERINFOPARAMMASK enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_PARAM_ADDTLCI_CALLERINFO, RIL_PARAM_ADDTLCI_CALLERINFOLENGTH, ntddrilapitypes/RIL_PARAM_ADDTLCI_CALLERINFOLENGTH, ntddrilapitypes/RIL_PARAM_ADDTLCI_CALLID, RIL_PARAM_ADDTLCI_CALLID, RILADDITIONALCALLERINFOPARAMMASK, ntddrilapitypes/RILADDITIONALCALLERINFOPARAMMASK
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
req.typenames : RILADDITIONALCALLERINFOPARAMMASK
---

# RILADDITIONALCALLERINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILADDITIONALCALLERINFOPARAMMASK { 
  RIL_PARAM_ADDTLCI_CALLID,
  RIL_PARAM_ADDTLCI_CALLERINFOLENGTH,
  RIL_PARAM_ADDTLCI_CALLERINFO,
  RIL_PARAM_ADDTLCI_ALL
} RILADDITIONALCALLERINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_ADDTLCI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ADDTLCI_CALLERINFO</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ADDTLCI_CALLERINFOLENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ADDTLCI_CALLID</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_ADDTLCI_EXECUTOR</td>
<td></td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h |