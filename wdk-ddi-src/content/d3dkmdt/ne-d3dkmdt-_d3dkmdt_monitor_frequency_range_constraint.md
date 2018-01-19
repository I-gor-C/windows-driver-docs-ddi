---
UID : NE:d3dkmdt._D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
title : _D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
author : windows-driver-content
description : The D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration is used to indicate the type of constraint under which a monitor frequency range is supported.
old-location : display\d3dkmdt_monitor_frequency_range_constraint.htm
old-project : display
ms.assetid : 12bf26fc-86c2-4b9b-82d4-1e8b2e38fa79
ms.author : windowsdriverdev
ms.date : 12/29/2017
ms.keywords : _D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT, D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : d3dkmdt.h
req.include-header : D3dkmdt.h
req.target-type : Windows
req.target-min-winverclnt : Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
req.alt-loc : d3dkmdt.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
req.typenames : D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
---

# _D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT Enumeration
The D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration is used to indicate the type of constraint under which a monitor frequency range is supported.

## Syntax
````
typedef enum _D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT { 
  D3DKMDT_MFRC_UNINITIALIZED  = 0,
  D3DKMDT_MFRC_ACTIVESIZE     = 1,
  D3DKMDT_MFRC_MAXPIXELRATE   = 2
} D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT;
````

## Constants

<table>

<tr>
<td>D3DKMDT_MFRC_ACTIVESIZE</td>
<td>Indicates that the constraint is an active region size.</td>
</tr>

<tr>
<td>D3DKMDT_MFRC_MAXPIXELRATE</td>
<td>Indicates that the constraint is a pixel rate.</td>
</tr>

<tr>
<td>D3DKMDT_MFRC_UNINITIALIZED</td>
<td>Indicates that a variable of type D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT has not yet been assigned a meaningful value.</td>
</tr>
</table>

## Remarks

The <b>ConstraintType</b> member of a <a href="..\d3dkmdt\ns-d3dkmdt-_d3dkmdt_monitor_frequency_range.md">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure is a value from the D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | d3dkmdt.h (include D3dkmdt.h) |