---
UID: NF.wdm.IoBuildAsynchronousFsdRequest
title: IoBuildAsynchronousFsdRequest function
author: windows-driver-content
description: The IoBuildAsynchronousFsdRequest routine allocates and sets up an IRP to be sent to lower-level drivers.
old-location: kernel\iobuildasynchronousfsdrequest.htm
old-project: kernel
ms.assetid: cb633146-c3ab-4a09-bbcd-5964ecbf6e44
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: IoBuildAsynchronousFsdRequest
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
req.alt-api: IoBuildAsynchronousFsdRequest
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: ForwardedAtBadIrqlFsdAsync, IoBuildFsdComplete, IoBuildFsdForward, IoBuildFsdFree, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.product: Windows 10 or later.
---

# IoBuildAsynchronousFsdRequest function



## -description
The <b>IoBuildAsynchronousFsdRequest</b> routine allocates and sets up an IRP to be sent to lower-level drivers.



## -syntax

````
PIRP IoBuildAsynchronousFsdRequest(
  _In_     ULONG            MajorFunction,
  _In_     PDEVICE_OBJECT   DeviceObject,
  _Inout_  PVOID            Buffer,
  _In_opt_ ULONG            Length,
  _In_opt_ PLARGE_INTEGER   StartingOffset,
  _In_opt_ PIO_STATUS_BLOCK IoStatusBlock
);
````


## -parameters

### -param MajorFunction [in]

The major function code to be set in the IRP. This code can be <a href="https://msdn.microsoft.com/library/windows/hardware/ff549268">IRP_MJ_PNP</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549235">IRP_MJ_FLUSH_BUFFERS</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549423">IRP_MJ_SHUTDOWN</a>.


### -param DeviceObject [in]

A pointer to the next-lower driver's device object. This object represents the target device for the read, write, flush, or shutdown operation.


### -param Buffer [in, out]

A pointer to a buffer into which data is read or from which data is written. The value of this argument is <b>NULL</b> for flush and shutdown requests.


### -param Length [in, optional]

The length, in bytes, of the buffer pointed to by <i>Buffer</i>. For devices such as disks, this value must be an integer multiple of the sector size. Starting with Windows 8, the sector size can be 4,096 or 512 bytes. In earlier versions of Windows, the sector size is always 512 bytes. This parameter is required for read and write requests, but must be zero for flush and shutdown requests.


### -param StartingOffset [in, optional]

A pointer to the starting offset on the input/output media. The value of this argument is zero for flush and shutdown requests.


### -param IoStatusBlock [in, optional]

A pointer to the address of an I/O status block in which the to-be-called drivers return final status about the requested operation.


## -returns
<b>IoBuildAsynchronousFsdRequest</b> returns a pointer to an IRP, or a <b>NULL</b> pointer if the IRP cannot be allocated.


## -remarks
Intermediate or highest-level drivers can call <b>IoBuildAsynchronousFsdRequest</b> to set up IRPs for requests sent to lower-level drivers. The calling driver must supply an <a href="..\wdm\nc-wdm-io_completion_routine.md">IoCompletion</a> routine for the IRP, so the IRP can be deallocated with <a href="kernel.iofreeirp">IoFreeIrp</a>. For more information about IRP deallocation, see Examples.

The IRP that gets built contains only enough information to get the operation started and to complete the IRP. No other context information is tracked because an asynchronous request is context-independent.

Lower-level drivers might impose restrictions on parameters supplied to this routine. For example, disk drivers might require that values supplied for <i>Length</i> and <i>StartingOffset</i> be integer multiples of the device's sector size.

An intermediate or highest-level driver also can call <a href="kernel.iobuilddeviceiocontrolrequest">IoBuildDeviceIoControlRequest</a>, <a href="kernel.ioallocateirp">IoAllocateIrp</a>, or <a href="kernel.iobuildsynchronousfsdrequest">IoBuildSynchronousFsdRequest</a> to set up requests it sends to lower-level drivers. Only a highest-level driver can call <a href="kernel.iomakeassociatedirp">IoMakeAssociatedIrp</a>.

During an <b>IoBuildAsynchronousFsdRequest</b> call, the I/O manager sets the <b>Tail.Overlay.Thread</b> member of the <a href="kernel.irp">IRP</a> structure to point to the caller's thread object, but does <u>not</u> take a counted reference to the thread object on behalf of the caller. After the caller sends the IRP to the driver for the target device, this driver might use the <b>Tail.Overlay.Thread</b> member to access the thread object. For example, a storage driver might call the <a href="kernel.iosetharderrororverifydevice">IoSetHardErrorOrVerifyDevice</a> routine and supply a pointer to the IRP as an input parameter. During this call, <b>IoSetHardErrorOrVerifyDevice</b> uses the <b>Tail.Overlay.Thread</b> member to access the thread object. When the thread object is accessed in this way, the driver that called <b>IoBuildAsynchronousFsdRequest</b> to allocate the IRP is responsible for ensuring that the thread object stays valid while the IRP is being handled.

