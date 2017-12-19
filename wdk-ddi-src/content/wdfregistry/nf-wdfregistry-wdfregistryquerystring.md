---
UID: NF.wdfregistry.WdfRegistryQueryString
title: WdfRegistryQueryString function
author: windows-driver-content
description: The WdfRegistryQueryString method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object.
old-location: wdf\wdfregistryquerystring.htm
old-project: wdf
ms.assetid: 2c1242ea-5d77-464e-9203-ef2236ea4619
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.lib: Wdf01000.sys (KMDF); WUDFx02000.dll (UMDF)
req.dll: 
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# WdfRegistryQueryString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRegistryQueryString</b> method retrieves the string data that is currently assigned to a specified registry string value and assigns the string to a specified framework string object.



## -syntax

````
NTSTATUS WdfRegistryQueryString(
  _In_ WDFKEY           Key,
  _In_ PCUNICODE_STRING ValueName,
  _In_ WDFSTRING        String
);
````


## -parameters

### -param Key [in]

A handle to a registry-key object that represents an opened registry key.


### -param ValueName [in]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains a name for the registry value. 


### -param String [in]

A handle to a framework string object. The framework will assign the registry value's string data to this object.


## -returns
<b>WdfRegistryQueryString</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>
<a href="wdf.wdfregistryquerystring">WdfRegistryQueryString</a> was not called at IRQL = PASSIVE_LEVEL. 
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was specified.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>There was insufficient memory to complete the operation.
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The driver did not open the registry key with KEY_QUERY_VALUE, KEY_READ, or KEY_ALL_ACCESS access.
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>The data type of the registry value that the <i>ValueName</i> parameter specified was not REG_SZ.
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>The registry value was not available.
<dl>
<dt><b>STATUS_RESOURCE_DATA_NOT_FOUND</b></dt>
</dl>The registry value exists under the specified key, but is empty. 

 

For a list of other return values that the <b>WdfRegistryQueryString</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
To obtain a string from a string object, your driver can call <a href="wdf.wdfstringgetunicodestring">WdfStringGetUnicodeString</a>. 

For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.

The following code example creates a string object, retrieves string data from a registry key, and obtains the string data from the string object.


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
<dt>Wdfregistry.h (include Wdf.h)</dt>
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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.kmdf_drivercreate">DriverCreate</a>, <a href="devtest.kmdf_kmdfirql">KmdfIrql</a>, <a href="devtest.kmdf_kmdfirql2">KmdfIrql2</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="wdf.wdfregistryquerymemory">WdfRegistryQueryMemory</a>
</dt>
<dt>
<a href="wdf.wdfregistryquerymultistring">WdfRegistryQueryMultiString</a>
</dt>
<dt>
<a href="wdf.wdfregistryqueryunicodestring">WdfRegistryQueryUnicodeString</a>
</dt>
<dt>
<a href="wdf.wdfregistryqueryulong">WdfRegistryQueryULong</a>
</dt>
<dt>
<a href="wdf.wdfregistryqueryvalue">WdfRegistryQueryValue</a>
</dt>
<dt>
<a href="wdf.wdfstringcreate">WdfStringCreate</a>
</dt>
<dt>
<a href="wdf.wdfstringgetunicodestring">WdfStringGetUnicodeString</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRegistryQueryString method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

