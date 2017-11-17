---
UID: NI.vpci.IOCTL_VPCI_READ_BLOCK
title: IOCTL_VPCI_READ_BLOCK
author: windows-driver-content
description: The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_READ_BLOCK I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack.
old-location: kernel\ioctl_vpci_read_block.htm
ms.assetid: C493724D-316B-4F64-866B-D26C2DBA822A
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: kernel
req.header: vpci.h
req.include-header: Wdm.h
req.target-type: Windows
req.target-min-winverclnt: Supported in Windows Server 2012 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_VPCI_READ_BLOCK
req.alt-loc: Vpci.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
ms.keywords: VMB_CHANNEL_STATE_CHANGE_CALLBACKS, VMB_CHANNEL_STATE_CHANGE_CALLBACKS, *PVMB_CHANNEL_STATE_CHANGE_CALLBACKS
req.iface: 
req.product: Windows 10 or later.
---

# IOCTL_VPCI_READ_BLOCK IOCTL



## -description
<p>
<p>The driver for a PCI Express (PCIe) virtual function (VF) issues an <b>IOCTL_VPCI_READ_BLOCK</b> 
    
   I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver  in the driver stack.</p>
</p>
<p>The driver for a PCI Express (PCIe) virtual function (VF) issues an <b>IOCTL_VPCI_READ_BLOCK</b> 
    
   I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver  in the driver stack.</p>


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer

<text></text>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block

Irp->IoStatus.Status is set to STATUS_SUCCESS if the request is successful.
Otherwise, Status to the appropriate error condition as a NTSTATUS code. 
For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks
<p>The driver must first allocate or reuse an I/O request packet (<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>). You can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548318">IoBuildDeviceIoControlRequest</a> function to specifically allocate an IOCTL IRP. You can also use general-purpose IRP creation and initialization functions, such as <a href="https://msdn.microsoft.com/library/windows/hardware/ff548257">IoAllocateIrp</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff549661">IoReuseIrp</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff549315">IoInitializeIrp</a>. For more information about IRP allocation, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542899">Creating IRPs for Lower-Level Drivers</a>.</p>

<p>The driver must then set the  members of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> structure as described in the following table.</p>

<p>The address of the caller-allocated buffer that will contain the configuration data to be read.</p>

<p>The address of the event object that was initialized in the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a> function.<div class="alert"><b>Note</b>  If asynchronous completion of the IOCTL request is not required, this member should be set to <b>NULL</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>.</div>
<div> </div>
</p>

<p>The address of a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure. This structure is updated by the lower driver to indicate the final status of the I/O request.</p>

<p> </p>

<p>The driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff549266">IoGetNextIrpStackLocation</a> function to access the lower driver's I/O stack location. This function returns a pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure that contains the parameters for the I/O stack location.</p>

<p>The driver must then set the members in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure as described in the following table.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>
</p>

<p><b>IOCTL_VPCI_READ_BLOCK</b></p>

<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451588">VPCI_READ_BLOCK_INPUT</a> structure. The driver formats this structure with the parameters for the <b>IOCTL_VPCI_READ_BLOCK</b> 
   I/O request.</p>

<p>The size, in bytes, of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451588">VPCI_READ_BLOCK_INPUT</a> structure.</p>

<p>The size, in bytes, of the caller-allocated buffer that will contain the configuration data to be read.<div class="alert"><b>Note</b>  This value must be the same as the value of the <b>BytesRequested</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh451588">VPCI_READ_BLOCK_INPUT</a> structure.</div>
<div> </div>
</p>

<p> </p>

<p>To issue this IOCTL request, the driver calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a> function to pass the request on to the next-lower driver  in the driver stack. The driver sets the parameters of <b>IoCallDriver</b> as described in the following table.</p>

<p>The device object of the lower driver.</p>

<p>The address of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a> that was previously allocated and initialized. For more information, see <a href="#preparing_an_i_o_request_packet_structure">Preparing an I/O Request Packet (IRP) Structure</a>.</p>

<p> </p>

<p>      When the <b>IOCTL_VPCI_READ_BLOCK</b> IOCTL request is completed, the <b>Status</b> member of the caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure is set to one of the values in the following table.</p>

<p><b>STATUS_SUCCESS</b></p>

<p>The IOCTL completed successfully.</p>

<p><b>STATUS_PENDING</b></p>

<p>The IOCTL has not completed. The driver must call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553350">KeWaitForSingleObject</a> function in order to put the current thread into a wait state. The driver sets the <i>Object</i> parameter to the address of an event object that was initialized in the call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552137">KeInitializeEvent</a> function. </p>

<p>The event is signaled when the IOCTL request is completed. Once the event is signaled, the thread resumes execution.</p>

<p><b>STATUS_BUFFER_TOO_SMALL</b></p>

<p>Either the <b>Parameters.DeviceIoControl.InputBufferLength</b> member or the <b>Parameters.DeviceIoControl.OutputBufferLength</b> member was set to a value that is less than the required buffer size.</p>

<p> </p>

<p>If the request completed successfully, the 
      <b>Information</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure is set to the number of bytes that were read. Otherwise, the 
      <b>Information</b> member is set to zero.</p>

<p>When the <b>IOCTL_VPCI_READ_BLOCK</b> IOCTL is issued, the driver of the PCIe physical function (PF) is notified to return the data from the specified VF configuration block.</p>

<p>A VF configuration block is used for backchannel communication between the drivers of the PCIe PF and a VF on a device that supports the SR-IOV interface. Data from a VF configuration block can be exchanged between the following drivers:</p>

<p>The VF driver, which runs in the guest operating system. This operating system runs within a Hyper-V child partition.

</p>

<p>The PF driver, which runs in the management operating system.

This operating system runs within the Hyper-V parent partition.</p>

<p>The  usage of the VF configuration block and the format of its configuration data are defined by the  independent hardware vendor (IHV) of the device. The configuration data is used only by the drivers of the PF and VF.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in Windows Server 2012 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Vpci.h (include Wdm.h)</dt>
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
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548336">IoCallDriver</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550694">IRP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439637">ReadVfConfigBlock</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451588">VPCI_READ_BLOCK_INPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IOCTL_VPCI_READ_BLOCK control code%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
