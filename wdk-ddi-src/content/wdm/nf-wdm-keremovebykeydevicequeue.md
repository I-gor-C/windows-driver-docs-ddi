---
UID: NF.wdm.KeRemoveByKeyDeviceQueue
title: KeRemoveByKeyDeviceQueue function
author: windows-driver-content
description: The KeRemoveByKeyDeviceQueue routine removes an entry, selected according to a sort key value, from the specified device queue.
old-location: kernel\keremovebykeydevicequeue.htm
old-project: kernel
ms.assetid: 9819567c-1c79-440c-9bac-f81f23df29ae
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: KeRemoveByKeyDeviceQueue
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
req.alt-api: KeRemoveByKeyDeviceQueue
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlDispatch, HwStorPortProhibitedDDIs, IrqlDispatch(storport)
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

# KeRemoveByKeyDeviceQueue function



## -description
The <b>KeRemoveByKeyDeviceQueue</b> routine removes an entry, selected according to a sort key value, from the specified device queue. 


## -syntax

````
PKDEVICE_QUEUE_ENTRY KeRemoveByKeyDeviceQueue(
  _Inout_ PKDEVICE_QUEUE DeviceQueue,
  _In_    ULONG          SortKey
);
````


## -parameters

### -param DeviceQueue [in, out]

Pointer to an initialized device queue object for which the caller provides the storage.

### -param SortKey [in]

Specifies the key to be used when searching the <i>DeviceQueue</i>. 

## -returns
<b>KeRemoveByKeyDeviceQueue</b> returns the device queue entry that was removed; returns <b>NULL</b> if the queue was empty.

## -remarks
This routine searches for the first entry in the device queue that has a value greater than or equal to the <i>SortKey</i>. After this entry is found, this routine removes the entry from the device queue and returns it. If no such entry is found, then the first entry in the queue is returned. If the device queue is empty, then the device is set to a not-busy state and a <b>NULL</b> pointer is returned. 

It is an error to call <b>KeRemoveByKeyDeviceQueue</b> when the device queue object is set to a not-busy state. 

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
<a href="devtest.wdm_irqldispatch">IrqlDispatch</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch(storport)</a>
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
<a href="kernel.keremovedevicequeue">KeRemoveDeviceQueue</a>
</dt>
<dt>
<a href="kernel.keremoveentrydevicequeue">KeRemoveEntryDeviceQueue</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRemoveByKeyDeviceQueue routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
