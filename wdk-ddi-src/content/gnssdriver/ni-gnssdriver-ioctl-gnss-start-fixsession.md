---
UID: NI.gnssdriver.IOCTL_GNSS_START_FIXSESSION
title: IOCTL_GNSS_START_FIXSESSION
author: windows-driver-content
description: The IOCTL_GNSS_START_FIXSESSION control code is used by the GNSS adapter to start a fix session.
old-location: sensors\ioctl_gnss_start_fixsession.htm
old-project: sensors
ms.assetid: C3D1902A-DEB6-4AC7-B452-66C4636416BB
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
req.alt-api: IOCTL_GNSS_START_FIXSESSION
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

# IOCTL_GNSS_START_FIXSESSION IOCTL



## -description
<p>The <b>IOCTL_GNSS_START_FIXSESSION</b> control code is used by the GNSS adapter to start a fix session.</p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="sensors.gnss_fixsession_param">GNSS_FIXSESSION_PARAM</a> structure.</p>

### -input-buffer-length
<p>Set to sizeof(GNSS_FIXSESSION_PARAM).</p>

<p>Set to sizeof(GNSS_FIXSESSION_PARAM).</p>

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

<p>The fix session successfully started.</p>

<p>A fix session of the same type is already active and the driver does not support multiple sessions.</p>

<p>If multi-session support is not present, the GNSS adapter ensures that multiple sessions of the same fix type are multiplexed properly so that the GNSS driver sees only one session of a given type of fix. The GNSS adapter can modify the fix session parameters of an active fix session through the <a href="..\gnssdriver\ni-gnssdriver-ioctl-gnss-modify-fixsession.md">IOCTL_GNSS_MODIFY_FIXSESSION</a> call.</p>

<p>The GNSS adapter does not start a get fix request unless the driver completes this call and returns a success status in the output.</p>

<p>If multi-session support is not present, and the GNSS adapter sends another start fix request for a fix type that is already active, the GNSS driver must fail the new session request. The driver should not replace the previous session with the new fix session details.</p>

<p>Multiple fix sessions of different fix types are always supported by the GNSS driver.</p>

<p>Once the GNSS driver accepts the fix session parameters, validates them, and kicks off the GNSS engine, it immediately completes the I/O with a success return code. Unless the start fix session returns with a success code, the GNSS adapter will not issue a get fix request. All fixes received for this specific fix session must be delivered to the GNSS adapter against a subsequent pending get fix call from the GNSS adapter that has the same session ID. If a fix becomes available and no pending get fix call is created by the adapter, the GNSS driver is required to queue the fix up to an implementation-specific timeout value, until a pending I/O is created that represents the session ID.</p>

<p>Once a fix session is started, it remains active unless the fix session is explicitly stopped by the GNSS adapter. This applies to all fix types.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_START_FIXSESSION control code%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
