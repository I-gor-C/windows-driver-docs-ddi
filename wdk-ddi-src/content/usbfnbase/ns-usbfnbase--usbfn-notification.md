---
UID: NS.usbfnbase._USBFN_NOTIFICATION
title: USBFN_NOTIFICATION
author: windows-driver-content
description: Describes information about a Universal Serial Bus (USB) event notification that was received by using IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION.
old-location: buses\usbfn_notification.htm
ms.assetid: 84B66823-F357-44DD-A401-79E27FA6B324
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: usbref
req.header: usbfnbase.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_NOTIFICATION
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
ms.keywords: USBFN_NOTIFICATION, USBFN_NOTIFICATION, *PUSBFN_NOTIFICATION
req.iface: 
req.product: Windows 10 or later.
---

# USBFN_NOTIFICATION structure



## -description
<p>Describes information about a Universal Serial Bus (USB)  event notification that was 
		received by using <a href="https://msdn.microsoft.com/library/windows/hardware/mt187892">IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION</a>.
		</p>


## -syntax

````
typedef struct _USBFN_NOTIFICATION {
  USBFN_EVENT Event;
  union {
    USBFN_BUS_SPEED               BusSpeed;
    USB_DEFAULT_PIPE_SETUP_PACKET SetupPacket;
    USHORT                        ConfigurationValue;
    USBFN_PORT_TYPE               PortType;
    ALTERNATE_INTERFACE           AlternateInterface;
  } u;
} USBFN_NOTIFICATION, *PUSBFN_NOTIFICATION;
````


## -struct-fields
<dl>

### -field <b>Event</b>

<dd>
<p>Bus notification indicated by a <a href="https://msdn.microsoft.com/library/windows/hardware/mt187994">USBFN_EVENT</a>-typed flag.</p>
</dd>

### -field <b>u</b>

<dd>
<dl>

### -field <b>BusSpeed</b>

<dd>
<p>The operating bus speed indicated by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187987">USBFN_BUS_SPEED</a>-typed flags.</p>
</dd>

### -field <b>SetupPacket</b>

<dd>
<p>Describes a setup packet in a  <b>USB_DEFAULT_PIPE_SETUP_PACKET</b> structure for a control transfer to or from the default endpoint as indicated by a <b>USB_DEFAULT_PIPE_SETUP_PACKET</b>-typed flag.</p>
</dd>

### -field <b>ConfigurationValue</b>

<dd>
<p>The <b>bConfigurationValue</b> field of a USB configuration descriptor.</p>
</dd>

### -field <b>PortType</b>

<dd>
<p>Possible port types supported by a function controller indicated by a <a href="https://msdn.microsoft.com/library/windows/hardware/mt188004">USBFN_PORT_TYPE</a>-typed flag.</p>
</dd>

### -field <b>AlternateInterface</b>

<dd>
<p>Alternate setting of the interface indicated by <a href="https://msdn.microsoft.com/library/windows/hardware/mt187816">ALTERNATE_INTERFACE</a>.</p>
</dd>
</dl>
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