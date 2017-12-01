---
UID: NE.usbfnbase._USBFN_PORT_TYPE
title: USBFN_PORT_TYPE
author: windows-driver-content
description: Defines the possible port types that can be returned by the client driver during port detection.
old-location: buses\usbfn_port_type.htm
old-project: usbref
ms.assetid: D45F8CD0-CB54-4DE4-BD6B-FF6A35FCBFEC
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
req.alt-api: USBFN_PORT_TYPE
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

# USBFN_PORT_TYPE enumeration



## -description
<p>Defines the possible port types that can be returned by the client driver during port detection.</p>


## -syntax

````
typedef enum _USBFN_PORT_TYPE { 
  UsbfnUnknownPort                       = 0,
  UsbfnStandardDownstreamPort,
  UsbfnChargingDownstreamPort,
  UsbfnDedicatedChargingPort,
  UsbfnInvalidDedicatedChargingPort,
  UsbfnProprietaryDedicatedChargingPort,
  UsbfnPortTypeMaximum
} USBFN_PORT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UsbfnUnknownPort"></a><a id="usbfnunknownport"></a><a id="USBFNUNKNOWNPORT"></a><b>UsbfnUnknownPort</b>

<dd>
<p>Port detection was unable to determine the port type.</p>
</dd>

### -field <a id="UsbfnStandardDownstreamPort"></a><a id="usbfnstandarddownstreamport"></a><a id="USBFNSTANDARDDOWNSTREAMPORT"></a><b>UsbfnStandardDownstreamPort</b>

<dd>
<p>The upstream port has been detected as a standard downstream port (SDP) (as defined in the Battery Charging Specification, revision 1.2).</p>
</dd>

### -field <a id="UsbfnChargingDownstreamPort"></a><a id="usbfnchargingdownstreamport"></a><a id="USBFNCHARGINGDOWNSTREAMPORT"></a><b>UsbfnChargingDownstreamPort</b>

<dd>
<p>The upstream port has been detected as a charging downstream port (CDP), as defined in the Battery Charging Specification, revision 1.2.</p>
</dd>

### -field <a id="UsbfnDedicatedChargingPort"></a><a id="usbfndedicatedchargingport"></a><a id="USBFNDEDICATEDCHARGINGPORT"></a><b>UsbfnDedicatedChargingPort</b>

<dd>
<p>The upstream port has been detected as a dedicated charging port (DCP) (as defined in the Battery Charging Specification, revision 1.2).</p>
</dd>

### -field <a id="UsbfnInvalidDedicatedChargingPort"></a><a id="usbfninvaliddedicatedchargingport"></a><a id="USBFNINVALIDDEDICATEDCHARGINGPORT"></a><b>UsbfnInvalidDedicatedChargingPort</b>

<dd>
<p>The upstream port has been detected as a dedicated charging port that does not comply with the Battery Charging Specification, revision 1.2.</p>
</dd>

### -field <a id="UsbfnProprietaryDedicatedChargingPort"></a><a id="usbfnproprietarydedicatedchargingport"></a><a id="USBFNPROPRIETARYDEDICATEDCHARGINGPORT"></a><b>UsbfnProprietaryDedicatedChargingPort</b>

<dd>
<p>A proprietary charger was attached.</p>
</dd>

### -field <a id="UsbfnPortTypeMaximum"></a><a id="usbfnporttypemaximum"></a><a id="USBFNPORTTYPEMAXIMUM"></a><b>UsbfnPortTypeMaximum</b>

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

## -see-also
<dl>
<dt>
<a href="buses.usbfn_get_attach_action">USBFN_GET_ATTACH_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_PORT_TYPE enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
