---
UID: NC.d3dkmddi.DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS
title: DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS
author: windows-driver-content
description: The pfnGetNumDescriptors function returns the number of descriptors in a monitor descriptor set.
old-location: display\dxgk_monitordescriptorset_interface_pfngetnumdescriptors.htm
ms.assetid: 7bfcef0b-1371-4e3b-b5dc-c4c548625c8f
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
req.alt-api: pfnGetNumDescriptors
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

# DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS callback



## -description
<p>The <b>pfnGetNumDescriptors</b> function returns the number of descriptors in a monitor descriptor set.</p>


## -prototype

````
DXGKDDI_MONITORDESCRIPTORSET_GETNUMDESCRIPTORS pfnGetNumDescriptors;

NTSTATUS APIENTRY pfnGetNumDescriptors(
  _In_  const D3DKMDT_HMONITORDESCRIPTORSET hMonitorDescriptorSet,
  _Out_       SIZE_T CONST                  *pNumMonitorDescriptors
)
{ ... }
````


## -parameters
<dl>

### -param <i>hMonitorDescriptorSet</i> [in]

<dd>
<p>[in] A handle to a monitor descriptor set object. The display miniport driver previously obtained this handle by calling the <a href="https://msdn.microsoft.com/e2244cd3-6630-440b-a4f7-1e0fa5702161">pfnGetMonitorDescriptorSet</a> function of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568433">Monitor interface</a>.</p>
</dd>

### -param <i>pNumMonitorDescriptors</i> [out]

<dd>
<p>[out] A SIZE_T-typed variable that receives the number of descriptors in the set.</p>
</dd>
</dl>

## -returns
<p>The <b>pfnGetNumDescriptors</b> function returns one of the following values.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The function succeeded.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was supplied.</p><dl>
<dt><b>STATUS_GRAPHICS_INVALID_MONITOR_DESCRIPTORSET</b></dt>
</dl><p>The handle supplied in <i>hMonitorDescriptorSet</i> was invalid.</p>

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