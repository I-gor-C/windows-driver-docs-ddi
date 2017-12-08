---
UID: NS.d3dkmddi._DXGK_MONITOR_INTERFACE_V2
title: DXGK_MONITOR_INTERFACE_V2
author: windows-driver-content
description: The DXGK_MONITOR_INTERFACE_V2 structure, available beginning with Windows 7, contains pointers to functions that belong to the Monitor Interface, which is implemented by the video present network (VidPN) manager.
old-location: display\dxgk_monitor_interface_v2.htm
old-project: display
ms.assetid: 5c08b988-2cc0-46e1-a8b5-66de840650e4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MONITOR_INTERFACE_V2,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmddi.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITOR_INTERFACE_V2
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

# DXGK_MONITOR_INTERFACE_V2 structure



## -description
<p>The DXGK_MONITOR_INTERFACE_V2 structure, available beginning with Windows 7, contains pointers to functions that belong to the <a href="display.monitor_interface">Monitor Interface</a>, which is implemented by the video present network (VidPN) manager.</p>


## -syntax

````
typedef struct _DXGK_MONITOR_INTERFACE_V2 {
  DXGK_MONITOR_INTERFACE_VERSION                  Version;
  DXGKDDI_MONITOR_ACQUIREMONITORSOURCEMODESET     pfnAcquireMonitorSourceModeSet;
  DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET     pfnReleaseMonitorSourceModeSet;
  DXGKDDI_MONITOR_GETMONITORFREQUENCYRANGESET     pfnGetMonitorFrequencyRangeSet;
  DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET         pfnGetMonitorDescriptorSet;
  DXGKDDI_MONITOR_GETADDITIONALMONITORMODESET     pfnGetAdditionalMonitorModeSet;
  DXGKDDI_MONITOR_RELEASEADDITIONALMONITORMODESET pfnReleaseAdditionalMonitorModeSet;
} DXGK_MONITOR_INTERFACE_V2;
````


## -struct-fields
<dl>

### -field Version

<dd>
<p>A value from the <a href="..\d3dkmddi\ne-d3dkmddi--dxgk-monitor-interface-version.md">DXGK_MONITOR_INTERFACE_VERSION</a> enumeration that indicates the monitor interface version. Must be set to 2.</p>
</dd>

### -field pfnAcquireMonitorSourceModeSet

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a> function.</p>
</dd>

### -field pfnReleaseMonitorSourceModeSet

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-releasemonitorsourcemodeset.md">pfnReleaseMonitorSourceModeSet</a> function.</p>
</dd>

### -field pfnGetMonitorFrequencyRangeSet

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitorfrequencyrangeset.md">pfnGetMonitorFrequencyRangeSet</a> function.</p>
</dd>

### -field pfnGetMonitorDescriptorSet

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function.</p>
</dd>

### -field pfnGetAdditionalMonitorModeSet

<dd>
<p>A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getadditionalmonitormodeset.md">pfnGetAdditionalMonitorModeSet</a> function.</p>
</dd>

### -field pfnReleaseAdditionalMonitorModeSet

<dd>
<p>
      A pointer to the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-releaseadditionalmonitormodeset.md">pfnReleaseAdditionalMonitorModeSet</a> function.
     </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of the Windows operating systems.</p>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitor-interface.md">DXGK_MONITOR_INTERFACE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MONITOR_INTERFACE_V2 structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
