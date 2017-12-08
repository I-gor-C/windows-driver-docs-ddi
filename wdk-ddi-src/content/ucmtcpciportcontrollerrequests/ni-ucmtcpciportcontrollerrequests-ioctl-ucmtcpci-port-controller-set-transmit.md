---
UID: NI.ucmtcpciportcontrollerrequests.IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT
title: IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT
author: windows-driver-content
description: Sets the TRANSMIT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification.
old-location: buses\ioctl_ucmtcpci_port_controller_set_transmit.htm
old-project: usbref
ms.assetid: 5E833F26-2BEC-4021-8D19-F9EFD49C7584
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION, *PUCMTCPCI_PORT_CONTROLLER_IDENTIFICATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ucmtcpciportcontrollerrequests.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT
req.alt-loc: UcmTcpciPortControllerRequests.h
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
req.product: Windows 10 or later.
---

# IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT IOCTL



## -description
<p>Sets the TRANSMIT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification.</p>


## -ioctlparameters

### -input-buffer
<p>A pointer to a <a href="..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md">UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS</a> structure that contains the value to set in the TRANSMIT Register. To get the structure, call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputbuffer.md">WdfRequestRetrieveInputBuffer</a> by passing the received framework request object. This structure is declared in UcmTcpciSpec.h.</p>

<p>A pointer to a <a href="..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md">UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS</a> structure that contains the value to set in the TRANSMIT Register. To get the structure, call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestretrieveinputbuffer.md">WdfRequestRetrieveInputBuffer</a> by passing the received framework request object. This structure is declared in UcmTcpciSpec.h.</p>

### -input-buffer-length
<p>The size of the <a href="..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md">UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS</a> structure.</p>

<p>The size of the <a href="..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md">UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS</a> structure.</p>

<p>The size of the <a href="..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md">UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS</a> structure.</p>

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

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to STATUS_SUCCESS if the request is successful. Otherwise, <b>Status</b> to the appropriate error condition as a <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> code. </p>

## -remarks
<p>The UcmTcpciCx class extension sends this IOCTL request to set the TRANSMIT Register. The value to set is provided in the supplied structure. After setting the value in the register, client driver must call <a href="..\wdfrequest\nf-wdfrequest-wdfrequestcomplete.md">WdfRequestComplete</a> to complete the request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>UcmTcpciPortControllerRequests.h</dt>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
