---
UID: NE.usbfnbase._USBFN_DEVICE_STATE
title: USBFN_DEVICE_STATE
author: windows-driver-content
description: Defines the Universal Serial Bus (USB) device states for the device/controller. These states correspond to the USB device states as defined in section 9.1 of the USB 2.0 Specification.
old-location: buses\usbfn_device_state.htm
old-project: usbref
ms.assetid: B367D0F7-5026-4C88-B88A-69068F76B675
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
req.alt-api: USBFN_DEVICE_STATE
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

# USBFN_DEVICE_STATE enumeration



## -description
<p>Defines the Universal Serial Bus (USB) device states for the device/controller.  These states correspond to the USB device states as defined in section 9.1 of the USB 2.0 Specification.</p>


## -syntax

````
typedef enum _USBFN_DEVICE_STATE { 
  UsbfnDeviceStateMinimum       = 0x0,
  UsbfnDeviceStateAttached,
  UsbfnDeviceStateDefault,
  UsbfnDeviceStateDetached,
  UsbfnDeviceStateAddressed,
  UsbfnDeviceStateConfigured,
  UsbfnDeviceStateSuspended,
  UsbfnDeviceStateStateMaximum
} USBFN_DEVICE_STATE;
````


## -enum-fields
<dl>

### -field UsbfnDeviceStateMinimum

<dd>
<p>The minimum value of the enumeration.</p>
</dd>

### -field UsbfnDeviceStateAttached

<dd>
<p>Device is attached to an upstream port.</p>
</dd>

### -field UsbfnDeviceStateDefault

<dd>
<p>Device is attached and connected to an upstream port but has not been reset.</p>
</dd>

### -field UsbfnDeviceStateDetached

<dd>
<p>Device is not attached to an upstream port.</p>
</dd>

### -field UsbfnDeviceStateAddressed

<dd>
<p>Device has been assigned a non-default USB address by the host.</p>
</dd>

### -field UsbfnDeviceStateConfigured

<dd>
<p>Device has been configured by the host.</p>
</dd>

### -field UsbfnDeviceStateSuspended

<dd>
<p>Device has been suspended.</p>
</dd>

### -field UsbfnDeviceStateStateMaximum

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