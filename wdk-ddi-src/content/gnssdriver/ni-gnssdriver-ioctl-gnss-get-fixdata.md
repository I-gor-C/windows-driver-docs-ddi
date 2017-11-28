---
UID: NI.gnssdriver.IOCTL_GNSS_GET_FIXDATA
title: IOCTL_GNSS_GET_FIXDATA
author: windows-driver-content
description: The IOCTL_GNSS_GET_FIXDATA control code is used by the GNSS adapter to register to receive the next fix data from an active fix session.
old-location: sensors\ioctl_gnss_get_fixdata.htm
old-project: sensors
ms.assetid: 037B5AD9-39C2-4F50-8E63-0736EA37FEF9
ms.author: windowsdriverdev
ms.date: 11/26/2017
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
req.alt-api: IOCTL_GNSS_GET_FIXDATA
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

# IOCTL_GNSS_GET_FIXDATA IOCTL



## -description
<p>The <b>IOCTL_GNSS_GET_FIXDATA</b> 
   control code is used by the GNSS adapter to register to receive the next fix data from an active fix session. This IOCTL provides the GNSS driver with a pending I/O request, the asynchronous resolution of which notifies the adapter that data is being provided through the overlapped structures <b>GnssEvent</b> member as a data buffer. The GnssEvent member is a <a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a> structure.
</p>


## -ioctlparameters

### -input-buffer
<p>Pointer to a DWORD value that represents the fix session ID.

</p>

### -input-buffer-length
<p>Set to sizeof(DWORD).

</p>

<p>Set to sizeof(DWORD).

</p>

### -output-buffer
<p>Set to NULL</p>

<p>Set to NULL</p>

<p>Set to NULL</p>

### -output-buffer-length
<p>Set to 0.

</p>

<p>Set to 0.

</p>

<p>Set to 0.

</p>

<p>Set to 0.

</p>

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
<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

<p><b>FixSessionID</b>: Session ID for an active fix.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn925134">GNSS_EVENT</a>
</p>

<p>The <b>EventType</b> element must be set to <b>GNSS_Event_FixAvailable</b>.</p>

<p>The data associated with this event is of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn925139">GNSS_FIXDATA</a>.</p>

<p>The GNSS adapter issues one or more get fix request after starting a fix session. This call creates a pending I/O against which the GNSS driver can return fix data when it is available from the underlying GNSS engine or cache value.</p>

<p>Whenever a fix data is ready, the driver fills the buffer and completes the I/O. The driver must ensure that the data is returned for the specified fix session ID.</p>

<p>Whenever fix data is ready, the driver must fill the buffer and complete the I/O request. It is the driver’s responsibility to ensure that the data is returned for the specified fix session ID. Additionally, when a fix session is stopped by the GNSS adapter issuing an <a href="https://msdn.microsoft.com/library/windows/hardware/dn917752">IOCTL_GNSS_STOP_FIXSESSION</a>, the driver must cancel all pending get fix requests for the given fix session ID.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548651">WdfIoTargetSendInternalIoctlOthersSynchronously</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548656">WdfIoTargetSendInternalIoctlSynchronously</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548660">WdfIoTargetSendIoctlSynchronously</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_GET_FIXDATA control code%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
