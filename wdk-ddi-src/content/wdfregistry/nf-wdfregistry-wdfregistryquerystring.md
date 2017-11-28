---
UID: NF.wdfregistry.WdfRegistryQueryString
title: WdfRegistryQueryString
author: windows-driver-content
description: The WdfRegistryQueryString method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object.
old-location: wdf\wdfregistryquerystring.htm
old-project: wdf
ms.assetid: 2c1242ea-5d77-464e-9203-ef2236ea4619
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WdfRegistryQueryString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfregistry.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRegistryQueryString
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll,WUDFx02000.dll,WUDFx02000.dll.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (KMDF); 
WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WdfRegistryQueryString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRegistryQueryString</b> method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object.</p>


## -syntax

````
NTSTATUS WdfRegistryQueryString(
  _In_ WDFKEY           Key,
  _In_ PCUNICODE_STRING ValueName,
  _In_ WDFSTRING        String
);
````


## -parameters
<dl>

### -param <i>Key</i> [in]

<dd>
<p>A handle to a registry-key object that represents an opened registry key.</p>
</dd>

### -param <i>ValueName</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains a name for the registry value. </p>
</dd>

### -param <i>String</i> [in]

<dd>
<p>A handle to a framework string object. The framework will assign the registry value's string data to this object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRegistryQueryString</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549923">WdfRegistryQueryString</a> was not called at IRQL = PASSIVE_LEVEL. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was specified.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>There was insufficient memory to complete the operation.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The driver did not open the registry key with KEY_QUERY_VALUE, KEY_READ, or KEY_ALL_ACCESS access.</p><dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl><p>The data type of the registry value that the <i>ValueName</i> parameter specified was not REG_SZ.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The registry value was not available.</p><dl>
<dt><b>STATUS_RESOURCE_DATA_NOT_FOUND</b></dt>
</dl><p>The registry value exists under the specified key, but is empty. </p>

<p> </p>

<p>For a list of other return values that the <b>WdfRegistryQueryString</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A bug check occurs if the driver supplies an invalid object handle.

</p>

## -remarks
<p>To obtain a string from a string object, your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550049">WdfStringGetUnicodeString</a>. </p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example creates a string object, retrieves string data from a registry key, and obtains the string data from the string object.</p>

<p>To obtain a string from a string object, your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff550049">WdfStringGetUnicodeString</a>. </p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example creates a string object, retrieves string data from a registry key, and obtains the string data from the string object.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfregistry.h (include Wdf.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549920">WdfRegistryQueryMemory</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549921">WdfRegistryQueryMultiString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549927">WdfRegistryQueryUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549925">WdfRegistryQueryULong</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549928">WdfRegistryQueryValue</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550046">WdfStringCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550049">WdfStringGetUnicodeString</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRegistryQueryString method%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
