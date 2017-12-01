---
UID: NF.sensorsclassextension.ISensorDriver.OnSetProperties
title: ISensorDriver::OnSetProperties
author: windows-driver-content
description: The ISensorDriver::OnSetProperties method specifies values for the specified list of properties.
old-location: sensors\isensordriver_onsetproperties.htm
old-project: sensors
ms.assetid: 7c3cca5b-1d08-42dc-8dc4-42eb1160b8bb
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ISensorDriver, OnSetProperties, ISensorDriver::OnSetProperties
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sensorsclassextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 7,Available in Windows 7.
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ISensorDriver.OnSetProperties
req.alt-loc: SensorsClassExtension.lib,SensorsClassExtension.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: SensorsClassExtension.lib
req.dll: 
req.irql: <= PASSIVE_LEVEL
req.iface: ISensorDriver
req.product: Windows 10 or later.
---

# ISensorDriver::OnSetProperties method



## -description
<p>The <b>ISensorDriver::OnSetProperties</b> method specifies values for the specified list of properties.</p>


## -syntax

````
HRESULT OnSetProperties(
  [in]  IWDFFile              *pClientFile,
  [in]  LPWSTR                pwszSensorID,
  [in]  IPortableDeviceValues *pPropertiesToSet,
  [out] IPortableDeviceValues **ppResults
);
````


## -parameters
<dl>

### -param <i>pClientFile</i> [in]

<dd>
<p>Pointer to an <a href="..\wudfddi\nn-wudfddi-iwdffile.md">IWDFFile</a> interface that represents the file object for the application specifying property values.</p>
</dd>

### -param <i>pwszSensorID</i> [in]

<dd>
<p><b>LPWSTR</b> that contains the ID for the sensor for which the client application is specifying property values.</p>
</dd>

### -param <i>pPropertiesToSet</i> [in]

<dd>
<p>Pointer to an <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> interface that contains the list of properties to set and their values.</p>
</dd>

### -param <i>ppResults</i> [out]

<dd>
<p>Address of an <a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> pointer that receives the list of properties that have been set successfully and their new values. If a property was not set, the new value contains an HRESULT error code.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, this method returns S_OK. Otherwise, this method returns one of the error codes that are defined in Winerror.h.</p>

## -remarks
<p>Properties describe the sensor device, as opposed to data fields, which contain sensor-generated data.  Platform-defined properties are defined in sensors.h.</p>

<p>The list of properties provided through <i>pPropertiesToSet</i> is typically  a subset of the list you returned through <a href="sensors.isensordriver_ongetsupportedproperties">ISensorDriver::OnGetSupportedProperties</a>. However, the sensor class extension does not enforce this condition on client applications.</p>

<p>The sensor class extension is responsible for freeing any <b>PROPVARIANT</b> structures returned by this method.</p>

<p><a href="http://go.microsoft.com/fwlink/p/?linkid=131486">IPortableDeviceValues</a> is documented in Windows Portable Devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Sensorsclassextension.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>SensorsClassExtension.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="sensors.isensordriver_ongetproperties">ISensorDriver::OnGetProperties</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [sensors\sensors]:%20ISensorDriver::OnSetProperties method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
