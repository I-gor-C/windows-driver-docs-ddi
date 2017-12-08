---
UID: NE.usbfnbase._USBFN_BUS_SPEED
title: USBFN_BUS_SPEED
author: windows-driver-content
description: The USBFN_BUS_SPEED enumeration defines possible bus speeds.
old-location: buses\usbfn_bus_speed.htm
old-project: usbref
ms.assetid: B97E27A1-0D95-41AA-8FF6-A92F70FBAD28
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
req.alt-api: USBFN_BUS_SPEED
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

# USBFN_BUS_SPEED enumeration



## -description
<p>The <b>USBFN_BUS_SPEED</b> enumeration defines possible bus speeds.</p>


## -syntax

````
typedef enum _USBFN_BUS_SPEED { 
  UsbfnBusSpeedLow,
  UsbfnBusSpeedFull,
  UsbfnBusSpeedHigh,
  UsbfnBusSpeedSuper,
  UsbfnBusSpeedMaximum
} USBFN_BUS_SPEED;
````


## -enum-fields
<dl>

### -field UsbfnBusSpeedLow

<dd>
<p>A low bandwidth bus speed of 1.5 Mbit per second.</p>
</dd>

### -field UsbfnBusSpeedFull

<dd>
<p>A full bandwidth bus speed of 12 MBit per second.</p>
</dd>

### -field UsbfnBusSpeedHigh

<dd>
<p>A high bus speed of 480 Mbit per second.</p>
</dd>

### -field UsbfnBusSpeedSuper

<dd>
<p>A SuperSpeed mode bus speed of 5 Gbit per second.</p>
</dd>

### -field UsbfnBusSpeedMaximum

<dd>
<p>The maximum value of the enumeration.</p>
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