---
UID : NE:rilapitypes.RILCALLMEDIAOFFERANSWERTYPE
title : RILCALLMEDIAOFFERANSWERTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaofferanswertype_2.htm
old-project : netvista
ms.assetid : 098392dc-f966-44f8-9202-9663b8cabc7e
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLMEDIAOFFERANSWERTYPE, RILCALLMEDIAOFFERANSWERTYPE
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
req.alt-api : RILCALLMEDIAOFFERANSWERTYPE
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
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | rilapitypes.h |