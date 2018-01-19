---
UID : NE:rilapitypes.RILIMSFAILUREMESSAGETYPE
title : RILIMSFAILUREMESSAGETYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimsfailuremessagetype_2.htm
old-project : netvista
ms.assetid : 9a29cc8c-7e46-4b7f-a428-d2f174945654
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILIMSFAILUREMESSAGETYPE, RILIMSFAILUREMESSAGETYPE
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
req.alt-api : RILIMSFAILUREMESSAGETYPE
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
req.typenames : RILIMSFAILUREMESSAGETYPE
req.product : Windows 10 or later.
---

# RILIMSFAILUREMESSAGETYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSFAILUREMESSAGETYPE { 
  RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE,
  RIL_IMSFAILUREMESSAGETYPE_INCALL,
  RIL_IMSFAILUREMESSAGETYPE_MAX
} RILIMSFAILUREMESSAGETYPE;
````

## Constants

<table>

<tr>
<td>RIL_IMSFAILUREMESSAGETYPE_INCALL</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSFAILUREMESSAGETYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSFAILUREMESSAGETYPE_SUBSCRIBE</td>
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