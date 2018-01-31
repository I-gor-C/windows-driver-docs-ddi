---
UID : NE:rilapitypes.RILCALLMEDIAOFFERANSWERTYPE
title : RILCALLMEDIAOFFERANSWERTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaofferanswertype_2.htm
old-project : netvista
ms.assetid : 098392dc-f966-44f8-9202-9663b8cabc7e
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_MAX, rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER, netvista.rilcallmediaofferanswertype_2, RILCALLMEDIAOFFERANSWERTYPE, RIL_CALLMEDIAOFFERANSWERTYPE_OFFER, RIL_CALLMEDIAOFFERANSWERTYPE_MAX, RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT, rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER, RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER, rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_OFFER, RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER, rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER, RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER, rilapitypes/RILCALLMEDIAOFFERANSWERTYPE, rilapitypes/RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT, RILCALLMEDIAOFFERANSWERTYPE enumeration [Network Drivers Starting with Windows Vista]
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
req.typenames : RILCALLMEDIAOFFERANSWERTYPE
req.product : Windows 10 or later.
---

# RILCALLMEDIAOFFERANSWERTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMEDIAOFFERANSWERTYPE { 
  RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT,
  RIL_CALLMEDIAOFFERANSWERTYPE_OFFER,
  RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER,
  RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER,
  RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER,
  RIL_CALLMEDIAOFFERANSWERTYPE_MAX
} RILCALLMEDIAOFFERANSWERTYPE;
````

## Constants

<table>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_ANSWER</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_CURRENT</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_OFFER</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_PEER_ANSWER</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_PEER_OFFER</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMEDIAOFFERANSWERTYPE_UNKNOWN</td>
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