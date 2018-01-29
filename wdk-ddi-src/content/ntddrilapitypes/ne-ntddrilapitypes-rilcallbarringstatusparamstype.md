---
UID : NE:ntddrilapitypes.RILCALLBARRINGSTATUSPARAMSTYPE
title : RILCALLBARRINGSTATUSPARAMSTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallbarringstatusparamstype.htm
old-project : netvista
ms.assetid : 95c15362-227c-4912-9eec-a18fee92f340
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : ntddrilapitypes/RIL_BARRTYPE_ALLINCOMINGBARRING, ntddrilapitypes/RILCALLBARRINGSTATUSPARAMSTYPE, RIL_BARRTYPE_ALLOUTGOINGBARRING, RILCALLBARRINGSTATUSPARAMSTYPE, RIL_BARRTYPE_ALLINCOMINGBARRING, RIL_BARRTYPE_OUTGOINGINT, RIL_BARRTYPE_OUTGOINGINTEXTOHOME, RIL_BARRTYPE_ALL, RILCALLBARRINGSTATUSPARAMSTYPE enumeration [Network Drivers Starting with Windows Vista], ntddrilapitypes/RIL_BARRTYPE_OUTGOINGINTEXTOHOME, ntddrilapitypes/RIL_BARRTYPE_ALLINCOMING, ntddrilapitypes/RIL_BARRTYPE_ALLBARRING, RIL_BARRTYPE_INCOMINGNOTINUICC, ntddrilapitypes/RIL_BARRTYPE_ALL, ntddrilapitypes/RIL_BARRTYPE_INCOMINGROAMING, RIL_BARRTYPE_ALLINCOMING, ntddrilapitypes/RIL_BARRTYPE_ALLOUTGOINGBARRING, netvista.rilcallbarringstatusparamstype, RIL_BARRTYPE_INCOMINGROAMING, ntddrilapitypes/RIL_BARRTYPE_INCOMINGNOTINUICC, ntddrilapitypes/RIL_BARRTYPE_OUTGOINGINT, RIL_BARRTYPE_ALLBARRING
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
req.typenames : RILCALLBARRINGSTATUSPARAMSTYPE
---

# RILCALLBARRINGSTATUSPARAMSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLBARRINGSTATUSPARAMSTYPE { 
  RIL_BARRTYPE_OUTGOINGINT,
  RIL_BARRTYPE_OUTGOINGINTEXTOHOME,
  RIL_BARRTYPE_ALLINCOMING,
  RIL_BARRTYPE_INCOMINGROAMING,
  RIL_BARRTYPE_INCOMINGNOTINUICC,
  RIL_BARRTYPE_ALLBARRING,
  RIL_BARRTYPE_ALLOUTGOINGBARRING,
  RIL_BARRTYPE_ALLINCOMINGBARRING,
  RIL_BARRTYPE_ALL
} RILCALLBARRINGSTATUSPARAMSTYPE;
````

## Constants

<table>

<tr>
<td>RIL_BARRTYPE_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_ALLBARRING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_ALLINCOMING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_ALLINCOMINGBARRING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_ALLOUTGOING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_ALLOUTGOINGBARRING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_INCOMINGNOTINUICC</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_INCOMINGROAMING</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_OUTGOINGINT</td>
<td></td>
</tr>

<tr>
<td>RIL_BARRTYPE_OUTGOINGINTEXTOHOME</td>
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