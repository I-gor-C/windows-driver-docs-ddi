---
UID: NF.wdm.IoInitializeWorkItem
title: IoInitializeWorkItem function
author: windows-driver-content
description: The IoInitializeWorkItem routine initializes a work item that the caller has already allocated.
old-location: kernel\ioinitializeworkitem.htm
old-project: kernel
ms.assetid: b7f4370e-75db-4238-8e23-9e48028a03f5
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoInitializeWorkItem
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoInitializeWorkItem
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: Any level
req.product: Windows 10 or later.
---

# IoInitializeWorkItem function



## -description
The <b>IoInitializeWorkItem</b> routine initializes a work item that the caller has already allocated.



## -syntax

````
VOID IoInitializeWorkItem(
  _In_ PVOID        IoObject,
  _In_ PIO_WORKITEM IoWorkItem
);
````


## -parameters

### -param IoObject [in]

Pointer to the caller's driver object or to one of the caller's device objects. If the caller will later pass the work item to <a href="kernel.ioqueueworkitem">IoQueueWorkItem</a>, <i>IoObject</i> must point to a device object.


### -param IoWorkItem [in]

Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550679">IO_WORKITEM</a> structure to initialize.


## -returns
None


## -remarks
The driver allocates its own storage for an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550679">IO_WORKITEM</a> structure, and then calls <b>IoInitializeWorkItem</b> to initialize it. Memory must be allocated from nonpaged pool. To determine the number of bytes that is necessary to hold an <b>IO_WORKITEM</b> structure, call <a href="kernel.iosizeofworkitem">IoSizeofWorkItem</a>.

An <b>IO_WORKITEM</b> structure that is initialized by <b>IoInitializeWorkItem</b><u>must</u> be uninitialized by <a href="kernel.iouninitializeworkitem">IoUninitializeWorkItem</a> before it is freed.

A related routine, <a href="kernel.ioallocateworkitem">IoAllocateWorkItem</a>, both allocates and initializes a work item. By combining allocation and initialization into a single call, <b>IoAllocateWorkItem</b> might be more convenient for some drivers to use than <b>IoInitializeWorkItem</b>, which does initialization only. However, <b>IoInitializeWorkItem</b> is required by drivers that must initialize work items in previously allocated storage.

For example, a driver might allocate a block of storage for a pool of work items. The driver can call <b>IoInitializeWorkItem</b> to initialize a work item when the work item is allocated from the pool. The driver can call <b>IoUninitializeWorkItem</b> to uninitialize the work item when it is returned to the pool. During the initial storage allocation for the pool, the driver can call <b>IoSizeofWorkitem</b> to determine how much storage to allocate for each work item.

For more information about work items, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff564587">System Worker Threads</a>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Vista and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
Any level

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550679">IO_WORKITEM</a>
</dt>
<dt>
<a href="kernel.ioallocateworkitem">IoAllocateWorkItem</a>
</dt>
<dt>
<a href="kernel.ioqueueworkitem">IoQueueWorkItem</a>
</dt>
<dt>
<a href="kernel.ioqueueworkitemex">IoQueueWorkItemEx</a>
</dt>
<dt>
<a href="kernel.iosizeofworkitem">IoSizeofWorkItem</a>
</dt>
<dt>
<a href="kernel.iouninitializeworkitem">IoUninitializeWorkItem</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoInitializeWorkItem routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

