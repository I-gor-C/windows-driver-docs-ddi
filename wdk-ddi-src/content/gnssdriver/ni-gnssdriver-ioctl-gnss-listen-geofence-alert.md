---
UID: NI.gnssdriver.IOCTL_GNSS_LISTEN_GEOFENCE_ALERT
title: IOCTL_GNSS_LISTEN_GEOFENCE_ALERT
author: windows-driver-content
description: The IOCTL_GNSS_LISTEN_GEOFENCE_ALERT control code is used to start listening for geofence alerts from the driver.
old-location: sensors\ioctl_gnss_listen_geofence_alert.htm
old-project: sensors
ms.assetid: 5803A28E-BEBD-4E0D-B8D6-AFE34881C9F5
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
req.alt-api: IOCTL_GNSS_LISTEN_GEOFENCE_ALERT
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

# IOCTL_GNSS_LISTEN_GEOFENCE_ALERT IOCTL



## -description
<p>The IOCTL_GNSS_LISTEN_GEOFENCE_ALERT control code is used to start listening for geofence alerts from the driver.</p>


## -ioctlparameters

### -input-buffer
<p>Set to NULL.</p>

### -input-buffer-length
<p>Set to 0.</p>

<p>Set to 0.</p>

### -output-buffer
<p>A pointer to a <a href="..\gnssdriver\ne-gnssdriver-gnss-event-type.md">GNSS_EVENT</a> structure.

</p>

<p>The EventType must be set to <b>GNSS_Event_GeofenceAlertData</b> and the <b>GeofenceAlertData</b> member filled in.
</p>

<p>A pointer to a <a href="..\gnssdriver\ne-gnssdriver-gnss-event-type.md">GNSS_EVENT</a> structure.

</p>

<p>The EventType must be set to <b>GNSS_Event_GeofenceAlertData</b> and the <b>GeofenceAlertData</b> member filled in.
</p>

<p>A pointer to a <a href="..\gnssdriver\ne-gnssdriver-gnss-event-type.md">GNSS_EVENT</a> structure.

</p>

<p>The EventType must be set to <b>GNSS_Event_GeofenceAlertData</b> and the <b>GeofenceAlertData</b> member filled in.
</p>

### -output-buffer-length
<p>Set to sizeof(GNSS_EVENT).</p>

<p>Set to sizeof(GNSS_EVENT).</p>

<p>Set to sizeof(GNSS_EVENT).</p>

<p>Set to sizeof(GNSS_EVENT).</p>

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
<p>The GNSS adapter keeps a pending request all the time.</p>

<p>When the driver completes the I/O call, the adapter issues another IOCTL to receive the next geofence alert.</p>

<p>The GNSS adapter may keep this IOCTL pending even if there are no geofences, or if geofence tracking operation has been reinitialized through the <b>GNSS_ResetGeofencesTracking</b> driver command. The GNSS driver must not treat this as an error condition.
</p>

<p>Whenever the GNSS driver gets a geofence alert notification from the GNSS engine, it completes the I/O operation.
</p>

<p>If the GNSS adapter is in the process of handling a previous alert and has not issued a pending IOCTL yet, the GNSS driver queues the alert locally and dequeues it whenever the adapter sends this IOCTL.</p>

<p>When a geofence is added for the first time, the initial state (as seen by HLOS) is passed in as a parameter. The GNSS engine should raise the first alert only when there is a change in state from the initial state. This must be handled natively by the GNSS engine itself, as opposed to the GNSS driver filtering out redundant alerts at the driver level, therefore defeating the purpose of unneeded application processor wake-up at initialization.
</p>

<p>This IO request is kept pending until an alert is received from the GNSS engine. When the driver completes the IO call, the GNSS adapter issues another IOCTL to receive the next geofence alert. This IOCTL is kept pending even if there are no geofences or tracking operation has been reinitialized through the <b>GNSS_ResetGeofencesTracking</b> command. If a new pending IOCTL has not been issued and another geofence alert is received, it is queued locally until the next pending IO request is received.
</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_LISTEN_GEOFENCE_ALERT control code%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
