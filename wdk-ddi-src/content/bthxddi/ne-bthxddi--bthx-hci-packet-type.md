---
UID: NE.bthxddi._BTHX_HCI_PACKET_TYPE
title: BTHX_HCI_PACKET_TYPE
author: windows-driver-content
description: The BTHX_HCI_PACKET_TYPE enumeration lists the different types of packets being sent from the Bluetooth stack to the transport driver.
old-location: bltooth\bthx_hci_packet_type.htm
old-project: bltooth
ms.assetid: 87265ABB-C2B7-468F-83FC-411AD9769517
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: BTHDDI_SDP_PARSE_INTERFACE, BTHDDI_SDP_PARSE_INTERFACE, *PBTHDDI_SDP_PARSE_INTERFACE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: bthxddi.h
req.include-header: BthXDDI.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BTHX_HCI_PACKET_TYPE
req.alt-loc: BthXDDI.h
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
---

# BTHX_HCI_PACKET_TYPE enumeration



## -description
<p>The BTHX_HCI_PACKET_TYPE enumeration lists the different types of packets being sent from the Bluetooth stack to the transport driver.</p>


## -syntax

````
typedef enum _BTHX_HCI_PACKET_TYPE { 
  HciPacketCommand  = 0x01,
  HciPacketAclData  = 0x02,
  HciPacketEvent    = 0x04
} BTHX_HCI_PACKET_TYPE;
````


## -enum-fields
<dl>

### -field <a id="HciPacketCommand"></a><a id="hcipacketcommand"></a><a id="HCIPACKETCOMMAND"></a><b>HciPacketCommand</b>

<dd>
<p>The packet represents a command.</p>
</dd>

### -field <a id="HciPacketAclData"></a><a id="hcipacketacldata"></a><a id="HCIPACKETACLDATA"></a><b>HciPacketAclData</b>

<dd>
<p>The packet represents ACL data.</p>
</dd>

### -field <a id="HciPacketEvent"></a><a id="hcipacketevent"></a><a id="HCIPACKETEVENT"></a><b>HciPacketEvent</b>

<dd>
<p>The packet represents an event.</p>
</dd>
</dl>

## -remarks
<p>The IOCTL_BTHX_HCI_READ and IOCTL_BTHX_HCI_WRITE IOCTLs are used to read/write data to/from the transport driver. The BTHX_HCI_PACKET_TYPE enumeration is used to specify with which type of packet the read/write is associated.</p>

<p>The IOCTL_BTHX_HCI_READ and IOCTL_BTHX_HCI_WRITE IOCTLs are used to read/write data to/from the transport driver. The BTHX_HCI_PACKET_TYPE enumeration is used to specify with which type of packet the read/write is associated.</p>

<p>The IOCTL_BTHX_HCI_READ and IOCTL_BTHX_HCI_WRITE IOCTLs are used to read/write data to/from the transport driver. The BTHX_HCI_PACKET_TYPE enumeration is used to specify with which type of packet the read/write is associated.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>BthXDDI.h (include BthXDDI.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\bthxddi\ni-bthxddi-ioctl-bthx-read-hci.md">IOCTL_BTHX_HCI_READ</a>
</dt>
<dt>
<a href="..\bthxddi\ni-bthxddi-ioctl-bthx-write-hci.md">IOCTL_BTHX_HCI_WRITE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [bltooth\bltooth]:%20BTHX_HCI_PACKET_TYPE enumeration%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
