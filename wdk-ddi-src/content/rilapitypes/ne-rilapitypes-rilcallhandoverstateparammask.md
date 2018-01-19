---
UID : NE:rilapitypes.RILCALLHANDOVERSTATEPARAMMASK
title : RILCALLHANDOVERSTATEPARAMMASK
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallhandoverstateparammask_2.htm
old-project : netvista
ms.assetid : a9a5c8dc-8ffa-4142-879c-3a782b45dbff
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLHANDOVERSTATEPARAMMASK, RILCALLHANDOVERSTATEPARAMMASK
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
req.alt-api : RILCALLHANDOVERSTATEPARAMMASK
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
req.typenames : RILCALLHANDOVERSTATEPARAMMASK
req.product : Windows 10 or later.
---

# RILCALLHANDOVERSTATEPARAMMASK Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLHANDOVERSTATEPARAMMASK { 
  RIL_PARAM_HANDOVER_OLD_TYPE,
  RIL_PARAM_HANDOVER_NEW_TYPE,
  RIL_PARAM_HANDOVER_3GPPCAUSE,
  RIL_PARAM_HANDOVER_ALL
} RILCALLHANDOVERSTATEPARAMMASK;
````

## Constants

<table>

<tr>
<td>RIL_PARAM_HANDOVER_3GPPCAUSE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HANDOVER_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HANDOVER_NEW_TYPE</td>
<td></td>
</tr>

<tr>
<td>RIL_PARAM_HANDOVER_OLD_TYPE</td>
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