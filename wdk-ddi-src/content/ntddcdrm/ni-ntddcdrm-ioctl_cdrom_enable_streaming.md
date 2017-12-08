---
UID: NI.ntddcdrm.IOCTL_CDROM_ENABLE_STREAMING
title: IOCTL_CDROM_ENABLE_STREAMING
author: windows-driver-content
description: Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests.
old-location: storage\ioctl_cdrom_enable_streaming.htm
old-project: storage
ms.assetid: DC31EABA-CE58-4B6F-ADCD-0BF72A92C6AB
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _WRITE_ROTATION, *PWRITE_ROTATION, WRITE_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Winioctl.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_CDROM_ENABLE_STREAMING
req.alt-loc: ntddcdrm.h
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

# IOCTL_CDROM_ENABLE_STREAMING IOCTL



## -description
Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests. 
To perform this operation, call the 
   <a href="base.deviceiocontrol">DeviceIoControl</a> 
   function and specify the <b>IOCTL_CDROM_ENABLE_STREAMING</b> I/O control request as the <i>dwIoControlCode</i> parameter.

<a href="storage.cdrom_streaming_control">CDROM_STREAMING_CONTROL</a>

None.
The <b>Information</b> field is set to the number of bytes returned. 
Because of  status code propagation from other APIs, the <b>Status</b> field can be set to (but not limited to) the following:

The request completed successfully.
The input buffer length is smaller than required.
The request type is not one of the four in types defined in the <b>STREAMING_CONTROL_REQUEST_TYPE</b> enumeration.
Cannot find the file object context in the request.
The requested streaming mode is not supported.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer

<a href="storage.cdrom_streaming_control">CDROM_STREAMING_CONTROL</a>

<a href="storage.cdrom_streaming_control">CDROM_STREAMING_CONTROL</a><b>CDROM_STREAMING_CONTROL</b>CDROM_STREAMING_CONTROL

### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
None.None.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes returned. The <b>Information</b>Information field is set to the number of bytes returned. 
Because of  status code propagation from other APIs, the <b>Status</b> field can be set to (but not limited to) the following:Because of  status code propagation from other APIs, the <b>Status</b>Status field can be set to (but not limited to) the following:

<dl>
<dt><a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS</dt>
<dd>
The request completed successfully.
</dd>
<dt><a id="STATUS_INFO_LENGTH_MISMATCH"></a><a id="status_info_length_mismatch"></a>STATUS_INFO_LENGTH_MISMATCH</dt>
<dd>
The input buffer length is smaller than required.
</dd>
<dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER</dt>
<dd>
The request type is not one of the four in types defined in the <b>STREAMING_CONTROL_REQUEST_TYPE</b> enumeration.
</dd>
<dt><a id="STATUS_INVALID_HANDLE"></a><a id="status_invalid_handle"></a>STATUS_INVALID_HANDLE</dt>
<dd>
Cannot find the file object context in the request.
</dd>
<dt><a id="STATUS_INVALID_DEVICE_REQUEST"></a><a id="status_invalid_device_request"></a>STATUS_INVALID_DEVICE_REQUEST</dt>
<dd>
The requested streaming mode is not supported.
</dd>
</dl>
<dt><a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS</dt><a id="STATUS_SUCCESS"></a><a id="status_success"></a>STATUS_SUCCESS
<dd>
The request completed successfully.
</dd>
The request completed successfully.The request completed successfully.

<dt><a id="STATUS_INFO_LENGTH_MISMATCH"></a><a id="status_info_length_mismatch"></a>STATUS_INFO_LENGTH_MISMATCH</dt><a id="STATUS_INFO_LENGTH_MISMATCH"></a><a id="status_info_length_mismatch"></a>STATUS_INFO_LENGTH_MISMATCH
<dd>
The input buffer length is smaller than required.
</dd>
The input buffer length is smaller than required.The input buffer length is smaller than required.

<dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER</dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER
<dd>
The request type is not one of the four in types defined in the <b>STREAMING_CONTROL_REQUEST_TYPE</b> enumeration.
</dd>
The request type is not one of the four in types defined in the <b>STREAMING_CONTROL_REQUEST_TYPE</b> enumeration.The request type is not one of the four in types defined in the <b>STREAMING_CONTROL_REQUEST_TYPE</b>STREAMING_CONTROL_REQUEST_TYPE enumeration.

<dt><a id="STATUS_INVALID_HANDLE"></a><a id="status_invalid_handle"></a>STATUS_INVALID_HANDLE</dt><a id="STATUS_INVALID_HANDLE"></a><a id="status_invalid_handle"></a>STATUS_INVALID_HANDLE
<dd>
Cannot find the file object context in the request.
</dd>
Cannot find the file object context in the request.Cannot find the file object context in the request.

<dt><a id="STATUS_INVALID_DEVICE_REQUEST"></a><a id="status_invalid_device_request"></a>STATUS_INVALID_DEVICE_REQUEST</dt><a id="STATUS_INVALID_DEVICE_REQUEST"></a><a id="status_invalid_device_request"></a>STATUS_INVALID_DEVICE_REQUEST
<dd>
The requested streaming mode is not supported.
</dd>
The requested streaming mode is not supported.The requested streaming mode is not supported.


## -remarks
By default, streaming is disabled for all newly opened raw CDROM handles. A playback application that does not want to use the  file system and prefers to work with raw data should open two file handles for the same device: a regular one for file system metadata and a streaming one for real-time files.


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdrm.h (include Winioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="base.deviceiocontrol">DeviceIoControl</a>
</dt>
<dt>
<a href="storage.cdrom_streaming_control">CDROM_STREAMING_CONTROL</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_ENABLE_STREAMING control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
