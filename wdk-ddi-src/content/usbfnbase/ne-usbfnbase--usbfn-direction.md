---
UID: NE.usbfnbase._USBFN_DIRECTION
title: USBFN_DIRECTION
author: windows-driver-content
description: Defines the USB data transfer direction types.
old-location: buses\usbfn_direction.htm
old-project: usbref
ms.assetid: C6E1FA5A-993C-4212-9428-0B759C09F5DE
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBFN_ON_ATTACH, USBFN_ON_ATTACH, *PUSBFN_ON_ATTACH
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_DIRECTION
req.alt-loc: usbfnbase.h
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
req.iface: 
req.product: Windows 10 or later.
---

# USBFN_DIRECTION enumeration



## -description
<p>Defines the USB data transfer direction types.</p>


## -syntax

````
typedef enum _USBFN_DIRECTION { 
  UsbfnDirectionMinimum  = 0x0,
  UsbfnDirectionIn,
  UsbfnDirectionOut,
  UsbfnDirectionTx       = UsbfnDirectionIn,
  UsbfnDirectionRx       = UsbfnDirectionOut,
  UsbfnDirectionMaximum
} USBFN_DIRECTION;
````


## -enum-fields
<dl>

### -field UsbfnDirectionMinimum

<dd>
<p>The minimum value in this enumeration.</p>
</dd>

### -field UsbfnDirectionIn

<dd>
<p>The transfer is to the host from an endpoint.</p>
</dd>

### -field UsbfnDirectionOut

<dd>
<p>The transfer is from the host to the endpoint.</p>
</dd>

### -field UsbfnDirectionTx

<dd>
<p>The bus transfer to the host from the device. </p>
</dd>

### -field UsbfnDirectionRx

<dd>
<p>The bus transfer is from the host to the device.</p>
</dd>

### -field UsbfnDirectionMaximum

<dd>
<p>The maximum value in this enumeration.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbfnbase.h</dt>
</dl>
</td>
</tr>
</table>