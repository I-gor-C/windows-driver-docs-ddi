---
UID: NS.usbioctl._USB_PORT_CONNECTOR_PROPERTIES
title: USB_PORT_CONNECTOR_PROPERTIES
author: windows-driver-content
description: The USB_PORT_CONNECTOR_PROPERTIES structure is used with the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request to retrieve information about a port on a particular SuperSpeed hub.
old-location: buses\usb_port_connector_properties.htm
old-project: usbref
ms.assetid: 93818067-A7EC-4796-B80F-75ADD6315ADF
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USB_PORT_CONNECTOR_PROPERTIES, USB_PORT_CONNECTOR_PROPERTIES, *PUSB_PORT_CONNECTOR_PROPERTIES
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: usbioctl.h
req.include-header: Usbioctl.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USB_PORT_CONNECTOR_PROPERTIES
req.alt-loc: Usbioctl.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# USB_PORT_CONNECTOR_PROPERTIES structure



## -description
<p>The <b>USB_PORT_CONNECTOR_PROPERTIES</b> structure is used with the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> I/O control request to retrieve information about a port on a particular SuperSpeed hub.</p>


## -syntax

````
typedef struct _USB_PORT_CONNECTOR_PROPERTIES {
  ULONG               ConnectionIndex;
  ULONG               ActualLength;
  USB_PORT_PROPERTIES UsbPortProperties;
  USHORT              CompanionIndex;
  USHORT              CompanionPortNumber;
  WCHAR               CompanionHubSymbolicLinkName[1];
} USB_PORT_CONNECTOR_PROPERTIES, *PUSB_PORT_CONNECTOR_PROPERTIES;
````


## -struct-fields
<dl>

### -field <b>ConnectionIndex</b>

<dd>
<p>The port number being queried in the request. <b>ConnectionIndex</b> is specified by the caller. If there are <i>n</i> ports on the SuperSpeed hub, the ports are numbered from 1 to <i>n</i>. To get the number of ports, the caller first sends an <a href="https://msdn.microsoft.com/library/windows/hardware/hh450860">IOCTL_USB_GET_HUB_INFORMATION_EX</a> I/O control request. The request retrieves the highest port number on the hub.</p>
</dd>

### -field <b>ActualLength</b>

<dd>
<p>The number of bytes required to hold the entire <b>USB_PORT_CONNECTOR_PROPERTIES</b>
    structure including the string that contains the symbolic link name of the companion hub. That string is stored in the <b>CompanionHubSymbolicLinkName</b> member. The <b>ActualLength</b> value is returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> request and used by the caller to allocate a buffer to hold the received information. For details, see <b>IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</b>. </p>
</dd>

### -field <b>UsbPortProperties</b>

<dd>
<p>The port properties. Upon completion of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> request, <b>UsbPortProperties</b> contains a bitwise <b>OR</b> of one or more flags indicating the properties and capabilities of the port. The flags are defined in <a href="https://msdn.microsoft.com/library/windows/hardware/hh406266">USB_PORT_PROPERTIES</a>.</p>
</dd>

### -field <b>CompanionIndex</b>

<dd>
<p>The index of the companion port that is associated with the port being queried (specified by <b>ConnectionIndex</b>). If there are <i>n</i> companion ports, those ports are indexed from 0 to <i>n</i>–1.</p>
<p>If a port is mapped to more than one companion port, <b>CompanionIndex</b> is incremented on multiple queries to enumerate all companion ports.</p>
<p>For SuperSpeed hubs and xHCI controllers, <b>CompanionIndex</b> is always 0. For more information, see Remarks.</p>
</dd>

### -field <b>CompanionPortNumber</b>

<dd>
<p>The port number of the companion port that is given by <b>CompanionIndex</b>. If the port being queried shares a USB connector with a port on another hub,  <b>CompanionPortNumber</b> indicates the port number of the port on the other hub. </p>
<div class="alert"><b>Note</b>  For root hub of an xHCI controller, the shared port might be on the same hub.</div>
<div> </div>
</dd>

### -field <b>CompanionHubSymbolicLinkName</b>

<dd>
<p>The Unicode string that contains the symbolic link  of the companion hub that shares the USB connector. If a companion hub exists, <b>CompanionPortNumber</b> is nonzero. Otherwise, <b>CompanionHubSymbolicLinkName [0]</b> is <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>A SuperSpeed 3.0 hub contains two independent hub implementations.  One is for USB 2.0 devices, and the hub implementation is similar to existing 2.0 hubs.  The other hub is only for SuperSpeed devices.  Because the USB 2.0 and 3.0 bus signaling are electrically independent, both of those hubs operate simultaneously.  Therefore, when a SuperSpeed hub is connected to the host, Windows enumerates the two hubs independently;  one hub is associated with a USB 2.0 port, and the other hub with a USB 3.0 port.  Each hub has its downstream and upstream ports. USB physical  connectors are shared between ports that are associated with  those two hub implementations. </p>

<p> Similarly,  an xHCI controller must be able to handle SuperSpeed, high-speed, full-speed, and low-speed devices. The USB 3.0 specification requires an xHCI controller to  contain two independent execution units each for USB 3.0 and USB 2.0 bus speeds. The USB 3.0 execution unit handles SuperSpeed traffic on the bus. The USB 2.0 execution unit must handle low, full, and high speed traffic. That requirement can be met in many ways. For instance, in one implementation, the USB 2.0 execution unit can have either a downstream USB 1.1 execution unit or a downstream USB 2.0 hub. The other execution unit handles SuperSpeed traffic on the bus. For instance, in one implementation, the xHCI controller can have a downstream USB 2.0 hub (instead of a USB 2.0 host controller) with a transaction translator to handle full-speed and low-speed traffic. That downstream hub shares connectors with the ports of the SuperSpeed root hub.</p>

<p>  In cases where USB connectors are shared, the port that is being queried through the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> I/O control request is specified by <b>ConnectionIndex</b>, and the port that shares the connector is called the <i>companion port</i>. Upon completion of the request, the <b>CompanionIndex</b>, <b>CompanionPortNumber</b>, and <b>CompanionHubSymbolicLinkName</b> members of <b>USB_PORT_CONNECTOR_PROPERTIES</b> can be used to determine the port routing in those cases.</p>

<p>If more than one companion port is associated with the port that is being queried, the application can get information about all companion ports by sending the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a> I/O control request in a loop and incrementing the <b>CompanionIndex</b> value in each iteration. When all of the ports have been enumerated and there is no  port associated with the index specified in <b>CompanionIndex</b>, the request completes successfully, <b>CompanionPortNumber</b> is set to 0, and <b>CompanionHubSymbolicLinkName</b> is NULL.</p>

<p>To get information about the operating speed of a device attached to a particular port, the application can send the <a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a> I/O control request.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Usbioctl.h (include Usbioctl.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450863">IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406265">USB_PORT_CONNECTOR_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406266">USB_PORT_PROPERTIES</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh406262">USB_HUB_INFORMATION_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh450861">IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USB_PORT_CONNECTOR_PROPERTIES structure%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
