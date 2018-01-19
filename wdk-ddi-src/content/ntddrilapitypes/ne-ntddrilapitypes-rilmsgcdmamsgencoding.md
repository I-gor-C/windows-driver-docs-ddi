---
UID : NE:ntddrilapitypes.RILMSGCDMAMSGENCODING
title : RILMSGCDMAMSGENCODING
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgcdmamsgencoding.htm
old-project : netvista
ms.assetid : d0bc5fa4-d08d-484c-b6e0-35c7f1d144c3
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGCDMAMSGENCODING, RILMSGCDMAMSGENCODING
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
req.alt-api : RILMSGCDMAMSGENCODING
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
req.typenames : RILMSGCDMAMSGENCODING
---

# RILMSGCDMAMSGENCODING Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCDMAMSGENCODING { 
  RIL_MSGCODING_7BITASCII,
  RIL_MSGCODING_UNICODE,
  RIL_MSGCODING_7BITGSM,
  RIL_MSGCODING_8BITGSM,
  RIL_MSGCODING_OCTET,
  RIL_MSGCODING_IA5,
  RIL_MSGCODING_JIS,
  RIL_MSGCODING_KOREAN,
  RIL_MSGCODING_LATIN_HEBREW,
  RIL_MSGCODING_LATIN,
  RIL_MSGCODING_MAX
} RILMSGCDMAMSGENCODING;
````

## Constants

<table>

<tr>
<td>RIL_MSGCODING_7BITASCII</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_7BITGSM</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_8BITGSM</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_IA5</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_JIS</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_KOREAN</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_LATIN</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_LATIN_HEBREW</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_OCTET</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCODING_UNICODE</td>
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