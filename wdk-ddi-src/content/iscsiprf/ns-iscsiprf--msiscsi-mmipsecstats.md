---
UID: NS.iscsiprf._MSiSCSI_MMIPSECStats
title: MSiSCSI_MMIPSECStats
author: windows-driver-content
description: The MSiSCSI_MMIPSECStats structure is used to report main mode IPsec statistics.
old-location: storage\msiscsi_mmipsecstats.htm
old-project: storage
ms.assetid: 75b11689-f940-467e-92ee-59b5e0adbf70
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: MSiSCSI_MMIPSECStats, MSiSCSI_MMIPSECStats, *PMSiSCSI_MMIPSECStats
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
req.alt-api: MSiSCSI_MMIPSECStats
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

# MSiSCSI_MMIPSECStats structure



## -description
<p>The MSiSCSI_MMIPSECStats structure is used to report main mode IPsec statistics. </p>


## -syntax

````
typedef struct _MSiSCSI_MMIPSECStats {
  ULONGLONG ActiveAcquire;
  ULONGLONG ActiveReceive;
  ULONGLONG AcquireFailures;
  ULONGLONG ReceiveFailures;
  ULONGLONG SendFailures;
  ULONGLONG AcquireHeapSize;
  ULONGLONG ReceiveHeapSize;
  ULONGLONG NegotiationFailures;
  ULONGLONG AuthenticationFailures;
  ULONGLONG InvalidCookiesReceived;
  ULONGLONG TotalGetSPI;
  ULONGLONG KeyAdditions;
  ULONGLONG KeyUpdates;
  ULONGLONG GetSPIFailures;
  ULONGLONG KeyAdditionFailures;
  ULONGLONG KeyUpdateFailures;
  ULONGLONG ConnectionListSize;
  ULONGLONG OakleyMainMode;
  ULONGLONG OakleyQuickMode;
  ULONGLONG InvalidPackets;
  ULONGLONG SoftAssociations;
} MSiSCSI_MMIPSECStats, *PMSiSCSI_MMIPSECStats;
````


## -struct-fields
<dl>

### -field <b>ActiveAcquire</b>

<dd>
<p>The number of active require requests that the IPsec driver has sent to the Internet Key Exchange (IKE) service. Typically, the number of active acquire requests is 1. Under a heavy load, the number of active acquire requests is 1 plus the number of requests that are waiting in the queue of the IKE service. </p>
</dd>

### -field <b>ActiveReceive</b>

<dd>
<p>The number of IKE messages (that is, active receive requests) that are queued for processing.</p>
</dd>

### -field <b>AcquireFailures</b>

<dd>
<p>The number of active acquire requests that have failed.</p>
</dd>

### -field <b>ReceiveFailures</b>

<dd>
<p>The number of failures that have occurred while drivers in the TCP stack are receiving IKE messages.</p>
</dd>

### -field <b>SendFailures</b>

<dd>
<p>The number of failures that have occurred while drivers in the TCP stack are sending IKE messages.</p>
</dd>

### -field <b>AcquireHeapSize</b>

<dd>
<p>The number of IKE messages that the acquire heap can hold. This number increases under a heavy load and then gradually decreases over time, as the acquire heap is emptied.</p>
</dd>

### -field <b>ReceiveHeapSize</b>

<dd>
<p>The number of incoming IKE messages that the IKE receive buffers can hold.</p>
</dd>

### -field <b>NegotiationFailures</b>

<dd>
<p>The total number of negotiation failures that occurred during main mode (also known as <i>phase 1</i>) negotiation or during quick mode (also known as <i>phase 2</i>) negotiation.</p>
</dd>

### -field <b>AuthenticationFailures</b>

<dd>
<p>The number of identity authentication failures that occurred during main mode negotiation. This number includes kerberos failures, certificate failures, and preshared key failures.</p>
</dd>

### -field <b>InvalidCookiesReceived</b>

<dd>
<p>The number of invalid cookies that the initiator has received in IKE messages. Cookies are invalid if the cookie state does not correspond to the state of an active main mode security association (SA).</p>
</dd>

### -field <b>TotalGetSPI</b>

<dd>
<p>The number of requests that the IKE service submitted to obtain a unique security parameters index (SPI).</p>
</dd>

### -field <b>KeyAdditions</b>

<dd>
<p>The number of outbound quick mode SAs that the IKE service has added.</p>
</dd>

### -field <b>KeyUpdates</b>

<dd>
<p>The number of inbound quick mode SAs that the IKE service has added.</p>
</dd>

### -field <b>GetSPIFailures</b>

<dd>
<p>The total number of unsuccessful attempts that the IKE service has made to obtain a unique SPI. </p>
</dd>

### -field <b>KeyAdditionFailures</b>

<dd>
<p>The number of outbound quick-mode SAs that the IKE service has submitted unsuccessfully.</p>
</dd>

### -field <b>KeyUpdateFailures</b>

<dd>
<p>The number of inbound quick-mode SAs that the IKE service has added.</p>
</dd>

### -field <b>ConnectionListSize</b>

<dd>
<p>The number of quick-mode state entries.</p>
</dd>

### -field <b>OakleyMainMode</b>

<dd>
<p>The number of successful SAs that are created during main mode negotiations.</p>
</dd>

### -field <b>OakleyQuickMode</b>

<dd>
<p>The number of successful SAs that are created during quick-mode negotiations.</p>
</dd>

### -field <b>InvalidPackets</b>

<dd>
<p>The number of received IKE messages that are invalid, including IKE messages with invalid header fields, incorrect payload lengths, or incorrect (nonzero) responder cookies that should be 0.</p>
</dd>

### -field <b>SoftAssociations</b>

<dd>
<p>The number of negotiations that resulted in the use of plaintext SAs (also known as <i>soft SAs</i>). This value typically reflects the number of associations that the initiator established with computers that did not respond to main mode negotiation attempts. Computers that do not respond might not support IPSec, or they might support IPSec but not have an IPSec policy with which to negotiate security with an IPSec peer.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563077">MSiSCSI_MMIPSECStats WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20MSiSCSI_MMIPSECStats structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
