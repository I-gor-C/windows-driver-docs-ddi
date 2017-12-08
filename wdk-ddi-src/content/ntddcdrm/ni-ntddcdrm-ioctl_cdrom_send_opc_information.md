---
UID: NI.ntddcdrm.IOCTL_CDROM_SEND_OPC_INFORMATION
title: IOCTL_CDROM_SEND_OPC_INFORMATION
author: windows-driver-content
description: The IOCTL_CDROM_SEND_OPC_INFORMATION control code can be used in file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish. The optical drive performs the OPC procedure to determine the optimum power of the laser during write. The procedure is necessary to ensure quality, but it wears out the media and should not be performed too often.
old-location: storage\ioctl_cdrom_send_opc_information.htm
old-project: storage
ms.assetid: 77289AB6-7733-4DA1-B4E9-585AA73D137C
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
req.alt-api: IOCTL_CDROM_SEND_OPC_INFORMATION
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

# IOCTL_CDROM_SEND_OPC_INFORMATION IOCTL



## -description
The <b>IOCTL_CDROM_SEND_OPC_INFORMATION</b> 
   control code can be used in  file systems and other implementations that want to perform the Optimum Power Calibration (OPC) procedure in advance, so that the first streaming write does not have to wait for the procedure to finish. The optical drive performs the OPC procedure to determine the optimum power of the laser during write. The procedure is necessary to ensure quality, but it wears out the media and should not be performed too often.
To perform this operation, call the 
   <a href="base.deviceiocontrol">DeviceIoControl</a> 
   function with   <b>IOCTL_CDROM_SEND_OPC_INFORMATION</b> as the <i>dwIoControlCode</i> parameter.

<a href="storage.cdrom_simple_opc_info">CDROM_SIMPLE_OPC_INFO</a>

None.
The <b>Information</b> field is set to the number of bytes returned. 
Because of  status code propagation from other APIs, the <b>Status</b> field can be set to (but is not limited to) the following:

The request completed successfully.
The input buffer length is smaller than required.
The request type is not <b>SimpleOpcInfo</b>.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer

<a href="storage.cdrom_simple_opc_info">CDROM_SIMPLE_OPC_INFO</a>

<a href="storage.cdrom_simple_opc_info">CDROM_SIMPLE_OPC_INFO</a><b>CDROM_SIMPLE_OPC_INFO</b>CDROM_SIMPLE_OPC_INFO

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
Because of  status code propagation from other APIs, the <b>Status</b> field can be set to (but is not limited to) the following:Because of  status code propagation from other APIs, the <b>Status</b>Status field can be set to (but is not limited to) the following:

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
The request type is not <b>SimpleOpcInfo</b>.
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
The request type is not <b>SimpleOpcInfo</b>.
</dd>
The request type is not <b>SimpleOpcInfo</b>.The request type is not <b>SimpleOpcInfo</b>SimpleOpcInfo.


## -remarks
The <b>IOCTL_CDROM_SEND_OPC_INFORMATION</b> IOCTL is a wrapper over the SEND OPC INFORMATION command of the MMC specification. The <b>Exclude0</b> and <b>Exclude1</b> fields directly map to the SEND OPC INFORMATION fields with the same names.

On failures, this IOCTL returns standard errors, such as STATUS_DEVICE_NOT_READY, STATUS_IO_TIMEOUT, STATUS_IO_DEVICE_ERROR.



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
<a href="storage.cdrom_simple_opc_info">CDROM_SIMPLE_OPC_INFO</a>
</dt>
<dt>
<a href="..\ntddcdrm\ni-ntddcdrm-ioctl_cdrom_send_opc_information.md">IOCTL_CDROM_SEND_OPC_INFORMATION</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_SEND_OPC_INFORMATION control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
