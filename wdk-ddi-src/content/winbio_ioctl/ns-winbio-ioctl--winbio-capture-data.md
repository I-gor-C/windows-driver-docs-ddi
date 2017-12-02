---
UID: NS.winbio_ioctl._WINBIO_CAPTURE_DATA
title: WINBIO_CAPTURE_DATA
author: windows-driver-content
description: The IOCTL_BIOMETRIC_CAPTURE_DATA IOCTL returns the WINBIO_CAPTURE_DATA structure as output.
old-location: biometric\winbio_capture_data.htm
old-project: biometric
ms.assetid: 1d1df123-4c1a-498b-b629-ca63336a762b
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_CAPTURE_DATA, WINBIO_CAPTURE_DATA, *PWINBIO_CAPTURE_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: winbio_ioctl.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WINBIO_CAPTURE_DATA
req.alt-loc: winbio_ioctl.h
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
req.iface: IWiaTransferCallback
req.product: Windows 10 or later.
---

# WINBIO_CAPTURE_DATA structure



## -description
<p>The <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-capture-data.md">IOCTL_BIOMETRIC_CAPTURE_DATA</a> IOCTL returns the WINBIO_CAPTURE_DATA structure as output.</p>


## -syntax

````
typedef struct _WINBIO_CAPTURE_DATA {
  DWORD                PayloadSize;
  HRESULT              WinBioHresult;
  WINBIO_SENSOR_STATUS SensorStatus;
  WINBIO_REJECT_DETAIL RejectDetail;
  WINBIO_DATA          CaptureData;
} WINBIO_CAPTURE_DATA, *PWINBIO_CAPTURE_DATA;
````


## -struct-fields
<dl>

### -field PayloadSize

<dd>
<p> The total size of the payload.  This includes the fixed length structure and any variable data at the end.</p>
</dd>

### -field WinBioHresult

<dd>
<p>The status detail of the I/O operation.  This is where WINBIO error and information codes will be passed. The following table shows possible values for this member.</p>
<table>
<tr>
<th>Status value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>S_OK</p>
</td>
<td>
<p>The operation completed successfully.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_DATA_COLLECTION_IN_PROGRESS</p>
</td>
<td>
<p>There is already a data collection IOCTL pending.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_UNSUPPORTED_DATA_FORMAT</p>
</td>
<td>
<p>The format specified is not supported by this driver and device.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_UNSUPPORTED_DATA_TYPE</p>
</td>
<td>
<p>The type of data requested is not supported by this driver and device.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_INVALID_DEVICE_STATE</p>
</td>
<td>
<p>The device could not be put into biometric capture mode.  This could be because the device is in another non-data collection mode.</p>
</td>
</tr>
<tr>
<td>
<p>HRESULT_FROM_NT(STATUS_IO_DEVICE_ERROR)</p>
</td>
<td>
<p>The operation was not completed due to device error.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_DEVICE_BUSY</p>
</td>
<td>
<p>The device is in the middle of a vendor-specific operation.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_CANCELED</p>
</td>
<td>
<p>The operation was canceled either by the caller, or an IOCTL_BIOMETRIC_RESET request.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_E_UNSUPPORTED_PURPOSE</p>
</td>
<td>
<p>The capture purpose specified is not supported by the driver.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field SensorStatus

<dd>
<p>The WINBIO_SENSOR_STATUS status of the sensor after the capture has occurred. It specifies the operating status of the sensor.</p>
<p>WINBIO_SENSOR_STATUS can be queried at any time.  When WINBIO_SENSOR_STATUS is returned upon a capture I/O completion, it indicates whether a capture was successful. Possible values are shown in the following table.</p>
<table>
<tr>
<th>
              
                Sensor status code
              
            </th>
<th>
              
                Description
              
            </th>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_ACCEPT</p>
</td>
<td>
<p>The sensor just successfully completed a capture operation.  This should only be returned immediately after a capture operation.  The sensor will then return to WINBIO_SENSOR_READY or WINBIO_SENSOR_BUSY.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_REJECT</p>
</td>
<td>
<p>The sensor rejected the previous capture operation.  This should only be returned immediately following a capture operation.  The sensor will then return to WINBIO_SENSOR_READY or WINBIO_SENSOR_BUSY.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_READY</p>
</td>
<td>
<p>The sensor is ready to capture data.  If there is a pending data capture IOCTL, the sensor is ready to accept data.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_BUSY</p>
</td>
<td>
<p>The sensor is busy or in a state where it cannot capture data.  For example, the device could still be initializing after it has been turned on.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_NOT_CALIBRATED</p>
</td>
<td>
<p>The sensor must be calibrated before it is put into data collection mode.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_SENSOR_FAILURE</p>
</td>
<td>
<p>The sensor device failed.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field RejectDetail

<dd>
<p>If the sensor status was WINBIO_SENSOR_REJECT, this member contains a WINBIO_REJECT_DETAIL value. WINBIO_SENSOR_REJECT specifies the reason a biometric sampling operation failed.</p>
<div class="alert"><b>Important</b>    Values defined for Windows 7 are for fingerprint reject details only.</div>
<div> </div>
<p>Failure detail values for WINBIO_TYPE_FINGERPRINT include:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>#define WINBIO_FP_TOO_HIGH          ((WINBIO_REJECT_DETAIL)1)
#define WINBIO_FP_TOO_LOW           ((WINBIO_REJECT_DETAIL)2)
#define WINBIO_FP_TOO_LEFT          ((WINBIO_REJECT_DETAIL)3)
#define WINBIO_FP_TOO_RIGHT         ((WINBIO_REJECT_DETAIL)4)
#define WINBIO_FP_TOO_FAST          ((WINBIO_REJECT_DETAIL)5)
#define WINBIO_FP_TOO_SLOW          ((WINBIO_REJECT_DETAIL)6)
#define WINBIO_FP_POOR_QUALITY      ((WINBIO_REJECT_DETAIL)7)
#define WINBIO_FP_TOO_SKEWED        ((WINBIO_REJECT_DETAIL)8)
#define WINBIO_FP_TOO_SHORT         ((WINBIO_REJECT_DETAIL)9)
#define WINBIO_FP_MERGE_FAILURE     ((WINBIO_REJECT_DETAIL)10)</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field CaptureData

<dd>
<p>A structure of type <a href="..\winbio_ioctl\ns-winbio-ioctl--winbio-data.md">WINBIO_DATA</a> that contains data captured by the device, of the format specified. The <b>Data</b> array member of the WINBIO_DATA structure should contain a <a href="..\winbio_types\ns-winbio-types--winbio-bir.md">WINBIO_BIR</a> structure.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winbio_ioctl.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-capture-data.md">IOCTL_BIOMETRIC_CAPTURE_DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_CAPTURE_DATA structure%20 RELEASE:%20(11/13/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
