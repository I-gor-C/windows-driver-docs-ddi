---
UID: NI.winbio_ioctl.IOCTL_BIOMETRIC_RESET
title: IOCTL_BIOMETRIC_RESET
author: windows-driver-content
description: The IOCTL_BIOMETRIC_RESET IOCTL resets the device to a known or idle state, according to the current power state. Vendor-supplied WBDI drivers must support this IOCTL.
old-location: biometric\ioctl_biometric_reset.htm
old-project: biometric
ms.assetid: 4385911b-ae38-4748-ad11-cc161922776a
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
req.alt-api: IOCTL_BIOMETRIC_RESET
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

# IOCTL_BIOMETRIC_RESET IOCTL



## -description
The IOCTL_BIOMETRIC_RESET IOCTL resets the device to a known or idle state, according to the current power state.  Vendor-supplied WBDI drivers must support this IOCTL.

None

The <b>AssociatedIrp</b>.<b>SystemBuffer</b> member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a> structure.

The vendor-supplied driver can optionally return a DWORD-sized buffer that specifies the buffer size necessary for the requested operation.

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
None</p>None


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The <b>AssociatedIrp</b>.<b>SystemBuffer</b> member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a> structure.</p>The <b>AssociatedIrp</b>AssociatedIrp.<b>SystemBuffer</b>SystemBuffer member points to a buffer that contains a <a href="biometric.winbio_blank_payload">WINBIO_BLANK_PAYLOAD</a><b>WINBIO_BLANK_PAYLOAD</b>WINBIO_BLANK_PAYLOAD structure.
The vendor-supplied driver can optionally return a DWORD-sized buffer that specifies the buffer size necessary for the requested operation.</p>The vendor-supplied driver can optionally return a DWORD-sized buffer that specifies the buffer size necessary for the requested operation.


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
IOCTL_BIOMETRIC_RESET cancels a data collection IOCTL, if one is pending.  If there is a vendor-specific operation in progress, the driver should cancel the operation and reset the device whenever possible. 

If the vendor-supplied driver passes back the entire payload, it should fill in the <b>WinBioHresult</b> member of WINBIO_BLANK_PAYLOAD with the status of the Biometric operation.


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