To keep the thread object valid, the driver that calls <b>IoBuildAsynchronousFsdRequest</b> can take a counted reference on the thread object before sending the IRP. For example, this driver can call the <a href="kernel.obreferenceobjectbypointerwithtag">ObReferenceObjectByPointerWithTag</a> routine and supply, as the <i>Object</i> parameter, the object pointer from the <b>Tail.Overlay.Thread</b> member of the <b>IRP</b> structure. Later, this driver's completion routine can dereference the object by calling a routine such as <a href="kernel.obdereferenceobjectwithtag">ObDereferenceObjectWithTag</a>.

A driver might call <b>IoBuildAsynchronousFsdRequest</b> in one thread, and send the IRP allocated by this call in another thread. Before sending the IRP, this driver should set the <b>Tail.Overlay.Thread</b> member of the IRP to point to the thread object for the sending thread. Typically, the driver calls the <a href="kernel.psgetcurrentthread">PsGetCurrentThread</a> routine to get the thread object pointer.

A driver that calls <b>IoBuildAsynchronousFsdRequest</b> to allocate an IRP does not necessarily need to take a counted reference on the thread object pointed to by the <b>Tail.Overlay.Thread</b> member of the IRP. The driver might instead use another technique to guarantee that this thread object remains valid while the IRP is being handled. For example, if the driver created the thread, the thread can wait until the IRP is completed to terminate itself.

Before calling <a href="kernel.iofreeirp">IoFreeIrp</a>, an additional step is required to free the buffer for an IRP built by <b>IoBuildAsynchronousFsdRequest</b> if the following are all true:

Before freeing the buffer for this IRP, call the <a href="kernel.mmunlockpages">MmUnlockPages</a> routine with <b>Irp-&gt;MdlAddress</b> as the parameter value. This call decrements the extra reference count that <b>IoBuildAsynchronousFsdRequest</b> added to the pool pages in the MDL. Otherwise, the subsequent call to <a href="kernel.iofreemdl">IoFreeMdl</a> will bug check because the reference count for these pool pages will be 2, not 1. The following code example shows the <b>MmUnlockPages</b>, <b>IoFreeMdl</b>, and <b>IoFreeIrp</b> calls for this case:


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
&lt;= APC_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_forwardedatbadirqlfsdasync">ForwardedAtBadIrqlFsdAsync</a>, <a href="devtest.wdm_iobuildfsdcomplete">IoBuildFsdComplete</a>, <a href="devtest.wdm_iobuildfsdforward">IoBuildFsdForward</a>, <a href="devtest.wdm_iobuildfsdfree">IoBuildFsdFree</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.io_stack_location">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="kernel.ioallocateirp">IoAllocateIrp</a>
</dt>
<dt>
<a href="kernel.iobuilddeviceiocontrolrequest">IoBuildDeviceIoControlRequest</a>
</dt>
<dt>
<a href="kernel.iobuildsynchronousfsdrequest">IoBuildSynchronousFsdRequest</a>
</dt>
<dt>
<a href="kernel.iocalldriver">IoCallDriver</a>
</dt>
<dt>
<a href="kernel.iofreeirp">IoFreeIrp</a>
</dt>
<dt>
<a href="kernel.iofreemdl">IoFreeMdl</a>
</dt>
<dt>
<a href="kernel.iomakeassociatedirp">IoMakeAssociatedIrp</a>
</dt>
<dt>
<a href="kernel.iosetcompletionroutine">IoSetCompletionRoutine</a>
</dt>
<dt>
<a href="kernel.iosetharderrororverifydevice">IoSetHardErrorOrVerifyDevice</a>
</dt>
<dt>
<a href="kernel.irp">IRP</a>
</dt>
<dt>
<a href="kernel.mmunlockpages">MmUnlockPages</a>
</dt>
<dt>
<a href="kernel.obdereferenceobjectwithtag">ObDereferenceObjectWithTag</a>
</dt>
<dt>
<a href="kernel.obreferenceobjectbypointerwithtag">ObReferenceObjectByPointerWithTag</a>
</dt>
<dt>
<a href="kernel.psgetcurrentthread">PsGetCurrentThread</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IoBuildAsynchronousFsdRequest routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

