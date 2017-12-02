---
UID: NF.d3dkmthk.D3DKMTSignalSynchronizationObjectFromCpu
title: D3DKMTSignalSynchronizationObjectFromCpu
author: windows-driver-content
description: D3DKMTSignalSynchronizationObjectFromCpu enables a driver to signal a monitored fence.D3DKMTSignalSynchronizationObjectFromCpu enables a driver to signal a monitored fence.
old-location: display\d3dkmtsignalsynchronizationobjectfromcpu.htm
old-project: display
ms.assetid: 23DC5EB1-E606-499D-B78A-AFF95E6B00A3
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMTSignalSynchronizationObjectFromCpu
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Universal
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMTSignalSynchronizationObjectFromCpu
req.alt-loc: GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-1.dll,GDI32.dll,API-MS-Win-DX-D3DKMT-L1-1-2.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: GDI32.lib
req.dll: GDI32.dll
req.irql: 
req.iface: 
---

# D3DKMTSignalSynchronizationObjectFromCpu function



## -description
<p>
<p><b>D3DKMTSignalSynchronizationObjectFromCpu</b> enables a driver to signal a monitored fence.</p>
</p>
<p><b>D3DKMTSignalSynchronizationObjectFromCpu</b> enables a driver to signal a monitored fence.</p>


## -syntax

````
HRESULT APIENTRY D3DKMTSignalSynchronizationObjectFromCpu(
  _In_ const D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMCPU *pData
);
````


## -parameters
<dl>

### -param pData [in]

<dd>
<p>A pointer to a <a href="..\d3dkmthk\ns-d3dkmthk--d3dkmt-signalsynchronizationobjectfromcpu.md">D3DKMT_SIGNALSYNCHRONIZATIONOBJECTFROMCPU</a> structure that provides the details of the requested operation..</p>
</dd>
</dl>

## -returns
<p><b>D3DKMTSignalSynchronizationObjectFromCpu</b> returns one of the following values:</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The operation was successful.</p>

<p> </p>

<p>This function might also return other values.</p>

## -remarks
<p>When a monitored fence object is signaled by the CPU, the graphics kernel will update the fence memory location with the signaled value, so it becomes immediately visible to any user mode reader as well as immediately un-wait any satisfied waiters.
However, the caller cannot assume that the signal operation will be completed upon the return from this function. Instead, the caller should use appropriate Wait functions to check for signal completion.
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>GDI32.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>GDI32.dll</dt>
</dl>
</td>
</tr>
</table>