---
UID: NF.poscx.PosCxOpen
title: PosCxOpen
author: windows-driver-content
description: PosCxOpen is called to create an open PosCx library instance. This function initializes all resources it needs to manage a single open instance. It should be called from the driver's EVT_WDF_DEVICE_FILE_CREATE callback.
old-location: pos\poscxopen.htm
old-project: pos
ms.assetid: 6AB1BB0A-B350-44D7-B0D0-9A19FD6DEE19
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxOpen
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxOpen
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
req.iface: 
req.product: Windows 10 or later.
---

# PosCxOpen function



## -description
<p>PosCxOpen is called to create an open PosCx library instance. This function initializes all resources it needs to manage a single open instance. It should be called from the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-device-file-create.md">EVT_WDF_DEVICE_FILE_CREATE</a>   callback.</p>


## -syntax

````
NTSTATUS PosCxOpen(
  _In_ WDFDEVICE     device,
  _In_ WDFFILEOBJECT fileObject,
  _In_ ULONG         deviceInterfaceTag
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>fileObject</i> [in]

<dd>
<p>A handle to a framework file object that identifies the caller associated with the open instance.</p>
</dd>

### -param <i>deviceInterfaceTag</i> [in]

<dd>
<p>An identifier used to specify the caller's device interface in a multi-function device.  For a single-interface device, this value should be 0.</p>
</dd>
</dl>

## -returns
<p>An appropriate NTSTATUS error code that indicates the open instance completion status.</p>

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