---
UID: NF.wdfusb.WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR
title: WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function
author: windows-driver-content
description: The WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a vendor-specific USB control transfer.
old-location: wdf\wdf_usb_control_setup_packet_init_vendor.htm
old-project: wdf
ms.assetid: 58774dcf-f48c-4d39-acbe-fe09b4c52d81
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfusb.h
req.include-header: Wdfusb.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR
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
req.irql: 
req.product: Windows 10 or later.
---

# WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]

The <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</b> function initializes a <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure for a vendor-specific USB control transfer.



## -syntax

````
VOID WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR(
  _Out_ PWDF_USB_CONTROL_SETUP_PACKET Packet,
  _In_  WDF_USB_BMREQUEST_DIRECTION   Direction,
  _In_  WDF_USB_BMREQUEST_RECIPIENT   Recipient,
  _In_  BYTE                          Request,
  _In_  USHORT                        Value,
  _In_  USHORT                        Index
);
````


## -parameters

### -param Packet [out]

A pointer to a <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.


### -param Direction [in]

A <a href="wdf.wdf_usb_bmrequest_direction">WDF_USB_BMREQUEST_DIRECTION</a>-typed value that is stored in the <b>Packet.bm.Request.Dir</b> member of the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure. 


### -param Recipient [in]

A <a href="wdf.wdf_usb_bmrequest_recipient">WDF_USB_BMREQUEST_RECIPIENT</a>-typed value that is stored in the <b>Packet.bm.Request.Recipient</b> member of the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure. 


### -param Request [in]

A request type constant that is stored in the <b>Packet.bRequest</b> member of the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.


### -param Value [in]

A request-specific value that is stored in the <b>Packet.wValue.Value</b> member of the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.


### -param Index [in]

A request-specific index value that is stored in the <b>Packet.wIndex.Value</b> member of the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.


## -returns
None


## -remarks
The <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</b> function does the following:

Zeros the <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.

Sets the <b>Packet.bm.Request.Type</b> member to <b>BmRequestVendor</b>.

Sets other structure members by using the <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</b> function's input arguments.

To initialize a <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure, the driver should call one of the following functions:


<a href="wdf.wdf_usb_control_setup_packet_init">WDF_USB_CONTROL_SETUP_PACKET_INIT</a>



<a href="wdf.wdf_usb_control_setup_packet_init_class">WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS</a>



<a href="wdf.wdf_usb_control_setup_packet_init_feature">WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</a>



<a href="wdf.wdf_usb_control_setup_packet_init_get_status">WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS</a>


<b>WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</b>

The following code example initializes a <a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a> structure.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Minimum KMDF version

</th>
<td width="70%">
1.0

</td>
</tr>
<tr>
<th width="30%">
Minimum UMDF version

</th>
<td width="70%">
2.0

</td>
</tr>
<tr>
<th width="30%">
Header

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
<a href="wdf.wdf_usb_bmrequest_direction">WDF_USB_BMREQUEST_DIRECTION</a>
</dt>
<dt>
<a href="wdf.wdf_usb_bmrequest_recipient">WDF_USB_BMREQUEST_RECIPIENT</a>
</dt>
<dt>
<a href="wdf.wdf_usb_control_setup_packet">WDF_USB_CONTROL_SETUP_PACKET</a>
</dt>
<dt>
<a href="wdf.wdf_usb_control_setup_packet_init">WDF_USB_CONTROL_SETUP_PACKET_INIT</a>
</dt>
<dt>
<a href="wdf.wdf_usb_control_setup_packet_init_class">WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS</a>
</dt>
<dt>
<a href="wdf.wdf_usb_control_setup_packet_init_feature">WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</a>
</dt>
<dt>
<a href="wdf.wdf_usb_control_setup_packet_init_get_status">WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR function%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

