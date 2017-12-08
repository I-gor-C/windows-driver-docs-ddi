---
UID: NS.d3dumddi.D3DDDICB_PRESENTMULTIPLANEOVERLAY
title: D3DDDICB_PRESENTMULTIPLANEOVERLAY
author: windows-driver-content
description: Describes multiplane overlay allocations that content is copied to and from.
old-location: display\d3dddicb_presentmultiplaneoverlay.htm
old-project: display
ms.assetid: 4161418c-4f56-4daf-bf3d-e76899ccd1b2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_PRESENTMULTIPLANEOVERLAY, D3DDDICB_PRESENTMULTIPLANEOVERLAY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_PRESENTMULTIPLANEOVERLAY
req.alt-loc: D3dumddi.h
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

# D3DDDICB_PRESENTMULTIPLANEOVERLAY structure



## -description
<p>Describes multiplane overlay allocations that content is copied to and from.</p>


## -syntax

````
typedef struct D3DDDICB_PRESENTMULTIPLANEOVERLAY {
  HANDLE                            hContext;
  UINT                              BroadcastContextCount;
  HANDLE                            BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
  UINT                              AllocationInfoCount;
  D3DDDI_MULTIPLANE_ALLOCATION_INFO AllocationInfo[D3DDDI_MAX_MULTIPLANE_OVERLAY_ALLOCATIONS];
} D3DDDICB_PRESENTMULTIPLANEOVERLAY;
````


## -struct-fields
<dl>

### -field hContext

<dd>
<p>[in] A handle to the context that the driver submits the copy operation to. The user-mode display driver previously created this context by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function.</p>
</dd>

### -field BroadcastContextCount

<dd>
<p>[in] The number of additional contexts in the array that the <b>BroadcastContext</b> member specifies.</p>
</dd>

### -field BroadcastContext

<dd>
<p>[in] An array of handles to the additional contexts to broadcast the current present operation to. The <b>D3DDDI_MAX_BROADCAST_CONTEXT</b> constant, which is defined as 64, defines the maximum number of additional contexts that the user-mode display driver can broadcast the current present operation to. </p>
<p>Broadcasting is supported only for flip operations. To broadcast a flip operation, the display miniport driver must support memory mapped I/O (MMIO)-based flips. To indicate support of MMIO flips, the display miniport driver sets the <b>FlipOnVSyncMmIo</b> bit-field flag in the <b>FlipCaps</b> member of the <a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a> structure when its <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function is called.</p>
<p>The original context that the <b>hContext</b> member specifies and that the user-mode display driver presents to is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the user-mode display driver sends the present operation to the owning context (<b>hContext</b>) and broadcasts to that one additional context. </p>
</dd>

### -field AllocationInfoCount

<dd>
<p>[in] The number of allocations in the array that the <b>AllocationInfo</b> member specifies. The maximum number is 16, the value of the <b>D3DDDI_MAX_MULTIPLANE_OVERLAY_ALLOCATIONS</b> constant.</p>
</dd>

### -field AllocationInfo

<dd>
<p>An array of structures of type <a href="display.d3dddi_multiplane_allocation_info">D3DDDI_MULTIPLANE_ALLOCATION_INFO</a> that specify info about the multiplane overlay allocations.</p>
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
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
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
<a href="display.d3dddi_multiplane_allocation_info">D3DDDI_MULTIPLANE_ALLOCATION_INFO</a>
</dt>
<dt>
<a href="..\d3dkmddi\ns-d3dkmddi--dxgk-drivercaps.md">DXGK_DRIVERCAPS</a>
</dt>
<dt>
<a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_PRESENTMULTIPLANEOVERLAY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
