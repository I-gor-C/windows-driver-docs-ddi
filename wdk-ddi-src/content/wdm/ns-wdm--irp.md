---
UID: NS.wdm._IRP
title: IRP
author: windows-driver-content
description: The IRP structure is a partially opaque structure that represents an I/O request packet. Drivers can use the following members of the IRP structure.
old-location: kernel\irp.htm
old-project: kernel
ms.assetid: 6e044704-2edf-416f-a5a1-2ae65363a165
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: IRP,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRP
req.alt-loc: Wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# IRP structure



## -description
<p>The <b>IRP</b> structure is a partially opaque structure that represents an <i>I/O request packet</i>. Drivers can use the following members of the IRP structure.</p>


## -syntax

````
typedef struct _IRP {
  PMDL            MdlAddress;
  ULONG           Flags;
  union {
    struct _IRP  *MasterIrp;
    PVOID       SystemBuffer;
  } AssociatedIrp;
  IO_STATUS_BLOCK IoStatus;
  KPROCESSOR_MODE RequestorMode;
  BOOLEAN         PendingReturned;
  BOOLEAN         Cancel;
  KIRQL           CancelIrql;
  PDRIVER_CANCEL  CancelRoutine;
  PVOID           UserBuffer;
  union {
    struct {
      union {
        KDEVICE_QUEUE_ENTRY DeviceQueueEntry;
        struct {
          PVOID DriverContext[4];
        };
      };
      PETHREAD   Thread;
      LIST_ENTRY ListEntry;
    } Overlay;
  } Tail;
} IRP, *PIRP;
````


## -struct-fields
<dl>

### -field <b>MdlAddress</b>

<dd>
<p>Pointer to an MDL describing a user buffer, if the driver is using direct I/O, and the IRP major function code is one of the following:</p>
<p></p>
<dl>

### -field <a id="IRP_MJ_READ"></a><a id="irp_mj_read"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>


<dd>
<p>The MDL describes an empty buffer that the device or driver fills in.</p>
</dd>

### -field <a id="IRP_MJ_WRITE"></a><a id="irp_mj_write"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>


<dd>
<p>The MDL describes a buffer that contains data for the device or driver.</p>
</dd>

### -field <a id="IRP_MJ_DEVICE_CONTROL_or_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a id="irp_mj_device_control_or_irp_mj_internal_device_control"></a><a id="IRP_MJ_DEVICE_CONTROL_OR_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>


<dd>
<p>If the IOCTL code specifies the METHOD_IN_DIRECT transfer type, the MDL describes a buffer that contains data for the device or driver.</p>
<p>If the IOCTL code specifies the METHOD_OUT_DIRECT transfer type, the MDL describes an empty buffer that the device or driver fills in.</p>
<p>For more information about the buffers that are associated with METHOD_IN_DIRECT and METHOD_OUT_DIRECT transfer types in IOCTL codes, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>
</dd>
</dl>
<p>If the driver is not using direct I/O, this pointer is <b>NULL</b>.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>File system drivers use this field, which is read-only for all drivers. Network and, possibly, highest-level device drivers also might read this field. This field is set either to zero or to the bitwise-OR of one or more of the following system-defined flag bits:</p>
<dl>
<dd>
<p>IRP_NOCACHE</p>
</dd>
<dd>
<p>IRP_PAGING_IO</p>
</dd>
<dd>
<p>IRP_MOUNT_COMPLETION</p>
</dd>
<dd>
<p>IRP_SYNCHRONOUS_API</p>
</dd>
<dd>
<p>IRP_ASSOCIATED_IRP</p>
</dd>
<dd>
<p>IRP_BUFFERED_IO</p>
</dd>
<dd>
<p>IRP_DEALLOCATE_BUFFER</p>
</dd>
<dd>
<p>IRP_INPUT_OPERATION</p>
</dd>
<dd>
<p>IRP_SYNCHRONOUS_PAGING_IO</p>
</dd>
<dd>
<p>IRP_CREATE_OPERATION</p>
</dd>
<dd>
<p>IRP_READ_OPERATION</p>
</dd>
<dd>
<p>IRP_WRITE_OPERATION</p>
</dd>
<dd>
<p>IRP_CLOSE_OPERATION</p>
</dd>
<dd>
<p>IRP_DEFER_IO_COMPLETION</p>
</dd>
<dd>
<p>IRP_OB_QUERY_NAME</p>
</dd>
<dd>
<p>IRP_HOLD_DEVICE_QUEUE</p>
</dd>
<dd>
<p>IRP_UM_DRIVER_INITIATED_IO</p>
</dd>
</dl>
</dd>

