---
UID: NF.wdfwmi.WdfWmiProviderCreate
title: WdfWmiProviderCreate
author: windows-driver-content
description: The WdfWmiProviderCreate method creates a WMI provider object that represents a WMI data block.
old-location: wdf\wdfwmiprovidercreate.htm
old-project: wdf
ms.assetid: 07aed86f-870e-431b-b1bb-403395c35946
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfWmiProviderCreate
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWmiProviderCreate
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfWmiProviderCreate function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WdfWmiProviderCreate</b> method creates a WMI provider object that represents a WMI data block.</p>


## -syntax

````
NTSTATUS WdfWmiProviderCreate(
  _In_     WDFDEVICE                Device,
  _In_     PWDF_WMI_PROVIDER_CONFIG WmiProviderConfig,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES   ProviderAttributes,
  _Out_    WDFWMIPROVIDER           *WmiProvider
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object that will be the new provider object's parent object. The device object cannot be a <a href="wdf.using_control_device_objects">control device object</a>.</p>
</dd>

### -param <i>WmiProviderConfig</i> [in]

<dd>
<p>A pointer to a caller-initialized <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure that contains configuration information about the WMI data block.</p>
</dd>

### -param <i>ProviderAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied object attributes for the new WMI provider object. (The structure's <b>ParentObject</b> member must be <b>NULL</b>.) This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>WmiProvider</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new WMI provider object.</p>
</dd>
</dl>

## -returns
<p><b>WdfWmiProviderCreate</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was detected.</p><dl>
<dt><b>STATUS_INFO_LENGTH_MISMATCH</b></dt>
</dl><p>The size of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure that the <i>WmiProviderConfig</i> parameter pointed to was incorrect.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory to complete the operation.</p><dl>
<dt><b>STATUS_OBJECT_NAME_EXISTS</b></dt>
</dl><p>The driver has already called <a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a> for the specified device and WMI data block.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfWmiProviderCreate</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>Your driver must call <b>WdfWmiProviderCreate</b> to create a WMI provider object if the driver will create multiple instances of the provider. If the driver will create only one instance of the provider, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a> without first calling <b>WdfWmiProviderCreate</b>. </p>

<p>A driver can call <b>WdfWmiProviderCreate</b> at any time, but drivers typically call <b>WdfWmiProviderCreate</b> from within their <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback functions. </p>

<p>The parent of each WMI provider object is the device's framework device object. The driver cannot change this parent, and the <b>ParentObject</b> member or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure must be <b>NULL</b>.</p>

<p>After a driver calls <b>WdfWmiProviderCreate</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551195">WdfWmiProviderGetDevice</a> to retrieve a handle to the provider object's parent device object.</p>

<p>After a driver creates a WMI provider object, the driver cannot delete the object. The framework deletes a device's WMI provider objects when it deletes the framework device object that represents the device. WMI provider objects use minimal system resources.</p>

<p>For more information about the <b>WdfWmiProviderCreate</b> method, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure and calls <b>WdfWmiProviderCreate</b>.</p>

<p>Your driver must call <b>WdfWmiProviderCreate</b> to create a WMI provider object if the driver will create multiple instances of the provider. If the driver will create only one instance of the provider, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a> without first calling <b>WdfWmiProviderCreate</b>. </p>

<p>A driver can call <b>WdfWmiProviderCreate</b> at any time, but drivers typically call <b>WdfWmiProviderCreate</b> from within their <a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a> callback functions. </p>

<p>The parent of each WMI provider object is the device's framework device object. The driver cannot change this parent, and the <b>ParentObject</b> member or the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure must be <b>NULL</b>.</p>

<p>After a driver calls <b>WdfWmiProviderCreate</b>, the driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551195">WdfWmiProviderGetDevice</a> to retrieve a handle to the provider object's parent device object.</p>

<p>After a driver creates a WMI provider object, the driver cannot delete the object. The framework deletes a device's WMI provider objects when it deletes the framework device object that represents the device. WMI provider objects use minimal system resources.</p>

<p>For more information about the <b>WdfWmiProviderCreate</b> method, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.</p>

<p>The following code example initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure and calls <b>WdfWmiProviderCreate</b>.</p>

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
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfwmi.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544957">DriverCreate</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff548167">KmdfIrql</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/hh975091">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdfdriver\nc-wdfdriver-evt-wdf-driver-device-add.md">EvtDriverDeviceAdd</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551195">WdfWmiProviderGetDevice</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWmiProviderCreate method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
