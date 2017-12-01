---
UID: NC.d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO
title: DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO
author: windows-driver-content
description: The pfnAcquireFirstDescriptorInfo function returns the first descriptor in a monitor descriptor set object.
old-location: display\dxgk_monitordescriptorset_interface_pfnacquirefirstdescriptorinfo.htm
old-project: display
ms.assetid: 228f6947-a7e5-4b76-8224-fac6889fc77a
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
req.alt-api: pfnAcquireFirstDescriptorInfo
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

# DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO callback



## -description
<p>The <b>pfnAcquireFirstDescriptorInfo</b> function returns the first descriptor in a monitor descriptor set object.</p>


## -prototype

````
DXGKDDI_MONITORDESCRIPTORSET_ACQUIREFIRSTDESCRIPTORINFO pfnAcquireFirstDescriptorInfo;

NTSTATUS APIENTRY pfnAcquireFirstDescriptorInfo(
  _In_  const D3DKMDT_HMONITORDESCRIPTORSET hMonitorDescriptorSet,
  _Out_ const D3DKMDT_MONITOR_DESCRIPTOR    **ppFirstMonitorDescriptorInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorDescriptorSet</i> [in]

<dd>
<p>[in] A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="display.monitor_interface">Monitor interface</a>.</p>
</dd>

### -param <i>ppFirstMonitorDescriptorInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure. The structure is the first descriptor in the set.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquireFirstDescriptorInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function successfully returned the first descriptor in the set.</p><dl>
<dt><b>STATUS_GRAPHICS_DATASET_IS_EMPTY</b></dt>
</dl><p>The function succeeded, but there were no descriptors in the set.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl><p>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using the D3DKMDT_MONITOR_DESCRIPTOR structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-releasedescriptorinfo.md">pfnReleaseDescriptorInfo</a>.</p>

<p>You can obtain all the descriptors in a monitor descriptor set by calling <b>pfnAcquireFirstDescriptorInfo</b> and then making a sequence of calls to <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirenextdescriptorinfo.md">pfnAcquireNextDescriptorInfo</a>.</p>

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