---
UID: NF.wdfdevice.WDF_DEVICE_PNP_CAPABILITIES_INIT
title: WDF_DEVICE_PNP_CAPABILITIES_INIT
author: windows-driver-content
description: The WDF_DEVICE_PNP_CAPABILITIES_INIT function initializes a WDF_DEVICE_PNP_CAPABILITIES structure.
old-location: wdf\wdf_device_pnp_capabilities_init.htm
ms.assetid: 5ae60715-ba51-4814-ae34-34967cdbab78
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfdevice.h
req.include-header: Wdf.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_DEVICE_PNP_CAPABILITIES_INIT
req.alt-loc: wdfdevice.h
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
ms.keywords: WDF_DEVICE_PNP_CAPABILITIES_INIT
req.iface: 
req.product: Windows 10 or later.
---

# WDF_DEVICE_PNP_CAPABILITIES_INIT function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b> function initializes a <a href="https://msdn.microsoft.com/library/windows/hardware/ff551257">WDF_DEVICE_PNP_CAPABILITIES</a> structure.</p>


## -syntax

````
VOID WDF_DEVICE_PNP_CAPABILITIES_INIT(
  _Out_ PWDF_DEVICE_PNP_CAPABILITIES Caps
);
````


## -parameters
<dl>

### -param <i>Caps</i> [out]

<dd>
<p>A pointer to a driver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff551257">WDF_DEVICE_PNP_CAPABILITIES</a> structure.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551257">WDF_DEVICE_PNP_CAPABILITIES</a> structure, sets the structure's <b>Size</b> member, and sets other members to default values.</p>

<p>For a code example that uses <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546898">WdfDeviceSetPnpCapabilities</a>.</p>

<p>The <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b> function zeros the specified <a href="https://msdn.microsoft.com/library/windows/hardware/ff551257">WDF_DEVICE_PNP_CAPABILITIES</a> structure, sets the structure's <b>Size</b> member, and sets other members to default values.</p>

<p>For a code example that uses <b>WDF_DEVICE_PNP_CAPABILITIES_INIT</b>, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff546898">WdfDeviceSetPnpCapabilities</a>.</p>

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
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfdevice.h (include Wdf.h)</dt>
</dl>
</td>
</tr>
</table>