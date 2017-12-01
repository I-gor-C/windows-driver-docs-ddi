---
UID: NS.winbio_ioctl._WINBIO_SENSOR_ATTRIBUTES
title: WINBIO_SENSOR_ATTRIBUTES
author: windows-driver-content
description: The IOCTL_BIOMETRIC_GET_ATTRIBUTES structure returns the WINBIO_SENSOR_ATTRIBUTES structure as output.
old-location: biometric\winbio_sensor_attributes.htm
old-project: biometric
ms.assetid: edfd5b49-f658-46c7-a3f3-221afb35abb7
ms.author: windowsdriverdev
ms.date: 11/13/2017
ms.keywords: WINBIO_SENSOR_ATTRIBUTES, WINBIO_SENSOR_ATTRIBUTES, *PWINBIO_SENSOR_ATTRIBUTES
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
req.alt-api: WINBIO_SENSOR_ATTRIBUTES
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

# WINBIO_SENSOR_ATTRIBUTES structure



## -description
<p>The <a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-get-attributes.md">IOCTL_BIOMETRIC_GET_ATTRIBUTES</a> structure returns the WINBIO_SENSOR_ATTRIBUTES structure as output.</p>


## -syntax

````
typedef struct _WINBIO_SENSOR_ATTRIBUTES {
  DWORD                           PayloadSize;
  HRESULT                         WinBioHresult;
  WINBIO_VERSION                  WinBioVersion;
  WINBIO_BIOMETRIC_TYPE           SensorType;
  WINBIO_BIOMETRIC_SENSOR_SUBTYPE SensorSubType;
  WINBIO_CAPABILITIES             Capabilities;
  WINBIO_STRING                   ManufacturerName;
  WINBIO_STRING                   ModelName;
  WINBIO_STRING                   SerialNumber;
  WINBIO_VERSION                  FirmwareVersion;
  DWORD                           SupportedFormatEntries;
  WINBIO_REGISTERED_FORMAT        SupportedFormat[1];
} WINBIO_SENSOR_ATTRIBUTES, *PWINBIO_SENSOR_ATTRIBUTES;
````


## -struct-fields
<dl>

### -field <b>PayloadSize</b>

<dd>
<p>A DWORD value that indicates the total size of the payload, including the fixed length structure and any variable data at the end.</p>
</dd>

### -field <b>WinBioHresult</b>

<dd>
<p>An HRESULT value that indicates containing status detail of the I/O operation.   The following table includes possible values.</p>
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
<p>HRESULT_FROM_NT(STATUS_IO_DEVICE_ERROR)</p>
</td>
<td>
<p>The driver could not gather the necessary information from the device.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>WinBioVersion</b>

<dd>
<p>A structure of type <a href="..\winbio_types\ns-winbio-types--winbio-version.md">WINBIO_VERSION</a> that contains a WinBio WBDI version that is supported by the driver. To be compatible with the WinBio service, <b>WinBioVersion</b> must contain the same major version as the current major version of the WinBio service, in addition to a minor version that is less than or equal to the current minor version of the WinBio service. </p>
</dd>

### -field <b>SensorType</b>

<dd>
<p>A DWORD bitmask of type WINBIO_BIOMETRIC_TYPE that contains biometric data that is collected by the sensor. In Windows 7, only WINBIO_TYPE_FINGERPRINT is supported.</p>
</dd>

### -field <b>SensorSubType</b>

<dd>
<p>A WINBIO_BIOMETRIC_SENSOR_SUBTYPE subtype that contains additional information about the sensor.  For example, this member could specify whether the sensor requires the user to simply touch the sensor or swipe a finger over the sensor.</p>
<p>WINBIO_BIOMETRIC_SENSOR_SUBTYPE can contain the values in the following table.</p>
<table>
<tr>
<th>
              
                Biometric subtype value
              
            </th>
<th>
              
                Description
              
            </th>
</tr>
<tr>
<td>
<p>WINBIO_FP_SENSOR_SUBTYPE_SWIPE</p>
</td>
<td>
<p>The device requires the user to swipe their fingertip over the sensor.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_FP_SENSOR_SUBTYPE_TOUCH</p>
</td>
<td>
<p>The device requires the user to place their entire fingerprint on a sensor pad.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>A WINBIO_CAPABILITIES subtype, which indicates which capabilities are supported by the device. </p>
<p>WINBIO_CAPABILITIES can contain the values in the following table.</p>
<table>
<tr>
<th>
       
        Biometric capability value
       
      </th>
<th>
       
        Description
       
      </th>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_SENSOR </p>
</td>
<td>
<p>The device can collect biometric data.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_MATCHING</p>
</td>
<td>
<p>The device can perform match operations.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_STORAGE</p>
</td>
<td>
<p>The device can store biometric templates.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_SECURE_STORAGE</p>
</td>
<td>
<p>The device can store secure data that is associated with a template.  The secure data is only released with a positive match.  The device must support at least the SHA-1 algorithm for secure hash computation to be used to store templates in the system pool.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_PROCESSING</p>
</td>
<td>
<p>The device can process samples and turn them into biometric templates.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_ENCRYPTION</p>
</td>
<td>
<p>The device supports encryption of samples and templates.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_SIGNING</p>
</td>
<td>
<p>The device can sign captured data.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_NAVIGATION</p>
</td>
<td>
<p>The device can be used as a navigation device.  Some devices and drivers can capture data in a format that can be translated by a user-mode application into navigation events, much like a mouse.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_INDICATOR</p>
</td>
<td>
<p>The device has an indicator that can be turned on or off.</p>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_VIRTUAL_SENSOR</p>
</td>
<td>
<p>The sensor adapter manages its own connection to the biometric hardware.</p>
<div class="alert"><b>Note</b>  This constant applies only for Windows 10 and later.</div>
<div> </div>
</td>
</tr>
<tr>
<td>
<p>WINBIO_CAPABILITY_SECURE_SENSOR</p>
</td>
<td>
<p>The device supports security methods available in the WinBio engine adapter interface version 4.0  or later.</p>
<div class="alert"><b>Note</b>  This constant applies only for Windows 10 and later.</div>
<div> </div>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>ManufacturerName</b>

<dd>
<p> A structure of type WINBIO_STRING that contains the name of the device manufacturer.</p>
</dd>

### -field <b>ModelName</b>

<dd>
<p> A structure of type WINBIO_STRING that contains the name of the device model.</p>
</dd>

### -field <b>SerialNumber</b>

<dd>
<p>A structure of type WINBIO_STRING that contains the serial number of the device, if one exists.</p>
</dd>

### -field <b>FirmwareVersion</b>

<dd>
<p> A structure of type <a href="..\winbio_types\ns-winbio-types--winbio-version.md">WINBIO_VERSION</a> that contains the version of the firmware that is loaded on the device.</p>
</dd>

### -field <b>SupportedFormatEntries</b>

<dd>
<p> The number of formats that are supported by the driver and device.  There must be at least one, which is the Windows standard format.</p>
</dd>

### -field <b>SupportedFormat</b>

<dd>
<p>A structure of type <a href="..\winbio_types\ns-winbio-types--winbio-registered-format.md">WINBIO_REGISTERED_FORMAT</a> that contains a list of the formats supported by the driver and device. </p>
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
<a href="..\winbio_ioctl\ni-winbio-ioctl-ioctl-biometric-get-attributes.md">IOCTL_BIOMETRIC_GET_ATTRIBUTES</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [biometric\biometric]:%20WINBIO_SENSOR_ATTRIBUTES structure%20 RELEASE:%20(11/13/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
