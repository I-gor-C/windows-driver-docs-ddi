---
UID: NI:hidclass.IOCTL_HID_GET_INPUT_REPORT
title: IOCTL_HID_GET_INPUT_REPORT
author: windows-driver-content
description: IOCTL_HID_GET_INPUT_REPORT returns an input report from a HID Class device.
old-location: hid\ioctl_hid_get_input_report.htm
old-project: hid
ms.assetid: 800bc24b-dfa3-4da1-b9de-9d8d6e470d7e
ms.author: windowsdriverdev
ms.date: 12/21/2017
ms.keywords: hid.ioctl_hid_get_input_report, IOCTL_HID_GET_INPUT_REPORT control code [Human Input Devices], IOCTL_HID_GET_INPUT_REPORT, hidclass/IOCTL_HID_GET_INPUT_REPORT, hidioreq_6b2d889e-4579-464f-bd03-0d55bcf99687.xml
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
topictype:
-	APIRef
-	kbSyntax
apitype:
-	HeaderDef
apilocation:
-	hidclass.h
apiname:
-	IOCTL_HID_GET_INPUT_REPORT
product: Windows
targetos: Windows
req.typenames: HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
---

# IOCTL_HID_GET_INPUT_REPORT IOCTL
IOCTL_HID_GET_INPUT_REPORT returns an input report from a HID Class device.

For general information about HIDClass devices, see <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID Collections</a>.

### Major Code
[IRP_MJ_DEVICE_CONTROL](xref:"https://docs.microsoft.com/en-us/windows-hardware/drivers/kernel/irp-mj-device-control")

### Input Buffer
<b>Irp-&gt;UserBuffer</b> points to a <a href="..\hidclass\ns-hidclass-_hid_xfer_packet.md">HID_XFER_PACKET</a> structure that the HID class driver uses to input the following members:

### Input Buffer Length
The size of a <a href="..\hidclass\ns-hidclass-_hid_xfer_packet.md">HID_XFER_PACKET</a> structure.

### Output Buffer
((PHID_XFER_PACKET)(<b>Irp-&gt;UserBuffer</b>))-&gt;<b>reportBuffer</b> points to the requester-allocated output buffer that the HID minidriver uses to return the input report.

### Output Buffer Length
The size of the input report.

### Input / Output Buffer
<text></text>

### Input / Output Buffer Length
<text></text>

### Status Block
HID minidrivers that carry out the I/O to the device set the following fields of <b>Irp-&gt;IoStatus</b>:
<ul>
<li>
<b>Information</b> is set to the number of bytes transferred from the device.

</li>
<li>
<b>Status</b> is set to STATUS_SUCCESS if the transfer completed without error. Otherwise, it is set to an appropriate NTSTATUS error code.

</li>
</ul>HID minidrivers that call other drivers with this IOCTL to carry out the I/O to their device, should ensure that the <b>Information</b> field of the status block is correct and not change the contents of the <b>Status</b> field.

## Remarks
IOCTL_HID_GET_INPUT_REPORT is used for making a one-time request to get the current, or the most recent report from the device. This request is typically sent down by the HID client (via HIDCLASS).

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | hidclass.h (include Hidclass.h) |

## See Also

<a href="..\hidclass\ns-hidclass-_hid_xfer_packet.md">HID_XFER_PACKET</a>

<a href="..\hidclass\ni-hidclass-ioctl_hid_set_feature.md">IOCTL_HID_SET_FEATURE</a>

<a href="..\hidport\ni-hidport-ioctl_hid_read_report.md">IOCTL_HID_READ_REPORT</a>

<a href="..\hidsdi\nf-hidsdi-hidd_setoutputreport.md">HidD_SetOutputReport</a>

<a href="..\hidclass\ni-hidclass-ioctl_hid_set_output_report.md">IOCTL_HID_SET_OUTPUT_REPORT</a>

<a href="..\hidclass\ni-hidclass-ioctl_hid_get_feature.md">IOCTL_HID_GET_FEATURE</a>

<a href="..\hidsdi\nf-hidsdi-hidd_getfeature.md">HidD_GetFeature</a>

<a href="..\hidsdi\nf-hidsdi-hidd_getinputreport.md">HidD_GetInputReport</a>

<a href="..\hidport\ni-hidport-ioctl_hid_write_report.md">IOCTL_HID_WRITE_REPORT</a>

<a href="..\hidsdi\nf-hidsdi-hidd_setfeature.md">HidD_SetFeature</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_GET_INPUT_REPORT control code%20 RELEASE:%20(12/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>