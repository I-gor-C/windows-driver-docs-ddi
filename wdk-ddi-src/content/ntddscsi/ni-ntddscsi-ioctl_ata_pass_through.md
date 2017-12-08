---
UID: NI.ntddscsi.IOCTL_ATA_PASS_THROUGH
title: IOCTL_ATA_PASS_THROUGH
author: windows-driver-content
description: Allows an application to send almost any ATA command to a target device, with the following restrictions: If a class driver for the target type of device exists, the application must send the request to the class driver.
old-location: storage\ioctl_ata_pass_through.htm
old-project: storage
ms.assetid: 350d9777-18d7-412a-ab60-1e17070a12af
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _MP_STORAGE_DIAGNOSTIC_TARGET_TYPE, MP_STORAGE_DIAGNOSTIC_TARGET_TYPE, *PMP_STORAGE_DIAGNOSTIC_TARGET_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddscsi.h
req.include-header: Ntddscsi.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows Server 2003.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_ATA_PASS_THROUGH
req.alt-loc: Ntddscsi.h
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
---

# IOCTL_ATA_PASS_THROUGH IOCTL



## -description

Allows an application to send almost any ATA command to a target device, with the following restrictions: 
<ul>
<li>
If a class driver for the target type of device exists, the application must send the request to the class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before processing a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application. 
</li>
<li>
This request cannot be used if the command requires the underlying driver to access memory directly. If the caller's command might require direct access to memory, use <a href="..\ntddscsi\ni-ntddscsi-ioctl_ata_pass_through_direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a> instead. 
</li>
<li>
Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous. 
</li>
<li>
Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device. 
</li>
</ul>
The calling application provides the ATA task file register contents for the intended command in the <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> structure. The system double buffers all data transfers. This request is typically used for transferring small amounts of data (less than 16 KB). 

Allows an application to send almost any ATA command to a target device, with the following restrictions: 
If a class driver for the target type of device exists, the application must send the request to the class driver. Thus, an application can send this request directly to the system port driver for a target logical unit (LU) only if there is no class driver for the type of device connected to that LU. The system port driver does not check to determine if a device has been claimed by a class driver before processing a pass-through request. Therefore, if an application bypasses a class driver that has claimed a device and sends a pass-through request for that device directly to the port driver, a conflict for control of the device can occur between the class driver and the application. 
This request cannot be used if the command requires the underlying driver to access memory directly. If the caller's command might require direct access to memory, use <a href="..\ntddscsi\ni-ntddscsi-ioctl_ata_pass_through_direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a> instead. 
Applications must not attempt to send a pass-through request asynchronously. All pass-through requests must be synchronous. 
Applications do not require administrative privileges to send a pass-through request to a device, but they must have read/write access to the device. 
The calling application provides the ATA task file register contents for the intended command in the <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> structure. The system double buffers all data transfers. This request is typically used for transferring small amounts of data (less than 16 KB). 


## -syntax

````
ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength
````


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
<b>
       Parameters.DeviceIoControl.InputBufferLength</b> indicates the size in bytes of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. If the embedded ATA command is a write operation, the size of the input buffer should be the sum of <b>sizeof</b>(<a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a>) and the value in the <b>DataTransferLength</b> member of <b>ATA_PASS_THROUGH_EX</b>. The following pseudocode example shows how to calculate the buffer size:
<b>
       Parameters.DeviceIoControl.InputBufferLength</b>
       Parameters.DeviceIoControl.InputBufferLength indicates the size in bytes of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. If the embedded ATA command is a write operation, the size of the input buffer should be the sum of <b>sizeof</b>sizeof(<a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a><b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX) and the value in the <b>DataTransferLength</b>DataTransferLength member of <b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX. The following pseudocode example shows how to calculate the buffer size:
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>
</td>
</tr>
</table></span></div><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>
</td>
</tr>
</table></span><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>
</td>
</tr>
</table>
<tr>
<th></th>
</tr>
<th></th>

<tr>
<td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>
</td>
</tr>
<td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>
</td>
<pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength</pre>ULONG buffsize; // size of the buffer
ATA_PASS_THROUGH_EX hdr;
hdr.DataTransferLength = size in bytes of the data transfer
buffsize = sizeof (ATA_PASS_THROUGH_EX) + hdr.DataTransferLength



