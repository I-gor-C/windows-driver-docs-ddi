---
UID : NE:ntddrilapitypes.RILMSGCLASS
title : RILMSGCLASS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgclass.htm
old-project : netvista
ms.assetid : 2f7e2c4f-56bc-4efd-8911-5161b657dbea
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGCLASS, RILMSGCLASS
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
req.alt-api : RILMSGCLASS
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
req.typenames : RILMSGCLASS
---

# RILMSGCLASS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGCLASS { 
  RIL_MSGCLASS_INCOMING,
  RIL_MSGCLASS_OUTGOING,
  RIL_MSGCLASS_BROADCAST,
  RIL_MSGCLASS_ALL
} RILMSGCLASS;
````

## Constants

<table>

<tr>
<td>RIL_MSGCLASS_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCLASS_BROADCAST</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCLASS_INCOMING</td>
<td></td>
</tr>

<tr>
<td>RIL_MSGCLASS_OUTGOING</td>
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