---
UID : NE:ntddrilapitypes.RILCALLINFODIRECTION
title : RILCALLINFODIRECTION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallinfodirection.htm
old-project : netvista
ms.assetid : 2243fb04-81a9-49d6-9ce2-d06d4a590fb1
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLINFODIRECTION, RILCALLINFODIRECTION
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
req.alt-api : RILCALLINFODIRECTION
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
req.typenames : RILCALLINFODIRECTION
---

# RILCALLINFODIRECTION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLINFODIRECTION { 
  RIL_CALLDIR_OUTGOING,
  RIL_CALLDIR_MAX
} RILCALLINFODIRECTION;
````

## Constants

<table>

<tr>
<td>RIL_CALLDIR_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLDIR_OUTGOING</td>
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