---
UID : NE:ntddrilapitypes.RILMSGMWITYPE
title : RILMSGMWITYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgmwitype.htm
old-project : netvista
ms.assetid : e5faa899-194a-412c-9308-a84227a31a6a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGMWITYPE, RILMSGMWITYPE
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
req.alt-api : RILMSGMWITYPE
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
req.typenames : RILMSGMWITYPE
---

# RILMSGMWITYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGMWITYPE { 
  RIL_MSGMWITYPE_VOICEMAIL,
  RIL_MSGMWITYPE_VIDEOMAIL,
  RIL_MSGMWITYPE_FAX,
  RIL_MSGMWITYPE_PAGER,
  RIL_MSGMWITYPE_MULTIMEDIA,
  RIL_MSGMWITYPE_TEXT,
  RIL_MSGMWITYPE_MAX
} RILMSGMWITYPE;
````

## Constants

<table>

<tr>
<td>RIL_MSGMWITYPE_FAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_MULTIMEDIA</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_PAGER</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_TEXT</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_VIDEOMAIL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGMWITYPE_VOICEMAIL</td>
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