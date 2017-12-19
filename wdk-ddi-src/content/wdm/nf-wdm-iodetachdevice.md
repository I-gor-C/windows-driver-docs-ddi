---
UID: NF.wdm.IoDetachDevice
title: IoDetachDevice function
author: windows-driver-content
description: The IoDetachDevice routine releases an attachment between the caller's device object and a lower driver's device object.
old-location: kernel\iodetachdevice.htm
old-project: kernel
ms.assetid: 5822b642-0ba4-46ee-bb60-b109c50691eb
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: IoDetachDevice
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
req.alt-api: IoDetachDevice
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive3, PnpSurpriseRemove, PowerIrpDDis, RemoveLockCheck, HwStorPortProhibitedDDIs
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

# IoDetachDevice function



## -description
The <b>IoDetachDevice</b> routine releases an attachment between the caller's device object and a lower driver's device object.



## -syntax

````
VOID IoDetachDevice(
  _Inout_ PDEVICE_OBJECT TargetDevice
);
````


## -parameters

### -param TargetDevice [in, out]

Pointer to the lower driver's device object. The caller previously called <a href="kernel.ioattachdevice">IoAttachDevice</a> or <a href="kernel.ioattachdevicetodevicestack">IoAttachDeviceToDeviceStack</a> successfully to get this pointer. 


## -returns
None


## -remarks
<b>IoDetachDevice</b> decrements the reference count of the <i>TargetDevice</i> object. If the reference count goes to zero and the lower driver has been marked for an unload operation, the lower driver is unloaded. 


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
<a href="devtest.wdm_irqliopassive3">IrqlIoPassive3</a>, <a href="devtest.wdm_pnpsurpriseremove">PnpSurpriseRemove</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.wdm_removelockcheck">RemoveLockCheck</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.ioattachdevice">IoAttachDevice</a>
</dt>
<dt>
<a href="kernel.ioattachdevicetodevicestack">IoAttachDeviceToDeviceStack</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoDetachDevice routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

