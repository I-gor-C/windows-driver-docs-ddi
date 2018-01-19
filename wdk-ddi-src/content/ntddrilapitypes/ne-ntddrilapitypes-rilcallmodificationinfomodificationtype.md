---
UID : NE:ntddrilapitypes.RILCALLMODIFICATIONINFOMODIFICATIONTYPE
title : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmodificationinfomodificationtype.htm
old-project : netvista
ms.assetid : 37b18047-7818-4e57-b25a-3c958106e215
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLMODIFICATIONINFOMODIFICATIONTYPE, RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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
req.alt-api : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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
req.typenames : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
---

# RILCALLMODIFICATIONINFOMODIFICATIONTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLMODIFICATIONINFOMODIFICATIONTYPE { 
  RIL_CALLMODIFICATIONTYPE_BLOCKED,
  RIL_CALLMODIFICATIONTYPE_MODIFIED,
  RIL_CALLMODIFICATIONTYPE_MAX
} RILCALLMODIFICATIONINFOMODIFICATIONTYPE;
````

## Constants

<table>

<tr>
<td>RIL_CALLMODIFICATIONTYPE_BLOCKED</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMODIFICATIONTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLMODIFICATIONTYPE_MODIFIED</td>
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