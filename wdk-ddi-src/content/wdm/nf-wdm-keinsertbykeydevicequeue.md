---
UID: NF.wdm.KeInsertByKeyDeviceQueue
title: KeInsertByKeyDeviceQueue function
author: windows-driver-content
description: The KeInsertByKeyDeviceQueue routine acquires the spin lock for the specified DeviceQueue and queues an entry according to the specified sort-key value if the device queue is set to a busy state.
old-location: kernel\keinsertbykeydevicequeue.htm
old-project: kernel
ms.assetid: fa395673-108f-4cf0-b05f-a160aa0b02ea
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: KeInsertByKeyDeviceQueue
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KeInsertByKeyDeviceQueue
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlDispatch, MarkingQueuedIrps, HwStorPortProhibitedDDIs, IrqlDispatch(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# KeInsertByKeyDeviceQueue function



## -description
The <b>KeInsertByKeyDeviceQueue</b> routine acquires the spin lock for the specified <i>DeviceQueue</i> and queues an entry according to the specified sort-key value if the device queue is set to a busy state.



## -syntax

````
BOOLEAN KeInsertByKeyDeviceQueue(
  _Inout_ PKDEVICE_QUEUE       DeviceQueue,
  _Inout_ PKDEVICE_QUEUE_ENTRY DeviceQueueEntry,
  _In_    ULONG                SortKey
);
````


## -parameters

### -param DeviceQueue [in, out]

Pointer to a control object of the device queue type for which the caller provides the storage.


### -param DeviceQueueEntry [in, out]

Pointer to the device queue entry to be inserted into the device queue according to the specific key value.


### -param SortKey [in]

Specifies the sort-key value that determines the position in the device queue in which to insert the entry. 


## -returns
If the device queue is empty, <b>FALSE</b> is returned, meaning the <i>DeviceQueueEntry</i> is not inserted in the device queue.


## -remarks
The specified device queue spin lock is acquired and the state of the device queue is checked. If the device queue is set to a busy state, the IRP specified by the <i>DeviceQueueEntry</i> is inserted into the device queue according to its sort key value and the device queue spin lock is released.

The new entry is positioned in the device queue after any entries in the queue with sort key values less than or equal to its sort key value and preceding any entries with sort key values that are greater.

If <b>KeInsertByKeyDeviceQueue</b> returns <b>FALSE</b>, the caller must begin processing the IRP. A call to <a href="kernel.keinsertdevicequeue">KeInsertDeviceQueue</a> or <b>KeInsertByKeyDeviceQueue</b> when the queue is empty causes the device queue to transition from a not-busy state to a busy state.

This routine is for code that queues an I/O request to a device driver. 


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
Available starting with Windows 2000.

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
DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqldispatch">IrqlDispatch</a>, <a href="devtest.wdm_markingqueuedirps">MarkingQueuedIrps</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keinitializedevicequeue">KeInitializeDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keinsertdevicequeue">KeInsertDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keremovedevicequeue">KeRemoveDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keremoveentrydevicequeue">KeRemoveEntryDeviceQueue</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeInsertByKeyDeviceQueue routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

