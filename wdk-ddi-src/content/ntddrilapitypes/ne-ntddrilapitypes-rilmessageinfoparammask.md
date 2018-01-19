---
UID : NE:ntddrilapitypes.RILMESSAGEINFOPARAMMASK
title : RILMESSAGEINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilmessageinfoparammask.htm
old-project : netvista
ms.assetid : 70e0f22c-14d4-43e6-bfb6-66523706ba52
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILMESSAGEINFOPARAMMASK, RILMESSAGEINFOPARAMMASK
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
req.alt-api : RILMESSAGEINFOPARAMMASK
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
req.typenames : RILMESSAGEINFOPARAMMASK
---

# RILMESSAGEINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILMESSAGEINFOPARAMMASK { 
  RIL_PARAM_MI_STATUS,
  RIL_PARAM_MI_MESSAGE,
  RIL_PARAM_MI_ALL
} RILMESSAGEINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_MI_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MI_MESSAGE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_MI_STATUS</td>
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