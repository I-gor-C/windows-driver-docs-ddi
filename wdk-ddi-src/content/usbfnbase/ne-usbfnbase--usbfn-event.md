---
UID: NE.usbfnbase._USBFN_EVENT
title: USBFN_EVENT
author: windows-driver-content
description: Defines notifications sent to class drivers.
old-location: buses\usbfn_event.htm
ms.assetid: 4A1A4E49-6452-4291-8CD4-FA390C1F167E
ms.author: windowsdriverdev
ms.date: 11/3/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: usbref
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
ms.keywords: USBFN_ON_ATTACH, USBFN_ON_ATTACH, *PUSBFN_ON_ATTACH
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

### -field <a id="UsbfnEventMinimum"></a><a id="usbfneventminimum"></a><a id="USBFNEVENTMINIMUM"></a><b>UsbfnEventMinimum</b>

<dd>
<p>The minimum value in this enumeration.</p>
</dd>

### -field <a id="UsbfnEventAttach"></a><a id="usbfneventattach"></a><a id="USBFNEVENTATTACH"></a><b>UsbfnEventAttach</b>

<dd>
<p>VBUS is powered. No action is required.</p>
</dd>

### -field <a id="UsbfnEventReset"></a><a id="usbfneventreset"></a><a id="USBFNEVENTRESET"></a><b>UsbfnEventReset</b>

<dd>
<p>USBFN has completed a USB Reset. If previously configured, class drivers should reset their state. Transfer requests will be cancelled.</p>
</dd>

### -field <a id="UsbfnEventDetach"></a><a id="usbfneventdetach"></a><a id="USBFNEVENTDETACH"></a><b>UsbfnEventDetach</b>

<dd>
<p>    VBUS is no longer powered.
    If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.
    The <b>BusSpeed</b> field of the notification is set appropriately.</p>
</dd>

### -field <a id="UsbfnEventSuspend"></a><a id="usbfneventsuspend"></a><a id="USBFNEVENTSUSPEND"></a><b>UsbfnEventSuspend</b>

<dd>
<p>    There have been no SOF packets on the bus for 3ms.
    If a class driver wants to issue a remote wake up,
     the driver must use <a href="https://msdn.microsoft.com/library/windows/hardware/mt187906">IOCTL_INTERNAL_USBFN_SIGNAL_REMOTE_WAKEUP</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/mt188024">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a>.</p>
</dd>

### -field <a id="UsbfnEventResume"></a><a id="usbfneventresume"></a><a id="USBFNEVENTRESUME"></a><b>UsbfnEventResume</b>

<dd>
<p>USBFN has resumed from suspend to the previous state.</p>
</dd>

### -field <a id="UsbfnEventSetupPacket"></a><a id="usbfneventsetuppacket"></a><a id="USBFNEVENTSETUPPACKET"></a><b>UsbfnEventSetupPacket</b>

<dd>
<p>    USBFN has received a setup packet with
    <b>bmRequestType.Type</b> set to BMREQUEST_CLASS and
    <b>bmRequestType.Recipient</b> set to BMREQUEST_TO_INTERFACE.
    USBFN forwarded the setup packet to the class driver
    specified in <b>wIndex.LowByte</b>.</p>
<p> The setup packet is available in the <b>SetupPacket</b> field of the
    event. If the control transfer does not require a data stage,
     class drivers should respond with
    <a href="https://msdn.microsoft.com/library/windows/hardware/mt187893">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</a>.
    If a data stage is required, class drivers should respond with
    one or more <a href="https://msdn.microsoft.com/library/windows/hardware/mt188024">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/mt187905">IOCTL_INTERNAL_USBFN_TRANSFER_OUT</a>, followed by
    <a href="https://msdn.microsoft.com/library/windows/hardware/mt188023">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_IN</a> or <b>IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</b> in the opposite
    direction.</p>
</dd>

### -field <a id="UsbfnEventConfigured"></a><a id="usbfneventconfigured"></a><a id="USBFNEVENTCONFIGURED"></a><b>UsbfnEventConfigured</b>

<dd>
<p>    USBFN has received a SET_CONFIGURATION setup packet. Transfer
    requests from class drivers are now permitted.
    The <b>ConfigurationValue</b> of the notification is set to <b>wValue.W</b>.</p>
</dd>

### -field <a id="UsbfnEventUnConfigured"></a><a id="usbfneventunconfigured"></a><a id="USBFNEVENTUNCONFIGURED"></a><b>UsbfnEventUnConfigured</b>

<dd>
<p>    USBFN has received a SET_CONFIGURATION setup packet with
    <b>wValue.W</b> set to 0. If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.</p>
</dd>

### -field <a id="UsbfnEventPortType"></a><a id="usbfneventporttype"></a><a id="USBFNEVENTPORTTYPE"></a><b>UsbfnEventPortType</b>

<dd>
<p>Deprecated.</p>
</dd>

### -field <a id="UsbfnEventBusTearDown"></a><a id="usbfneventbusteardown"></a><a id="USBFNEVENTBUSTEARDOWN"></a><b>UsbfnEventBusTearDown</b>

<dd>
<p>Deprecated.</p>
</dd>

### -field <a id="UsbfnEventSetInterface"></a><a id="usbfneventsetinterface"></a><a id="USBFNEVENTSETINTERFACE"></a><b>UsbfnEventSetInterface</b>

<dd>
<p>USBFN has received a SET_INTERFACE setup packet.  On receiving this
    notification the class driver should query for the new endpoint set
    for the interface.</p>
</dd>

### -field <a id="UsbfnEventMaximum"></a><a id="usbfneventmaximum"></a><a id="USBFNEVENTMAXIMUM"></a><b>UsbfnEventMaximum</b>

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