---
UID : NE:rilapitypes.RILCALLHANDOVERPHASE
title : RILCALLHANDOVERPHASE
author : windows-driver-content
description : This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location : netvista\rilcallhandoverphase_2.htm
old-project : netvista
ms.assetid : 181363b5-08fa-4a6b-aa91-c9827a82b80e
ms.author : windowsdriverdev
ms.date : 1/11/2018
ms.keywords : RILCALLHANDOVERPHASE, RILCALLHANDOVERPHASE
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
req.alt-api : RILCALLHANDOVERPHASE
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
req.typenames : RILCALLHANDOVERPHASE
req.product : Windows 10 or later.
---

# RILCALLHANDOVERPHASE Enumeration
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
````
typedef enum _RILCALLHANDOVERPHASE { 
  RIL_CALLHANDOVERPHASE_COMPLETED,
  RIL_CALLHANDOVERPHASE_FAILED,
  RIL_CALLHANDOVERPHASE_CANCELLED,
  RIL_CALLHANDOVERPHASE_MAX
} RILCALLHANDOVERPHASE;
````

## Constants

<table>

<tr>
<td>RIL_CALLHANDOVERPHASE_CANCELLED</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLHANDOVERPHASE_COMPLETED</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLHANDOVERPHASE_FAILED</td>
<td></td>
</tr>

<tr>
<td>RIL_CALLHANDOVERPHASE_MAX</td>
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