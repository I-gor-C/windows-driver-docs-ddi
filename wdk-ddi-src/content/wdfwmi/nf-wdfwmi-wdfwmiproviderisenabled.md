---
UID: NF.wdfwmi.WdfWmiProviderIsEnabled
title: WdfWmiProviderIsEnabled function
author: windows-driver-content
description: The WdfWmiProviderIsEnabled method determines if either data collection or event notification is enabled for a specified WMI data provider.
old-location: wdf\wdfwmiproviderisenabled.htm
old-project: wdf
ms.assetid: 7b4fd9ff-09a7-44df-a3e6-0af5d7ea624e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WdfWmiProviderIsEnabled
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
req.alt-api: WdfWmiProviderIsEnabled
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

# WdfWmiProviderIsEnabled function



## -description
<p class="CCE_Message">[Applies to KMDF only]
The <b>WdfWmiProviderIsEnabled</b> method determines if either data collection or event notification is enabled for a specified WMI data provider.


## -syntax

````
BOOLEAN WdfWmiProviderIsEnabled(
  _In_ WDFWMIPROVIDER           WmiProvider,
  _In_ WDF_WMI_PROVIDER_CONTROL ProviderControl
);
````


## -parameters

### -param WmiProvider [in]

A handle to a WMI provider object that the driver obtained by calling <a href="wdf.wdfwmiprovidercreate">WdfWmiProviderCreate</a> or <a href="wdf.wdfwmiinstancegetprovider">WdfWmiInstanceGetProvider</a>.

### -param ProviderControl [in]

A <a href="wdf.wdf_wmi_provider_control">WDF_WMI_PROVIDER_CONTROL</a>-typed value that specifies one of the types of control functions (data collection or event notification) that a WMI data provider can support.

## -returns
<b>WdfWmiProviderIsEnabled</b> returns <b>TRUE</b> if the capability that the <i>ProviderControl</i> parameter specifies is enabled and <b>FALSE</b> otherwise.

A bug check occurs if the driver supplies an invalid object handle.



## -remarks
A driver that does not provide an <a href="..\wdfwmi\nc-wdfwmi-evt_wdf_wmi_provider_function_control.md">EvtWmiProviderFunctionControl</a> callback function can call <b>WdfWmiProviderIsEnabled</b> to determine if data collection or event notification is enabled.

The following code example determines if event notification is enabled for a specified WMI data provider.

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
<a href="..\wdfwmi\nc-wdfwmi-evt_wdf_wmi_provider_function_control.md">EvtWmiProviderFunctionControl</a>
</dt>
<dt>
<a href="wdf.wdf_wmi_provider_control">WDF_WMI_PROVIDER_CONTROL</a>
</dt>
<dt>
<a href="wdf.wdfwmiinstancegetprovider">WdfWmiInstanceGetProvider</a>
</dt>
<dt>
<a href="wdf.wdfwmiprovidercreate">WdfWmiProviderCreate</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WdfWmiProviderIsEnabled method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
