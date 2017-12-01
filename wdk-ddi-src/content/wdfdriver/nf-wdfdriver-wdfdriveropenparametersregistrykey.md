---
UID: NF.wdfdriver.WdfDriverOpenParametersRegistryKey
title: WdfDriverOpenParametersRegistryKey
author: windows-driver-content
description: The WdfDriverOpenParametersRegistryKey method opens the driver's Parameters registry key and retrieves a handle to a framework registry-key object that represents the key.
old-location: wdf\wdfdriveropenparametersregistrykey.htm
old-project: wdf
ms.assetid: e0f22096-3d82-4e1c-9398-d5e441fbb473
ms.author: windowsdriverdev
ms.date: 11/28/2017
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
req.iface: 
req.product: Windows 10 or later.
---

# WdfDriverOpenParametersRegistryKey function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WdfDriverOpenParametersRegistryKey</b> method opens the driver's <b>Parameters</b> registry key and retrieves a handle to a framework registry-key object that represents the key.</p>


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
<dl>

### -param <i>Driver</i> [in]

<dd>
<p>A handle to the driver's framework driver object that the driver obtained from a previous call to <a href="..\wdfdriver\nf-wdfdriver-wdfdrivercreate.md">WdfDriverCreate</a> or <a href="..\wdfdriver\nf-wdfdriver-wdfgetdriver.md">WdfGetDriver</a>.</p>
</dd>

### -param <i>DesiredAccess</i> [in]

<dd>
<p>An <a href="https://msdn.microsoft.com/library/windows/hardware/ff540466">ACCESS_MASK</a>-typed value that specifies an access mask for the <b>Parameters</b> registry key.</p>
<p>A KMDF driver typically requests <b>KEY_READ</b>, <b>KEY_WRITE</b>, or <b>KEY_READ | KEY_WRITE</b>.</p>
<p>If you are writing a UMDF driver, use <b>KEY_READ</b> or <b>KEY_READ | KEY_SET_VALUE</b>.</p>
<p>As a best practice, ask for only the types of access that your driver needs.</p>
</dd>

### -param <i>KeyAttributes</i> [in, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a> structure that specifies object attributes for the framework registry-key object. This parameter is optional and can be WDF_NO_OBJECT_ATTRIBUTES.</p>
</dd>

### -param <i>Key</i> [out]

<dd>
<p>A pointer to a location that receives a handle to a framework registry-key object.</p>
</dd>
</dl>

## -returns
<p><b>WdfDriverOpenParametersRegistryKey</b> returns STATUS_SUCCESS if the operation succeeds. Additional return values include:</p><dl>
<dt><b>STATUS_ACCESS_DENIED</b></dt>
</dl><p> A UMDF driver specified one of the following flags in the <i>DesiredAccess</i> parameter:<ul>
<li>GENERIC_WRITE</li>
<li>KEY_CREATE_SUBKEY</li>
<li>WRITE_DAC</li>
</ul>
</p>

<p>Because the above values are invalid for UMDF drivers, universal flags such as GENERIC_ALL and STANDARD_RIGHTS_ALL also cause <a href="..\wdfdriver\nf-wdfdriver-wdfdriveropenparametersregistrykey.md">WdfDriverOpenParametersRegistryKey</a> to fail with this return value.</p>

<p> </p>

<p>For more information about return values, see <a href="wdf.framework_object_creation_errors">Framework Object Creation Errors</a>.</p>

<p>This method might also return other <a href="https://msdn.microsoft.com/library/windows/hardware/ff557697">NTSTATUS values</a>.</p>

<p>A system bug check occurs if a KMDF driver specifies an invalid handle in <i>Driver</i>.</p>

## -remarks
<p>The driver's <b>Parameters</b> key is located in the registry's <a href="https://msdn.microsoft.com/library/windows/hardware/dn926947">Services</a> tree. If the driver's <b>Parameters</b> key does not exist, the <b>WdfDriverOpenParametersRegistryKey</b> method creates it. </p>

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
<dt>Wdfdriver.h (include Wdf.h)</dt>
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
<a href="..\wdfobject\ns-wdfobject--wdf-object-attributes.md">WDF_OBJECT_ATTRIBUTES</a>
</dt>
<dt>
<a href="..\wdfdriver\nf-wdfdriver-wdfdrivercreate.md">WdfDriverCreate</a>
</dt>
<dt>
<a href="..\wdfdriver\nf-wdfdriver-wdfdrivergetregistrypath.md">WdfDriverGetRegistryPath</a>
</dt>
<dt>
<a href="..\wdfdriver\nf-wdfdriver-wdfgetdriver.md">WdfGetDriver</a>
</dt>
<dt>
<a href="..\wdfregistry\nf-wdfregistry-wdfregistryclose.md">WdfRegistryClose</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDriverOpenParametersRegistryKey method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
