---
UID: NF.wdfdevice.WdfDeviceInitSetFileObjectConfig
title: WdfDeviceInitSetFileObjectConfig function
author: windows-driver-content
description: The WdfDeviceInitSetFileObjectConfig method registers event callback functions and sets configuration information for the driver's framework file objects.
old-location: wdf\wdfdeviceinitsetfileobjectconfig.htm
old-project: wdf
ms.assetid: e309a741-1f61-4668-8176-baf0c8e26dff
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDeviceInitSetFileObjectConfig
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDeviceInitSetFileObjectConfig
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: ChildDeviceInitAPI, ControlDeviceInitAPI, DeviceInitAPI, DriverCreate, FileObjectConfigured, KmdfIrql, KmdfIrql2, PdoDeviceInitAPI
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfDeviceInitSetFileObjectConfig function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDeviceInitSetFileObjectConfig</b> method registers event callback functions and sets configuration information for the driver's framework file objects.



## -syntax

````
VOID WdfDeviceInitSetFileObjectConfig(
  _In_     PWDFDEVICE_INIT        DeviceInit,
  _In_     PWDF_FILEOBJECT_CONFIG FileObjectConfig,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES FileObjectAttributes
);
````


## -parameters

### -param DeviceInit [in]

A pointer to a <a href="wdf.wdfdevice_init">WDFDEVICE_INIT</a> structure.


### -param FileObjectConfig [in]

A pointer to a caller-allocated <a href="wdf.wdf_fileobject_config">WDF_FILEOBJECT_CONFIG</a> structure.


### -param FileObjectAttributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied object attributes for the driver's framework file objects. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


## -returns
None


## -remarks
If a driver calls <b>WdfDeviceInitSetFileObjectConfig</b>, it must do so before it calls <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>.

By default, each framework file object inherits its synchronization scope and execution level from its parent device object. If the parent device object's synchronization scope and execution level are not <b>WdfSynchronizationScopeNone</b> and <b>WdfExecutionLevelPassive</b>, the driver must set the <b>WdfSynchronizationScopeNone</b> and <b>WdfExecutionLevelPassive</b> values in the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that the <i>FileObjectAttributes </i>parameter specifies. Otherwise, <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a> will return an error status code. For more information about synchronization scope and execution level, see <a href="wdf.using_automatic_synchronization">Using Automatic Synchronization</a>.

For more information about calling <a href="wdf.wdfdevicecreate">WdfDeviceCreate</a>, see <a href="wdf.creating_a_framework_device_object">Creating a Framework Device Object</a>.

For more information about framework file objects, see <a href="wdf.framework_file_objects">Framework File Objects</a>


The following code example initializes a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure and a <a href="wdf.wdf_fileobject_config">WDF_FILEOBJECT_CONFIG</a> structure and then calls <b>WdfDeviceInitSetFileObjectConfig</b>.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (KMDF); </dt>
<dt>WUDFx02000.dll (UMDF)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_childdeviceinitapi">ChildDeviceInitAPI</a>, <a href="devtest.kmdf_controldeviceinitapi">ControlDeviceInitAPI</a>, <a href="devtest.kmdf_deviceinitapi">DeviceInitAPI</a>, <a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_fileobjectconfigured">FileObjectConfigured</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>, <a href="devtest.kmdf_pdodeviceinitapi">PdoDeviceInitAPI</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.wdf_object_attributes_init">WDF_OBJECT_ATTRIBUTES_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_fileobject_config_init">WDF_FILEOBJECT_CONFIG_INIT</a>
</dt>
<dt>
<a href="wdf.wdffdoinitseteventcallbacks">WdfFdoInitSetEventCallbacks</a>
</dt>
<dt>
<a href="wdf.wdfpdoinitseteventcallbacks">WdfPdoInitSetEventCallbacks</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceInitSetFileObjectConfig method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

