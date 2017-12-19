---
UID: NF.wdfregistry.WdfRegistryQueryMultiString
title: WdfRegistryQueryMultiString function
author: windows-driver-content
description: The WdfRegistryQueryMultiString method retrieves the strings that are currently assigned to a specified multi-string registry value, creates a framework string object for each string, and adds each string object to a specified object collection.
old-location: wdf\wdfregistryquerymultistring.htm
old-project: wdf
ms.assetid: 9ce754b4-a783-4b2e-978d-e38a30c5d3dd
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRegistryQueryMultiString
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
req.alt-api: WdfRegistryQueryMultiString
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

# WdfRegistryQueryMultiString function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRegistryQueryMultiString</b> method retrieves the strings that are currently assigned to a specified multi-string registry value, creates a framework string object for each string, and adds each string object to a specified <a href="wdf.framework_object_collections">object collection</a>.



## -syntax

````
NTSTATUS WdfRegistryQueryMultiString(
  _In_     WDFKEY                 Key,
  _In_     PCUNICODE_STRING       ValueName,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES StringsAttributes,
  _In_     WDFCOLLECTION          Collection
);
````


## -parameters

### -param Key [in]

A handle to a registry-key object that represents an opened registry key.


### -param ValueName [in]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains a value name. 


### -param StringsAttributes [in, optional]

A pointer to a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains object attributes for each new string object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES. 


### -param Collection [in]

A handle to a driver-supplied framework collection object.


## -returns
<b>WdfRegistryQueryMultiString</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>
<a href="wdf.wdfregistryquerymultistring">WdfRegistryQueryMultiString</a> was not called at IRQL = PASSIVE_LEVEL. 
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was specified.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A string object could not be allocated.
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The driver did not open the registry key with KEY_QUERY_VALUE, KEY_READ, or KEY_ALL_ACCESS access.
<dl>
<dt><b>STATUS_OBJECT_TYPE_MISMATCH</b></dt>
</dl>The data type of the registry value that the <i>ValueName</i> parameter specified was not REG_MULTI_SZ.
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>The registry value was not available.
<dl>
<dt><b>STATUS_RESOURCE_DATA_NOT_FOUND</b></dt>
</dl>The registry value exists under the specified key, but is empty. 

 

For a list of other return values that the <b>WdfRegistryQueryMultiString</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A bug check occurs if the driver supplies an invalid object handle.




## -remarks
Before your driver calls <b>WdfRegistryQueryMultiString</b>, it must call <a href="wdf.wdfcollectioncreate">WdfCollectionCreate</a> to create a collection object. 

After <b>WdfRegistryQueryMultiString</b> returns, the driver can call <a href="wdf.wdfcollectiongetcount">WdfCollectionGetCount</a> to obtain the number of retrieved strings and <a href="wdf.wdfcollectiongetitem">WdfCollectionGetItem</a> to obtain string objects from the collection.

If the collection contains objects before the driver calls the <b>WdfRegistryQueryMultiString</b> method, the method does not remove those objects or change their index values. The new objects are appended to the end of the collection.

To obtain a string from a string object, the driver can call <a href="wdf.wdfstringgetunicodestring">WdfStringGetUnicodeString</a>. 

For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.

The following code example creates a collection object, initializes a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure so that the collection object will be the parent of all of the string objects that the framework creates for the collection, and retrieves the strings from a multi-string registry value. Finally, the example obtains the number of string objects that the framework added to the collection.


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
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdfcollectioncreate">WdfCollectionCreate</a>
</dt>
<dt>
<a href="wdf.wdfcollectiongetcount">WdfCollectionGetCount</a>
</dt>
<dt>
<a href="wdf.wdfcollectiongetitem">WdfCollectionGetItem</a>
</dt>
<dt>
<a href="wdf.wdfregistryquerymemory">WdfRegistryQueryMemory</a>
</dt>
<dt>
<a href="wdf.wdfregistryquerystring">WdfRegistryQueryString</a>
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
<a href="wdf.wdfstringgetunicodestring">WdfStringGetUnicodeString</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRegistryQueryMultiString method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

