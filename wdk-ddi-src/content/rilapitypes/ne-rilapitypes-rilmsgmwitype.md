---
UID : NE:rilapitypes.RILMSGMWITYPE
title : RILMSGMWITYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgmwitype_2.htm
old-project : netvista
ms.assetid : 55f06d11-60b7-4dc0-8f78-eb9901d49d1a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGMWITYPE, RILMSGMWITYPE
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
req.alt-api : RILMSGMWITYPE
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
req.typenames : RILMSGMWITYPE
req.product : Windows 10 or later.
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
| **Header** | rilapitypes.h |