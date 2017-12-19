---
UID: NF.wdm.KeRemoveEntryDeviceQueue
title: KeRemoveEntryDeviceQueue function
author: windows-driver-content
description: The KeRemoveEntryDeviceQueue routine returns whether the specified entry is in the device queue and removes it, if it was queued, from the device queue.
old-location: kernel\keremoveentrydevicequeue.htm
old-project: kernel
ms.assetid: 2dc32517-3730-4a1c-a59a-f5036d6f54ef
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: KeRemoveEntryDeviceQueue
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
req.alt-api: KeRemoveEntryDeviceQueue
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlKeDispatchLte, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# KeRemoveEntryDeviceQueue function



## -description
The <b>KeRemoveEntryDeviceQueue</b> routine returns whether the specified entry is in the device queue and removes it, if it was queued, from the device queue.



## -syntax

````
BOOLEAN KeRemoveEntryDeviceQueue(
  _Inout_ PKDEVICE_QUEUE       DeviceQueue,
  _Inout_ PKDEVICE_QUEUE_ENTRY DeviceQueueEntry
);
````


## -parameters

### -param DeviceQueue [in, out]

Pointer to an initialized device queue object for which the caller provides the storage.


### -param DeviceQueueEntry [in, out]

Pointer to the entry to be removed from the specified <i>DeviceQueue</i>.


## -returns
If the <i>DeviceQueueEntry</i> is queued, it is removed and <b>KeRemoveEntryDeviceQueue</b> returns <b>TRUE</b>.


## -remarks
The IRQL is set to DISPATCH_LEVEL and the <i>DeviceQueue</i> spin lock is acquired.

If the specified <i>DeviceQueueEntry</i> is not in the queue, the IRP either is already being processed, or the IRP has been canceled. In this case, <b>KeRemoveEntryDeviceQueue</b> simply returns <b>FALSE</b>.

The specified <i>DeviceQueue</i> spin lock is released and IRQL is restored to its previous value. 


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
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlkedispatchlte">IrqlKeDispatchLte</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.keinitializedevicequeue">KeInitializeDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keinsertbykeydevicequeue">KeInsertByKeyDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keinsertdevicequeue">KeInsertDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keremovebykeydevicequeue">KeRemoveByKeyDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keremovedevicequeue">KeRemoveDeviceQueue</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRemoveEntryDeviceQueue routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

