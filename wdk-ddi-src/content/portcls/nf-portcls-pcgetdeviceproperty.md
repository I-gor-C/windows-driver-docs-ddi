---
UID: NF.portcls.PcGetDeviceProperty
title: PcGetDeviceProperty
author: windows-driver-content
description: The PcGetDeviceProperty function returns the requested device property from the registry.
old-location: audio\pcgetdeviceproperty.htm
old-project: audio
ms.assetid: 75d66965-ab97-4f67-b62f-e7fedbf524a6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcGetDeviceProperty
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: The PortCls system driver implements the PcGetDeviceProperty function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PcGetDeviceProperty
req.alt-loc: Portcls.lib,Portcls.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# PcGetDeviceProperty function



## -description
<p>The <b>PcGetDeviceProperty</b> function returns the requested device property from the registry.</p>


## -syntax

````
NTSTATUS PcGetDeviceProperty(
  _In_  PVOID                    DeviceObject,
  _In_  DEVICE_REGISTRY_PROPERTY DeviceProperty,
  _In_  ULONG                    BufferLength,
  _Out_ PVOID                    PropertyBuffer,
  _Out_ PULONG                   ResultLength
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>Pointer to the device object for the device. This parameter points to a <a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a> system structure but is cast to type PVOID.</p>
</dd>

### -param DeviceProperty [in]

<dd>
<p>Specifies the Plug and Play device property that is requested. For a list of property specifier values, see the following Remarks section.</p>
</dd>

### -param BufferLength [in]

<dd>
<p>Specifies the length in bytes of the buffer that is to receive the requested property data.</p>
</dd>

### -param PropertyBuffer [out]

<dd>
<p>Pointer to a caller-allocated buffer into which the method is to write the requested property data. The buffer must be large enough to contain the number of bytes specified in <i>BufferLength</i>.</p>
</dd>

### -param ResultLength [out]

<dd>
<p>Pointer to a caller-allocated variable into which the method outputs a count specifying the number of bytes actually written to the buffer. If the buffer size specified in <i>BufferLength</i> is too small to hold the property data, the method instead outputs the number of bytes required for the property data and returns STATUS_BUFFER_TOO_SMALL.</p>
</dd>
</dl>

## -returns
<p><b>PcGetDeviceProperty</b> returns STATUS_SUCCESS if the call was successful. Otherwise, it returns an appropriate error code. The routine returns STATUS_BUFFER_TOO_SMALL if the buffer size specified in <i>BufferLength</i> was not large enough to contain the requested property data.</p>

## -remarks
<p>Set the <b>DeviceProperty</b> parameter to one of the following DEVICE_REGISTRY_PROPERTY enumeration values from header file wdm.h:</p>

<p><b>DevicePropertyAddress</b></p>

<p><b>DevicePropertyBootConfiguration</b></p>

<p><b>DevicePropertyBootConfigurationTranslated</b></p>

<p><b>DevicePropertyBusNumber</b></p>

<p><b>DevicePropertyBusTypeGuid</b></p>

<p><b>DevicePropertyClassGuid</b></p>

<p><b>DevicePropertyClassName</b></p>

<p><b>DevicePropertyCompatibleIDs</b></p>

<p><b>DevicePropertyDetachability</b></p>

<p><b>DevicePropertyDeviceDescription</b></p>

<p><b>DevicePropertyDriverKeyName</b></p>

<p><b>DevicePropertyEnumeratorName</b></p>

<p><b>DevicePropertyFriendlyName</b></p>

<p><b>DevicePropertyHardwareID</b></p>

<p><b>DevicePropertyInstallState</b></p>

<p><b>DevicePropertyLegacyBusType</b></p>

<p><b>DevicePropertyLocationInformation</b></p>

<p><b>DevicePropertyManufacturer</b></p>

<p><b>DevicePropertyPhysicalDeviceObjectName</b></p>

<p><b>DevicePropertyUINumber</b></p>

<p>For a description of the preceding DeviceProperty<i>Xxx</i> values, see <a href="..\wdm\nf-wdm-iogetdeviceproperty.md">IoGetDeviceProperty</a>.</p>

<p>Two calls to <b>PcGetDeviceProperty</b> might be necessary to determine the required <i>BufferLength</i>. In the first call, <i>BufferLength</i> can either be zero or a best-guess estimate of the required buffer size. If the return status is STATUS_BUFFER_TOO_SMALL, this means that the caller should allocate a buffer of the size that was output through <i>ResultLength</i> and call <b>PcGetDeviceProperty</b> again. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>The PortCls system driver implements the PcGetDeviceProperty function in Microsoft Windows 98/Me and in Windows 2000 and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.h (include Portcls.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Portcls.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--device-object.md">DEVICE_OBJECT</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iogetdeviceproperty.md">IoGetDeviceProperty</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20PcGetDeviceProperty function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
