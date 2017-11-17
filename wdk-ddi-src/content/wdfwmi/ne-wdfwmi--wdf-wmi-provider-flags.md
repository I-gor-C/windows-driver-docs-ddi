---
UID: NE.wdfwmi._WDF_WMI_PROVIDER_FLAGS
title: WDF_WMI_PROVIDER_FLAGS
author: windows-driver-content
description: The WDF_WMI_PROVIDER_FLAGS enumeration defines configuration flags for a driver's WMI data provider.
old-location: wdf\wdf_wmi_provider_flags.htm
ms.assetid: 85b1a4b4-53e0-4663-b813-18801f8b639b
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_WMI_PROVIDER_FLAGS
req.alt-loc: wdfwmi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: WdfVerifierKeBugCheck
req.iface: 
req.product: Windows 10 or later.
---

# WDF_WMI_PROVIDER_FLAGS enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_WMI_PROVIDER_FLAGS</b> enumeration defines configuration flags for a driver's WMI data provider.</p>


## -syntax

````
typedef enum _WDF_WMI_PROVIDER_FLAGS { 
  WdfWmiProviderEventOnly   = 0x0001,
  WdfWmiProviderExpensive   = 0x0002,
  WdfWmiProviderTracing     = 0x0004,
  WdfWmiProviderValidFlags  = WdfWmiProviderEventOnly | WdfWmiProviderExpensive | WdfWmiProviderTracing
} WDF_WMI_PROVIDER_FLAGS;
````


## -enum-fields
<dl>

### -field <a id="WdfWmiProviderEventOnly"></a><a id="wdfwmiprovidereventonly"></a><a id="WDFWMIPROVIDEREVENTONLY"></a><b>WdfWmiProviderEventOnly</b>

<dd>
<p>WMI clients can receive notification of WMI events, but they cannot query or set instance data. The driver can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551182">WdfWmiInstanceFireEvent</a>, but it does not provide any instance-specific callback functions.</p>
</dd>

### -field <a id="WdfWmiProviderExpensive"></a><a id="wdfwmiproviderexpensive"></a><a id="WDFWMIPROVIDEREXPENSIVE"></a><b>WdfWmiProviderExpensive</b>

<dd>
<p>Collecting the provider's data can potentially affect the driver's performance, so the driver will not collect data unless a WMI client has registered to use it. The framework calls the driver's <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function, passing the <b>WdfWmiInstanceControl</b> value (from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553078">WDF_WMI_PROVIDER_CONTROL</a> enumeration), to inform the driver to begin collecting data. If the driver does not provide an <i>EvtWmiProviderFunctionControl</i> callback function, it can call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>.</p>
</dd>

### -field <a id="WdfWmiProviderTracing"></a><a id="wdfwmiprovidertracing"></a><a id="WDFWMIPROVIDERTRACING"></a><b>WdfWmiProviderTracing</b>

<dd>
<p>The WMI data provider supports WMI event tracing. The driver can obtain the tracing handle by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551198">WdfWmiProviderGetTracingHandle</a>. If this flag is set, no other flags can be set.</p>
</dd>

### -field <a id="WdfWmiProviderValidFlags"></a><a id="wdfwmiprovidervalidflags"></a><a id="WDFWMIPROVIDERVALIDFLAGS"></a><b>WdfWmiProviderValidFlags</b>

<dd>
<p>The bitwise OR of all flags. Drivers should not use this value.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_WMI_PROVIDER_FLAGS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure.</p>

<p>The <b>WDF_WMI_PROVIDER_FLAGS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure.</p>

<p>The <b>WDF_WMI_PROVIDER_FLAGS</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure.</p>

## -requirements
<table>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfwmi.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/c545b0a6-bb36-47a7-b55c-ee7eed5ade3a">WdfWmiInstanceControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551182">WdfWmiInstanceFireEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551198">WdfWmiProviderGetTracingHandle</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WMI_PROVIDER_FLAGS enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
