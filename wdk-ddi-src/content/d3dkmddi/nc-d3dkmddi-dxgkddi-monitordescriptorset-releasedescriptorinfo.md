---
UID: NC.d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO
title: DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO
author: windows-driver-content
description: The pfnReleaseDescriptorInfo function releases a D3DKMDT_MONITOR_DESCRIPTOR structure that the VidPN manager previously provided to the display miniport driver.
old-location: display\dxgk_monitordescriptorset_interface_pfnreleasedescriptorinfo.htm
old-project: display
ms.assetid: 8debdd01-c4e4-4b7c-b4cd-c1143ea7ebaa
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
req.alt-api: pfnReleaseDescriptorInfo
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

# DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO callback



## -description
<p>The <b>pfnReleaseDescriptorInfo</b> function releases a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure that the VidPN manager previously provided to the display miniport driver.</p>


## -prototype

````
DXGKDDI_MONITORDESCRIPTORSET_RELEASEDESCRIPTORINFO pfnReleaseDescriptorInfo;

NTSTATUS APIENTRY pfnReleaseDescriptorInfo(
  _In_ const D3DKMDT_HMONITORDESCRIPTORSET    hMonitorDescriptorSet,
  _In_ const D3DKMDT_MONITOR_DESCRIPTOR CONST *pMonitorDescriptorInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorDescriptorSet</i> [in]

<dd>
<p>A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="display.monitor_interface">Monitor interface</a>.</p>
</dd>

### -param <i>pMonitorDescriptorInfo</i> [in]

<dd>
<p>A pointer to the D3DKMDT_MONITOR_DESCRIPTOR structure to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnReleaseDescriptorInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_DESCRIPTOR</b></dt>
</dl><p>The descriptor supplied in <i>pMonitorDescriptorInfo</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl><p>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using a D3DKMDT_MONITOR_DESCRIPTOR structure that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> or <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirenextdescriptorinfo.md">pfnAcquireNextDescriptorInfo</a>, you must release it by calling <b>pfnReleaseDescriptorInfo</b>.</p>

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