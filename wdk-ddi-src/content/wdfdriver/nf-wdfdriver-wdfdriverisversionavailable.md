---
UID: NF.wdfdriver.WdfDriverIsVersionAvailable
title: WdfDriverIsVersionAvailable function
author: windows-driver-content
description: The WdfDriverIsVersionAvailable method returns a Boolean value that indicates whether the driver is running with a specified version of the Kernel-Mode Driver Framework library.
old-location: wdf\wdfdriverisversionavailable.htm
old-project: wdf
ms.assetid: 5635b99d-c58d-4a17-bb51-2dc38e51421a
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WdfDriverIsVersionAvailable
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
req.alt-api: WdfDriverIsVersionAvailable
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

# WdfDriverIsVersionAvailable function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WdfDriverIsVersionAvailable</b> method returns a Boolean value that indicates whether the driver is running with a specified version of the Kernel-Mode Driver Framework library.



## -syntax

````
BOOLEAN WdfDriverIsVersionAvailable(
  _In_ WDFDRIVER                            Driver,
  _In_ PWDF_DRIVER_VERSION_AVAILABLE_PARAMS VersionAvailableParams
);
````


## -parameters

### -param Driver [in]

A handle to the driver's framework driver object that the driver obtained from a previous call to <a href="wdf.wdfdrivercreate">WdfDriverCreate</a> or <a href="wdf.wdfgetdriver">WdfGetDriver</a>.


### -param VersionAvailableParams [in]

A pointer to a <a href="wdf.wdf_driver_version_available_params">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a> structure that identifies a version of the framework library.


## -returns
<b>WdfDriverIsVersionAvailable</b> returns <b>TRUE</b> if the driver is running with the version of the library that the <i>VersionAvailableParams</i> parameter specifies. 

The method returns <b>FALSE</b> if the driver is not running with the specified library version or if the WDF_DRIVER_VERSION_AVAILABLE_PARAMS structure is invalid.

A system bug check occurs if the <i>Driver</i> handle is invalid.




## -remarks
For more information about library versions, see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.

The following code example reports an error if it detects an unexpected library version number.


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
<a href="wdf.wdf_driver_version_available_params">WDF_DRIVER_VERSION_AVAILABLE_PARAMS</a>
</dt>
<dt>
<a href="wdf.wdfdrivercreate">WdfDriverCreate</a>
</dt>
<dt>
<a href="wdf.wdfdriverretrieveversionstring">WdfDriverRetrieveVersionString</a>
</dt>
<dt>
<a href="wdf.wdfgetdriver">WdfGetDriver</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfDriverIsVersionAvailable method%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

