---
UID: NS.iscsiprf._MSiSCSI_SessionStatistics
title: MSiSCSI_SessionStatistics
author: windows-driver-content
description: The MSiSCSI_SessionStatistics structure is used by iSCSI initiators to report session statistics.
old-location: storage\msiscsi_sessionstatistics.htm
ms.assetid: 04ceffce-cd5f-4e62-98cb-450e8552a811
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsiprf.h
req.include-header: Iscsiprf.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_SessionStatistics
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
ms.keywords: MSiSCSI_SessionStatistics, MSiSCSI_SessionStatistics, *PMSiSCSI_SessionStatistics
req.iface: 
---

# MSiSCSI_SessionStatistics structure



## -description
<p>The MSiSCSI_SessionStatistics structure is used by iSCSI initiators to report session statistics. </p>


## -syntax

````
typedef struct _MSiSCSI_SessionStatistics {
  WCHAR     iSCSIName[223 + 1];
  ULONGLONG USID;
  ULONGLONG UniqueAdapterId;
  ULONGLONG BytesSent;
  ULONGLONG BytesReceived;
  ULONGLONG PDUCommandsSent;
  ULONGLONG PDUResponsesReceived;
  ULONGLONG DigestErrors;
  ULONGLONG ConnectionTimeoutErrors;
  ULONGLONG FormatErrors;
} MSiSCSI_SessionStatistics, *PMSiSCSI_SessionStatistics;
````


## -struct-fields
<dl>

### -field <b>iSCSIName</b>

<dd>
<p>A wide character string that contains the name of an iSCSI target.</p>
</dd>

### -field <b>USID</b>

<dd>
<p>The iSCSI session identifier (ID) for this connection instance. This ID is an internal value that the iSCSI protocol uses to identify the session. Do not use this ID. Application software should use the session identifier that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff550121">AddConnectionToSession</a> methods return in the <i>UniqueSessionId</i> parameter.</p>
</dd>

### -field <b>UniqueAdapterId</b>

<dd>
<p>A 64-bit integer that uniquely identifies an HBA initiator and a loaded instance of a storage miniport driver that manages the HBA. The initiator should use the address of the adapter extension or another address that the device driver owns to construct this ID. The initiator reports this value in the <i>UniqueAdapterId</i> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a> structure.</p>
</dd>

### -field <b>BytesSent</b>

<dd>
<p>The number of bytes that are sent over this session. </p>
</dd>

### -field <b>BytesReceived</b>

<dd>
<p>The number of bytes that are received over this session. </p>
</dd>

### -field <b>PDUCommandsSent</b>

<dd>
<p>The number of PDUs that are sent over this session. </p>
</dd>

### -field <b>PDUResponsesReceived</b>

<dd>
<p>The number of PDUs that are received over this session. </p>
</dd>

### -field <b>DigestErrors</b>

<dd>
<p>The number of digest errors that have occurred in this session.</p>
</dd>

### -field <b>ConnectionTimeoutErrors</b>

<dd>
<p>The number of connection time-out errors that have occurred in this session. </p>
</dd>

### -field <b>FormatErrors</b>

<dd>
<p>The number of format errors that have occurred in this session.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550121">AddConnectionToSession</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561599">LoginToTarget</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563012">MSiSCSI_HBAInformation</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563139">MSiSCSI_SessionStatistics WMI Class</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20MSiSCSI_SessionStatistics structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
