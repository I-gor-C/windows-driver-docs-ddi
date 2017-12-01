---
UID: NC.d3dumddi.PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB
title: PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB
author: windows-driver-content
description: pfnSignalSynchronizationObjectFromCpuCb enables a driver to signal a monitored fence.
old-location: display\pfnsignalsynchronizationobjectfromcpucb.htm
old-project: display
ms.assetid: E6FD5215-09CE-4DC8-B5AB-F65E68E2A884
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Desktop
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: pfnSignalSynchronizationObjectFromCpuCb
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB callback



## -description
<p><b>pfnSignalSynchronizationObjectFromCpuCb</b> enables a driver to signal a monitored fence.</p>


## -prototype

````
PFND3DDDI_SIGNALSYNCHRONIZATIONOBJECTFROMCPUCB pfnSignalSynchronizationObjectFromCpuCb;

HRESULT APIENTRY CALLBACK* pfnSignalSynchronizationObjectFromCpuCb(
  _In_ HANDLE                                      hDevice,
  _In_ D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU *pData
)
{ ... }
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the display device.</p>
</dd>

### -param <i>pData</i> [in]

<dd>
<p>A pointer to a <a href="..\d3dumddi\ns-d3dumddi-d3dddicb-signalsynchronizationobjectfromcpu.md">D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMCPU</a> structure that provides the details of the requested operation.</p>
</dd>
</dl>

## -returns
<p>If this callback function succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks
<p>When a monitored fence object is signaled by the CPU, the graphics kernel will update the fence memory location with the signaled value, so it becomes immediately visible to any user mode reader as well as immediately un-wait any satisfied waiters.
However, the caller cannot assume that the signal operation will be completed upon the return from this function. Instead, the caller should use appropriate <i>Wait</i> functions to check for signal completion.
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
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>