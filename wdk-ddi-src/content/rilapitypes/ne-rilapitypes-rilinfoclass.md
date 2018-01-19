---
UID : NE:rilapitypes.RILINFOCLASS
title : RILINFOCLASS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilinfoclass_2.htm
old-project : netvista
ms.assetid : 19927cd1-8afa-4006-a882-d5222c690724
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILINFOCLASS, RILINFOCLASS
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
req.alt-api : RILINFOCLASS
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
req.typenames : RILINFOCLASS
req.product : Windows 10 or later.
---

# RILINFOCLASS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILINFOCLASS { 
  RIL_INFOCLASS_VOICE,
  RIL_INFOCLASS_DATA,
  RIL_INFOCLASS_FAX,
  RIL_INFOCLASS_SMS,
  RIL_INFOCLASS_DATACIRCUITSYNC,
  RIL_INFOCLASS_DATACIRCUITASYNC,
  RIL_INFOCLASS_PACKETACCESS,
  RIL_INFOCLASS_PADACCESS,
  RIL_INFOCLASS_ALL
} RILINFOCLASS;
````

## Constants

<table>

<tr>
<td>RIL_INFOCLASS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATA</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATACIRCUITASYNC</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_DATACIRCUITSYNC</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_FAX</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_PACKETACCESS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_PADACCESS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_SMS</td>
<td></td>
</tr>

<tr>
<td>RIL_INFOCLASS_VOICE</td>
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