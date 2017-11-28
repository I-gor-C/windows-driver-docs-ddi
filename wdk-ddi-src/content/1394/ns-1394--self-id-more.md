---
UID: NS.1394._SELF_ID_MORE
title: SELF_ID_MORE
author: windows-driver-content
description: The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details.
old-location: ieee\self_id_more.htm
old-project: IEEE
ms.assetid: d3c164a6-4830-4f1f-9fa5-5cd61e796e31
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: SELF_ID_MORE, SELF_ID_MORE, *PSELF_ID_MORE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 1394.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SELF_ID_MORE
req.alt-loc: 1394.h
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
---

# SELF_ID_MORE structure



## -description
<p>The SELF_ID_MORE structure contains a raw packet one, two, or three self-ID packet. See the IEEE 1394 specification for details.</p>


## -syntax

````
typedef struct _SELF_ID_MORE {
  ULONG SID_Phys_ID  :6;
  ULONG SID_Packet_ID  :2;
  ULONG SID_PortA  :2;
  ULONG SID_Reserved2  :2;
  ULONG SID_Sequence  :3;
  ULONG SID_One  :1;
  ULONG SID_PortE  :2;
  ULONG SID_PortD  :2;
  ULONG SID_PortC  :2;
  ULONG SID_PortB  :2;
  ULONG SID_More_Packets  :1;
  ULONG SID_Reserved3  :1;
  ULONG SID_PortH  :2;
  ULONG SID_PortG  :2;
  ULONG SID_PortF  :2;
} SELF_ID_MORE, *PSELF_ID_MORE;
````


## -struct-fields
<dl>

### -field <b>SID_Phys_ID</b>

<dd>
<p>Specifies the device node number. This member specifies bits 0-10 of the node address. This member contains bits 0-5 of byte 0 of the self ID packet. </p>
</dd>

### -field <b>SID_Packet_ID</b>

<dd>
<p>Must be PHY_PACKET_ID_SELF_ID. This member specifies bits 0-10 of the node address. This member contains bits 6-7 of byte 0 of the self ID packet. </p>
</dd>

### -field <b>SID_PortA</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 0-1 of byte 1 of the self ID packet. </p>
</dd>

### -field <b>SID_Reserved2</b>

<dd>
<p>Reserved. This member contains bits 2-3 of byte 1 of the self ID packet. </p>
</dd>

### -field <b>SID_Sequence</b>

<dd>
<p>Specifies the packet number in sequence (the first SELF_ID_MORE packet is packet zero). This member contains bits 4-5 of byte 1 of the self ID packet. </p>
</dd>

### -field <b>SID_One</b>

<dd>
<p>Always a 1. This member contains bit 6 of byte 1 of the self ID packet. </p>
</dd>

### -field <b>SID_PortE</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member specifies bits 0-1 of byte 2 of the self ID packet. </p>
</dd>

### -field <b>SID_PortD</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member specifies bits 2-3 of byte 2 of the self ID packet. </p>
</dd>

### -field <b>SID_PortC</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 4-5 of byte 2 of the self ID packet. </p>
</dd>

### -field <b>SID_PortB</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 6-7 of byte 2 of the self ID packet. </p>
</dd>

### -field <b>SID_More_Packets</b>

<dd>
<p>One if this packet will be followed by more SELF_ID_MORE packets, zero otherwise. This member contains bit 0 of byte 3 of the self ID packet. </p>
</dd>

### -field <b>SID_Reserved3</b>

<dd>
<p>Reserved. This member contains bit 1 of byte 3 of the self ID packet.</p>
</dd>

### -field <b>SID_PortH</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 2-3 of byte 3 of the self ID packet. </p>
</dd>

### -field <b>SID_PortG</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 4-5 of byte 3 of the self ID packet. </p>
</dd>

### -field <b>SID_PortF</b>

<dd>
<p>Specifies port status. Possible values are:</p>
<dl>
<dd>
<p>SELF_ID_CONNECTED_TO_CHILD</p>
</dd>
<dd>
<p>SELF_ID_CONNECTED_TO_PARENT</p>
</dd>
<dd>
<p>SELF_ID_NOT_CONNECTED</p>
</dd>
<dd>
<p>SELF_ID_NOT_PRESENT</p>
</dd>
</dl>
<p>This member contains bits 6-7 of byte 3 of the self ID packet.</p>
</dd>
</dl>

## -remarks
<p>This structure corresponds to self ID packet 1, as described in the <i>P1394a</i> specification. Note that type 2 self ID packets are identical to type 1 packets, except that the last five fields are replaced by a reserved area. The SELF_ID_MORE structure can be used to access all of the significant information in both type 1 and type 2 self ID packets. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>1394.h (include 1394.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff538877">TOPOLOGY_MAP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [IEEE\buses]:%20SELF_ID_MORE structure%20 RELEASE:%20(10/23/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
