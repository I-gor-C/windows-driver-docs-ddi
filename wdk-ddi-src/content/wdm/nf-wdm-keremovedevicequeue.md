---
UID: NF.wdm.KeRemoveDeviceQueue
title: KeRemoveDeviceQueue
author: windows-driver-content
description: The KeRemoveDeviceQueue routine removes an entry from the head of a specified device queue.
old-location: kernel\keremovedevicequeue.htm
old-project: kernel
ms.assetid: 9cad7d89-bcaa-47d6-b3e5-51653cbef318
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KeRemoveDeviceQueue
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
req.alt-api: KeRemoveDeviceQueue
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
req.iface: 
req.product: Windows 10 or later.
---

# KeRemoveDeviceQueue function



## -description
<p>The <b>KeRemoveDeviceQueue</b> routine removes an entry from the head of a specified device queue.</p>


## -syntax

````
PKDEVICE_QUEUE_ENTRY KeRemoveDeviceQueue(
  _Inout_ PKDEVICE_QUEUE DeviceQueue
);
````


## -parameters
<dl>

### -param <i>DeviceQueue</i> [in, out]

<dd>
<p>Pointer to an initialized device queue object for which the caller provides the storage. </p>
</dd>
</dl>

## -returns
<p>If the device queue is empty but is set to a busy state, <b>KeRemoveDeviceQueue</b> returns <b>NULL</b>.</p>

## -remarks
<p>The specified device queue spin lock is acquired and the state of the device queue is checked. If the device queue is set to a busy state and an IRP is queued, this routine dequeues the entry and returns a pointer to the IRP. A call to <b>KeRemoveDeviceQueue</b> when the device queue object is set to a busy state but no IRPs are queued causes a state change to not-busy. The specified device queue's spin lock is released.</p>

<p>It is an error to call <b>KeRemoveDeviceQueue</b> when the device queue object is set to a not-busy state. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqldispatch">IrqlDispatch</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-keinitializedevicequeue.md">KeInitializeDeviceQueue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinsertbykeydevicequeue.md">KeInsertByKeyDeviceQueue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keinsertdevicequeue.md">KeInsertDeviceQueue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keremovebykeydevicequeue.md">KeRemoveByKeyDeviceQueue</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-keremoveentrydevicequeue.md">KeRemoveEntryDeviceQueue</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20KeRemoveDeviceQueue routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
