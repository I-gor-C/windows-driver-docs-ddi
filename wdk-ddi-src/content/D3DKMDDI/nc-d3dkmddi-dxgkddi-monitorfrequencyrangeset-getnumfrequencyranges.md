---
UID: NC.d3dkmddi.DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES
title: DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES
author: windows-driver-content
description: The pfnGetNumFrequencyRanges returns the number of frequency range descriptors in a specified monitor frequency range set object.
old-location: display\dxgk_monitorfrequencyrangeset_interface_pfngetnumfrequencyranges.htm
ms.assetid: ba70c191-832f-4dd1-b949-cb47cf736c6e
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnGetNumFrequencyRanges
req.alt-loc: d3dkmddi.h
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
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
req.iface: 
---

# DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES callback



## -description
<p>The <b>pfnGetNumFrequencyRanges</b> returns the number of frequency range descriptors in a specified monitor frequency range set object.</p>


## -prototype

````
DXGKDDI_MONITORFREQUENCYRANGESET_GETNUMFREQUENCYRANGES pfnGetNumFrequencyRanges;

NTSTATUS APIENTRY pfnGetNumFrequencyRanges(
  _In_  const D3DKMDT_HMONITORFREQUENCYRANGESET hMonitorFrequencyRangeSet,
  _Out_       SIZE_T CONST                      *pNumMonitorFrequencyRanges
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorFrequencyRangeSet</i> [in]

<dd>
<p>[in] A handle to a monitor frequency range set object. The display miniport driver previously obtained this handle by calling the <b>pfnGetMonitorFrequencyRangeSet</b> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>. </p>
</dd>

### -param <i>pNumMonitorFrequencyRanges</i> [out]

<dd>
<p>[out] A pointer to a SIZE_T-typed variable that receives the number of descriptors in the set.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnGetNumFrequencyRanges</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_FREQUENCYRANGESET</b></dt>
</dl><p>The handle supplied in <i>hMonitorFrequencyRangeSet</i> was invalid.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
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
<dt>D3dkmddi.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>