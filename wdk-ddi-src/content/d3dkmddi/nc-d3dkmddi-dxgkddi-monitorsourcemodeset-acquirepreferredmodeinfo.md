---
UID: NC.d3dkmddi.DXGKDDI_MONITORSOURCEMODESET_ACQUIREPREFERREDMODEINFO
title: DXGKDDI_MONITORSOURCEMODESET_ACQUIREPREFERREDMODEINFO
author: windows-driver-content
description: The pfnAcquirePreferredModeInfo returns a descriptor of the preferred mode in a specified monitor source mode set object.
old-location: display\dxgk_monitorsourcemodeset_interface_pfnacquirepreferredmodeinfo.htm
old-project: display
ms.assetid: 80d3d199-42ad-4f21-8122-05dfad37016d
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
req.alt-api: pfnAcquirePreferredModeInfo
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

# DXGKDDI_MONITORSOURCEMODESET_ACQUIREPREFERREDMODEINFO callback



## -description
<p>The <b>pfnAcquirePreferredModeInfo</b> returns a descriptor of the preferred mode in a specified monitor source mode set object.</p>


## -prototype

````
DXGKDDI_MONITORSOURCEMODESET_ACQUIREPREFERREDMODEINFO pfnAcquirePreferredModeInfo;

NTSTATUS APIENTRY pfnAcquirePreferredModeInfo(
  _In_  const D3DKMDT_HMONITORSOURCEMODESET hMonitorSourceModeSet,
  _Out_ const D3DKMDT_MONITOR_SOURCE_MODE   **ppFirstMonitorSourceModeInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorSourceModeSet</i> [in]

<dd>
<p>[in] A handle to a monitor source mode set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a> function of the <a href="display.monitor_interface">Monitor interface</a>.</p>
</dd>

### -param <i>ppFirstMonitorSourceModeInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-source-mode.md">D3DKMDT_MONITOR_SOURCE_MODE</a> structure. The structure contains a variety of information about the preferred monitor source mode, including its ID and video signal.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquirePreferredModeInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function successfully returned a descriptor of the preferred mode.</p><dl>
<dt><b>STATIS_GRAPHICS_NO_PREFERRED_MODE</b></dt>
</dl><p>The function succeeded, but the specified monitor source mode set does not have a preferred mode.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_SOURCEMODESET</b></dt>
</dl><p>The handle supplied in <i>hMonitorSourceModeSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using the <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-source-mode.md">D3DKMDT_MONITOR_SOURCE_MODE</a> structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitorsourcemodeset-releasemodeinfo.md">pfnReleaseModeInfo</a>.</p>

<p>The D3DKMDT_HMONITORSOURCEMODESET data type is defined in <i>D3dkmdt.h</i>. </p>

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