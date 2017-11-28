---
UID: NS.d3dkmthk._D3DKMT_CREATEPAGINGQUEUE
title: D3DKMT_CREATEPAGINGQUEUE
author: windows-driver-content
description: D3DKMT_CREATEPAGINGQUEUE is used with D3DKMTCreatePagingQueue to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident.
old-location: display\d3dkmt_createpagingqueue.htm
old-project: display
ms.assetid: F7C2847F-D095-4A79-ADBB-DA0745E3192A
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_CREATEPAGINGQUEUE, D3DKMT_CREATEPAGINGQUEUE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: D3dkmthk.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_CREATEPAGINGQUEUE
req.alt-loc: d3dkmthk.h
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

# D3DKMT_CREATEPAGINGQUEUE structure



## -description
<p><b>D3DKMT_CREATEPAGINGQUEUE</b> is used with <a href="https://msdn.microsoft.com/library/windows/hardware/dn906771">D3DKMTCreatePagingQueue</a> to create a device paging queue that can be used to synchronize with video memory management operations for the device, such as making the device resource resident.</p>


## -syntax

````
typedef struct _D3DKMT_CREATEPAGINGQUEUE {
  D3DKMT_HANDLE               hDevice;
  D3DDDI_PAGINGQUEUE_PRIORITY Priority;
  D3DKMT_HANDLE               hPagingQueue;
  D3DKMT_HANDLE               hSyncObject;
  VOID                        *FenceValueCPUVirtualAddress;
  UINT                        PhysicalAdapterIndex;
} D3DKMT_CREATEPAGINGQUEUE;
````


## -struct-fields
<dl>

### -field <b>hDevice</b>

<dd>
<p>[in] Device to create a new paging queue object for.</p>
</dd>

### -field <b>Priority</b>

<dd>
<p>[in] Scheduling priority relative to other paging queues on this device. Paging queues with higher priority values will be processed ahead of paging queues with lower priority values.</p>
</dd>

### -field <b>hPagingQueue</b>

<dd>
<p>[out] A paging queue handle that will be used to synchronize paging operations.</p>
</dd>

### -field <b>hSyncObject</b>

<dd>
<p>[out] Handle to the monitored fence object used to synchronize paging operations for this paging queue. Destroying the paging queue (either implicitly or explicitly) will automatically destroy this sync object.</p>
</dd>

### -field <b>FenceValueCPUVirtualAddress</b>

<dd>
<p>[out] A read-only mapping of the paging fence object value for the CPU. This is a user mode address readable from the process that created the monitored fence object.</p>
</dd>

### -field <b>PhysicalAdapterIndex</b>

<dd>
<p>[in] Physical adapter index (engine ordinal) for the queue.</p>
</dd>
</dl>

## -remarks
<p>A device can have multiple paging queues created for it. Paging queues can be destroyed either explicitly by calling <a href="https://msdn.microsoft.com/library/windows/hardware/dn906773">D3DKMTDestroyPagingQueue</a>, or by implicitly destroying the device they belong to. After the latter, paging queue handles will become invalid.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906771">D3DKMTCreatePagingQueue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn906773">D3DKMTDestroyPagingQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DKMT_CREATEPAGINGQUEUE structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
