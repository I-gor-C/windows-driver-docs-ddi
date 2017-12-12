---
UID: NI.winbio_ioctl.IOCTL_BIOMETRIC_UPDATE_FIRMWARE
title: IOCTL_BIOMETRIC_UPDATE_FIRMWARE
author: windows-driver-content
description: The IOCTL_BIOMETRIC_UPDATE_FIRMWARE IOCTL tells the driver to update the firmware for the device with the given firmware image. This IOCTL is optional.
old-location: biometric\ioctl_biometric_update_firmware.htm
old-project: biometric
ms.assetid: 0337956a-09d0-4c9c-8f2d-ac63210431ba
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: _BMP_IMAGE_INFO, BMP_IMAGE_INFO, *PBMP_IMAGE_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_BIOMETRIC_UPDATE_FIRMWARE
req.alt-loc: Winbio_ioctl.h
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
req.product: Windows 10 or later.
---

# IOCTL_BIOMETRIC_UPDATE_FIRMWARE IOCTL



## -description
The IOCTL_BIOMETRIC_UPDATE_FIRMWARE IOCTL tells the driver to update the firmware for the device with the given firmware image.  This IOCTL is optional. 


<a href="biometric.winbio_update_firmware">WINBIO_UPDATE_FIRMWARE</a>


The AssociatedIrp.SystemBuffer member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a> structure.

The smallest valid output buffer size is the size of DWORD.  If the driver receives an DWORD-sized output buffer, the driver should return the buffer size necessary for the requested operation.

Indicates whether the DeviceIoControl call to the driver completed and the OUT payload is valid.

The <b>Status</b> member is set to one of the values in the following table.

S_OK, STATUS_SUCCESS

The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.

E_INVALIDARG

The parameters were not specified correctly.

E_UNKNOWN

Any other failure that prevents the payload from being filled in.

E_UNEXPECTED

Any other failure that prevents the payload from being filled in.

E_FAIL

Any other failure that prevents the payload from being filled in.

 



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer

<a href="biometric.winbio_update_firmware">WINBIO_UPDATE_FIRMWARE</a>


<a href="biometric.winbio_update_firmware">WINBIO_UPDATE_FIRMWARE</a><b>WINBIO_UPDATE_FIRMWARE</b>WINBIO_UPDATE_FIRMWARE

### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The AssociatedIrp.SystemBuffer member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a> structure.</p>The AssociatedIrp.SystemBuffer member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a><b>WINBIO_BLANK_PAYLOAD</b>WINBIO_BLANK_PAYLOAD structure.
The smallest valid output buffer size is the size of DWORD.  If the driver receives an DWORD-sized output buffer, the driver should return the buffer size necessary for the requested operation.</p>The smallest valid output buffer size is the size of DWORD.  If the driver receives an DWORD-sized output buffer, the driver should return the buffer size necessary for the requested operation.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
Indicates whether the DeviceIoControl call to the driver completed and the OUT payload is valid.</p>Indicates whether the DeviceIoControl call to the driver completed and the OUT payload is valid.
The <b>Status</b> member is set to one of the values in the following table.</p>The <b>Status</b>Status member is set to one of the values in the following table.
<table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<tr>
<td>
S_OK, STATUS_SUCCESS

</td>
<td>
The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.

</td>
</tr>
<tr>
<td>
E_INVALIDARG

</td>
<td>
The parameters were not specified correctly.

</td>
</tr>
<tr>
<td>
E_UNKNOWN

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
<tr>
<td>
E_UNEXPECTED

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
<tr>
<td>
E_FAIL

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
</table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<th>Status value</th>Status value
<th>Description</th>Description

<tr>
<td>
S_OK, STATUS_SUCCESS

</td>
<td>
The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.

</td>
</tr>
<td>
S_OK, STATUS_SUCCESS

</td>
S_OK, STATUS_SUCCESS</p>S_OK, STATUS_SUCCESS

<td>
The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.

</td>
The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.</p>The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.


<tr>
<td>
E_INVALIDARG

</td>
<td>
The parameters were not specified correctly.

</td>
</tr>
<td>
E_INVALIDARG

</td>
E_INVALIDARG</p>E_INVALIDARG

<td>
The parameters were not specified correctly.

</td>
The parameters were not specified correctly.</p>The parameters were not specified correctly.


<tr>
<td>
E_UNKNOWN

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
<td>
E_UNKNOWN

</td>
E_UNKNOWN</p>E_UNKNOWN

<td>
Any other failure that prevents the payload from being filled in.

</td>
Any other failure that prevents the payload from being filled in.</p>Any other failure that prevents the payload from being filled in.


<tr>
<td>
E_UNEXPECTED

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
<td>
E_UNEXPECTED

</td>
E_UNEXPECTED</p>E_UNEXPECTED

<td>
Any other failure that prevents the payload from being filled in.

</td>
Any other failure that prevents the payload from being filled in.</p>Any other failure that prevents the payload from being filled in.


<tr>
<td>
E_FAIL

</td>
<td>
Any other failure that prevents the payload from being filled in.

</td>
</tr>
<td>
E_FAIL

</td>
E_FAIL</p>E_FAIL

<td>
Any other failure that prevents the payload from being filled in.

</td>
Any other failure that prevents the payload from being filled in.</p>Any other failure that prevents the payload from being filled in.



 </p> 


## -remarks
The firmware image is specific to each vendor and may contain both firmware data and any extra data that the driver needs to validate the image.

If the device has a different firmware update mechanism, the driver can return E_NOTIMPL for this IOCTL.

If the vendor-supplied driver passes back the entire payload, it should fill in the WinBioHresult member of WINBIO_BLANK_PAYLOAD with the status of the Biometric operation.

Possible values include:



The operation completed successfully.

The device cannot update firmware while in data collection mode.

The device could not be put into firmware update mode.

The firmware was not updated due to device error.


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows 7 and later versions of Windows.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Winbio_ioctl.h</dt>
</dl>
</td>
</tr>
</table>