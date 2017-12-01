---
UID: NF.ntddk.IoAllocateController
title: IoAllocateController
author: windows-driver-content
description: The IoAllocateController routine sets up the call to a driver-supplied ControllerControl routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object.
old-location: kernel\ioallocatecontroller.htm
old-project: kernel
ms.assetid: bfeec8b1-48fb-420e-b602-699a5f2d659a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IoAllocateController
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoAllocateController
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlDispatch, HwStorPortProhibitedDDIs, IrqlDispatch(storport), SpNoWait, StorPortStartIo
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
---

# IoAllocateController function



## -description
<p>The <b>IoAllocateController</b> routine sets up the call to a driver-supplied <a href="..\wdm\nc-wdm-driver-control.md">ControllerControl</a> routine as soon as the device controller, represented by the given controller object, is available to carry out an I/O operation for the target device, represented by the given device object.</p>


## -syntax

````
VOID IoAllocateController(
  _In_     PCONTROLLER_OBJECT ControllerObject,
  _In_     PDEVICE_OBJECT     DeviceObject,
  _In_     PDRIVER_CONTROL    ExecutionRoutine,
  _In_opt_ PVOID              Context
);
````


## -parameters
<dl>

### -param <i>ControllerObject</i> [in]

<dd>
<p>Pointer to a driver-created controller object, usually representing a physical controller to be allocated for an I/O operation on an attached device.</p>
</dd>

### -param <i>DeviceObject</i> [in]

<dd>
<p>Pointer to the device object, representing the target device of the current IRP.</p>
</dd>

### -param <i>ExecutionRoutine</i> [in]

<dd>
<dl>
<dd>
<p>Pointer to the driver-supplied <a href="..\wdm\nc-wdm-driver-control.md">ControllerControl</a> routine.</p>
</dd>
</dl>
</dd>

### -param <i>Context</i> [in, optional]

<dd>
<p>Pointer to a driver-determined context, passed to the driver's <i>ControllerControl</i> routine when it is called. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This routine reserves exclusive access to the hardware controller for the specified device.</p>

<p>The <a href="..\wdm\nc-wdm-driver-control.md">ControllerControl</a> routine returns a value indicating whether the controller remains allocated to the device, either <b>DeallocateObject</b> or <b>KeepObject</b>. If it returns <b>KeepObject</b>, the driver must subsequently call <b>IoFreeController</b> to release the controller object.</p>

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
<dt>Ntddk.h (include Ntddk.h)</dt>
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
<a href="devtest.wdm_irqldispatch">IrqlDispatch</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch(storport)</a>, <a href="devtest.storport_spnowait">SpNoWait</a>, <a href="devtest.storport_storportstartio">StorPortStartIo</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nc-wdm-driver-control.md">ControllerControl</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatecontroller.md">IoCreateController</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iodeletecontroller.md">IoDeleteController</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iofreecontroller.md">IoFreeController</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoAllocateController routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
