---
UID: NE.d3dkmdt._D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
title: D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
author: windows-driver-content
description: The D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration is used to indicate the type of constraint under which a monitor frequency range is supported.
old-location: display\d3dkmdt_monitor_frequency_range_constraint.htm
ms.assetid: 12bf26fc-86c2-4b9b-82d4-1e8b2e38fa79
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT
req.alt-loc: d3dkmdt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO, DXGK_CHECK_MULTIPLANE_OVERLAY_SUPPORT_RETURN_INFO
req.iface: 
---

# D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration



## -description
<p>The D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration is used to indicate the type of constraint under which a monitor frequency range is supported.</p>


## -syntax

````
typedef enum _D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT { 
  D3DKMDT_MFRC_UNINITIALIZED  = 0,
  D3DKMDT_MFRC_ACTIVESIZE     = 1,
  D3DKMDT_MFRC_MAXPIXELRATE   = 2
} D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT;
````


## -enum-fields
<dl>

### -field <a id="D3DKMDT_MFRC_UNINITIALIZED"></a><a id="d3dkmdt_mfrc_uninitialized"></a><b>D3DKMDT_MFRC_UNINITIALIZED</b>

<dd>
<p>Indicates that a variable of type D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="D3DKMDT_MFRC_ACTIVESIZE"></a><a id="d3dkmdt_mfrc_activesize"></a><b>D3DKMDT_MFRC_ACTIVESIZE</b>

<dd>
<p>Indicates that the constraint is an active region size.</p>
</dd>

### -field <a id="D3DKMDT_MFRC_MAXPIXELRATE"></a><a id="d3dkmdt_mfrc_maxpixelrate"></a><b>D3DKMDT_MFRC_MAXPIXELRATE</b>

<dd>
<p>Indicates that the constraint is a pixel rate.</p>
</dd>
</dl>

## -remarks
<p>The <b>ConstraintType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546103">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure is a value from the D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration.</p>

<p>The <b>ConstraintType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546103">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure is a value from the D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration.</p>

<p>The <b>ConstraintType</b> member of a <a href="https://msdn.microsoft.com/library/windows/hardware/ff546103">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure is a value from the D3DKMDT_MONITOR_FREQUENCY_RANGE_CONSTRAINT enumeration.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmdt.h (include D3dkmdt.h)</dt>
</dl>
</td>
</tr>
</table>