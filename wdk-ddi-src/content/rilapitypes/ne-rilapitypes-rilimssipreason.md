---
UID : NE:rilapitypes.RILIMSSIPREASON
title : RILIMSSIPREASON
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilimssipreason_2.htm
old-project : netvista
ms.assetid : 45cee356-e05e-4f3a-bccf-4d95a64587d4
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILIMSSIPREASON, RILIMSSIPREASON
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
req.alt-api : RILIMSSIPREASON
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
req.typenames : RILIMSSIPREASON
req.product : Windows 10 or later.
---

# RILIMSSIPREASON Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILIMSSIPREASON { 
  RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE,
  RIL_IMSSIPREASON_MAX
} RILIMSSIPREASON;
````

## Constants

<table>

<tr>
<td>RIL_IMSSIPREASON_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_IMSSIPREASON_NOT_AUTHORIZED_FOR_SERVICE</td>
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