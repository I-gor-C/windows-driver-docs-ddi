---
UID: NF.wdfregistry.WdfRegistryOpenKey
title: WdfRegistryOpenKey
author: windows-driver-content
description: The WdfRegistryOpenKey method opens a specified registry key and creates a framework registry-key object that represents the registry key.
old-location: wdf\wdfregistryopenkey.htm
ms.assetid: a79f6f98-1ebb-498e-9e20-cfdd22a0da7a
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfregistry.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfRegistryOpenKey
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
ms.keywords: WdfRegistryOpenKey
req.iface: 
req.product: Windows 10 or later.
---

# WdfRegistryOpenKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfRegistryOpenKey</b> method opens a specified registry key and creates a framework registry-key object that represents the registry key.</p>


## -syntax

````
NTSTATUS WdfRegistryOpenKey(
  _In_opt_ WDFKEY                 ParentKey,
  _In_     PCUNICODE_STRING       KeyName,
  _In_     ACCESS_MASK            DesiredAccess,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES KeyAttributes,
  _Out_    WDFKEY                 *Key
);
````


## -parameters
<dl>

### -param <i>ParentKey</i> [in, optional]

<dd>
<p>A handle to a framework registry-key object. This object represents a parent registry key that the driver has opened. This parameter is optional and can be <b>NULL</b>. If the parameter is not <b>NULL</b>, the key that <i>KeyName</i> specifies must reside under this parent key in the registry. For more information about this parent key, see the Remarks section.</p>
</dd>

### -param <i>KeyName</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a> structure that contains the name of the key to be opened. The key name can include path information. If <i>ParentKey</i> is <b>NULL</b>, <i>KeyName</i> must specify a complete path to a registry key. For examples, see the Remarks section.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies access rights that the driver is requesting for the specified registry key. For a list of access rights that drivers typically use for registry keys, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff558746">Opening a Handle to a Registry-Key Object</a>. Your driver must ask for only the types of access that it needs. For example, the driver must not ask for KEY_ALL_ACCESS if it will only read the registry key. </p>
</dd>

### -param <i>KeyAttributes</i> [in, optional]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a> structure that contains driver-supplied attributes for the new registry-key object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Key</i> [out]

<dd>
<p>A pointer to a location that receives a handle to the new registry-key object.</p>
</dd>
</dl>

## -returns
<p><b>WdfRegistryOpenKey</b> returns STATUS_SUCCESS if the operation succeeds. Otherwise, the method might return one of the following values:</p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549919">WdfRegistryOpenKey</a> was not called at IRQL = PASSIVE_LEVEL. </p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>An invalid parameter was specified.</p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p>A registry-key object could not be allocated.</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p>The system denied the specified access rights.</p><dl>
<dt><b>STATUS_OBJECT_NAME_NOT_FOUND</b></dt>
</dl><p>The specified registry key does not exist.</p>

<p> </p>

<p>For a list of other return values that the <b>WdfRegistryOpenKey</b> method might return, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

</p>

<p>This method also might return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

## -remarks
<p>To obtain a handle to a registry-key object that represents a parent key, your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547202">WdfDriverOpenParametersRegistryKey</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546804">WdfDeviceOpenRegistryKey</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547249">WdfFdoInitOpenRegistryKey</a>.</p>

<p>The string format specified in the <i>KeyName</i> parameter  depends on whether the caller is a KMDF driver or a UMDF driver. For example, to open the following path:</p>

<p>
<p><b>HKLM\System\CurrentControlSet\Control</b></p>
</p>

<p><b>HKLM\System\CurrentControlSet\Control</b></p>

<p>Your driver might use this conditional logic:</p>

<p>When the driver has finished using a registry key that it opens with <b>WdfRegistryOpenKey</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a>.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example opens a driver's software key, and then it opens the <b>MySubKey</b> registry key, which is located under the driver's software key.</p>

<p>To obtain a handle to a registry-key object that represents a parent key, your driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff547202">WdfDriverOpenParametersRegistryKey</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff546804">WdfDeviceOpenRegistryKey</a>, or <a href="https://msdn.microsoft.com/library/windows/hardware/ff547249">WdfFdoInitOpenRegistryKey</a>.</p>

<p>The string format specified in the <i>KeyName</i> parameter  depends on whether the caller is a KMDF driver or a UMDF driver. For example, to open the following path:</p>

<p>
<p><b>HKLM\System\CurrentControlSet\Control</b></p>
</p>

<p><b>HKLM\System\CurrentControlSet\Control</b></p>

<p>Your driver might use this conditional logic:</p>

<p>When the driver has finished using a registry key that it opens with <b>WdfRegistryOpenKey</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a>.</p>

<p>For more information about registry-key objects, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.</p>

<p>The following code example opens a driver's software key, and then it opens the <b>MySubKey</b> registry key, which is located under the driver's software key.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561934">RtlInitUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564879">UNICODE_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552400">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff546804">WdfDeviceOpenRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547202">WdfDriverOpenParametersRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547249">WdfFdoInitOpenRegistryKey</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549914">WdfRegistryClose</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff549917">WdfRegistryCreateKey</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfRegistryOpenKey method%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
