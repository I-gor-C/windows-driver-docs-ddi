---
UID: NC.d3dkmddi.DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET
title: DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET
author: windows-driver-content
description: The pfnGetMonitorDescriptorSet function returns a handle to a monitor descriptor set object that is associated with a specified monitor.
old-location: display\dxgk_monitor_interface_pfngetmonitordescriptorset.htm
old-project: display
ms.assetid: e2244cd3-6630-440b-a4f7-1e0fa5702161
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
req.alt-api: pfnGetMonitorDescriptorSet
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

# DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET callback



## -description
<p>The <b>pfnGetMonitorDescriptorSet</b> function returns a handle to a monitor descriptor set object that is associated with a specified monitor.</p>


## -prototype

````
DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET pfnGetMonitorDescriptorSet;

NTSTATUS APIENTRY pfnGetMonitorDescriptorSet(
  _In_  const D3DKMDT_ADAPTER                     hAdapter,
  _In_  const D3DDDI_VIDEO_PRESENT_TARGET_ID      VideoPresentTargetId,
  _Out_       PD3DKMDT_HMONITORDESCRIPTORSET      *phMonitorDescriptorSet,
  _Out_ const DXGK_MONITORDESCRIPTORSET_INTERFACE **ppMonitorDescriptorSetInterface
)
{ ... }
````


## -parameters
<dl>

### -param hAdapter [in]

<dd>
<p>[in] A handle that identifies a display adapter. The Microsoft DirectX graphics kernel subsystem previously provided this handle to the display miniport driver in the <i>DxgkInterface</i> parameter of the <a href="display.dxgkddistartdevice">DxgkDdiStartDevice</a> function.</p>
</dd>

### -param VideoPresentTargetId [in]

<dd>
<p>[in] An integer that identifies one of the video present targets on the display adapter. The returned monitor descriptor set object contains descriptors for the monitor that is connected to this video present target.</p>
</dd>

### -param phMonitorDescriptorSet [out]

<dd>
<p>[out] A pointer to a variable that receives a handle to a monitor descriptor set object.</p>
</dd>

### -param ppMonitorDescriptorSetInterface [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitordescriptorset-interface.md">DXGK_MONITORDESCRIPTORSET_INTERFACE</a> structure. The structure contains pointers to functions that the display miniport driver can call to inspect and alter the monitor descriptor set object.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnGetMonitorDescriptorSet</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_DISPLAY_ADAPTER</b></dt>
</dl><p>The handle supplied in <i>hAdapter</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_VIDEO_PRESENT_TARGET</b></dt>
</dl><p>The identifier supplied in <i>VideoPresentTargetId</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_MONITOR_NOT_CONNECTED</b></dt>
</dl><p>There is no monitor connected to the video present target identified by <i>VideoPresentTargetId</i>.</p>

<p> </p>

## -remarks
<p>VidPN target identifiers are assigned by the display miniport driver. The <a href="display.dxgkddiquerychildrelations">DxgkDdiQueryChildRelations</a> function, implemented by the display miniport driver, returns an array of <a href="..\dispmprt\ns-dispmprt--dxgk-child-descriptor.md">DXGK_CHILD_DESCRIPTOR</a> structures, each of which contains an identifier.</p>

<p>You do not need to release the handle returned in <i>phMonitorDescriptorSet</i>.</p>

<p>This function is also available in the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitor-interface-v2.md">DXGK_MONITOR_INTERFACE_V2</a> interface beginning with Windows 7.</p>

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
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-monitor-interface-v2.md">DXGK_MONITOR_INTERFACE_V2</a>
</dt>
<dt>
<a href="display.dxgkddienumvidpncofuncmodality">DxgkDdiEnumVidPnCofuncModality</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGKDDI_MONITOR_GETMONITORDESCRIPTORSET callback function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
