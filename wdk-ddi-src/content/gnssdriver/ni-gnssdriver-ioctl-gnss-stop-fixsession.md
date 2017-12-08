---
UID: NI.gnssdriver.IOCTL_GNSS_STOP_FIXSESSION
title: IOCTL_GNSS_STOP_FIXSESSION
author: windows-driver-content
description: The IOCTL_GNSS_STOP_FIXSESSION control code is used by the GNSS adapter to stop an active fix session.
old-location: sensors\ioctl_gnss_stop_fixsession.htm
old-project: sensors
ms.assetid: 3A15A61A-8822-4E20-9979-B89BFA092281
ms.author: windowsdriverdev
ms.date: 11/30/2017
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
req.alt-api: IOCTL_GNSS_STOP_FIXSESSION
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

# IOCTL_GNSS_STOP_FIXSESSION IOCTL



## -description
<p>The <b>IOCTL_GNSS_STOP_FIXSESSION</b> control code is used by the GNSS adapter to stop an active fix session.</p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="sensors.gnss_stopfixsession_param">GNSS_STOPFIXSESSION_PARAM</a> structure.</p>

### -input-buffer-length
<p>Set to sizeof(GNSS_STOPFIXSESSION_PARAM).</p>

<p>Set to sizeof(GNSS_STOPFIXSESSION_PARAM).</p>

### -output-buffer
<p>Set to NULL.</p>

<p>Set to NULL.</p>

<p>Set to NULL.</p>

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
<p>The driver sets an NTSTATUS value to indicate one of the following results.</p>

<p>The fix session successfully stopped.</p>

<p>The fix session is already stopped or is not active.</p>

<p>The GNSS adapter always issues a stop fix for every successful start fix. If multi-session support is not present, the GNSS adapter stops any active fix session of the same type before issuing a new start fix request.</p>

<p>The GNSS driver must cancel/stop all pending fix requests and then complete the I/O so that when this call returns, the adapter does not receive any fix data pertaining to the stopped session.</p>

<p>If no other fix sessions are active, the GNSS driver should keep the GNSS engine in a cold state.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_STOP_FIXSESSION control code%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
