---
UID: NI.pcivirt.IOCTL_SRIOV_ATTACH
title: IOCTL_SRIOV_ATTACH
author: windows-driver-content
description: The request indicates that the virtualization stack wants to register for Plug and Play events received by the SR-IOV device.
old-location: pci\ioctl-sriov-attach.htm
old-project: PCI
ms.assetid: c1129d60-eeb0-4c90-b181-365f3379d89e
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PARCLASS_INFORMATION, PARCLASS_INFORMATION, *PPARCLASS_INFORMATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: pcivirt.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SRIOV_ATTACH
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
req.iface: 
---

# IOCTL_SRIOV_ATTACH IOCTL



## -description
<p>The  request indicates that the virtualization stack wants to register for Plug and Play events received by the SR-IOV device. </p>


## -syntax

````
    case IOCTL_SRIOV_ATTACH:
        TraceEvents(TRACE_LEVEL_VERBOSE, DBG_IOCTL, "IOCTL_SRIOV_ATTACH:\n");

        WdfWaitLockAcquire(fdoContext->PnpStateLock, NULL);

        //
        // Block until it is safe for the VSP to attach.  Don't
        // bother with pending this IRP since this is always a sent as
        // a synchronous kernel-mode IRP and the caller would block
        // the thread anyway.  May need to repeat the wait since since
        // waiting for the safe-to-attach event must not be done while
        // holding the state lock.
        //
        while (fdoContext->PnpSafeToAttach == FALSE)
        {
            WdfWaitLockRelease(fdoContext->PnpStateLock);

            KeWaitForSingleObject(&fdoContext->PnpSafeEvent,
                                  Executive,
                                  KernelMode,
                                  FALSE,
                                  NULL);

            WdfWaitLockAcquire(fdoContext->PnpStateLock, NULL);
        }

        //
        // Allow only a single attach at any time.
        //
        if (fdoContext->PnpVspAttached == FALSE)
        {
            fdoContext->PnpVspAttached = TRUE;
            status = STATUS_SUCCESS;
        }
        else
        {
            status = STATUS_SHARING_VIOLATION;
        }
        WdfWaitLockRelease(fdoContext->PnpStateLock);

        break;

````


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
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks
<p>This IOCTL request is sent by the virtualization stack to the  PCI Express SR-IOV Physical Function (PF) driver that exposes GUID_DEVINTERFACE_VIRTUALIZABLE_DEVICE.</p>

<p>This request is unsafe if the PF device is currently stopped or stopping for resource re-balance. A device is
considered to be stopped after it received  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551725">IRP_MN_QUERY_STOP_DEVICE</a> and restarted when it receives  <a href="https://msdn.microsoft.com/library/windows/hardware/ff550826">IRP_MN_CANCEL_STOP_DEVICE</a> or when  <a href="https://msdn.microsoft.com/library/windows/hardware/ff551749">IRP_MN_START_DEVICE</a> 
is completed by the lower devices in the stack. In this case, the driver must delay the completion of this request until the device is restarted.    </p>

<p>It is not necessary to keep  this IRP pending because the request always a sent as
        a synchronous kernel-mode IRP causing the caller to block the thread in any case.  
</p>

<p>Upon the completion of this request, the VSP can subsequently  send
<a href="buses.ioctl_sriov_notification">IOCTL_SRIOV_NOTIFICATION</a> and <a href="buses.ioctl_sriov_event_complete">IOCTL_SRIOV_EVENT_COMPLETE</a> requests.  </p>

<p>To unregister for Plug and Play events, the VSP sends the <a href="buses.ioctl_sriov_detach">IOCTL_SRIOV_DETACH</a> request.</p>

<p>These events (defined in <a href="buses._sriov_pf_event">SRIOV_PF_EVENT</a>) cause the completion of  <a href="buses.ioctl_sriov_notification">IOCTL_SRIOV_NOTIFICATION</a> and a wait for  <a href="buses.ioctl_sriov_event_complete">IOCTL_SRIOV_EVENT_COMPLETE</a>:
</p>

<p>In this example handling of the IOCTL_SRIOV_ATTACH request, the PF driver maintains PnP states in its device context. The deviceContext-&gt;PnpRebalancing is set to TRUE, when the driver receives IRP_MN_QUERY_STOP_DEVICE and set to FALSE when it receives IRP_MN_START_DEVICE.</p>

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
<dt>
<a href="buses.ioctl_sriov_detach">IOCTL_SRIOV_DETACH</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [PCI\buses]:%20IOCTL_SRIOV_ATTACH control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