### -field <b>AssociatedIrp</b>

<dd>
<dl>

### -field <b>MasterIrp</b>

<dd>
<p>Pointer to the master IRP in an IRP that was created by a highest-level driver's call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff549397">IoMakeAssociatedIrp</a>.</p>
</dd>

### -field <b>SystemBuffer</b>

<dd>
<p>Pointer to a system-space buffer.</p>
<p>If the driver is using buffered I/O, the buffer's purpose is determined by the IRP major function code, as follows:</p>
<p></p>
<dl>

### -field <a id="IRP_MJ_READ"></a><a id="irp_mj_read"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>


<dd>
<p>The buffer receives data from the device or driver. The buffer's length is specified by <b>Parameters.Read.Length</b> in the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure.</p>
</dd>

### -field <a id="IRP_MJ_WRITE"></a><a id="irp_mj_write"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>


<dd>
<p>The buffer supplies data for the device or driver. The buffer's length is specified by <b>Parameters.Write.Length</b> in the driver's <b>IO_STACK_LOCATION</b> structure.</p>
</dd>

### -field <a id="IRP_MJ_DEVICE_CONTROL_or_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a id="irp_mj_device_control_or_irp_mj_internal_device_control"></a><a id="IRP_MJ_DEVICE_CONTROL_OR_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>


<dd>
<p>The buffer represents both the input and output buffers that are supplied to <b>DeviceIoControl</b> and <b>IoBuildDeviceIoControlRequest</b>. Output data overwrites input data.</p>
<p>For input, the buffer's length is specified by <b>Parameters.DeviceIoControl.InputBufferLength</b> in the driver's <b>IO_STACK_LOCATION</b> structure.</p>
<p>For output, the buffer's length is specified by <b>Parameters.DeviceIoControl.OutputBufferLength</b> in the driver's <b>IO_STACK_LOCATION</b> structure.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>
</dd>
</dl>
<p>If the driver is using direct I/O, the buffer's purpose is determined by the IRP major function code, as follows:</p>
<p></p>
<dl>

### -field <a id="IRP_MJ_READ"></a><a id="irp_mj_read"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff549327">IRP_MJ_READ</a>


<dd>
<p><b>NULL</b>.</p>
</dd>

### -field <a id="IRP_MJ_WRITE"></a><a id="irp_mj_write"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff550819">IRP_MJ_WRITE</a>


<dd>
<p><b>NULL</b>.</p>
</dd>

### -field <a id="IRP_MJ_DEVICE_CONTROL_or_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a id="irp_mj_device_control_or_irp_mj_internal_device_control"></a><a id="IRP_MJ_DEVICE_CONTROL_OR_IRP_MJ_INTERNAL_DEVICE_CONTROL"></a><a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>


<dd>
<p>The buffer represents the input buffer that is supplied to <b>DeviceIoControl</b> and <b>IoBuildDeviceIoControlRequest</b>.</p>
<p>The buffer's length is specified by <b>Parameters.DeviceIoControl.InputBufferLength</b> in the driver's <b>IO_STACK_LOCATION</b> structure.</p>
<p>For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>
</dd>
</dl>
</dd>
</dl>
</dd>

### -field <b>IoStatus</b>

<dd>
<p>Contains the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a> structure in which a driver stores status and information before calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff548343">IoCompleteRequest</a>.</p>
</dd>

### -field <b>RequestorMode</b>

<dd>
<p>Indicates the execution mode of the original requester of the operation, one of <b>UserMode</b> or <b>KernelMode</b>. </p>
</dd>

### -field <b>PendingReturned</b>

<dd>
<p>If set to <b>TRUE</b>, a driver has marked the IRP pending. Each <a href="https://msdn.microsoft.com/library/windows/hardware/ff548354">IoCompletion</a> routine should check the value of this flag. If the flag is <b>TRUE</b>, and if the IoCompletion routine will not return STATUS_MORE_PROCESSING_REQUIRED, the routine should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549422">IoMarkIrpPending</a> to propagate the pending status to drivers above it in the device stack.</p>
</dd>

