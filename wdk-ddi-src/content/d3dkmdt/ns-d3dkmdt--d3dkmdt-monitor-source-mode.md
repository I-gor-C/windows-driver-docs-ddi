---
UID: NS.d3dkmdt._D3DKMDT_MONITOR_SOURCE_MODE
title: D3DKMDT_MONITOR_SOURCE_MODE
author: windows-driver-content
description: The D3DKMDT_MONITOR_SOURCE_MODE structure contains information about a monitor source mode.
old-location: display\d3dkmdt_monitor_source_mode.htm
old-project: display
ms.assetid: bccacf88-b66b-4d55-b3a8-9d9b8cfcede8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMDT_MONITOR_SOURCE_MODE,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmdt.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMDT_MONITOR_SOURCE_MODE
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
req.irql: 
req.iface: 
---

# D3DKMDT_MONITOR_SOURCE_MODE structure



## -description
<p>The D3DKMDT_MONITOR_SOURCE_MODE structure contains information about a monitor source mode.</p>


## -syntax

````
typedef struct _D3DKMDT_MONITOR_SOURCE_MODE {
  D3DKMDT_MONITOR_SOURCE_MODE_ID      Id;
  D3DKMDT_VIDEO_SIGNAL_INFO           VideoSignalInfo;
  D3DKMDT_COLOR_BASIS                 ColorBasis;
  D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES  ColorCoeffDynamicRanges;
  D3DKMDT_MONITOR_CAPABILITIES_ORIGIN Origin;
  D3DKMDT_MODE_PREFERENCE             Preference;
} D3DKMDT_MONITOR_SOURCE_MODE;
````


## -struct-fields
<dl>

### -field <b>Id</b>

<dd>
<p>An integer that identifies the monitor source mode.</p>
</dd>

### -field <b>VideoSignalInfo</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff546625">D3DKMDT_VIDEO_SIGNAL_INFO</a> enumerator that indicates the video mode standard (if any) that defines the mode.</p>
</dd>

### -field <b>ColorBasis</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545984">D3DKMDT_COLOR_BASIS</a> enumerator that indicates the color basis of the mode.</p>
</dd>

### -field <b>ColorCoeffDynamicRanges</b>

<dd>
<p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff545986">D3DKMDT_COLOR_COEFF_DYNAMIC_RANGES</a> structure that contains the dynamic ranges for the color channels in the mode's color basis.</p>
</dd>

### -field <b>Origin</b>

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546075">D3DKMDT_MONITOR_CAPABILITIES_ORIGIN</a> enumeration that indicates the source of the mode information. For example the mode information could be from a default monitor profile or it could be from an override in an INF file.</p>
</dd>

### -field <b>Preference</b>

<dd>
<p>A value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff546061">D3DKMDT_MODE_PREFERENCE</a> enumeration that indicates whether the mode is the preferred mode in a <a href="display.monitor_source_mode_set_interface">monitor source mode set</a>.</p>
</dd>
</dl>

## -remarks
<p>The D3DKMDT_MONITOR_SOURCE_MODE_ID data type is defined in <i>D3dkmdt.h</i>.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546724">D3DKMDT_VIDPN_SOURCE_MODE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546729">D3DKMDT_VIDPN_TARGET_MODE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMDT_MONITOR_SOURCE_MODE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
