---
UID: NE.usbfnattach._USBFN_ATTACH_ACTION
title: USBFN_ATTACH_ACTION
author: windows-driver-content
description: Defines the actions that the Universal Serial Bus (USB) function stack takes when a device is attached to a USB port.
old-location: buses\usbfn_attach_action.htm
old-project: usbref
ms.assetid: 4470EBAB-6B1F-43D3-B036-F0DD07BC8321
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: USBD_INTERFACE_LIST_ENTRY, USBD_INTERFACE_LIST_ENTRY, *PUSBD_INTERFACE_LIST_ENTRY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: usbfnattach.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: USBFN_ATTACH_ACTION
req.alt-loc: usbfnattach.h
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

# USBFN_ATTACH_ACTION enumeration



## -description
<p>Defines the actions that the Universal Serial Bus (USB) function stack takes when a device is attached to a USB port.</p>


## -syntax

````
typedef enum _USBFN_ATTACH_ACTION { 
  UsbfnPortDetected              = 0,
  UsbfnPortDetectedNoCad,
  UsbfnProceedWithAttach,
  UsbfnIgnoreAttach,
  UsbfnDetectProprietaryCharger
} USBFN_ATTACH_ACTION;
````


## -enum-fields
<dl>

### -field <a id="UsbfnPortDetected"></a><a id="usbfnportdetected"></a><a id="USBFNPORTDETECTED"></a><b>UsbfnPortDetected</b>

<dd>
<p>The USB function stack uses the returned port type to determine charging current and notify the Charging Aggregation Driver (CAD) of the power source change.  If the detected port type is <b>UsbFnStandardDownstreamPort</b> or <b>UsbfnChargingDownstreamPort</b>, the USB function stack will attempt to connect to the host (see <a href="https://msdn.microsoft.com/library/windows/hardware/mt188004">USBFN_PORT_TYPE</a> for more information).</p>
</dd>

### -field <a id="UsbfnPortDetectedNoCad"></a><a id="usbfnportdetectednocad"></a><a id="USBFNPORTDETECTEDNOCAD"></a><b>UsbfnPortDetectedNoCad</b>

<dd>
<p>The USB function stack does not notify the CAD of the power source change.  If the detected port type is <b>UsbFnStandardDownstreamPort</b> or <b>UsbfnChargingDownstreamPort</b>, the USB function stack attempts to connect to the host (see <a href="https://msdn.microsoft.com/library/windows/hardware/mt188004">USBFN_PORT_TYPE</a> for more information).</p>
</dd>

### -field <a id="UsbfnProceedWithAttach"></a><a id="usbfnproceedwithattach"></a><a id="USBFNPROCEEDWITHATTACH"></a><b>UsbfnProceedWithAttach</b>

<dd>
<p>The USB function stack continues with the legacy software-based detection that exists in the client drivers, and issues the CAD notifications about power source notifications.</p>
</dd>

### -field <a id="UsbfnIgnoreAttach"></a><a id="usbfnignoreattach"></a><a id="USBFNIGNOREATTACH"></a><b>UsbfnIgnoreAttach</b>

<dd>
<p>The USB function stack discontinues further port detection operations and does not notify CAD of a power source update.</p>
</dd>

### -field <a id="UsbfnDetectProprietaryCharger"></a><a id="usbfndetectproprietarycharger"></a><a id="USBFNDETECTPROPRIETARYCHARGER"></a><b>UsbfnDetectProprietaryCharger</b>

<dd>
<p>The USB function stack calls the <a href="https://msdn.microsoft.com/library/windows/hardware/mt187981">UFX_PROPRIETARY_CHARGER_DETECT</a> event callback function implemented by the USB lower filter driver, to perform proprietary charger detection.</p>
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
<dt>Usbfnattach.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt187995">USBFN_GET_ATTACH_ACTION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [usbref\buses]:%20USBFN_ATTACH_ACTION enumeration%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