### -field <b>Cancel</b>

<dd>
<p>If set to <b>TRUE</b>, the IRP either is or should be canceled.</p>
</dd>

### -field <b>CancelIrql</b>

<dd>
<p>Contains the IRQL at which a driver is running when <a href="https://msdn.microsoft.com/library/windows/hardware/ff548196">IoAcquireCancelSpinLock</a> is called.</p>
</dd>

### -field <b>CancelRoutine</b>

<dd>
<p>Contains the entry point for a driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/hh406716">Cancel</a> routine to be called if the IRP is canceled. <b>NULL</b> indicates that the IRP is not currently cancelable.</p>
</dd>

### -field <b>UserBuffer</b>

<dd>
<p>Contains the address of an output buffer if both of the following conditions apply:</p>
<ul>
<li>The major function code in the I/O stack location is <a href="https://msdn.microsoft.com/library/windows/hardware/ff548649">IRP_MJ_DEVICE_CONTROL</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff550766">IRP_MJ_INTERNAL_DEVICE_CONTROL</a>.</li>
<li>The I/O control code was defined with METHOD_NEITHER or METHOD_BUFFERED.</li>
</ul>
<p>For METHOD_BUFFERED, the driver should use the buffer pointed to by <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> as the output buffer. When the driver completes the request, the I/O manager copies the contents of this buffer to the output buffer that is pointed to by <b>Irp-&gt;UserBuffer</b>. The driver should not write directly to the buffer pointed to by <b>Irp-&gt;UserBuffer</b>. For more information, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540663">Buffer Descriptions for I/O Control Codes</a>.</p>
</dd>

### -field <b>Tail</b>

<dd>
<dl>

### -field <b>Overlay</b>

<dd>
<dl>

### -field <b>DeviceQueueEntry</b>

<dd>
<p>If IRPs are queued in the device queue associated with the driver's device object, this field links IRPs in the device queue. These links can be used only while the driver is processing the IRP.</p>
</dd>

### -field <b>DriverContext</b>

<dd>
<p>If IRPs are not queued in the device queue associated with the driver's device object, this field can be used by the driver to store up to four pointers. This field can be used only while the driver owns the IRP.</p>
</dd>

### -field <b>Thread</b>

<dd>
<p>A pointer to the caller's thread control block (TCB). For requests that originate in user-mode, the I/O manager always sets this field to point to the TCB of the thread that issued the request.</p>
</dd>

### -field <b>ListEntry</b>

<dd>
<p>If a driver manages its own internal queues of IRPs, it uses this field to link one IRP to the next. These links can be used only while the driver is holding the IRP in its queue or is processing the IRP.</p>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>Undocumented members of the IRP structure are reserved, used only by the I/O manager or, in some cases, by FSDs.</p>

<p>An IRP is the basic I/O manager structure used to communicate with drivers and to allow drivers to communicate with each other. A packet consists of two different parts:</p>

<p><i>Header</i>, or <i>fixed part of the packet</i>— This is used by the I/O manager to store information about the original request, such as the caller's device-independent parameters, the address of the device object upon which a file is open, and so on. It is also used by drivers to store information such as the final status of the request.</p>

<p><i>I/O stack locations</i>— Following the header is a set of <a href="https://msdn.microsoft.com/library/windows/hardware/ff551821">I/O stack locations</a>, one per driver in the chain of layered drivers for which the request is bound. Each stack location contains the parameters, function codes, and context used by the corresponding driver to determine what it is supposed to be doing. For more information, see the <a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a> structure.</p>

<p>While a higher-level driver might check the value of the <b>Cancel</b> Boolean in an IRP, that driver cannot assume the IRP will be completed with STATUS_CANCELLED by a lower-level driver even if the value is <b>TRUE</b>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548397">IoCreateDevice</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549174">IoGetCurrentIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549266">IoGetNextIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549674">IoSetCancelRoutine</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550321">IoSetNextIrpStackLocation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550659">IO_STACK_LOCATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550671">IO_STATUS_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20IRP structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
