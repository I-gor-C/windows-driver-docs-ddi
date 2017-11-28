---
UID: NS.iscsiprf._MSiSCSI_QMIPSECStats
title: MSiSCSI_QMIPSECStats
author: windows-driver-content
description: The MSiSCSI_QMIPSECStats structure can be used by an iSCSI initiator to report IPsec statistics for an HBA.
old-location: storage\msiscsi_qmipsecstats.htm
old-project: storage
ms.assetid: 265ed956-1065-44be-ac8e-94bab2e4e8b8
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSiSCSI_QMIPSECStats, MSiSCSI_QMIPSECStats, *PMSiSCSI_QMIPSECStats
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iscsiprf.h
req.include-header: Iscsiprf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_QMIPSECStats
req.alt-loc: iscsiprf.h
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

# MSiSCSI_QMIPSECStats structure



## -description
<p>The MSiSCSI_QMIPSECStats structure can be used by an iSCSI initiator to report IPsec statistics for an HBA. </p>


## -syntax

````
typedef struct _MSiSCSI_QMIPSECStats {
  ULONGLONG ActiveSA;
  ULONGLONG PendingKeyOperations;
  ULONGLONG KeyAdditions;
  ULONGLONG KeyDeletions;
  ULONGLONG ReKeys;
  ULONGLONG ActiveTunnels;
  ULONGLONG BadSPIPackets;
  ULONGLONG PacketsNotDecrypted;
  ULONGLONG PacketsNotAuthenticated;
  ULONGLONG PacketsWithReplayDetection;
  ULONGLONG ConfidentialBytesSent;
  ULONGLONG ConfidentialBytesReceived;
  ULONGLONG AuthenticatedBytesSent;
  ULONGLONG AuthenticatedBytesReceived;
  ULONGLONG TransportBytesSent;
  ULONGLONG TransportBytesReceived;
  ULONGLONG TunnelBytesSent;
  ULONGLONG TunnelBytesReceived;
} MSiSCSI_QMIPSECStats, *PMSiSCSI_QMIPSECStats;
````


## -struct-fields
<dl>

### -field <b>ActiveSA</b>

<dd>
<p>The number of active IPsec security associations (SAs). </p>
</dd>

### -field <b>PendingKeyOperations</b>

<dd>
<p>The number of IPsec key operations that are in progress. </p>
</dd>

### -field <b>KeyAdditions</b>

<dd>
<p>The number of successful IPsec SA negotiations. </p>
</dd>

### -field <b>KeyDeletions</b>

<dd>
<p>The number of IPsec SA key deletions. </p>
</dd>

### -field <b>ReKeys</b>

<dd>
<p>The number of re-key operations for IPsec SAs. </p>
</dd>

### -field <b>ActiveTunnels</b>

<dd>
<p>The number of active IPsec tunnels. </p>
</dd>

### -field <b>BadSPIPackets</b>

<dd>
<p>The number of packets for which the security parameters index (SPI) was incorrect.</p>
</dd>

### -field <b>PacketsNotDecrypted</b>

<dd>
<p>The number of failed decryption packets. </p>
</dd>

### -field <b>PacketsNotAuthenticated</b>

<dd>
<p>The number of packets for which data could not be verified.</p>
</dd>

### -field <b>PacketsWithReplayDetection</b>

<dd>
<p>The number of packets that contained a valid sequence number field.</p>
</dd>

### -field <b>ConfidentialBytesSent</b>

<dd>
<p>The number of bytes that are sent by using the encapsulating security payload (ESP) protocol.</p>
</dd>

### -field <b>ConfidentialBytesReceived</b>

<dd>
<p>The number of bytes that are received by using the ESP protocol.</p>
</dd>

### -field <b>AuthenticatedBytesSent</b>

<dd>
<p>The number of bytes that are sent by using the authentication header (AH) protocol.</p>
</dd>

### -field <b>AuthenticatedBytesReceived</b>

<dd>
<p>The number of bytes that are received by using the AH protocol.</p>
</dd>

### -field <b>TransportBytesSent</b>

<dd>
<p>The number of bytes that are sent by using the IPsec protocol. </p>
</dd>

### -field <b>TransportBytesReceived</b>

<dd>
<p>The number of bytes that are received by using the IPsec protocol. </p>
</dd>

### -field <b>TunnelBytesSent</b>

<dd>
<p>The number of bytes that are sent by using the IPsec tunnel mode.</p>
</dd>

### -field <b>TunnelBytesReceived</b>

<dd>
<p>The number of bytes that are received by using the IPsec tunnel mode.</p>
</dd>
</dl>

## -remarks
<p>It is optional that you implement this class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsiprf.h (include Iscsiprf.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563105">MSiSCSI_QMIPSECStats WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_QMIPSECStats structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
