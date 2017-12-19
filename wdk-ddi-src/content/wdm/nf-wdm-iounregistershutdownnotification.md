---
UID: NF.wdm.IoUnregisterShutdownNotification
title: IoUnregisterShutdownNotification function
author: windows-driver-content
description: The IoUnregisterShutdownNotification routine removes a registered driver from the shutdown notification queue.
old-location: kernel\iounregistershutdownnotification.htm
old-project: kernel
ms.assetid: b48a38ff-60b9-4c01-ac71-4ae07010db1f
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# IoUnregisterShutdownNotification function



## -description
The <b>IoUnregisterShutdownNotification</b> routine removes a registered driver from the shutdown notification queue.



## -syntax

````
VOID IoUnregisterShutdownNotification(
  _In_ PDEVICE_OBJECT DeviceObject
);
````


## -parameters

### -param DeviceObject [in]

Pointer to the driver's device object.


## -returns
None


## -remarks
<b>IoUnregisterShutdownNotification</b> can be called by a driver only if that driver previously called <a href="kernel.ioregistershutdownnotification">IoRegisterShutdownNotification</a> or <a href="kernel.ioregisterlastchanceshutdownnotification">IoRegisterLastChanceShutdownNotification</a> with the given <i>DeviceObject</i>. This routine is usually called from a driver's <a href="kernel.unload">Unload</a> routine.

Calling <b>IoUnregisterShutdownNotification</b> cancels all shutdown notifications that have been registered for the given <i>DeviceObject</i>. 


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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqliopassive5">IrqlIoPassive5</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioregistershutdownnotification">IoRegisterShutdownNotification</a>
</dt>
<dt>
<a href="kernel.ioregisterlastchanceshutdownnotification">IoRegisterLastChanceShutdownNotification</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoUnregisterShutdownNotification routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

