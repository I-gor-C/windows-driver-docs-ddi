---
UID : NE:ntddrilapitypes.RILCALLSUPPORTCAPS
title : RILCALLSUPPORTCAPS
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallsupportcaps.htm
old-project : netvista
ms.assetid : 1573a1bd-8c47-4fdc-89d1-242e91ff0e47
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLSUPPORTCAPS, RILCALLSUPPORTCAPS
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
req.alt-api : RILCALLSUPPORTCAPS
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
req.typenames : RILCALLSUPPORTCAPS
---

# RILCALLSUPPORTCAPS Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLSUPPORTCAPS { 
  RIL_CAPS_CALLSUPPORT_CD,
  RIL_CAPS_CALLSUPPORT_CNAP,
  RIL_CAPS_CALLSUPPORT_CUG,
  RIL_CAPS_CALLSUPPORT_EMLPP,
  RIL_CAPS_CALLSUPPORT_FM,
  RIL_CAPS_CALLSUPPORT_MSP,
  RIL_CAPS_CALLSUPPORT_USSD_PHASE2,
  RIL_CAPS_CALLSUPPORT_USS,
  RIL_CAPS_CALLSUPPORT_ALL
} RILCALLSUPPORTCAPS;
````

## Constants

<table>

<tr>
<td>RIL_CAPS_CALLSUPPORT_ALL</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_CD</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_CNAP</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_CUG</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_EMLPP</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_FM</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_MSP</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_USS</td>
<td></td>
</tr>

<tr>
<td>RIL_CAPS_CALLSUPPORT_USSD_PHASE2</td>
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