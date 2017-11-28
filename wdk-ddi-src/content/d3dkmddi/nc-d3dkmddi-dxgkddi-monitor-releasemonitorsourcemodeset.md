---
UID: NC.d3dkmddi.DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET
title: DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET
author: windows-driver-content
description: The pfnReleaseMonitorSourceModeSet function releases a handle to a monitor source mode set object.
old-location: display\dxgk_monitor_interface_pfnreleasemonitorsourcemodeset.htm
old-project: display
ms.assetid: af5f4a1b-232c-4192-96b4-8fa31dfe3019
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
req.alt-api: pfnReleaseMonitorSourceModeSet
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

# DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET callback



## -description
<p>The <b>pfnReleaseMonitorSourceModeSet</b> function releases a handle to a monitor source mode set object.</p>


## -prototype

````
DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET pfnReleaseMonitorSourceModeSet;

NTSTATUS APIENTRY pfnReleaseMonitorSourceModeSet(
  _In_ const D3DKMDT_ADAPTER               hAdapter,
  _In_ const D3DKMDT_HMONITORSOURCEMODESET hMonitorSourceModeSet
)
{ ... }
````


## -parameters
<dl>

### -param <i>hAdapter</i> [in]

<dd>
<p>[in] A handle that identifies a display adapter. The Microsoft DirectX graphics kernel subsystem previously provided this handle to the display miniport driver in the <i>DxgkInterface</i> parameter of the <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -param <i>hMonitorSourceModeSet</i> [in]

<dd>
<p>[in] The handle to be released.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnReleaseMonitorSourceModeSet</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_DISPLAY_ADAPTER</b></dt>
</dl><p>The handle supplied in <i>hAdapter</i> was invalid.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_SOURCEMODESET</b></dt>
</dl><p>The handle supplied in <i>hMonitorSourceModeSet</i> was invalid.</p>

<p> </p>

<p>This function might also return other error codes that are defined in <i>Ntstatus.h</i>.</p>

## -remarks
<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a>, you must release the handle by calling <b>pfnReleaseMonitorSourceModeSet</b>.</p>

<p>This function is also available in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561968">DXGK_MONITOR_INTERFACE_V2</a> interface beginning with Windows 7.</p>

<p>When you have finished using a handle that you obtained by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-acquiremonitorsourcemodeset.md">pfnAcquireMonitorSourceModeSet</a>, you must release the handle by calling <b>pfnReleaseMonitorSourceModeSet</b>.</p>

<p>This function is also available in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561968">DXGK_MONITOR_INTERFACE_V2</a> interface beginning with Windows 7.</p>

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

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561968">DXGK_MONITOR_INTERFACE_V2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_MONITOR_RELEASEMONITORSOURCEMODESET callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
