---
UID: NS.ntddndis._NDIS_PM_PACKET_PATTERN
title: NDIS_PM_PACKET_PATTERN
author: windows-driver-content
description: The NDIS_PM_PACKET_PATTERN structure specifies a wake-up pattern, which, when detected by a network adapter that has pattern-match enabled, causes the network adapter to signal a power-management wake-up event.
old-location: netvista\ndis_pm_packet_pattern.htm
old-project: netvista
ms.assetid: dfda0b5f-06fc-4e94-b14c-6bd32c2c138a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PM_PACKET_PATTERN, NDIS_PM_PACKET_PATTERN, *PNDIS_PM_PACKET_PATTERN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NDIS_PM_PACKET_PATTERN (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NDIS_PM_PACKET_PATTERN (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_PM_PACKET_PATTERN
req.alt-loc: ntddndis.h
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

# NDIS_PM_PACKET_PATTERN structure



## -description
<p>The NDIS_PM_PACKET_PATTERN structure specifies a wake-up pattern, which, when detected by a network adapter that
  has pattern-match enabled, causes the network adapter to signal a power-management wake-up event.</p>


## -syntax

````
typedef struct _NDIS_PM_PACKET_PATTERN {
  ULONG Priority;
  ULONG Reserved;
  ULONG MaskSize;
  ULONG PatternOffset;
  ULONG PatternSize;
  ULONG PatternFlags;
} NDIS_PM_PACKET_PATTERN, *PNDIS_PM_PACKET_PATTERN;
````


## -struct-fields
<dl>

### -field <b>Priority</b>

<dd>
<p>This member is reserved.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>This member is reserved.</p>
</dd>

### -field <b>MaskSize</b>

<dd>
<p>Specifies the size in bytes of the pattern mask that immediately follows the
     NDIS_PM_PACKET_PATTERN structure in the 
     <i>InformationBuffer</i>.</p>
</dd>

### -field <b>PatternOffset</b>

<dd>
<p>Specifies in bytes the offset from the beginning of the 
     <i>InformationBuffer</i> to the start of the wake-up pattern.</p>
</dd>

### -field <b>PatternSize</b>

<dd>
<p>Specifies in bytes the size of the wake-up pattern.</p>
</dd>

### -field <b>PatternFlags</b>

<dd>
<p>These flags are reserved.</p>
</dd>
</dl>

## -remarks
<p>NDIS_PM_PACKET_PATTERN is supplied in the 
    <i>InformationBuffer</i> of the 
    <a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a> structure for following
    OIDs:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569773">OID_PNP_ADD_WAKE_UP_PATTERN</a>
</p>

<p>A protocol driver sends this OID to a miniport driver to specify a wake-up pattern. The wake-up
      pattern, along with its mask, is described by an NDIS_PM_PACKET_PATTERN structure.</p>

<p>
<a href="netvista.oid_pnp_remove_wake_up_pattern">
       OID_PNP_REMOVE_WAKE_UP_PATTERN</a>
</p>

<p>A protocol driver sends this OID to a miniport driver to delete a wake-up pattern that it previously
      specified with an OID_PNP_ADD_WAKE_UP_PATTERN request. The wake-up pattern, along with its mask, is
      described by an NDIS_PM_PACKET_PATTERN structure.</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569783">OID_PNP_WAKE_UP_PATTERN_LIST</a>
</p>

<p>A protocol uses this OID to request a list of the wake-up patterns currently set for the miniport
      driver's network adapter. Each wake-up pattern, along with its mask, is described by an NDIS_PM_PACKET_PATTERN
      structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/318c5c9d-01d9-466a-b994-5f5cffd83d0a">NDIS_PM_PACKET_PATTERN (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NDIS_PM_PACKET_PATTERN (NDIS
   5.1)</b>) in Windows XP.</p>
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
<dt>
<a href="..\ndis\ns-ndis--ndis-oid-request.md">NDIS_OID_REQUEST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569773">OID_PNP_ADD_WAKE_UP_PATTERN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569779">OID_PNP_REMOVE_WAKE_UP_PATTERN</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569783">OID_PNP_WAKE_UP_PATTERN_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PM_PACKET_PATTERN structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
