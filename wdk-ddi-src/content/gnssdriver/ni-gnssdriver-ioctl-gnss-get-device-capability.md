---
UID: NI.gnssdriver.IOCTL_GNSS_GET_DEVICE_CAPABILITY
title: IOCTL_GNSS_GET_DEVICE_CAPABILITY
author: windows-driver-content
description: The IOCTL_GNSS_GET_DEVICE_CAPABILITY control code is used by the GNSS adapter to get the GNSS driver and device capabilities.
old-location: sensors\ioctl_gnss_get_device_capability.htm
old-project: sensors
ms.assetid: 28673D2A-5DD6-42CD-BD91-5C30B905ECF0
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
req.alt-api: IOCTL_GNSS_GET_DEVICE_CAPABILITY
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

# IOCTL_GNSS_GET_DEVICE_CAPABILITY IOCTL



## -description
<p>The IOCTL_GNSS_GET_DEVICE_CAPABILITY control code is used by the GNSS adapter to get the GNSS driver and device capabilities. The GNSS driver also specifies various support requirements from the HLOS components. This information is needed by the GNSS driver as well as the location service for deferring location-specific functionality to the GNSS device.</p>


## -ioctlparameters

### -input-buffer
<p>Set to NULL.</p>

### -input-buffer-length
<p>Set to 0.</p>

<p>Set to 0.</p>

### -output-buffer
<p>Pointer to a GNSS_DEVICE_CAPABILITY structure.</p>

<p>Pointer to a GNSS_DEVICE_CAPABILITY structure.</p>

<p>Pointer to a GNSS_DEVICE_CAPABILITY structure.</p>

### -output-buffer-length
<p>Set to sizeof(GNSS_DEVICE_CAPABILITY).</p>

<p>Set to sizeof(GNSS_DEVICE_CAPABILITY).</p>

<p>Set to sizeof(GNSS_DEVICE_CAPABILITY).</p>

<p>Set to sizeof(GNSS_DEVICE_CAPABILITY).</p>

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
<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

<p>On completion, the GNSS adapter stores the capability information in its state variables and communicates the same to other location components. Depending on the specific device capabilities and/or support requirements, the GNSS adapter can also load/unload other components to provide the needed support.</p>

<p>Driver fills the output buffer and completes the I/O.</p>

<p>This should be called when the GNSS adapter is initializing the GNSS driver.</p>

<p>Even if the driver supports a specific functionality or needs a specific functionality support from the HLOS, it is not guaranteed that the HLOS will leverage a specific driver capability, or will provided the needed level of support to the driver.</p>

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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20IOCTL_GNSS_GET_DEVICE_CAPABILITY control code%20 RELEASE:%20(11/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
