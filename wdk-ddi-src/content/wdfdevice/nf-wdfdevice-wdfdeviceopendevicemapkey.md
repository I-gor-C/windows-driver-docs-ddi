---
UID: NF.wdfdevice.WdfDeviceOpenDevicemapKey
title: WdfDeviceOpenDevicemapKey
author: windows-driver-content
description: The WdfDeviceOpenDevicemapKey method opens the DEVICEMAP key and creates a framework registry-key object that represents the registry key.
old-location: wdf\wdfdeviceopendevicemapkey.htm
old-project: wdf
ms.assetid: EAFC6B53-98E9-46A4-9D45-56B0A32993B1
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WdfDeviceOpenDevicemapKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.15
req.umdf-ver: 2.15
req.alt-api: WdfDeviceOpenDevicemapKey
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfDeviceOpenDevicemapKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDeviceOpenDevicemapKey</b> method opens the <b>DEVICEMAP</b> key and creates a framework registry-key object that represents the registry key.</p>


## -syntax

````
NTSTATUS WdfDeviceOpenDevicemapKey(
  _In_     WDFDEVICE              Device,
  _In_     PCUNICODE_STRING       KeyName,
  _In_     ACCESS_MASK            DesiredAccess,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES KeyAttributes,
  _Out_    WDFKEY                 *Key
);
````


## -parameters
<dl>

### -param <i>Device</i> [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param <i>KeyName</i> [in]

<dd>
<p>A pointer to a <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that specifies the name of the subkey to open under <b>DEVICEMAP</b>.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies access rights that the driver is requesting for the specified registry key.</p>
<p>A KMDF driver typically requests <b>KEY_READ</b>, <b>KEY_WRITE</b>, or <b>KEY_READ | KEY_WRITE</b>.</p>
<p>A UMDF driver typically requests <b>KEY_READ</b> or <b>KEY_SET_VALUE</b>.</p>
</dd>

### -param <i>KeyAttributes</i> [in, optional]

<dd>
<p>A pointer to a <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied attributes for the new registry-key object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Key</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new registry-key object.  The </p>
</dd>
</dl>

## -returns
<p><b>WdfDeviceOpenDevicemapKey</b>  returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceopendevicemapkey.md">WdfDeviceOpenDevicemapKey</a> was not called at IRQL = PASSIVE_LEVEL. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was specified. For UMDF, this return value can indicate insufficient access rights.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A registry-key object could not be allocated.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The specified registry key does not exist.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfDeviceOpenDevicemapKey</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>The method might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.</p>

## -remarks
<p>The registry contains a <b>HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP</b> key that some drivers for older technologies, such as serial and parallel ports, use. If your driver supports a technology that uses the <b>DEVICEMAP</b> key, the driver can access subkeys and values under the key by calling <b>WdfDeviceOpenDevicemapKey</b>.</p>

<p><b>WdfDeviceOpenDevicemapKey</b> returns a volatile <i>Key</i>. This means that the information is not preserved when the corresponding registry hive is unloaded.</p>

<p>When the driver has finished using the registry key that it opened with <b>WdfDeviceOpenDevicemapKey</b>, the driver must call <a href="..\wdfregistry\nf-wdfregistry-wdfregistryclose.md">WdfRegistryClose</a>.</p>

<p>For more information about the registry, hardware and software keys, and registry objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

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
<p>1.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.15</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
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
<a href="..\wdfdevice\nf-wdfdevice-wdfdeviceopenregistrykey.md">WdfDeviceOpenRegistryKey</a>
</dt>
<dt>
<a href="..\wdffdo\nf-wdffdo-wdffdoinitopenregistrykey.md">WdfFdoInitOpenRegistryKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDeviceOpenDevicemapKey method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
