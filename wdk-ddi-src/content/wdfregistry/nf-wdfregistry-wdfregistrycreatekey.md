---
UID: NF.wdfregistry.WdfRegistryCreateKey
title: WdfRegistryCreateKey function
author: windows-driver-content
description: The WdfRegistryCreateKey method creates and opens a specified registry key, or just opens the key if it already exists, and creates a framework registry-key object that represents the registry key.
old-location: wdf\wdfregistrycreatekey.htm
old-project: wdf
ms.assetid: acaf7024-b73a-4fe5-89e2-83e28cf2fdd1
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfRegistryCreateKey
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
req.alt-api: WdfRegistryCreateKey
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

# WdfRegistryCreateKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfRegistryCreateKey</b> method creates and opens a specified registry key, or just opens the key if it already exists, and creates a framework registry-key object that represents the registry key.



## -syntax

````
NTSTATUS WdfRegistryCreateKey(
  _In_opt_  WDFKEY                 ParentKey,
  _In_      PCUNICODE_STRING       KeyName,
  _In_      ACCESS_MASK            DesiredAccess,
  _In_      ULONG                  CreateOptions,
  _Out_opt_ PULONG                 CreateDisposition,
  _In_opt_  PWDF_OBJECT_ATTRIBUTES KeyAttributes,
  _Out_     WDFKEY                 *Key
);
````


## -parameters

### -param ParentKey [in, optional]

A handle to a framework registry-key object. This object represents a parent registry key that the driver has opened. This parameter is optional and can be <b>NULL</b>. If the parameter is not <b>NULL</b>, the key that <i>KeyName</i> specifies must reside under this parent key in the registry. For more information about this parent key, see the Remarks section.


### -param KeyName [in]

A pointer to a <a href="kernel.unicode_string">UNICODE_STRING</a> structure that contains the name of the key to be opened. The key name can include path information. If <i>ParentKey</i> is <b>NULL</b>, <i>KeyName</i> must specify a complete path to a registry key.


### -param DesiredAccess [in]

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies access rights that the driver is requesting for the specified registry key. For a list of access rights that drivers typically use for registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558746">Opening a Handle to a Registry-Key Object</a>. Your driver must ask for only the types of access that it needs. For example, the driver must not ask for KEY_ALL_ACCESS if it will only read the registry key. 


### -param CreateOptions [in]

One or more flags. For information about these flags, see the <i>CreateOptions</i> parameter or <a href="kernel.zwcreatekey">ZwCreateKey</a>.


### -param CreateDisposition [out, optional]

A pointer to a location that receives REG_CREATED_NEW_KEY if a new key is created or REG_OPENED_EXISTING_KEY if an existing key is opened. These values are defined in <i>Wdm.h</i>. This pointer is optional and can be <b>NULL</b>.


### -param KeyAttributes [in, optional]

A pointer to a <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied attributes for the new registry-key object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.


### -param Key [out]

A pointer to a location that receives a handle to the new registry-key object.


## -returns
<b>WdfRegistryCreateKey</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:
<dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl>
<a href="wdf.wdfregistrycreatekey">WdfRegistryCreateKey</a> was not called at IRQL = PASSIVE_LEVEL. 
<dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl>An invalid parameter was specified.
<dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl>A registry-key object could not be allocated.
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl>The system denied the specified access rights.
<dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl>The specified registry key does not exist.

 

For a list of other return values that the <b>WdfRegistryCreateKey</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.



This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.


## -remarks
To obtain a handle to a registry-key object that represents a parent key, your driver can call <a href="wdf.wdfdriveropenparametersregistrykey">WdfDriverOpenParametersRegistryKey</a>, <a href="wdf.wdfdeviceopenregistrykey">WdfDeviceOpenRegistryKey</a>, or <a href="wdf.wdffdoinitopenregistrykey">WdfFdoInitOpenRegistryKey</a>.

By default, the new registry-key object's parent is the framework driver object that the <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> method creates. You can use the <b>ParentObject</b> member of the <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure to specify a different parent. The framework deletes the registry-key object when it deletes the parent object. If your driver does not change the default parent, the driver should delete the registry-key object when it has finished using the object; otherwise, the registry-key object will remain until the I/O manager unloads your driver. 

 If your driver does not change the default parent, the driver should call <a href="wdf.wdfregistryclose">WdfRegistryClose</a> when it has finished using the object; otherwise, the registry-key object will remain until the I/O manager unloads your driver. Alternatively,  the driver can call <a href="wdf.wdfobjectdelete">WdfObjectDelete</a> to delete the registry-key object.

For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.

The following code example opens a driver's software key, and then it creates and opens the <b>MySubKey</b> registry key, which is located under the driver's software key.


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="kernel.rtlinitunicodestring">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfdeviceopenregistrykey">WdfDeviceOpenRegistryKey</a>
</dt>
<dt>
<a href="wdf.wdfdriveropenparametersregistrykey">WdfDriverOpenParametersRegistryKey</a>
</dt>
<dt>
<a href="wdf.wdffdoinitopenregistrykey">WdfFdoInitOpenRegistryKey</a>
</dt>
<dt>
<a href="wdf.wdfregistryopenkey">WdfRegistryOpenKey</a>
</dt>
<dt>
<a href="kernel.zwcreatekey">ZwCreateKey</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRegistryCreateKey method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

