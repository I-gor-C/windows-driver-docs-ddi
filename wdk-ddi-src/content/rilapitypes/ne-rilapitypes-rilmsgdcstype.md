---
UID : NE:rilapitypes.RILMSGDCSTYPE
title : RILMSGDCSTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgdcstype_2.htm
old-project : netvista
ms.assetid : 5eabc972-f372-4d70-ab38-8830f7907a7a
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGDCSTYPE, RILMSGDCSTYPE
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
req.alt-api : RILMSGDCSTYPE
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
req.typenames : RILMSGDCSTYPE
req.product : Windows 10 or later.
---

# RILMSGDCSTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGDCSTYPE { 
  RIL_DCSTYPE_MSGWAIT,
  RIL_DCSTYPE_MSGCLASS,
  RIL_DCSTYPE_LANGUAGE,
  RIL_DCSTYPE_MAX
} RILMSGDCSTYPE;
````

## Constants

<table>

<tr>
<td>RIL_DCSTYPE_LANGUAGE</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSTYPE_MSGCLASS</td>
<td></td>
</tr>

<tr>
<td>RIL_DCSTYPE_MSGWAIT</td>
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