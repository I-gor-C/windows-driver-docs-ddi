---
UID: NF.wdm.IoAttachDevice
title: IoAttachDevice
author: windows-driver-content
description: The IoAttachDevice routine attaches the caller's device object to a named target device object, so that I/O requests bound for the target device are routed first to the caller.
old-location: kernel\ioattachdevice.htm
ms.assetid: 0227751d-739b-4e0c-84bd-9135f117ec9b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: kernel
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows 2000 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoAttachDevice
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlIoPassive1, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
ms.keywords: IoAttachDevice
req.iface: 
req.product: Windows 10 or later.
---

# IoAttachDevice function



## -description
<p>The <b>IoAttachDevice</b> routine attaches the caller's device object to a named target device object, so that I/O requests bound for the target device are routed first to the caller.</p>


## -syntax

````
NTSTATUS IoAttachDevice(
  _In_  PDEVICE_OBJECT  SourceDevice,
  _In_  PUNICODE_STRING TargetDevice,
  _Out_ PDEVICE_OBJECT  *AttachedDevice
);
````


## -parameters
<dl>

### -param <i>SourceDevice</i> [in]

<dd>
<p>Pointer to the caller-created device object.</p>
</dd>

### -param <i>TargetDevice</i> [in]

<dd>
<p>Pointer to a buffer containing the name of the device object to which the specified <i>SourceDevice</i> is to be attached.</p>
</dd>

### -param <i>AttachedDevice</i> [out]

<dd>
<p>Pointer to caller-allocated storage for a pointer. On return, contains a pointer to the target device object if the attachment succeeds.</p>
</dd>
</dl>

## -returns
<p><b>IoAttachDevice</b> can return one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>

## -remarks
<p><b>IoAttachDevice</b> establishes layering between drivers so that the same IRPs can be sent to each driver in the chain.</p>

<p>This routine is used by intermediate drivers during initialization. It allows such a driver to attach its own device object to another device in such a way that any requests being made to the original device are given first to the intermediate driver.</p>

<p>The caller can be layered only at the top of an existing chain of layered drivers. <b>IoAttachDevice</b> searches for the highest device object layered over <i>TargetDevice</i> and attaches to that object (that can be the <i>TargetDevice</i>). Therefore, this routine must not be called if a driver that must be higher-level has already layered itself over the target device.</p>

<p>Note that for file system drivers and drivers in the storage stack, <b>IoAttachDevice</b> opens the target device with FILE_READ_ATTRIBUTES and then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549277">IoGetRelatedDeviceObject</a>. This does not cause a file system to be mounted. Thus, a successful call to <b>IoAttachDevice</b> returns the device object of the storage driver, not that of the file system driver.</p>

<p>This routine sets the <b>AlignmentRequirement</b> in <i>SourceDevice</i> to the value in the next-lower device object and sets the <b>StackSize</b> to the value in the next-lower object plus one.</p>

<p><b>IoAttachDevice</b> establishes layering between drivers so that the same IRPs can be sent to each driver in the chain.</p>

<p>This routine is used by intermediate drivers during initialization. It allows such a driver to attach its own device object to another device in such a way that any requests being made to the original device are given first to the intermediate driver.</p>

<p>The caller can be layered only at the top of an existing chain of layered drivers. <b>IoAttachDevice</b> searches for the highest device object layered over <i>TargetDevice</i> and attaches to that object (that can be the <i>TargetDevice</i>). Therefore, this routine must not be called if a driver that must be higher-level has already layered itself over the target device.</p>

<p>Note that for file system drivers and drivers in the storage stack, <b>IoAttachDevice</b> opens the target device with FILE_READ_ATTRIBUTES and then calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff549277">IoGetRelatedDeviceObject</a>. This does not cause a file system to be mounted. Thus, a successful call to <b>IoAttachDevice</b> returns the device object of the storage driver, not that of the file system driver.</p>

<p>This routine sets the <b>AlignmentRequirement</b> in <i>SourceDevice</i> to the value in the next-lower device object and sets the <b>StackSize</b> to the value in the next-lower object plus one.</p>

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
<p>Available in Windows 2000 and later versions of Windows.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547763">IrqlIoPassive1</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh454220">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543147">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548300">IoAttachDeviceToDeviceStack</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548236">IoAttachDeviceToDeviceStackSafe</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549277">IoGetRelatedDeviceObject</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549087">IoDetachDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAttachDevice routine%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
