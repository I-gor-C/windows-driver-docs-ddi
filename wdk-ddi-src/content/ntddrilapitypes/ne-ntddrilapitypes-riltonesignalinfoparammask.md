---
UID : NE:ntddrilapitypes.RILTONESIGNALINFOPARAMMASK
title : RILTONESIGNALINFOPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\riltonesignalinfoparammask.htm
old-project : netvista
ms.assetid : 5ebacb12-4ccd-4e92-ba73-b79c1969eb4f
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILTONESIGNALINFOPARAMMASK, RILTONESIGNALINFOPARAMMASK
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
req.alt-api : RILTONESIGNALINFOPARAMMASK
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
req.typenames : RILTONESIGNALINFOPARAMMASK
---

# RILTONESIGNALINFOPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILTONESIGNALINFOPARAMMASK { 
  RIL_PARAM_TONESIGNAL_GPP2TONE,
  RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING,
  RIL_PARAM_TONESIGNAL_EXECUTOR,
  RIL_PARAM_TONESIGNAL_All
} RILTONESIGNALINFOPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_TONESIGNAL_All</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_TONESIGNAL_EXECUTOR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_TONESIGNAL_GPP2ISDNALERTING</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_TONESIGNAL_GPP2TONE</td>
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