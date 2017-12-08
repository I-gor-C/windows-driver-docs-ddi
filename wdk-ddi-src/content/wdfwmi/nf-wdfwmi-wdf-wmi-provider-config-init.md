---
UID: NF.wdfwmi.WDF_WMI_PROVIDER_CONFIG_INIT
title: WDF_WMI_PROVIDER_CONFIG_INIT
author: windows-driver-content
description: The WDF_WMI_PROVIDER_CONFIG_INIT function initializes a WDF_WMI_PROVIDER_CONFIG structure.
old-location: wdf\wdf_wmi_provider_config_init.htm
old-project: wdf
ms.assetid: a63079ab-45ec-44b2-8769-f5b30f378972
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_WMI_PROVIDER_CONFIG_INIT
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
req.alt-api: WDF_WMI_PROVIDER_CONFIG_INIT
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
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# WDF_WMI_PROVIDER_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_WMI_PROVIDER_CONFIG_INIT</b> function initializes a <a href="..\wdfwmi\ns-wdfwmi--wdf-wmi-provider-config.md">WDF_WMI_PROVIDER_CONFIG</a> structure.</p>


## -syntax

````
VOID WDF_WMI_PROVIDER_CONFIG_INIT(
  _Out_       PWDF_WMI_PROVIDER_CONFIG Config,
  _In_  const GUID                     *Guid
);
````


## -parameters
<dl>

### -param Config [out]

<dd>
<p>A pointer to a <a href="..\wdfwmi\ns-wdfwmi--wdf-wmi-provider-config.md">WDF_WMI_PROVIDER_CONFIG</a> structure.</p>
</dd>

### -param Guid [in]

<dd>
<p>A pointer to a GUID that identifies a WMI data provider's data block. </p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_WMI_PROVIDER_CONFIG_INIT</b> function zeros the specified <a href="..\wdfwmi\ns-wdfwmi--wdf-wmi-provider-config.md">WDF_WMI_PROVIDER_CONFIG</a> structure and sets its <b>Size</b> member. This function also copies the specified GUID into the structure's <b>Guid</b> member.</p>

<p>For a code example that uses <b>WDF_WMI_PROVIDER_CONFIG_INIT</b>, see <a href="..\wdfwmi\nf-wdfwmi-wdfwmiprovidercreate.md">WdfWmiProviderCreate</a>.</p>

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
<a href="..\wdfwmi\ns-wdfwmi--wdf-wmi-provider-config.md">WDF_WMI_PROVIDER_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WMI_PROVIDER_CONFIG_INIT function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
