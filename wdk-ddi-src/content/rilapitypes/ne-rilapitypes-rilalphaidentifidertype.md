---
UID : NE:rilapitypes.RILALPHAIDENTIFIDERTYPE
title : RILALPHAIDENTIFIDERTYPE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilalphaidentifidertype_2.htm
old-project : netvista
ms.assetid : 25e65540-b221-453a-95ff-ec2b96857475
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILALPHAIDENTIFIDERTYPE, RILALPHAIDENTIFIDERTYPE
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
req.alt-api : RILALPHAIDENTIFIDERTYPE
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
req.typenames : RILALPHAIDENTIFIDERTYPE
req.product : Windows 10 or later.
---

# RILALPHAIDENTIFIDERTYPE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILALPHAIDENTIFIDERTYPE { 
  RIL_ALPHAIDENTIFIERTYPE_PRESENT,
  RIL_ALPHAIDENTIFIERTYPE_NOTPRESENT,
  RIL_ALPHAIDENTIFIERTYPE_MAX
} RILALPHAIDENTIFIDERTYPE;
````

## Constants

<table>

<tr>
<td>RIL_ALPHAIDENTIFIERTYPE_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_ALPHAIDENTIFIERTYPE_NOTPRESENT</td>
<td></td>
</tr>

<tr>
<td>RIL_ALPHAIDENTIFIERTYPE_PRESENT</td>
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