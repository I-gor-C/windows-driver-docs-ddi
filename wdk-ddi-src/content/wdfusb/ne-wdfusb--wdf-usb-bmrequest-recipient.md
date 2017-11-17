---
UID: NE.wdfusb._WDF_USB_BMREQUEST_RECIPIENT
title: WDF_USB_BMREQUEST_RECIPIENT
author: windows-driver-content
description: The WDF_USB_BMREQUEST_RECIPIENT enumeration identifies the data transfer recipient for a USB control transfer.
old-location: wdf\wdf_usb_bmrequest_recipient.htm
ms.assetid: 0749d03d-8174-4f6e-816e-4689594c0c84
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: wdf
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_BMREQUEST_RECIPIENT
req.alt-loc: wdfusb.h
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
ms.keywords: WDF_TIMER_CONFIG, WDF_TIMER_CONFIG, *PWDF_TIMER_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_BMREQUEST_RECIPIENT enumeration



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_BMREQUEST_RECIPIENT</b> enumeration identifies the data transfer recipient for a USB control transfer. </p>


## -syntax

````
typedef enum _WDF_USB_BMREQUEST_RECIPIENT { 
  BmRequestToDevice     = BMREQUEST_TO_DEVICE,
  BmRequestToInterface  = BMREQUEST_TO_INTERFACE,
  BmRequestToEndpoint   = BMREQUEST_TO_ENDPOINT,
  BmRequestToOther      = BMREQUEST_TO_OTHER
} WDF_USB_BMREQUEST_RECIPIENT;
````


## -enum-fields
<dl>

### -field <a id="BmRequestToDevice"></a><a id="bmrequesttodevice"></a><a id="BMREQUESTTODEVICE"></a><b>BmRequestToDevice</b>

<dd>
<p>The data transfer recipient is a device.</p>
</dd>

### -field <a id="BmRequestToInterface"></a><a id="bmrequesttointerface"></a><a id="BMREQUESTTOINTERFACE"></a><b>BmRequestToInterface</b>

<dd>
<p>The data transfer recipient is a device interface.</p>
</dd>

### -field <a id="BmRequestToEndpoint"></a><a id="bmrequesttoendpoint"></a><a id="BMREQUESTTOENDPOINT"></a><b>BmRequestToEndpoint</b>

<dd>
<p>The data transfer recipient is a pipe endpoint.</p>
</dd>

### -field <a id="BmRequestToOther"></a><a id="bmrequesttoother"></a><a id="BMREQUESTTOOTHER"></a><b>BmRequestToOther</b>

<dd>
<p>The data transfer recipient is not a device, interface, or endpoint.</p>
</dd>
</dl>

## -remarks
<p>The<b>WDF_USB_BMREQUEST_RECIPIENT</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552568">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>

<p>For more information about the data transfer recipient for a USB control transfer, see the USB specification.</p>

<p>The<b>WDF_USB_BMREQUEST_RECIPIENT</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552568">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>

<p>For more information about the data transfer recipient for a USB control transfer, see the USB specification.</p>

<p>The<b>WDF_USB_BMREQUEST_RECIPIENT</b> enumeration is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/ff552568">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>

<p>For more information about the data transfer recipient for a USB control transfer, see the USB specification.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfusb.h (include Wdfusb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552568">WDF_USB_CONTROL_SETUP_PACKET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_BMREQUEST_RECIPIENT enumeration%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
