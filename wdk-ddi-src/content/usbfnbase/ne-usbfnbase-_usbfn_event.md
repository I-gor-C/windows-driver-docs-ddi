---
UID : NE:usbfnbase._USBFN_EVENT
title : "_USBFN_EVENT"
author : windows-driver-content
description : Defines notifications sent to class drivers.
old-location : buses\usbfn_event.htm
old-project : usbref
ms.assetid : 4A1A4E49-6452-4291-8CD4-FA390C1F167E
ms.author : windowsdriverdev
ms.date : 1/4/2018
ms.keywords : usbfnbase/UsbfnEventAttach, UsbfnEventAttach, UsbfnEventUnConfigured, *PUSBFN_EVENT, UsbfnEventMinimum, UsbfnEventDetach, usbfnbase/UsbfnEventConfigured, usbfnbase/UsbfnEventMinimum, usbfnbase/USBFN_EVENT, usbfnbase/UsbfnEventBusTearDown, usbfnbase/UsbfnEventSuspend, UsbfnEventResume, UsbfnEventMaximum, USBFN_EVENT enumeration [Buses], usbfnbase/UsbfnEventUnConfigured, UsbfnEventReset, buses.usbfn_event, USBFN_EVENT, usbfnbase/UsbfnEventMaximum, UsbfnEventConfigured, UsbfnEventBusTearDown, usbfnbase/UsbfnEventSetInterface, usbfnbase/UsbfnEventSetupPacket, usbfnbase/UsbfnEventReset, _USBFN_EVENT, UsbfnEventPortType, UsbfnEventSetupPacket, usbfnbase/UsbfnEventPortType, usbfnbase/UsbfnEventDetach, UsbfnEventSuspend, usbfnbase/UsbfnEventResume, UsbfnEventSetInterface
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : enum
req.header : usbfnbase.h
req.include-header : 
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : PASSIVE_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : USBFN_EVENT, *PUSBFN_EVENT
req.product : Windows 10 or later.
---

# _USBFN_EVENT Enumeration
Defines notifications sent to class drivers.

## Syntax
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

## Constants

<table>

<tr>
<td>UsbfnEventAttach</td>
<td>VBUS is powered. No action is required.</td>
</tr>

<tr>
<td>UsbfnEventBusTearDown</td>
<td>Deprecated.</td>
</tr>

<tr>
<td>UsbfnEventConfigured</td>
<td>USBFN has received a SET_CONFIGURATION setup packet. Transfer
    requests from class drivers are now permitted.
    The <b>ConfigurationValue</b> of the notification is set to <b>wValue.W</b>.</td>
</tr>

<tr>
<td>UsbfnEventDetach</td>
<td>VBUS is no longer powered.
    If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.
    The <b>BusSpeed</b> field of the notification is set appropriately.</td>
</tr>

<tr>
<td>UsbfnEventMaximum</td>
<td>The minimum value in this enumeration.</td>
</tr>

<tr>
<td>UsbfnEventMinimum</td>
<td>The minimum value in this enumeration.</td>
</tr>

<tr>
<td>UsbfnEventPortType</td>
<td>Deprecated.</td>
</tr>

<tr>
<td>UsbfnEventReset</td>
<td>USBFN has completed a USB Reset. If previously configured, class drivers should reset their state. Transfer requests will be cancelled.</td>
</tr>

<tr>
<td>UsbfnEventResume</td>
<td>USBFN has resumed from suspend to the previous state.</td>
</tr>

<tr>
<td>UsbfnEventSetInterface</td>
<td>USBFN has received a SET_INTERFACE setup packet.  On receiving this
    notification the class driver should query for the new endpoint set
    for the interface.</td>
</tr>

<tr>
<td>UsbfnEventSetupPacket</td>
<td>USBFN has received a setup packet with
    <b>bmRequestType.Type</b> set to BMREQUEST_CLASS and
    <b>bmRequestType.Recipient</b> set to BMREQUEST_TO_INTERFACE.
    USBFN forwarded the setup packet to the class driver
    specified in <b>wIndex.LowByte</b>.

 The setup packet is available in the <b>SetupPacket</b> field of the
    event. If the control transfer does not require a data stage,
     class drivers should respond with
    <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_control_status_handshake_out.md">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</a>.
    If a data stage is required, class drivers should respond with
    one or more <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_transfer_in.md">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a> or <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_transfer_out.md">IOCTL_INTERNAL_USBFN_TRANSFER_OUT</a>, followed by
    <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_control_status_handshake_in.md">IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_IN</a> or <b>IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT</b> in the opposite
    direction.</td>
</tr>

<tr>
<td>UsbfnEventSuspend</td>
<td>There have been no SOF packets on the bus for 3ms.
    If a class driver wants to issue a remote wake up,
     the driver must use <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_signal_remote_wakeup.md">IOCTL_INTERNAL_USBFN_SIGNAL_REMOTE_WAKEUP</a> or <a href="..\usbfnioctl\ni-usbfnioctl-ioctl_internal_usbfn_transfer_in.md">IOCTL_INTERNAL_USBFN_TRANSFER_IN</a>.</td>
</tr>

<tr>
<td>UsbfnEventUnConfigured</td>
<td>USBFN has received a SET_CONFIGURATION setup packet with
    <b>wValue.W</b> set to 0. If previously configured, class drivers should
    reset their state. Transfer requests will be cancelled.</td>
</tr>
</table>


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | usbfnbase.h |