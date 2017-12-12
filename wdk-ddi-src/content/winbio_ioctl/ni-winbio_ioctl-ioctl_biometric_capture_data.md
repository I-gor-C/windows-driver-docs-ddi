---
UID: NI.winbio_ioctl.IOCTL_BIOMETRIC_CAPTURE_DATA
title: IOCTL_BIOMETRIC_CAPTURE_DATA
author: windows-driver-content
description: The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL directs the driver to retrieve the next scan of biometric data. This call should put the device into capture mode.Vendor-supplied WBDI drivers must support IOCTL_BIOMETRIC_CAPTURE_DATA.
old-location: biometric\ioctl_biometric_capture_data.htm
old-project: biometric
ms.assetid: 52c7007f-6038-41d8-b459-f0fa1b90fd5e
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
req.alt-api: IOCTL_BIOMETRIC_CAPTURE_DATA
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

# IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL



## -description
The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL directs the driver to retrieve the next scan of biometric data.   This call should put the device into capture mode.Vendor-supplied WBDI drivers must support IOCTL_BIOMETRIC_CAPTURE_DATA.



Vendor-supplied WBDI drivers must support IOCTL_BIOMETRIC_CAPTURE_DATA.


<a href="biometric.winbio_capture_parameters">WINBIO_CAPTURE_PARAMETERS</a>


The <b>AssociatedIrp</b>.<b>SystemBuffer</b> member points to a buffer that contains a <a href="biometric.winbio_capture_data">WINBIO_CAPTURE_DATA</a> structure.

The smallest valid output buffer size is the size of DWORD.

If the driver receives a DWORD-sized output buffer, the driver must immediately return the buffer size necessary to complete the operation.  Do not wait for the swipe to occur to send the required buffer size.

The vendor-specific data in the WINBIO_BIR structure can be in any format the vendor would like to collect from the driver.  Vendors can choose to process data in the WBDI driver or in the engine adapter, but the data must be passed in one structure.  

Indicates whether the DeviceIoControl call to the driver completed and the OUT payload is valid.

The <b>Status</b> member is set to one of the values in the following table.

S_OK, STATUS_SUCCESS

The operation completed successfully.  If the size of data returned is DWORD, the payload contains the size of the buffer necessary for the call.  Otherwise, the payload contains the full output buffer.

E_INVALIDARG

The parameters were not specified correctly.

WINBIO_E_DATA_COLLECTION_IN_PROGRESS

Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.

E_UNKNOWN

Any other failure that prevents the payload from being filled in.

E_UNEXPECTED

Any other failure that prevents the payload from being filled in.

E_FAIL

Any other failure that prevents the payload from being filled in.

 



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer

<a href="biometric.winbio_capture_buffer">WINBIO_CAPTURE_BUFFER</a>


<a href="biometric.winbio_capture_buffer">WINBIO_CAPTURE_BUFFER</a><b>WINBIO_CAPTURE_BUFFER</b>WINBIO_CAPTURE_BUFFER

### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The <b>AssociatedIrp</b>.<b>SystemBuffer</b> member points to a buffer that contains a <a href="biometric.winbio_capture_data">WINBIO_CAPTURE_DATA</a> structure.</p>The <b>AssociatedIrp</b>AssociatedIrp.<b>SystemBuffer</b>SystemBuffer member points to a buffer that contains a <a href="biometric.winbio_capture_data">WINBIO_CAPTURE_DATA</a><b>WINBIO_CAPTURE_DATA</b>WINBIO_CAPTURE_DATA structure.
The smallest valid output buffer size is the size of DWORD.</p>The smallest valid output buffer size is the size of DWORD.
If the driver receives a DWORD-sized output buffer, the driver must immediately return the buffer size necessary to complete the operation.  Do not wait for the swipe to occur to send the required buffer size.</p>If the driver receives a DWORD-sized output buffer, the driver must immediately return the buffer size necessary to complete the operation.  Do not wait for the swipe to occur to send the required buffer size.
The vendor-specific data in the WINBIO_BIR structure can be in any format the vendor would like to collect from the driver.  Vendors can choose to process data in the WBDI driver or in the engine adapter, but the data must be passed in one structure.  </p>The vendor-specific data in the WINBIO_BIR structure can be in any format the vendor would like to collect from the driver.  Vendors can choose to process data in the WBDI driver or in the engine adapter, but the data must be passed in one structure.  


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
WINBIO_E_DATA_COLLECTION_IN_PROGRESS

</td>
<td>
Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.

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
WINBIO_E_DATA_COLLECTION_IN_PROGRESS

</td>
<td>
Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.

</td>
</tr>
<td>
WINBIO_E_DATA_COLLECTION_IN_PROGRESS

</td>
WINBIO_E_DATA_COLLECTION_IN_PROGRESS</p>WINBIO_E_DATA_COLLECTION_IN_PROGRESS

<td>
Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.

</td>
Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.</p>Device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending.


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
Only one data collection IOCTL can be pending at any time.  If the device has an IOCTL_BIOMETRIC_CAPTURE_DATA pending, IOCTL_BIOMETRIC_CAPTURE_DATA must return WINBIO_E_DATA_COLLECTION_IN_PROGRESS.

IOCTL_BIOMETRIC_CAPTURE_DATA is a blocking data collection IOCTL that is completed when the biometric data capture occurs. 

If the vendor-supplied driver passes back the entire payload, it should fill in the <b>WinBioHresult</b> member of WINBIO_CAPTURE_DATA with the status of the Biometric operation.

Possible values include:



The operation completed successfully.

There is already a data collection IOCTL pending.

The format specified is not supported by this driver and device.

The type of data requested is not supported by this driver and device.

The device could not be put into biometric capture mode.  This could be because the device is in another non-data collection mode.

The operation was not completed due to device error.

The device is in the middle of a vendor-specific operation.

The operation was canceled either by the caller, or by someone issuing an IOCTL_BIOMETRIC_RESET

The capture purpose specified is not supported by the driver.


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