If the embedded ATA command is a read operation or a device control operation that does not involve data transfer, <b>InputBufferLength</b> should be equal to <b>sizeof</b> (ATA_PASS_THROUGH_EX). If the embedded ATA command is a read operation or a device control operation that does not involve data transfer, <b>InputBufferLength</b>InputBufferLength should be equal to <b>sizeof</b>sizeof (ATA_PASS_THROUGH_EX). 
In either case, if <b>InputBufferLength</b> is less than <b>sizeof</b> (ATA_PASS_THROUGH_EX), the port driver fails the I/O request and returns an error.In either case, if <b>InputBufferLength</b>InputBufferLength is less than <b>sizeof</b>sizeof (ATA_PASS_THROUGH_EX), the port driver fails the I/O request and returns an error.
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> should contain an <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> structure, which includes a set of task file input registers that indicate the sort of command to be performed and its parameters. The caller must initialize all the members of this structure except for <b>PathId</b>, <b>TargetId</b>, and <b>Lun</b>, which the port driver fills in. For a data-out command, the <b>DataBufferOffset</b> member of the structure must point to a cache-aligned buffer containing the data to be written. The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer should contain an <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a><b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX structure, which includes a set of task file input registers that indicate the sort of command to be performed and its parameters. The caller must initialize all the members of this structure except for <b>PathId</b>PathId, <b>TargetId</b>TargetId, and <b>Lun</b>Lun, which the port driver fills in. For a data-out command, the <b>DataBufferOffset</b>DataBufferOffset member of the structure must point to a cache-aligned buffer containing the data to be written. 


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The port driver formats the return data using an <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> structure and stores the data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. The port driver formats the return data using an <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a><b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX structure and stores the data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. 
The port driver updates the <b>DataTransferLength</b> member of <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> to indicate the amount of data actually transferred from the device. If the embedded ATA command is a write operation or a device control operation that does not transfer data, <b>OutputBufferLength</b> is equal to <b>sizeof</b>(ATA_PASS_THROUGH_EX). If the embedded ATA command is a read operation, <b>OutputBufferLength</b> is equal to <b>sizeof</b>(ATA_PASS_THROUGH_EX) + <b>DataTransferLength</b>. The port driver updates the <b>DataTransferLength</b>DataTransferLength member of <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a><b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX to indicate the amount of data actually transferred from the device. If the embedded ATA command is a write operation or a device control operation that does not transfer data, <b>OutputBufferLength</b>OutputBufferLength is equal to <b>sizeof</b>sizeof(ATA_PASS_THROUGH_EX). If the embedded ATA command is a read operation, <b>OutputBufferLength</b>OutputBufferLength is equal to <b>sizeof</b>sizeof(ATA_PASS_THROUGH_EX) + <b>DataTransferLength</b>DataTransferLength. 
The port driver fills the <b>CurrentTaskFile</b> member with the values that are present in the device's output registers at the completion of the embedded ATA command. If the command was a data transfer, the port driver stores the transferred data in a cache-aligned buffer that is located at an offset of <b>DataBufferOffset</b> bytes from the beginning of the structure. The application is responsible for interpreting the contents of the output registers to determine what errors, if any, were returned by the device. The port driver fills the <b>CurrentTaskFile</b>CurrentTaskFile member with the values that are present in the device's output registers at the completion of the embedded ATA command. If the command was a data transfer, the port driver stores the transferred data in a cache-aligned buffer that is located at an offset of <b>DataBufferOffset</b>DataBufferOffset bytes from the beginning of the structure. The application is responsible for interpreting the contents of the output registers to determine what errors, if any, were returned by the device. 


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> member is set to the number of bytes returned in the output buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. The <b>Status</b> member is set to STATUS_SUCCESS or possibly to STATUS_BUFFER_TOO_SMALL or STATUS_INVALID_PARAMETER if the input <b>Status</b> value in <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a> is improperly set. The <b>Information</b>Information member is set to the number of bytes returned in the output buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. The <b>Status</b>Status member is set to STATUS_SUCCESS or possibly to STATUS_BUFFER_TOO_SMALL or STATUS_INVALID_PARAMETER if the input <b>Status</b>Status value in <a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a><b>ATA_PASS_THROUGH_EX</b>ATA_PASS_THROUGH_EX is improperly set. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Available starting with Windows Server 2003.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddscsi.h (include Ntddscsi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.ata_pass_through_ex">ATA_PASS_THROUGH_EX</a>
</dt>
<dt>
<a href="..\ntddscsi\ni-ntddscsi-ioctl_ata_pass_through_direct.md">IOCTL_ATA_PASS_THROUGH_DIRECT</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_ATA_PASS_THROUGH control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
