---
UID: NS.wdfwmi._WDF_WMI_INSTANCE_CONFIG
title: WDF_WMI_INSTANCE_CONFIG
author: windows-driver-content
description: The WDF_WMI_INSTANCE_CONFIG structure contains configuration information for an instance of a WMI data provider.
old-location: wdf\wdf_wmi_instance_config.htm
old-project: wdf
ms.assetid: b2b2fd0c-c331-4132-b037-05c816626563
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WDF_WMI_INSTANCE_CONFIG, WDF_WMI_INSTANCE_CONFIG, *PWDF_WMI_INSTANCE_CONFIG
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
req.alt-api: WDF_WMI_INSTANCE_CONFIG
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

# WDF_WMI_INSTANCE_CONFIG structure



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_WMI_INSTANCE_CONFIG</b> structure contains configuration information for an instance of a WMI data provider.</p>


## -syntax

````
typedef struct _WDF_WMI_INSTANCE_CONFIG {
  ULONG                               Size;
  WDFWMIPROVIDER                      Provider;
  PWDF_WMI_PROVIDER_CONFIG            ProviderConfig;
  BOOLEAN                             UseContextForQuery;
  BOOLEAN                             Register;
  PFN_WDF_WMI_INSTANCE_QUERY_INSTANCE EvtWmiInstanceQueryInstance;
  PFN_WDF_WMI_INSTANCE_SET_INSTANCE   EvtWmiInstanceSetInstance;
  PFN_WDF_WMI_INSTANCE_SET_ITEM       EvtWmiInstanceSetItem;
  PFN_WDF_WMI_INSTANCE_EXECUTE_METHOD EvtWmiInstanceExecuteMethod;
} WDF_WMI_INSTANCE_CONFIG, *PWDF_WMI_INSTANCE_CONFIG;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>The size, in bytes, of this structure.</p>
</dd>

### -field <b>Provider</b>

<dd>
<p>A handle to a WMI provider object that a driver obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a>. If this member is <b>NULL</b>, the <b>ProviderConfig</b> member must not be <b>NULL</b>.</p>
</dd>

### -field <b>ProviderConfig</b>

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a> structure. If this member is <b>NULL</b>, the <b>Provider</b> member must not be <b>NULL</b>.</p>
</dd>

### -field <b>UseContextForQuery</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the driver will store instance data in the WMI instance object's context space and will not provide an <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md">EvtWmiInstanceQueryInstance</a> callback function. Instead, the framework will service a WMI client's request for instance data by sending the contents of the context space to WMI. If this member is <b>FALSE</b>, the driver must provide an <i>EvtWmiInstanceQueryInstance</i> callback function (unless the instance data is write-only).</p>
<p>If <b>UseContextForQuery</b> is <b>TRUE</b>, the instance data must be read-only and therefore the driver cannot provide <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md">EvtWmiInstanceSetInstance</a> or <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-item.md">EvtWmiInstanceSetItem</a> callback functions.</p>
</dd>

### -field <b>Register</b>

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the framework will register the provider instance with the system's WMI service after it creates a WMI instance object. If this member is <b>FALSE</b>, the driver must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff551190">WdfWmiInstanceRegister</a> to register the provider instance. </p>
</dd>

### -field <b>EvtWmiInstanceQueryInstance</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md">EvtWmiInstanceQueryInstance</a> callback function for the provider instance, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtWmiInstanceSetInstance</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md">EvtWmiInstanceSetInstance</a> callback function for the provider instance, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtWmiInstanceSetItem</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-item.md">EvtWmiInstanceSetItem</a> callback function for the provider instance, or <b>NULL</b>.</p>
</dd>

### -field <b>EvtWmiInstanceExecuteMethod</b>

<dd>
<p>A pointer to the driver's <a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-execute-method.md">EvtWmiInstanceExecuteMethod</a> callback function for the provider instance, or <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>The <b>WDF_WMI_INSTANCE_CONFIG</b> structure is used as input to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a> method.</p>

<p>To initialize a <b>WDF_WMI_INSTANCE_CONFIG</b> structure, your driver should call <a href="https://msdn.microsoft.com/library/windows/hardware/ff553061">WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff553063">WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG</a>.</p>

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
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-execute-method.md">EvtWmiInstanceExecuteMethod</a>
</dt>
<dt>
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-query-instance.md">EvtWmiInstanceQueryInstance</a>
</dt>
<dt>
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-instance.md">EvtWmiInstanceSetInstance</a>
</dt>
<dt>
<a href="..\wdfwmi\nc-wdfwmi-evt-wdf-wmi-instance-set-item.md">EvtWmiInstanceSetItem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553061">WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553063">WDF_WMI_INSTANCE_CONFIG_INIT_PROVIDER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553067">WDF_WMI_PROVIDER_CONFIG</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551178">WdfWmiInstanceCreate</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551190">WdfWmiInstanceRegister</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff551193">WdfWmiProviderCreate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_WMI_INSTANCE_CONFIG structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
