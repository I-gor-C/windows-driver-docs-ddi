---
UID: NS.d3dumddi.D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
title: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
author: windows-driver-content
description: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU is used with pfnSignalSynchronizationObjectFromGpuCb to signal a monitored fence.
old-location: display\d3dddicb_signalsynchronizationobjectfromgpu.htm
old-project: display
ms.assetid: FF098E63-842F-4D88-A184-BE886E0ED507
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU, D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU
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

# D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure



## -description
<p><b>D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU</b> is used with <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpucb.md">pfnSignalSynchronizationObjectFromGpuCb</a> to signal a monitored fence.</p>


## -syntax

````
typedef struct D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU {
  HANDLE              hContext;
  UINT                ObjectCount;
  const D3DKMT_HANDLE *ObjectHandleArray;
  union {
    const UINT64 *MonitoredFenceValueArray;
    UINT64       Reserved[8];
  };
} D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU;
````


## -struct-fields
<dl>

### -field <b>hContext</b>

<dd>
<p>[in] A kernel-mode handle to the context stream.</p>
</dd>

### -field <b>ObjectCount</b>

<dd>
<p>[in] The number of synchronization events in the <b>ObjectHandleArray</b> array and fence values in <b>MonitoredFenceValueArray</b> arrays.</p>
</dd>

### -field <b>ObjectHandleArray</b>

<dd>
<p>[in] An array of kernel-mode handles to the synchronization events that the <b>hContext</b> member signals.</p>
</dd>

### -field <b>MonitoredFenceValueArray</b>

<dd>
<p>[in] An array of 64-bit monitored fence values to signal, each of which correspond to a synchronization object in <b>ObjectHandleArray</b>.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved and should be set to zero.
</p>
</dd>
</dl>

## -remarks


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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-signalsynchronizationobjectfromgpucb.md">pfnSignalSynchronizationObjectFromGpuCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_SIGNALSYNCHRONIZATIONOBJECTFROMGPU structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
