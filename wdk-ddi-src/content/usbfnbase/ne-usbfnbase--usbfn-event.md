---
UID: NE.usbfnbase._USBFN_EVENT
title: USBFN_EVENT
author: windows-driver-content
description: Defines notifications sent to class drivers.
old-location: buses\usbfn_event.htm
old-project: usbref
ms.assetid: 4A1A4E49-6452-4291-8CD4-FA390C1F167E
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
req.alt-api: USBFN_EVENT
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

# USBFN_EVENT enumeration



## -description
<p>Defines notifications sent to class drivers.</p>


## -syntax

````
typedef enum _USBFN_EVENT { 
  UsbfnEventMinimum       = 0x0,
  UsbfnEventAttach,
  UsbfnEventReset,
  UsbfnEventDetach,
  UsbfnEventSuspend,
  UsbfnEventResume,
  UsbfnEventSetupPacket,
  UsbfnEventConfigured,
  UsbfnEventUnConfigured,
  UsbfnEventPortType,
  UsbfnEventBusTearDown,
  UsbfnEventSetInterface,
  UsbfnEventMaximum
} USBFN_EVENT;
````


## -enum-fields
<dl>

### -field UsbfnEventMinimum

<dd>
<p>The minimum value in this enumeration.</p>
</dd>

### -field UsbfnEventAttach

<dd>
<p>VBUS is powered. No action is required.</p>
</dd>

### -field UsbfnEventReset

<dd>
<p>USBFN has completed a USB Reset. If previously configured, class drivers should reset their state. Transfer requests will be cancelled.</p>
</dd>

### -field UsbfnEventDetach

<dd>
<p>    VBUS is no longer powered.
    If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.
    The <b>BusSpeed</b> field of the notification is set appropriately.</p>
</dd>

### -field UsbfnEventSuspend

<dd>
<p>    There have been no SOF packets on the bus for 3ms.
    If a class driver wants to issue a remote wake up,
     the driver must use <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-signal-remote-wakeup.md">IOCTL_INTERNAL_USBFN_SIGNAL_REMOTE_WAKEUP</a> or <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-in.md">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a>.</p>
</dd>

### -field UsbfnEventResume

<dd>
<p>USBFN has resumed from suspend to the previous state.</p>
</dd>

### -field UsbfnEventSetupPacket

<dd>
<p>    USBFN has received a setup packet with
    <b>bmRequestType.Type</b> set to BMREQUEST_CLASS and
    <b>bmRequestType.Recipient</b> set to BMREQUEST_TO_INTERFACE.
    USBFN forwarded the setup packet to the class driver
    specified in <b>wIndex.LowByte</b>.</p>
<p> The setup packet is available in the <b>SetupPacket</b> field of the
    event. If the control transfer does not require a data stage,
     class drivers should respond with
    <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-out.md">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</a>.
    If a data stage is required, class drivers should respond with
    one or more <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-in.md">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a> or <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-out.md">IOCTL_INTERNAL_USBFN_TRANSFER_OUT</a>, followed by
    <a href="..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-in.md">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_IN</a> or <b>IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</b> in the opposite
    direction.</p>
</dd>

### -field UsbfnEventConfigured

<dd>
<p>    USBFN has received a SET_CONFIGURATION setup packet. Transfer
    requests from class drivers are now permitted.
    The <b>ConfigurationValue</b> of the notification is set to <b>wValue.W</b>.</p>
</dd>

### -field UsbfnEventUnConfigured

<dd>
<p>    USBFN has received a SET_CONFIGURATION setup packet with
    <b>wValue.W</b> set to 0. If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.</p>
</dd>

### -field UsbfnEventPortType

<dd>
<p>Deprecated.</p>
</dd>

### -field UsbfnEventBusTearDown

<dd>
<p>Deprecated.</p>
</dd>

### -field UsbfnEventSetInterface

<dd>
<p>USBFN has received a SET_INTERFACE setup packet.  On receiving this
    notification the class driver should query for the new endpoint set
    for the interface.</p>
</dd>

### -field UsbfnEventMaximum

<dd>
<p>The minimum value in this enumeration.</p>
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