---
UID: NC.d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO
title: DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO
author: windows-driver-content
description: The pfnAcquireNextDescriptorInfo function returns the next descriptor in a monitor descriptor set, given the current descriptor.
old-location: display\dxgk_monitordescriptorset_interface_pfnacquirenextdescriptorinfo.htm
old-project: display
ms.assetid: 34d048df-d4a1-4ef5-b917-791f35de9e3a
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
req.alt-api: pfnAcquireNextDescriptorInfo
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

# DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO callback



## -description
<p>The <b>pfnAcquireNextDescriptorInfo</b> function returns the next descriptor in a monitor descriptor set, given the current descriptor.</p>


## -prototype

````
DXGKDDI_MONITORDESCRIPTORSET_ACQUIRENEXTDESCRIPTORINFO pfnAcquireNextDescriptorInfo;

NTSTATUS APIENTRY pfnAcquireNextDescriptorInfo(
  _In_  const D3DKMDT_HMONITORDESCRIPTORSET    hMonitorDescriptorSet,
  _In_  const D3DKMDT_MONITOR_DESCRIPTOR CONST *pMonitorDescriptorInfo,
  _Out_ const D3DKMDT_MONITOR_DESCRIPTOR       **ppNextMonitorDescriptorInfo
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorDescriptorSet</i> [in]

<dd>
<p>[in] A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitor-getmonitordescriptorset.md">pfnGetMonitorDescriptorSet</a> function of the <a href="display.monitor_interface">Monitor interface</a>.</p>
</dd>

### -param <i>pMonitorDescriptorInfo</i> [in]

<dd>
<p>[in] A pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure that is the current descriptor. The display miniport driver previously obtained this pointer by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> or <b>pfnAcquireNextDescriptorInfo</b>. </p>
</dd>

### -param <i>ppNextMonitorDescriptorInfo</i> [out]

<dd>
<p>[out] A pointer to a variable that receives a pointer to a <a href="..\d3dkmdt\ns-d3dkmdt--d3dkmdt-monitor-descriptor.md">D3DKMDT_MONITOR_DESCRIPTOR</a> structure. The structure is the next descriptor in the set.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnAcquireNextDescriptorInfo</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function successfully returned the next descriptor in the set.</p><dl>
<dt><b>STATUS_GRAPHICS_NO_MORE_ELEMENTS_IN_DATASET</b></dt>
</dl><p>The function succeeded, but there were no more descriptors in the set.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_INVALID_MONITOR_DESCRIPTOR</b></dt>
</dl><p>The descriptor supplied in <i>pMonitorDescriptorInfo</i> was invalid.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl><p>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.</p>

<p> </p>

## -remarks
<p>When you have finished using the D3DKMDT_MONITOR_DESCRIPTOR structure, you must release the structure by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-releasedescriptorinfo.md">pfnReleaseDescriptorInfo</a>.</p>

<p>You can obtain all the descriptors in a monitor descriptor set by calling <a href="..\d3dkmddi\nc-d3dkmddi-dxgkddi-monitordescriptorset-acquirefirstdescriptorinfo.md">pfnAcquireFirstDescriptorInfo</a> and then making a sequence of calls to <b>pfnAcquireNextDescriptorInfo</b>.</p>

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