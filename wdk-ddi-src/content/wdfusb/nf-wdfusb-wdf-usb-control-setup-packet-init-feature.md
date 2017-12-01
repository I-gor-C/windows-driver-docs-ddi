---
UID: NF.wdfusb.WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE
title: WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE
author: windows-driver-content
description: The WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE function initializes a WDF_USB_CONTROL_SETUP_PACKET structure for a USB control transfer that sets or clears a device feature.
old-location: wdf\wdf_usb_control_setup_packet_init_feature.htm
old-project: wdf
ms.assetid: ef3f7b9f-8b4b-4d47-8457-17452e3e918a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE
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
req.alt-api: WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE
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
req.iface: 
req.product: Windows 10 or later.
---

# WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE function



## -description
<p class="CCE_Message">[Applies to KMDF and UMDF]</p>
<p>The <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</b> function initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure for a USB control transfer that sets or clears a device feature.</p>


## -syntax

````
VOID WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE(
  _Out_ PWDF_USB_CONTROL_SETUP_PACKET Packet,
  _In_  WDF_USB_BMREQUEST_RECIPIENT   BmRequestRecipient,
  _In_  USHORT                        FeatureSelector,
  _In_  USHORT                        Index,
  _In_  BOOLEAN                       SetFeature
);
````


## -parameters
<dl>

### -param <i>Packet</i> [out]

<dd>
<p>A pointer to a <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>
</dd>

### -param <i>BmRequestRecipient</i> [in]

<dd>
<p>A <a href="..\wdfusb\ne-wdfusb--wdf-usb-bmrequest-recipient.md">WDF_USB_BMREQUEST_RECIPIENT</a>-typed value that is stored in the <b>Packet.bm.Request.Recipient</b> member of the <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure. </p>
</dd>

### -param <i>FeatureSelector</i> [in]

<dd>
<p>A feature-specific value that is stored in the <b>Packet.wValue.Value</b> member of the <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>
</dd>

### -param <i>Index</i> [in]

<dd>
<p>A feature-specific index value that is stored in the <b>Packet.wIndex.Value</b> member of the <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>
</dd>

### -param <i>SetFeature</i> [in]

<dd>
<p>A Boolean value that, if <b>TRUE</b>, indicates that the specified feature will be set. If <b>FALSE</b>, the specified feature will be cleared.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</b> function does the following:</p>

<p>Zeros the <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>

<p>Sets the <b>Packet.bm.Request.Type</b> member to <b>BmRequestStandard</b>.</p>

<p>Sets the <b>Packet.bm.Request.Dir</b> member to <b>BmRequestDeviceToDevice</b>.</p>

<p>Sets the <b>Packet.bRequest</b> member to either a "set feature" or a "clear feature" request value, based on the <i>SetFeature</i> argument.</p>

<p>Sets other structure members by using the <b>WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</b> function's input arguments.</p>

<p>To initialize a <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure, the driver should call one of the following functions:</p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init.md">WDF_USB_CONTROL_SETUP_PACKET_INIT</a>
</p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-class.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS</a>
</p>

<p><b>WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE</b></p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-get-status.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS</a>
</p>

<p>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-vendor.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</a>
</p>

<p>The following code example initializes a <a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
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
<a href="..\wdfusb\ne-wdfusb--wdf-usb-bmrequest-recipient.md">WDF_USB_BMREQUEST_RECIPIENT</a>
</dt>
<dt>
<a href="..\wdfusb\ns-wdfusb--wdf-usb-control-setup-packet.md">WDF_USB_CONTROL_SETUP_PACKET</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init.md">WDF_USB_CONTROL_SETUP_PACKET_INIT</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-class.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_CLASS</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-get-status.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_GET_STATUS</a>
</dt>
<dt>
<a href="..\wdfusb\nf-wdfusb-wdf-usb-control-setup-packet-init-vendor.md">WDF_USB_CONTROL_SETUP_PACKET_INIT_VENDOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [wdf\wdf]:%20WDF_USB_CONTROL_SETUP_PACKET_INIT_FEATURE function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
