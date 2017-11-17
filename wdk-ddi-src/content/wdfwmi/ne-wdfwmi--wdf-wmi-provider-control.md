---
UID: NE.wdfwmi._WDF_WMI_PROVIDER_CONTROL
title: WDF_WMI_PROVIDER_CONTROL
author: windows-driver-content
description: The WDF_WMI_PROVIDER_CONTROL enumeration defines the type of control functions that a WMI data provider can support.
old-location: wdf\wdf_wmi_provider_control.htm
ms.assetid: c545b0a6-bb36-47a7-b55c-ee7eed5ade3a
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
req.alt-api: WDF_WMI_PROVIDER_CONTROL
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

# WDF_WMI_PROVIDER_CONTROL enumeration



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_WMI_PROVIDER_CONTROL</b> enumeration defines the type of control functions that a WMI data provider can support.</p>


## -syntax

````
typedef enum _WDF_WMI_PROVIDER_CONTROL { 
  WdfWmiControlInvalid   = 0,
  WdfWmiEventControl     = 1,
  WdfWmiInstanceControl  = 2
} WDF_WMI_PROVIDER_CONTROL;
````


## -enum-fields
<dl>

### -field <a id="WdfWmiControlInvalid"></a><a id="wdfwmicontrolinvalid"></a><a id="WDFWMICONTROLINVALID"></a><b>WdfWmiControlInvalid</b>

<dd>
<p>For internal use only.</p>
</dd>

### -field <a id="WdfWmiEventControl"></a><a id="wdfwmieventcontrol"></a><a id="WDFWMIEVENTCONTROL"></a><b>WdfWmiEventControl</b>

<dd>
<p>The driver must enable or disable delivering events for a provider instance.</p>
</dd>

### -field <a id="WdfWmiInstanceControl"></a><a id="wdfwmiinstancecontrol"></a><a id="WDFWMIINSTANCECONTROL"></a><b>WdfWmiInstanceControl</b>

<dd>
<p>The driver must enable or disable collecting data for a provider instance.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_WMI_PROVIDER_CONTROL</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a> method and the driver's <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function.</p>

<p>The <b>WDF_WMI_PROVIDER_CONTROL</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a> method and the driver's <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function.</p>

<p>The <b>WDF_WMI_PROVIDER_CONTROL</b> enumeration is used as an input parameter to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a> method and the driver's <a href="https://msdn.microsoft.com/89b48747-d3aa-48c7-825c-94545f378f07">EvtWmiProviderFunctionControl</a> callback function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551200">WdfWmiProviderIsEnabled</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WMI_PROVIDER_CONTROL enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
