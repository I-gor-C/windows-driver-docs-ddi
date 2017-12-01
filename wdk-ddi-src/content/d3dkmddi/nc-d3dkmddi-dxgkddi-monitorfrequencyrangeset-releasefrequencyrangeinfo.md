---
UID: NC.d3dkmddi.DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO
title: DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO
author: windows-driver-content
description: The pfnReleaseFrequencyRangeInfo function releases a D3DKMDT_MONITOR_FREQUENCY_RANGE structure that the VidPN manager previously provided to the display miniport driver.
old-location: display\dxgk_monitorfrequencyrangeset_interface_pfnreleasefrequencyrangeinfo.htm
old-project: display
ms.assetid: 54e3d08b-5f0d-4d98-9b93-e2aec96d3362
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DD_MULTISAMPLEQUALITYLEVELSDATA, DD_MULTISAMPLEQUALITYLEVELSDATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnReleaseFrequencyRangeInfo
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
req.iface: 
---

# DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO callback



## -description
<p>The <b>pfnReleaseFrequencyRangeInfo</b> function releases a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-frequency-range.md">D3DKMDT_MONITOR_FREQUENCY_RANGE</a> structure that the VidPN manager previously provided to the display miniport driver.</p>


## -prototype

````
DXGKDDI_MONITORFREQUENCYRANGESET_RELEASEFREQUENCYRANGEINFO pfnReleaseFrequencyRangeInfo;

NTSTATUS APIENTRY pfnReleaseFrequencyRangeInfo(
  _In_ const D3DKMDT_HMONITORFREQUENCYRANGESET     hMonitorFrequencyRangeSet,
  _In_ const D3DKMDT_MONITOR_FREQUENCY_RANGE CONST *pMonitorFrequencyRangeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorFrequencyRangeSet</i> [in]

<dd>
<p>[in] A handle to a monitor frequency range set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitorfrequencyrangeset.md">pfnGetMonitorFrequencyRangeSet</a> function of the <a href="display.monitor_interface">Monitor interface</a>.</p>
</dd>

### -param <i>pMonitorFrequencyRangeInfo</i> [in]

<dd>
<p>[in] A pointer to the D3DKMDT_MONITOR_FREQUENCY_RANGE structure that is to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquireNextFrequencyRangeInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_FREQUENCY_RANGE</b></dt>
</dl><p>The frequency range descriptor supplied in <i>pMonitorFrequencyRangeInfo</i> was invalid.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_FREQUENCYRANGESET</b></dt>
</dl><p>The handle supplied in <i>hMonitorFrequencyRangeSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using a D3DKMDT_MONITOR_FREQUENCY_RANGE structure that you obtained by calling <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirefirstfrequencyrangei">pfnAcquireFirstFrequencyRangeInfo</a> or <a href="display.dxgk_monitorfrequencyrangeset_interface_pfnacquirenextfrequencyrangein">pfnAcquireNextFrequencyRangeInfo</a>, you must release it by calling <b>pfnReleaseFrequencyRangeInfo</b>.</p>

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