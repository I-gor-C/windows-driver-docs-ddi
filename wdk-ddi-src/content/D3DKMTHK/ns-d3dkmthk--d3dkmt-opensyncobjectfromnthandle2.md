---
UID: NS.d3dkmthk._D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
title: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
author: windows-driver-content
description: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 is used with D3DKMTOpenSyncObjectFromNtHandle2 to open a monitored fence object.
old-location: display\d3dkmt_opensyncobjectfromnthandle2.htm
ms.assetid: 7C5F9ACF-AA21-4A2B-B943-3B1D940284E1
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
req.alt-loc: D3dkmthk.h
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
ms.keywords: D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2, D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2
req.iface: 
---

# D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure



## -description
<p><b>D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a> to open a monitored fence object.</p>


## -syntax

````
typedef struct _D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 {
  HANDLE                             hNtHandle;
  D3DKMT_HANDLE                      hDevice;
  D3DDDI_SYNCHRONIZATIONOBJECT_FLAGS Flags;
  D3DKMT_HANDLE                      hSyncObject;
  union {
    struct {
      VOID                   *FenceValueCPUVirtualAddress;
      D3DGPU_VIRTUAL_ADDRESS FenceValueGPUVirtualAddress;
      UINT                   EngineAffinity;
    } MonitoredFence;
    UINT64 Reserved[8];
  };
} D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2;
````


## -struct-fields
<dl>

### -field <b>hNtHandle</b>

<dd>
<p>[in] NT handle for the sync object to be opened.</p>
</dd>

### -field <b>hDevice</b>

<dd>
<p>[in] Device handle to use this sync object on.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>[in] Specifies the desired sync object behavior for this device, such as wait and signal semantics and TDR handling.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>[out] Handle to the sync object that can be used in this process.</p>
</dd>

### -field <b>MonitoredFence</b>

<dd>
<p>Contains sync object virtual addresses that can be used in this process.</p>
<dl>

### -field <b>FenceValueCPUVirtualAddress</b>

<dd>
<p>[out] A read-only mapping of the fence value for the CPU. This is a user mode address readable from the process that created the monitored fence object. For 32 bit platforms that support 64 bit atomic reads via methods such as <code>InterlockedCompareExchange64(pointer,0,0)</code>, the mapping will be made read-write instead of read-only to avoid an access violation during the interlocked operation. Depending on the value of <b>No64BitAtomics</b> cap, this address points to either a 32 bit or a 64 bit underlying value.</p>
</dd>

### -field <b>FenceValueGPUVirtualAddress</b>

<dd>
<p>[out] A read-write mapping of the fence value for the GPU. A driver can signal a new fence value by inserting a GPU write command for this address into a command buffer, and the DirectX graphics  kernel will unblock waiters for this fence object value. This GPU virtual address is mapped asynchronously, and the driver should wait for the device that opened or created the monitored fence synchronization object to reach <b>PagingFenceValue</b> on its paging fence object prior to accessing this GPU virtual address. Depending on the value of <b>No64BitAtomics</b> cap, this address points to either a 32 bit or a 64 bit underlying value.</p>
</dd>

### -field <b>EngineAffinity</b>

<dd>
<p>[in] A bit field, where each bit position (starting from zero) defines a physical adapter index in an linked display adapter link where the GPU virtual address will be committed. Zero means that GPU virtual address will be committed to all physical adapters.</p>
</dd>
</dl>
</dd>

### -field <b>Reserved</b>

<dd>
<p>The consolidated value of the <b>MonitoredFence</b> structure.</p>
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
<dt>D3dkmthk.h (include D3dkmthk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906778">D3DKMTOpenSyncObjectFromNtHandle2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_OPENSYNCOBJECTFROMNTHANDLE2 structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
