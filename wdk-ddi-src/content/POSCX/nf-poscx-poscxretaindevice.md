---
UID: NF.poscx.PosCxRetainDevice
title: PosCxRetainDevice
author: windows-driver-content
description: PosCxRetainDevice is called to extend the ownership of the device.
old-location: pos\poscxretaindevice.htm
ms.assetid: 0DF5E1DA-35BA-406A-A708-461534373F12
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxRetainDevice
req.alt-loc: poscx.h
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
ms.keywords: PosCxRetainDevice
req.iface: 
req.product: Windows 10 or later.
---

# PosCxRetainDevice function



## -description
<p>PosCxRetainDevice is called to extend the ownership of the device.</p>


## -syntax

````
NTSTATUS PosCxRetainDevice(
  _In_ WDFDEVICE  device,
  _In_ WDFREQUEST request
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>request</i> [in]

<dd>
<p>A handle to a framework request object that represents the request. This request must come from a WDF IO queue. The caller must always complete the request.</p>
</dd>
</dl>

## -returns
<p>Possible return values are:</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>