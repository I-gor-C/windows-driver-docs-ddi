---
UID: NI.gnssdriver.IOCTL_GNSS_INJECT_AGNSS
title: IOCTL_GNSS_INJECT_AGNSS
author: windows-driver-content
description: The IOCTL_GNSS_INJECT_AGNSS control code is used by the GNSS adapter to inject AGNSS data into the driver. This IOCTL is sent as a result of the driver previously responding to a pending IOCTL_GNSS_LISTEN_AGNSS request.
old-location: sensors\ioctl_gnss_inject_agnss.htm
old-project: sensors
ms.assetid: 68EC4397-1983-4D02-BF6E-599DC987E7E9
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: FWPS_VSWITCH_EVENT_DISPATCH_TABLE0_, FWPS_VSWITCH_EVENT_DISPATCH_TABLE0
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_GNSS_INJECT_AGNSS
req.alt-loc: gnssdriver.h
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

# IOCTL_GNSS_INJECT_AGNSS IOCTL



## -description
<p>The <b>IOCTL_GNSS_INJECT_AGNSS</b> control code is used by the GNSS adapter to inject AGNSS data into the driver. This IOCTL is sent as a result of the driver previously responding to a pending <a href="..\gnssdriver\ni-gnssdriver-ioctl-gnss-listen-agnss.md">IOCTL_GNSS_LISTEN_AGNSS</a> request. </p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="sensors.gnss_agnss_inject">GNSS_AGNSS_INJECT</a> structure.</p>

### -input-buffer-length
<p>Set to sizeof(GNSS_AGNSS_INJECT).</p>

<p>Set to sizeof(GNSS_AGNSS_INJECT).</p>

### -output-buffer
<p>Set to <b>NULL</b>.</p>

<p>Set to <b>NULL</b>.</p>

<p>Set to <b>NULL</b>.</p>

### -output-buffer-length
<p>Set to 0.</p>

<p>Set to 0.</p>

<p>Set to 0.</p>

<p>Set to 0.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks
<p>
<a href="sensors.gnss_agnss_inject">GNSS_AGNSS_INJECT</a>
</p>

<p>Depending on the InjectionType element, the appropriate data element is filled.</p>

<p>NTSTATUS with the following indications:</p>

<p>Success: AGNSS data injection was accepted.</p>

<p>Failed: AGNSS data injection failed.</p>

<p>When the GNSS adapter fails to get time for injection, it sets the InjectionStatus element. The driver must check that this element indicates success, before actually using the element data.</p>

<p>In case of failure in gathering injection data, the adapter does not automatically retry. It is up to the driver to retry the same request sequent.</p>

<p>This is a fire-and-forget IOCTL. The GNSS adapter does not handle error even if the driver returns a failure indicating that the injection data was not used.</p>

<p>The GNSS driver completes the I/O request after consuming the injection data.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
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
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_INJECT_AGNSS control code%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
