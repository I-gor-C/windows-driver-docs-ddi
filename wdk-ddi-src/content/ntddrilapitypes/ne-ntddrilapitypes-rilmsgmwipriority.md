---
UID : NE:ntddrilapitypes.RILMSGMWIPRIORITY
title : RILMSGMWIPRIORITY
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgmwipriority.htm
old-project : netvista
ms.assetid : a974af39-a4a6-44f2-9010-e612f50c83df
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGMWIPRIORITY, RILMSGMWIPRIORITY
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
req.alt-api : RILMSGMWIPRIORITY
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
req.typenames : RILMSGMWIPRIORITY
---

# RILMSGMWIPRIORITY Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGMWIPRIORITY { 
  RIL_MSGMWIPRIORITY_LOW,
  RIL_MSGMWIPRIORITY_NORMAL,
  RIL_MSGMWIPRIORITY_URGENT,
  RIL_MSGMWIPRIORITY_EMERGENCY,
  RIL_MSGMWIPRIORITY_MAX
} RILMSGMWIPRIORITY;
````

## Constants

<table>

<tr>
<td>RIL_MSGMWIPRIORITY_EMERGENCY</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWIPRIORITY_LOW</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWIPRIORITY_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWIPRIORITY_NORMAL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWIPRIORITY_URGENT</td>
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