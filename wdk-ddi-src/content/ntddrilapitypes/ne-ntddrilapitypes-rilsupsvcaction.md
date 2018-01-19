---
UID : NE:ntddrilapitypes.RILSUPSVCACTION
title : RILSUPSVCACTION
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsupsvcaction.htm
old-project : netvista
ms.assetid : 14c9b97d-7f3f-45ef-9be2-c36495c69081
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSUPSVCACTION, RILSUPSVCACTION
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
req.alt-api : RILSUPSVCACTION
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
req.typenames : RILSUPSVCACTION
---

# RILSUPSVCACTION Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSUPSVCACTION { 
  RIL_SUPSVCACTION_DEACTIVATE,
  RIL_SUPSVCACTION_REGISTER,
  RIL_SUPSVCACTION_ERASE,
  RIL_SUPSVCACTION_INTERROGATE,
  RIL_SUPSVCACTION_REGISTER_PW,
  RIL_SUPSVCACTION_USSD,
  RIL_SUPSVCACTION_MAX
} RILSUPSVCACTION;
````

## Constants

<table>

<tr>
<td>RIL_SUPSVCACTION_DEACTIVATE</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_ERASE</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_INTERROGATE</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_MAX</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_REGISTER</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_REGISTER_PW</td>
<td></td>
</tr>

<tr>
<td>RIL_SUPSVCACTION_USSD</td>
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