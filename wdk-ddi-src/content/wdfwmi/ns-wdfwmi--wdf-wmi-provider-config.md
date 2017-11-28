---
UID: NS.wdfwmi._WDF_WMI_PROVIDER_CONFIG
title: WDF_WMI_PROVIDER_CONFIG
author: windows-driver-content
description: The WDF_WMI_PROVIDER_CONFIG structure contains configuration information for a driver's WMI data block.
old-location: wdf\wdf_wmi_provider_config.htm
old-project: wdf
ms.assetid: 91b8e4e8-f144-4469-bedf-18f40be7e649
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_WMI_PROVIDER_CONFIG, WDF_WMI_PROVIDER_CONFIG, *PWDF_WMI_PROVIDER_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wdfwmi.h
req.include-header: Wdf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_WMI_PROVIDER_CONFIG
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
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# WDF_WMI_PROVIDER_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_WMI_PROVIDER_CONFIG</b> structure contains configuration information for a driver's WMI data block.</p>


## -syntax

````
typedef struct _WDF_WMI_PROVIDER_CONFIG {
  ULONG                                 Size;
  GUID                                  Guid;
  ULONG                                 Flags;
  ULONG                                 MinInstanceBufferSize;
  PFN_WDF_WMI_PROVIDER_FUNCTION_CONTROL EvtWmiProviderFunctionControl;
} WDF_WMI_PROVIDER_CONFIG, *PWDF_WMI_PROVIDER_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Guid</b>

<dd>
<p>The symbolic name of a <a href="https://msdn.microsoft.com/library/windows/hardware/dn922935">GUID</a> that identifies a WMI data block.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>A bitwise OR of <a href="https://msdn.microsoft.com/library/windows/hardware/ff553082">WDF_WMI_PROVIDER_FLAGS</a>-typed values. </p>
</dd>

### -field <b>MinInstanceBufferSize</b>

<dd>
<p>The minimum size, in bytes, of fixed-length buffers that the <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md">EvtWmiInstanceQueryInstance</a> and <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md">EvtWmiInstanceSetInstance</a> callback functions will use for provider instances. This member must be zero for variable-length buffers. This member is ignored if <b>WdfWmiProviderEventOnly</b> is set in the <b>Flags</b> member.</p>
</dd>

### -field <b>EvtWmiProviderFunctionControl</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-provider-function-control.md">EvtWmiProviderFunctionControl</a> callback function, or <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_WMI_PROVIDER_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a> method.</p>

<p>To initialize a <b>WDF_WMI_PROVIDER_CONFIG</b> structure, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553070">WDF_WMI_PROVIDER_CONFIG_INIT</a>.</p>

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
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-provider-function-control.md">EvtWmiProviderFunctionControl</a>
</dt>
<dt>
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md">EvtWmiInstanceQueryInstance</a>
</dt>
<dt>
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md">EvtWmiInstanceSetInstance</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553070">WDF_WMI_PROVIDER_CONFIG_INIT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553082">WDF_WMI_PROVIDER_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WMI_PROVIDER_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
