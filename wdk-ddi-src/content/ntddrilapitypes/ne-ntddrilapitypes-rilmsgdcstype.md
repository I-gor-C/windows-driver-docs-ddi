---
UID : NE:ntddrilapitypes.RILMSGDCSTYPE
title : RILMSGDCSTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgdcstype.htm
old-project : netvista
ms.assetid : 557fc92e-6550-44ea-ac09-bb0b74e1275f
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGDCSTYPE, RILMSGDCSTYPE
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
req.alt-api : RILMSGDCSTYPE
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
req.typenames : RILMSGDCSTYPE
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
| **Header** | ntddrilapitypes.h |