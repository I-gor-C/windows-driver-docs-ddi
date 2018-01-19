---
UID : NE:ntddrilapitypes.RILMSGSERVICEINFOPARAMMASK
title : RILMSGSERVICEINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmsgserviceinfoparammask.htm
old-project : netvista
ms.assetid : 9314909a-4580-49f9-b587-4d5e70ff0d4f
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMSGSERVICEINFOPARAMMASK, RILMSGSERVICEINFOPARAMMASK
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
req.alt-api : RILMSGSERVICEINFOPARAMMASK
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
req.typenames : RILMSGSERVICEINFOPARAMMASK
---

# RILMSGSERVICEINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMSGSERVICEINFOPARAMMASK { 
  RIL_PARAM_MSI_STOREUSED,
  RIL_PARAM_MSI_STORETOTAL,
  RIL_PARAM_MSI_ALL
} RILMSGSERVICEINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_MSI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSI_STORETOTAL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MSI_STOREUSED</td>
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