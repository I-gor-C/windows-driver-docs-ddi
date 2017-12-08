---
UID: NF.wdfwmi.WdfWmiInstanceDeregister
title: WdfWmiInstanceDeregister function
author: windows-driver-content
description: The WdfWmiInstanceDeregister method deregisters a specified instance of a WMI data provider from the system's WMI service.
old-location: wdf\wdfwmiinstancederegister.htm
old-project: wdf
ms.assetid: 2167504e-ca92-4427-9101-04a2c2bf66df
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfWmiInstanceDeregister
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WdfWmiInstanceDeregister
req.alt-loc: Wdf01000.sys,Wdf01000.sys.dll
req.ddi-compliance: DriverCreate, KmdfIrql, KmdfIrql2
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Wdf01000.sys (see Framework Library Versioning.)
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# WdfWmiInstanceDeregister function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfWmiInstanceDeregister</b> method deregisters a specified instance of a WMI data provider from the system's WMI service.


## -syntax

````
VOID WdfWmiInstanceDeregister(
  _In_ WDFWMIINSTANCE WmiInstance
);
````


## -parameters

### -param WmiInstance [in]

A handle to a WMI instance object that the driver obtained from a previous call to <a href="wdf.wdfwmiinstancecreate">WdfWmiInstanceCreate</a>.

## -returns
None.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
For more information about the <b>WdfWmiInstanceDeregister</b> method, see <a href="wdf.initializing_wmi_support_in_your_driver#registering_provider_instances#registering_provider_instances">Registering Provider Instances</a>. For more information about WMI, see <a href="wdf.supporting_wmi_in_kmdf_drivers">Supporting WMI in Framework-Based Drivers</a>.


<a href="wdf.wdfwmiinstanceregister">WdfWmiInstanceRegister</a> deregisters the provider instance synchronously (that is, before returning) if it is called at IRQL = PASSIVE_LEVEL and asynchronously if it is called at IRQL &gt; PASSIVE_LEVEL. 

The following code example deregisters a specified instance of a WMI data provider from the system's WMI service.

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
Header
</th>
<td width="70%">
<dl>
<dt>Wdfwmi.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Wdf01000.sys (see <a href="wdf.framework_library_versioning">Framework Library Versioning</a>.)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
&lt;=DISPATCH_LEVEL
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
<a href="wdf.wdfwmiinstancecreate">WdfWmiInstanceCreate</a>
</dt>
<dt>
<a href="wdf.wdfwmiinstanceregister">WdfWmiInstanceRegister</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWmiInstanceDeregister method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
