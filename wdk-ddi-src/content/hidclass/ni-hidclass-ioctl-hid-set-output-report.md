---
UID: NI.hidclass.IOCTL_HID_SET_OUTPUT_REPORT
title: IOCTL_HID_SET_OUTPUT_REPORT
author: windows-driver-content
description: The IOCTL_HID_SET_OUTPUT_REPORT request sends an output report to a top-level collection.
old-location: hid\ioctl_hid_set_output_report.htm
old-project: hid
ms.assetid: f5c0f3a7-5d90-4a95-9ba0-01aea98d8c79
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: HDAUDIO_STREAM_FORMAT, HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: hidclass.h
req.include-header: Hidclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HID_SET_OUTPUT_REPORT
req.alt-loc: hidclass.h
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

# IOCTL_HID_SET_OUTPUT_REPORT IOCTL



## -description
<p>The IOCTL_HID_SET_OUTPUT_REPORT request sends an output report to a <a href="https://msdn.microsoft.com/dcbee8e3-d03a-45c8-92e4-0897b9f55177">top-level collection</a>.</p>
<p>For general information about HIDClass devices, see <a href="NULL">HID Collections</a>. </p>


## -ioctlparameters

### -input-buffer
<p>The <b>Parameters.DeviceIoControl.InputBufferLength</b> member is set to the size, in bytes, of a requester-allocated input buffer that contains a HID class output report.</p>

<p>The input buffer size, in bytes, must be large enough to hold the output report -- excluding its report ID, if report IDs are used -- plus one additional byte that specifies a nonzero report ID or zero.</p>

<p>The <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> member points to the input buffer that contains an output report. If the collection includes report IDs, the requester must set the first byte of the buffer to a nonzero report ID. Otherwise, the requester must set the first byte to zero. The output report -- excluding its report ID, if report IDs are used -- is located at ((PUCHAR)<i>ReportBuffer</i> + 1).</p>

### -input-buffer-length
<p>The input buffer size, in bytes, must be large enough to hold the output report -- excluding its report ID, if report IDs are used -- plus one additional byte that specifies a nonzero report ID or zero.</p>

<p>The input buffer size, in bytes, must be large enough to hold the output report -- excluding its report ID, if report IDs are used -- plus one additional byte that specifies a nonzero report ID or zero.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

### -output-buffer-length
<p>None.</p>

<p>None.</p>

<p>None.</p>

<p>None.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to zero. </p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to zero. </p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to zero. </p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to zero. </p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

<p>The HID class driver sets the following fields of <b>Irp-&gt;IoStatus</b>:</p>

<p><b>Information</b> is set to zero. </p>

<p><b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidclass.h (include Hidclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538910">HidD_GetFeature</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538945">HidD_GetInputReport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539684">HidD_SetFeature</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff539690">HidD_SetOutputReport</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541100">IOCTL_HID_GET_FEATURE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541126">IOCTL_HID_GET_INPUT_REPORT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541176">IOCTL_HID_SET_FEATURE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_SET_OUTPUT_REPORT control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
