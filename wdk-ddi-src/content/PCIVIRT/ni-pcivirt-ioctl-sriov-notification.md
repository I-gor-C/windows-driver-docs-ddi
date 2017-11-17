---
UID: NI.pcivirt.IOCTL_SRIOV_NOTIFICATION
title: IOCTL_SRIOV_NOTIFICATION
author: windows-driver-content
description: The request indicates that the virtualization stack wants to be notified when one of the events listed in SRIOV_PF_EVENT occurs.
old-location: pci\ioctl-sriov-notification.htm
ms.assetid: 3f2d67e0-abab-40a1-b4a9-cb65e81884e9
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: PCI
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SRIOV_NOTIFICATION
req.alt-loc: Pcivirt.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
req.iface: 
---

# IOCTL_SRIOV_NOTIFICATION IOCTL



## -description
<p>The  request indicates that the virtualization stack wants to be notified when one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a> occurs.  </p>


## -syntax

````
    case IOCTL_SRIOV_NOTIFICATION:
        TraceEvents(TRACE_LEVEL_VERBOSE, DBG_IOCTL, 
            "IOCTL_SRIOV_NOTIFICATION:\n");

        status = WdfRequestForwardToIoQueue(Request,
                                            fdoContext->NotificationQueue);
        if (!NT_SUCCESS(status))
        {
            // not able to push it into manual queue, too bad.
            TraceEvents(TRACE_LEVEL_ERROR, DBG_PNP,
                        "WdfRequestForwardToIoQueue failed status=%!STATUS!\n",
                        status);
            break;
        }

        //
        // Pnp might arrived before SRIOV_NOTIFICATION. Serve the new
        // outstanding pnp if there is one.
        //
        CheckPendingNotifications(fdoContext);
        status = STATUS_PENDING;
        break;




````


## -ioctlparameters

### -input-buffer

<text></text>

### -input-buffer-length

<text></text>

### -output-buffer
<p>A buffer that contains an <a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>-type value that is filled by the  physical function (PF) driver when it completes the request.</p>

<p>A buffer that contains an <a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>-type value that is filled by the  physical function (PF) driver when it completes the request.</p>

### -output-buffer-length
<p>A pointer to the variable, which is assigned the number of
    written bytes to the output buffer when the request is completed.</p>

<p>A pointer to the variable, which is assigned the number of
    written bytes to the output buffer when the request is completed.</p>

<p>A pointer to the variable, which is assigned the number of
    written bytes to the output buffer when the request is completed.</p>

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

## -remarks
<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>. The driver then completes the pending request.
</p>

<p>If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.
</p>

<p>The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.</p>

<p>  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>. The driver then completes the pending request.
</p>

<p>If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.
</p>

<p>The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.</p>

<p>  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>. The driver then completes the pending request.
</p>

<p>If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.
</p>

<p>The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.</p>

<p>  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>. The driver then completes the pending request.
</p>

<p>If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.
</p>

<p>The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.</p>

<p>  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>The <b>IOCTL_SRIOV_NOTIFICATION</b> request is held in a queue by the PF driver until the request is either cancelled by sender or the device experiences one of the events listed in
<a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>. The driver then completes the pending request.
</p>

<p>If the PF driver receives this IOCTL request while processing a Plug and Play event  for which the driver has not 
yet completed a notification, it should complete the IOCTL request immediately with the 
event details in the output buffer.  Otherwise, the driver should queue the request until either it is cancelled
or a Plug and Play event that requires notification occurs.
</p>

<p>The virtualization stack can send the <b>IOCTL_SRIOV_NOTIFICATION</b> request immediately after the previous <b>IOCTL_SRIOV_NOTIFICATION</b> request completes.   The PF driver must keep track of the fact 
that an event notification has been delivered and must not complete two IOCTL requests for the same event twice.</p>

<p>  It is pended by the PF driver until it is canceled by the sender or until the PF driver experiences one of several PnP events, at which point it is completed. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pcivirt.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>