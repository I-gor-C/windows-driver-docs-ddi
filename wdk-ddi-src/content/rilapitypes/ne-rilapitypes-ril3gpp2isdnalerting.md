---
UID : NE:rilapitypes.RIL3GPP2ISDNALERTING
title : RIL3GPP2ISDNALERTING
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\ril3gpp2isdnalerting_2.htm
old-project : netvista
ms.assetid : 9fff629b-ad85-4158-b8c4-f5f6abe8e3f5
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : RIL_3GPP2ISDNALERTING_PINGRING, rilapitypes/RIL_3GPP2ISDNALERTING_PINGRING, RIL_3GPP2ISDNALERTING_SPECIAL, RIL_3GPP2ISDNALERTING_INTERGROUP, rilapitypes/RIL_3GPP2ISDNALERTING_SPECIAL, RIL3GPP2ISDNALERTING, netvista.ril3gpp2isdnalerting_2, rilapitypes/RIL_3GPP2ISDNALERTING_NORMAL, rilapitypes/RIL_3GPP2ISDNALERTING_MAX, RIL3GPP2ISDNALERTING enumeration [Network Drivers Starting with Windows Vista], RIL_3GPP2ISDNALERTING_NORMAL, rilapitypes/RIL3GPP2ISDNALERTING, rilapitypes/RIL_3GPP2ISDNALERTING_INTERGROUP, RIL_3GPP2ISDNALERTING_MAX
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
req.typenames : RIL3GPP2ISDNALERTING
req.product : Windows 10 or later.
---

# RIL3GPP2ISDNALERTING Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RIL3GPP2ISDNALERTING { 
  RIL_3GPP2ISDNALERTING_NORMAL,
  RIL_3GPP2ISDNALERTING_INTERGROUP,
  RIL_3GPP2ISDNALERTING_SPECIAL,
  RIL_3GPP2ISDNALERTING_PINGRING,
  RIL_3GPP2ISDNALERTING_MAX
} RIL3GPP2ISDNALERTING;
````

## Constants

<table>

<tr>
<td>RIL_3GPP2ISDNALERTING_ALERTINGOFF</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPP2ISDNALERTING_INTERGROUP</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPP2ISDNALERTING_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPP2ISDNALERTING_NORMAL</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPP2ISDNALERTING_PINGRING</td>
<td></td>
</tr>

<tr>
<td>RIL_3GPP2ISDNALERTING_SPECIAL</td>
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