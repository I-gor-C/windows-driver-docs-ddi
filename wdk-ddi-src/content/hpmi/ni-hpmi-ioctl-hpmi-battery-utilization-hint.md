---
UID: NI.hpmi.IOCTL_HPMI_BATTERY_UTILIZATION_HINT
title: IOCTL_HPMI_BATTERY_UTILIZATION_HINT
author: windows-driver-content
description: Set command sent to HPMI to provide battery utilization hints.
old-location: powermeter\ioctl_hpmi_battery_utilization_hint.htm
old-project: powermeter
ms.assetid: CE326F69-64A4-466E-8A02-5C08AFF8490C
ms.author: windowsdriverdev
ms.date: 11/6/2017
ms.keywords: HIDD_ATTRIBUTES, HIDD_ATTRIBUTES, *PHIDD_ATTRIBUTES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: hpmi.h
req.include-header: Hpmi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1709 and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HPMI_BATTERY_UTILIZATION_HINT
req.alt-loc: hpmi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# IOCTL_HPMI_BATTERY_UTILIZATION_HINT IOCTL



## -description
<p class="CCE_Message">[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.]</p>
<p>Set command sent to HPMI to provide battery utilization hints.
</p>


## -ioctlparameters

### -input-buffer
<p>The AssociatedIrp.SystemBuffer member of the I/O request packet (IRP) points to an initiator-allocated buffer that is used both as the input buffer and the output buffer for the request. On input, this buffer contains a <a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a> structure  in which the version is set to a valid value. </p>

<p>The AssociatedIrp.SystemBuffer member of the I/O request packet (IRP) points to an initiator-allocated buffer that is used both as the input buffer and the output buffer for the request. On input, this buffer contains a <a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a> structure  in which the version is set to a valid value. </p>

### -input-buffer-length
<p>The Parameters.DeviceIoControl.InputBufferLength member of the IRP's current I/O stack location (IO_STACK_LOCATION) is set to the size in bytes of the buffer that is pointed to by the AssociatedIrp.SystemBuffer member. This size must be greater than or equal to sizeof <a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a>  structure  or the request will fail with an error status of STATUS_INVALID_PARAMETER.</p>

<p>The Parameters.DeviceIoControl.InputBufferLength member of the IRP's current I/O stack location (IO_STACK_LOCATION) is set to the size in bytes of the buffer that is pointed to by the AssociatedIrp.SystemBuffer member. This size must be greater than or equal to sizeof <a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a>  structure  or the request will fail with an error status of STATUS_INVALID_PARAMETER.</p>

<p>The Parameters.DeviceIoControl.InputBufferLength member of the IRP's current I/O stack location (IO_STACK_LOCATION) is set to the size in bytes of the buffer that is pointed to by the AssociatedIrp.SystemBuffer member. This size must be greater than or equal to sizeof <a href="..\hpmi\ns-hpmi--hpmi-battery-utilization-hint.md">HPMI_BATTERY_UTILIZATION_HINT</a>  structure  or the request will fail with an error status of STATUS_INVALID_PARAMETER.</p>

### -output-buffer
<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

### -output-buffer-length
<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

<p>TBD</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code, for example STATUS_INVALID_PARAMETER. </p>

## -remarks
<p> This IOCTL may be issued multiple times if HPMI requests HPMI_REQUEST_SERVICE_BATTERY_UTILIZATION_HINTS service.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 10, version 1709 and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hpmi.h (include Hpmi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="powermeter.hpmi_h">hpmi.h</a>
</dt>
<dt>
<a href="..\hpmi\ne-hpmi--hpmi-hint-bool.md">HPMI_HINT_BOOL</a>
</dt>
<dt>
<a href="..\hpmi\ni-hpmi-ioctl-hpmi-battery-utilization-hint.md">IOCTL_HPMI_BATTERY_UTILIZATION_HINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542894">Creating IOCTL Requests in Drivers</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlotherssynchronously.md">WdfIoTargetSendInternalIoctlOthersSynchronously</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendinternalioctlsynchronously.md">WdfIoTargetSendInternalIoctlSynchronously</a>
</dt>
<dt>
<a href="..\wdfiotarget\nf-wdfiotarget-wdfiotargetsendioctlsynchronously.md">WdfIoTargetSendIoctlSynchronously</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--irp.md">IRP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [powermeter\powermeter]:%20IOCTL_HPMI_BATTERY_UTILIZATION_HINT control code%20 RELEASE:%20(11/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
