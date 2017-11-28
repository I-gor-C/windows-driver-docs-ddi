---
UID: NS.d3dumddi._D3DDDICB_PRESENT
title: D3DDDICB_PRESENT
author: windows-driver-content
description: The D3DDDICB_PRESENT structure describes allocations that content is copied to and from.
old-location: display\d3dddicb_present.htm
old-project: display
ms.assetid: 086d95a3-1b3a-4e09-9a39-e1972e0e306c
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDICB_PRESENT, D3DDDICB_PRESENT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDICB_PRESENT
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

# D3DDDICB_PRESENT structure



## -description
<p>The D3DDDICB_PRESENT structure describes allocations that content is copied to and from. </p>


## -syntax

````
typedef struct _D3DDDICB_PRESENT {
  D3DKMT_HANDLE hSrcAllocation;
  D3DKMT_HANDLE hDstAllocation;
  HANDLE        hContext;
  UINT          BroadcastContextCount;
  HANDLE        BroadcastContext[D3DDDI_MAX_BROADCAST_CONTEXT];
} D3DDDICB_PRESENT;
````


## -struct-fields
<dl>

### -field <b>hSrcAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the source allocation. The Microsoft Direct3D runtime's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a> function returns this handle. Therefore, the user-mode display driver should use this handle to copy content from.</p>
</dd>

### -field <b>hDstAllocation</b>

<dd>
<p>[in] A D3DKMT_HANDLE data type that represents a kernel-mode handle to the destination allocation. <b>hDstAllocation</b> can be zero if the destination is unknown; kernel mode will determine the destination just before DMA of the hardware command stream to the graphics processor.</p>
</dd>

### -field <b>hContext</b>

<dd>
<p>[in] A handle to the context that the driver submits the copy operation to. The user-mode display driver previously created this context by calling the <a href="https://msdn.microsoft.com/f3f5d6bc-3bc6-4214-830a-cffff01069cc">pfnCreateContextCb</a> function. </p>
</dd>

### -field <b>BroadcastContextCount</b>

<dd>
<p>[in] The number of additional contexts in the array that the <b>BroadcastContext</b> member specifies.</p>
</dd>

### -field <b>BroadcastContext</b>

<dd>
<p>[in] An array of handles to the additional contexts to broadcast the current present operation to. The D3DDDI_MAX_BROADCAST_CONTEXT constant, which is defined as 64, defines the maximum number of additional contexts that the user-mode display driver can broadcast the current present operation to. </p>
<p>Broadcasting is supported only for flip operations. To broadcast a flip operation, the display miniport driver must support memory mapped I/O (MMIO)-based flips. To indicate support of MMIO flips, the display miniport driver sets the <b>FlipOnVSyncMmIo</b> bit-field flag in the <b>FlipCaps</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561062">DXGK_DRIVERCAPS</a> structure when its <a href="display.dxgkddiqueryadapterinfo">DxgkDdiQueryAdapterInfo</a> function is called.</p>
<p>The original context that the <b>hContext</b> member specifies and that the user-mode display driver presents to is not an element in the <b>BroadcastContext</b> array. For example, if the <b>BroadcastContext</b> array contains one element, the user-mode display driver sends the present operation to the owning context (<b>hContext</b>) and broadcasts to that one additional context. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
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
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-allocatecb.md">pfnAllocateCb</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-presentcb.md">pfnPresentCb</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDICB_PRESENT structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
