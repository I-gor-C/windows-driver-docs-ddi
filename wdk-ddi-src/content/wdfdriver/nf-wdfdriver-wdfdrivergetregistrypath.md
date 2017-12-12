---
UID: NF.wdfdriver.WdfDriverGetRegistryPath
title: WdfDriverGetRegistryPath function
author: windows-driver-content
description: The WdfDriverGetRegistryPath method retrieves the path to the driver's registry key in the registry's Services tree.
old-location: wdf\wdfdrivergetregistrypath.htm
old-project: wdf
ms.assetid: 5f237d2e-5ffd-40af-8cd8-ea1414807086
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: WdfDriverGetRegistryPath
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
req.alt-api: WdfDriverGetRegistryPath
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

# WdfDriverGetRegistryPath function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDriverGetRegistryPath</b> method retrieves the path to the driver's registry key in the registry's <a href="https://msdn.microsoft.com/library/windows/hardware/dn926947">Services</a> tree.



## -syntax

````
PWSTR WdfDriverGetRegistryPath(
  _In_ WDFDRIVER Driver
);
````


## -parameters

### -param Driver [in]

A handle to the driver's framework driver object, obtained by a previous call to <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> or <a href="wdf.wdfgetdriver">WdfGetDriver</a>. 


## -returns
<b>WdfDriverGetRegistryPath</b> returns a pointer to a NULL-terminated Unicode string that represents the driver's registry path. A system bug check occurs if the <i>Driver</i> handle is invalid.


## -remarks
The registry path string that <b>WdfDriverGetRegistryPath</b> returns is obtained from the <a href="kernel.unicode_string">UNICODE_STRING</a> structure that the driver received as input to its <a href="https://msdn.microsoft.com/library/windows/hardware/ff552644">DriverEntry</a> routine. 

For more information about the registry, see <a href="wdf.using_the_registry_in_kmdf_drivers">Using the Registry in Framework-Based Drivers</a>.

The following code example obtains the path to a driver's registry key in the registry's <b>Services</b> tree.


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
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfdriveropenparametersregistrykey">WdfDriverOpenParametersRegistryKey</a>
</dt>
<dt>
<a href="wdf.wdfgetdriver">WdfGetDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDriverGetRegistryPath method%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

