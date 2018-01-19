---
UID : NE:rilapitypes.RILSIGNALQUALITYPARAMMASK
title : RILSIGNALQUALITYPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilsignalqualityparammask_2.htm
old-project : netvista
ms.assetid : be6c46bb-9c14-4daf-b76a-679d71269965
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILSIGNALQUALITYPARAMMASK, RILSIGNALQUALITYPARAMMASK
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
req.alt-api : RILSIGNALQUALITYPARAMMASK
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
req.typenames : RILSIGNALQUALITYPARAMMASK
req.product : Windows 10 or later.
---

# RILSIGNALQUALITYPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILSIGNALQUALITYPARAMMASK { 
  RIL_PARAM_SQ_SYSTEMTYPE,
  RIL_PARAM_SQ_NUMSIGNALBARS,
  RIL_PARAM_SQ_SIGNALSTRENGTH,
  RIL_PARAM_SQ_SNR,
  RIL_PARAM_SQ_ALL
} RILSIGNALQUALITYPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_SQ_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SQ_NUMSIGNALBARS</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SQ_SIGNALSTRENGTH</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SQ_SNR</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_SQ_SYSTEMTYPE</td>
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