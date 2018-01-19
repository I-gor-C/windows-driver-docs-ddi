---
UID : NE:ntddrilapitypes.RILCALLMEDIAOFFERANSWERTYPE
title : RILCALLMEDIAOFFERANSWERTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmediaofferanswertype.htm
old-project : netvista
ms.assetid : cc0c3fc5-1482-424c-8ca8-c1bfe641bc03
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLMEDIAOFFERANSWERTYPE, RILCALLMEDIAOFFERANSWERTYPE
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
req.alt-api : RILCALLMEDIAOFFERANSWERTYPE
req.alt-loc : ntddrilapitypes.h
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
| **Header** | ntddrilapitypes.h |