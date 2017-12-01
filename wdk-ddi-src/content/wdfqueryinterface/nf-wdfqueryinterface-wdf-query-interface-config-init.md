---
UID: NF.wdfqueryinterface.WDF_QUERY_INTERFACE_CONFIG_INIT
title: WDF_QUERY_INTERFACE_CONFIG_INIT
author: windows-driver-content
description: The WDF_QUERY_INTERFACE_CONFIG_INIT function initializes a driver's WDF_QUERY_INTERFACE_CONFIG structure.
old-location: wdf\wdf_query_interface_config_init.htm
old-project: wdf
ms.assetid: 509f4fa5-37c8-4098-aade-767aad5d6d6a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_QUERY_INTERFACE_CONFIG_INIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfqueryinterface.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 
req.alt-api: WDF_QUERY_INTERFACE_CONFIG_INIT
req.alt-loc: Wdfqueryinterface.h
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

# WDF_QUERY_INTERFACE_CONFIG_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF only]</p>
<p>The <b>WDF_QUERY_INTERFACE_CONFIG_INIT</b> function initializes a driver's <a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure.</p>


## -syntax

````
VOID WDF_QUERY_INTERFACE_CONFIG_INIT(
  _Out_          PWDF_QUERY_INTERFACE_CONFIG                    InterfaceConfig,
  _In_           PINTERFACE                                     Interface,
  _In_     const GUID                                           *InterfaceType,
  _In_opt_       PFN_WDF_DEVICE_PROCESS_QUERY_INTERFACE_REQUEST EvtDeviceProcessQueryInterfaceRequest
);
````


## -parameters
<dl>

### -param <i>InterfaceConfig</i> [out]

<dd>
<p>A pointer to the driver's <a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a> structure.</p>
</dd>

### -param <i>Interface</i> [in]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--interface.md">INTERFACE</a> structure.</p>
</dd>

### -param <i>InterfaceType</i> [in]

<dd>
<p>A pointer to the GUID that identifies the interface.</p>
</dd>

### -param <i>EvtDeviceProcessQueryInterfaceRequest</i> [in, optional]

<dd>
<p>A pointer to the driver's <a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a> event callback function, which is called when another driver requests the interface.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>For more information about driver-defined interfaces, see <a href="wdf.using_driver_defined_interfaces">Using Driver-Defined Interfaces</a>.</p>

<p>For a code example that uses <b>WDF_QUERY_INTERFACE_CONFIG_INIT</b>, see <a href="..\wdfqueryinterface\nf-wdfqueryinterface-wdfdeviceaddqueryinterface.md">WdfDeviceAddQueryInterface</a>.</p>

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
<dt>Wdfqueryinterface.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="wdf.evtdeviceprocessqueryinterfacerequest">EvtDeviceProcessQueryInterfaceRequest</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--interface.md">INTERFACE</a>
</dt>
<dt>
<a href="..\wdfqueryinterface\ns-wdfqueryinterface--wdf-query-interface-config.md">WDF_QUERY_INTERFACE_CONFIG</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_QUERY_INTERFACE_CONFIG_INIT function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
