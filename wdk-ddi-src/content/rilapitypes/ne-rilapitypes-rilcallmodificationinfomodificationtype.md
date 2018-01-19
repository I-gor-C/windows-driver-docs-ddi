---
UID : NE:rilapitypes.RILCALLMODIFICATIONINFOMODIFICATIONTYPE
title : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallmodificationinfomodificationtype_2.htm
old-project : netvista
ms.assetid : e73abe84-1688-40f1-9b8c-e4e34cc87b78
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLMODIFICATIONINFOMODIFICATIONTYPE, RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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
req.alt-api : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
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
req.typenames : RILCALLMODIFICATIONINFOMODIFICATIONTYPE
req.product : Windows 10 or later.
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
| **Header** | rilapitypes.h |