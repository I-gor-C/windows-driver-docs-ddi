---
UID: NF.wdm.IoUnregisterShutdownNotification
title: IoUnregisterShutdownNotification
author: windows-driver-content
description: The IoUnregisterShutdownNotification routine removes a registered driver from the shutdown notification queue.
old-location: kernel\iounregistershutdownnotification.htm
old-project: kernel
ms.assetid: b48a38ff-60b9-4c01-ac71-4ae07010db1f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoUnregisterShutdownNotification
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
req.alt-api: IoUnregisterShutdownNotification
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive5, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# IoUnregisterShutdownNotification function



## -description
<p>The <b>IoUnregisterShutdownNotification</b> routine removes a registered driver from the shutdown notification queue.</p>


## -syntax

````
VOID IoUnregisterShutdownNotification(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the driver's device object.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>IoUnregisterShutdownNotification</b> can be called by a driver only if that driver previously called <a href="..\wdm\nf-wdm-ioregistershutdownnotification.md">IoRegisterShutdownNotification</a> or <a href="..\wdm\nf-wdm-ioregisterlastchanceshutdownnotification.md">IoRegisterLastChanceShutdownNotification</a> with the given <i>DeviceObject</i>. This routine is usually called from a driver's <a href="kernel.unload">Unload</a> routine.</p>

<p>Calling <b>IoUnregisterShutdownNotification</b> cancels all shutdown notifications that have been registered for the given <i>DeviceObject</i>. </p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqliopassive5">IrqlIoPassive5</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-ioregistershutdownnotification.md">IoRegisterShutdownNotification</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-ioregisterlastchanceshutdownnotification.md">IoRegisterLastChanceShutdownNotification</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoUnregisterShutdownNotification routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
