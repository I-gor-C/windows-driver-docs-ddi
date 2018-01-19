---
UID : NE:rilapitypes.RILOPERATORINFOSTATUS
title : RILOPERATORINFOSTATUS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riloperatorinfostatus_2.htm
old-project : netvista
ms.assetid : 8b17ae4a-b3ea-48b6-8269-f947e1d74b86
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILOPERATORINFOSTATUS, RILOPERATORINFOSTATUS
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
req.alt-api : RILOPERATORINFOSTATUS
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
req.typenames : RILOPERATORINFOSTATUS
req.product : Windows 10 or later.
---

# RILOPERATORINFOSTATUS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILOPERATORINFOSTATUS { 
  RIL_OPSTATUS_AVAILABLE,
  RIL_OPSTATUS_CURRENT,
  RIL_OPSTATUS_FORBIDDEN,
  RIL_OPSTATUS_MAX
} RILOPERATORINFOSTATUS;
````

## Constants

<table>

<tr>
<td>RIL_OPSTATUS_AVAILABLE</td>
<td></td>
</tr>

<tr>
<td>RIL_OPSTATUS_CURRENT</td>
<td></td>
</tr>

<tr>
<td>RIL_OPSTATUS_FORBIDDEN</td>
<td></td>
</tr>

<tr>
<td>RIL_OPSTATUS_MAX</td>
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