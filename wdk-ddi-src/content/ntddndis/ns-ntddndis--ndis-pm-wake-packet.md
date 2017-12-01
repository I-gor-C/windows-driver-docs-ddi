---
UID: NS.ntddndis._NDIS_PM_WAKE_PACKET
title: NDIS_PM_WAKE_PACKET
author: windows-driver-content
description: The NDIS_PM_WAKE_PACKET structure describes a network packet (known as a wake packet) that caused the network adapter to generate a wake-up event.
old-location: netvista\ndis_pm_wake_packet.htm
old-project: netvista
ms.assetid: b3d7adcf-79cd-42f4-ada2-c57de6310020
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PM_WAKE_PACKET, NDIS_PM_WAKE_PACKET, *PNDIS_PM_WAKE_PACKET
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.30 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PM_WAKE_PACKET
req.alt-loc: Ntddndis.h
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
---

# NDIS_PM_WAKE_PACKET structure



## -description
<p>The <b>NDIS_PM_WAKE_PACKET</b> structure describes a network packet (known as a <i>wake packet</i>) that caused the network adapter to generate a wake-up event.</p>


## -syntax

````
typedef struct _NDIS_PM_WAKE_PACKET {
  NDIS_OBJECT_HEADER     Header;
  ULONG                  Flags;
  ULONG                  PatternId;
  NDIS_PM_COUNTED_STRING PatternFriendlyName;
  ULONG                  OriginalPacketSize;
  ULONG                  SavedPacketSize;
  ULONG                  SavedPacketOffset;
} NDIS_PM_WAKE_PACKET, *PNDIS_PM_WAKE_PACKET;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The type, revision, and size of the <b>NDIS_PM_WAKE_PACKET</b> structure. This member is formatted as an <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure.</p>
<p>The miniport driver must set the <b>Type</b> member of <b>Header</b> to NDIS_OBJECT_TYPE_DEFAULT. To specify the version of the <b>NDIS_PM_WAKE_PACKET</b> structure, the driver must set the <b>Revision</b> member of <b>Header</b> to the following value: </p>
<p></p>
<dl>

### -field <a id="NDIS_SIZEOF_PM_WAKE_PACKET_REVISION_1"></a><a id="ndis_sizeof_pm_wake_packet_revision_1"></a>NDIS_SIZEOF_PM_WAKE_PACKET_REVISION_1

<dd>
<p>Original version for NDIS 6.30 and later.</p>
<p>Set the <b>Size</b> member to NDIS_SIZEOF_PM_WAKE_PACKET_REVISION_1.</p>
</dd>
</dl>
</dd>

### -field <b>Flags</b>

<dd>
<p>A <b>ULONG</b> value that contains a bitwise <b>OR</b> of flags. This member is reserved for NDIS.

</p>
</dd>

### -field <b>PatternId</b>

<dd>
<p>A <b>ULONG</b> value that specifies the identifier of the wake-on-LAN (WOL) pattern that matches the wake packet. This identifier is specified by the <b>PatternId</b> member of the <a href="..\ntddndis\ns-ntddndis--ndis-pm-wol-pattern.md">NDIS_PM_WOL_PATTERN</a> structure that is passed to the driver during an OID set request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a>.</p>
</dd>

### -field <b>PatternFriendlyName</b>

<dd>
<p>An <a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a> value that contains the friendly description of the wake pattern that is specified by the  <b>PatternId</b> member.
This value is specified by the <b>FriendlyName</b> member of the <a href="..\ntddndis\ns-ntddndis--ndis-pm-wol-pattern.md">NDIS_PM_WOL_PATTERN</a> structure that is passed to the driver during an OID request of <a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a>.</p>
<div class="alert"><b>Note</b>  The miniport driver does not need to initialize this member. NDIS sets the <b>PatternFriendlyName</b> member to the correct value before it passes the <b>NDIS_PM_WAKE_PACKET</b> structure to overlying drivers.

</div>
<div> </div>
</dd>

### -field <b>OriginalPacketSize</b>

<dd>
<p>A <b>ULONG</b> value that specifies the original length, in units of bytes, of the wake packet.</p>
</dd>

### -field <b>SavedPacketSize</b>

<dd>
<p>A <b>ULONG</b> value that specifies the length, in units of bytes, of the wake packet data that follows this structure. 
</p>
<div class="alert"><b>Note</b>  The value of this member should at least<code> min(wake packet size, 128)</code> bytes.</div>
<div> </div>
</dd>

### -field <b>SavedPacketOffset</b>

<dd>
<p>A <b>ULONG</b> value that specifies the offset, in units of bytes, to the wake packet data that follows this structure. The offset is measured from the start of the <b>NDIS_PM_WAKE_PACKET</b> structure to the beginning of a buffer that contains the wake packet.</p>
<div class="alert"><b>Note</b>  The offset to the saved wake packet must be aligned on a 64-bit boundary.</div>
<div> </div>
</dd>
</dl>

## -remarks
<p>The <b>NDIS_PM_WAKE_PACKET</b> structure is used in the <a href="https://msdn.microsoft.com/library/windows/hardware/hh439808">NDIS_STATUS_PM_WAKE_REASON</a> status indication. For more information about how to issue this status indication, see <a href="NULL">Issuing NDIS Wake Reason Status Indications</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt><b></b></dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-pm-counted-string.md">NDIS_PM_COUNTED_STRING</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-pm-wol-pattern.md">NDIS_PM_WOL_PATTERN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439808">NDIS_STATUS_PM_WAKE_REASON</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569764">OID_PM_ADD_WOL_PATTERN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_WAKE_PACKET structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
