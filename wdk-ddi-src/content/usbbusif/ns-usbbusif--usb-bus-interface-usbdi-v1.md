---
UID: NS.usbbusif._USB_BUS_INTERFACE_USBDI_V1
title: USB_BUS_INTERFACE_USBDI_V1
author: windows-driver-content
description: The USB_BUS_INTERFACE_USBDI_V1 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs.
old-location: buses\usb_bus_interface_usbdi_v1.htm
old-project: usbref
ms.assetid: 9c90c182-86ac-43e5-9e77-0ea2da76e6b9
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_BUS_INTERFACE_USBDI_V1, USB_BUS_INTERFACE_USBDI_V1, *PUSB_BUS_INTERFACE_USBDI_V1
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbbusif.h
req.include-header: Usbbusif.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_BUS_INTERFACE_USBDI_V1
req.alt-loc: usbbusif.h
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

# USB_BUS_INTERFACE_USBDI_V1 structure



## -description
<p>The <b>USB_BUS_INTERFACE_USBDI_V1</b> structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. </p>


## -syntax

````
typedef struct _USB_BUS_INTERFACE_USBDI_V1 {
  USHORT                             Size;
  USHORT                             Version;
  PVOID                              BusContext;
  PINTERFACE_REFERENCE               InterfaceReference;
  PINTERFACE_DEREFERENCE             InterfaceDereference;
  PUSB_BUSIFFN_GETUSBDI_VERSION      GetUSBDIVersion;
  PUSB_BUSIFFN_QUERY_BUS_TIME        QueryBusTime;
  PUSB_BUSIFFN_SUBMIT_ISO_OUT_URB    SubmitIsoOutUrb;
  PUSB_BUSIFFN_QUERY_BUS_INFORMATION QueryBusInformation;
  PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED  IsDeviceHighSpeed;
} USB_BUS_INTERFACE_USBDI_V1, *PUSB_BUS_INTERFACE_USBDI_V1;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>Specifies the size in bytes of the buffer that holds the interface pointers. </p>
</dd>

### -field Version

<dd>
<p>Indicates, on input, the version of the interface. The values that this member can take are as follows.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>USB_BUSIF_USBDI_VERSION_0</p>
</td>
<td>
<p>Version 0 of the interface.</p>
</td>
</tr>
<tr>
<td>
<p>USB_BUSIF_USBDI_VERSION_1</p>
</td>
<td>
<p>Version 1 of the interface.</p>
</td>
</tr>
<tr>
<td>
<p>USB_BUSIF_USBDI_VERSION_2</p>
</td>
<td>
<p>Version 2 of the interface.</p>
</td>
</tr>
<tr>
<td>
<p>USB_BUSIF_USBDI_VERSION_3</p>
</td>
<td>
<p>Version 3 of the interface.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field BusContext

<dd>
<p>Contains information that describes the USB bus and the USB bus driver that exposes this interface. This is an opaque entity that the caller must pass to the interface routines. </p>
</dd>

### -field InterfaceReference

<dd>
<p>Pointer to a routine that increments the number of references to this interface. For more information about this routine, see <a href="kernel.interfacereference">InterfaceReference</a>. </p>
</dd>

### -field InterfaceDereference

<dd>
<p>Pointer to a routine that decrements the number of references to this interface. For more information about this routine, see <a href="kernel.interfacedereference">InterfaceDereference</a>. </p>
</dd>

### -field GetUSBDIVersion

<dd>
<p>Pointer to a routine that returns the USB interface version number, the version number of USB specification that defines the interface, along with host controller capabilities information. This routine returns the highest USBDI interface version supported by the port driver. For more information about this routine, see <a href="buses.getusbdiversion">GetUSBDIVersion</a>. </p>
</dd>

### -field QueryBusTime

<dd>
<p>Pointer to a routine that returns the current 32-bit USB frame number. This routine replaces the <b>USBD_QueryBusTime</b> function provided by usbd.sys. For more information about this routine, see <a href="buses.querybustime">QueryBusTime</a>. </p>
</dd>

### -field SubmitIsoOutUrb

<dd>
<p>Reserved. Do not use.</p>
</dd>

### -field QueryBusInformation

<dd>
<p>Pointer to a routine that retrieves information about the bus. The information that is returned depends on the value of the <b>Level </b>member. If <b>Level</b> is 0, this routine returns bus bandwidth information. If <b>Level</b> is 1, it returns bus bandwidth information and the host controller's symbolic name. This routine replaces the <b>USBD_QueryBusInformation</b> function provided by usbd.sys. For more information about this routine, see <a href="buses.querybusinformation">QueryBusInformation</a>. </p>
</dd>

### -field IsDeviceHighSpeed

<dd>
<p>Pointer to a routine that determines whether the USB device is operating at high speed. This routine returns <b>TRUE</b> if the USB device is operating at high speed (USB 2.0-compliant device). Otherwise this routine returns <b>FALSE</b>. For more information about this routine, see <a href="buses.isdevicehighspeed">IsDeviceHighSpeed</a>. </p>
</dd>
</dl>

## -remarks
<p>The <b>IsDeviceHighSpeed</b> member does not indicate whether a device is capable of high speed operation, but rather whether it is in fact operating at high speed. </p>

<p>The routines in this structure must be callable at IRQL &gt;= DISPATCH_LEVEL. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbbusif.h (include Usbbusif.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="buses.usb_interfaces">Bus Driver Interface Routines for USB Client Drivers</a>
</dt>
<dt>
<a href="buses.usb_structures_and_enumerations">USB Structures</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_BUS_INTERFACE_USBDI_V1 structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
