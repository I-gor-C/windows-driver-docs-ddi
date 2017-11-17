---
UID: NF.ufxclient.UFX_DEVICE_CAPABILITIES_INIT
title: UFX_DEVICE_CAPABILITIES_INIT
author: windows-driver-content
description: The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure.
old-location: buses\ufx_device_capabilities_init.htm
ms.assetid: 7C55EB8D-1B68-484A-B95A-E0150FBA9AB8
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: usbref
req.header: ufxclient.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: UFX_DEVICE_CAPABILITIES_INIT
req.alt-loc: ufxclient.h
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
ms.keywords: UFX_DEVICE_CAPABILITIES_INIT
req.iface: 
req.product: Windows 10 or later.
---

# UFX_DEVICE_CAPABILITIES_INIT function



## -description
<p>The <b>UFX_DEVICE_CAPABILITIES_INIT</b> macro the initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187973">UFX_DEVICE_CAPABILITIES</a> structure.</p>


## -syntax

````
void UFX_DEVICE_CAPABILITIES_INIT(
  _Out_ PUFX_DEVICE_CAPABILITIES Capabilities
);
````


## -parameters
<dl>

### -param <i>Capabilities</i> [out]

<dd>
<p>Pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187973">UFX_DEVICE_CAPABILITIES</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ufxclient.h</dt>
</dl>
</td>
</tr>
</table>