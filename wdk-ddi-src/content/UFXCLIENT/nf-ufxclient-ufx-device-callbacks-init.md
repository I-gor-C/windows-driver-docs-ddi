---
UID: NF.ufxclient.UFX_DEVICE_CALLBACKS_INIT
title: UFX_DEVICE_CALLBACKS_INIT
author: windows-driver-content
description: The UFX_DEVICE_CALLBACKS_INIT macro initializes the UFX_DEVICE_CALLBACKS structure.
old-location: buses\ufx_device_callbacks_init.htm
ms.assetid: D9E7D359-5FC8-44C8-ACA2-641DEFF17616
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
req.alt-api: UFX_DEVICE_CALLBACKS_INIT
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
ms.keywords: UFX_DEVICE_CALLBACKS_INIT
req.iface: 
req.product: Windows 10 or later.
---

# UFX_DEVICE_CALLBACKS_INIT function



## -description
<p>The <b>UFX_DEVICE_CALLBACKS_INIT</b> macro initializes the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure.</p>


## -syntax

````
FORCEINLINE void UFX_DEVICE_CALLBACKS_INIT(
  _Out_ PUFX_DEVICE_CALLBACKS Callbacks
);
````


## -parameters
<dl>

### -param <i>Callbacks</i> [out]

<dd>
<p>A pointer to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure.</p>
</dd>
</dl>

## -returns
<p>This function does not return a value.</p>

## -remarks
<p>The <b>UFX_DEVICE_CALLBACKS_INIT</b> macro will set all fields of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure to zero and set the <b>Size</b> field appropriately.</p>

<p>The client driver uses the <b>UFX_DEVICE_CALLBACKS_INIT</b> macro the initialize the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure prior to calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a>.</p>

<p>The <b>UFX_DEVICE_CALLBACKS_INIT</b> macro will set all fields of the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure to zero and set the <b>Size</b> field appropriately.</p>

<p>The client driver uses the <b>UFX_DEVICE_CALLBACKS_INIT</b> macro the initialize the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187971">UFX_DEVICE_CALLBACKS</a> structure prior to calling <a href="https://msdn.microsoft.com/library/windows/hardware/mt187951">UfxDeviceCreate</a>.</p>

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