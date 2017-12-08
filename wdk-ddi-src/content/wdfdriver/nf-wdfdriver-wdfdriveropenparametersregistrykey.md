---
UID: NF.wdfdriver.WdfDriverOpenParametersRegistryKey
title: WdfDriverOpenParametersRegistryKey function
author: windows-driver-content
description: The WdfDriverOpenParametersRegistryKey method opens the driver's Parameters registry key and retrieves a handle to a framework registry-key object that represents the key.
old-location: wdf\wdfdriveropenparametersregistrykey.htm
old-project: wdf
ms.assetid: e0f22096-3d82-4e1c-9398-d5e441fbb473
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfDriverOpenParametersRegistryKey
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfdriver.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WdfDriverOpenParametersRegistryKey
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

# WdfDriverOpenParametersRegistryKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]
The <b>WdfDriverOpenParametersRegistryKey</b> method opens the driver's <b>Parameters</b> registry key and retrieves a handle to a framework registry-key object that represents the key.


## -syntax

````
NTSTATUS WdfDriverOpenParametersRegistryKey(
  _In_     WDFDRIVER              Driver,
  _In_     ACCESS_MASK            DesiredAccess,
  _In_opt_ PWDF_OBJECT_ATTRIBUTES KeyAttributes,
  _Out_    WDFKEY                 *Key
);
````


## -parameters

### -param Driver [in]

A handle to the driver's framework driver object that the driver obtained from a previous call to <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> or <a href="wdf.wdfgetdriver">WdfGetDriver</a>.

### -param DesiredAccess [in]

An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies an access mask for the <b>Parameters</b> registry key.
A KMDF driver typically requests <b>KEY_READ</b>, <b>KEY_WRITE</b>, or <b>KEY_READ | KEY_WRITE</b>.
If you are writing a UMDF driver, use <b>KEY_READ</b> or <b>KEY_READ | KEY_SET_VALUE</b>.
As a best practice, ask for only the types of access that your driver needs.

### -param KeyAttributes [in, optional]

A pointer to a caller-allocated <a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the framework registry-key object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.

### -param Key [out]

A pointer to a location that receives a handle to a framework registry-key object.

## -returns
<b>WdfDriverOpenParametersRegistryKey</b> returns STATUS_SUCCESS if the operation succeeds. Additional return values include:
<dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl> A UMDF driver specified one of the following flags in the <i>DesiredAccess</i> parameter:<ul>
<li>GENERIC_WRITE</li>
<li>KEY_CREATE_SUBKEY</li>
<li>WRITE_DAC</li>
</ul>


Because the above values are invalid for UMDF drivers, universal flags such as GENERIC_ALL and STANDARD_RIGHTS_ALL also cause <a href="wdf.wdfdriveropenparametersregistrykey">WdfDriverOpenParametersRegistryKey</a> to fail with this return value.

 

For more information about return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.

This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.

A system bug check occurs if a KMDF driver specifies an invalid handle in <i>Driver</i>.

## -remarks
The driver's <b>Parameters</b> key is located in the registry's <a href="https://msdn.microsoft.com/library/windows/hardware/dn926947">Services</a> tree. If the driver's <b>Parameters</b> key does not exist, the <b>WdfDriverOpenParametersRegistryKey</b> method creates it. 

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
<dt>Wdfdriver.h (include Wdf.h)</dt>
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
<a href="wdf.wdf_object_attributes">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfdrivergetregistrypath">WdfDriverGetRegistryPath</a>
</dt>
<dt>
<a href="wdf.wdfgetdriver">WdfGetDriver</a>
</dt>
<dt>
<a href="wdf.wdfregistryclose">WdfRegistryClose</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDriverOpenParametersRegistryKey method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
