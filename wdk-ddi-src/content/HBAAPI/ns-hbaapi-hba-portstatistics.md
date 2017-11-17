---
UID: NS.hbaapi.HBA_PortStatistics
title: HBA_PortStatistics
author: windows-driver-content
description: The HBA_PortStatistics structure contains statistical information about a port.
old-location: storage\hba_portstatistics.htm
ms.assetid: 3a0d6633-b4a6-4864-96ae-4f91de11daa1
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbaapi.h
req.include-header: Hbaapi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: HBA_PORTSTATISTICS
req.alt-loc: hbaapi.h
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
ms.keywords: HBA_PortStatistics, HBA_PORTSTATISTICS, *PHBA_PORTSTATISTICS
req.iface: 
---

# HBA_PortStatistics structure



## -description
<p>The HBA_PortStatistics structure contains statistical information about a port. </p>


## -syntax

````
typedef struct HBA_PortStatistics {
  HBA_INT64 SecondsSinceLastReset;
  HBA_INT64 TxFrames;
  HBA_INT64 TxWords;
  HBA_INT64 RxFrames;
  HBA_INT64 RxWords;
  HBA_INT64 LIPCount;
  HBA_INT64 NOSCount;
  HBA_INT64 ErrorFrames;
  HBA_INT64 DumpedFrames;
  HBA_INT64 LinkFailureCount;
  HBA_INT64 LossOfSyncCount;
  HBA_INT64 LossOfSignalCount;
  HBA_INT64 PrimitiveSeqProtocolErrCount;
  HBA_INT64 InvalidTxWordCount;
  HBA_INT64 InvalidCRCCount;
} HBA_PORTSTATISTICS, *PHBA_PORTSTATISTICS;
````


## -struct-fields
<dl>

### -field <b>SecondsSinceLastReset</b>

<dd>
<p>Reports the number of seconds since the statistics were last reset.</p>
</dd>

### -field <b>TxFrames</b>

<dd>
<p>Reports the number of fibre channel frames transmitted for all protocols and classes.</p>
</dd>

### -field <b>TxWords</b>

<dd>
<p>Reports the number of fibre channel words transmitted for all protocols and classes. </p>
</dd>

### -field <b>RxFrames</b>

<dd>
<p>Reports the number of fibre channel frames received for all protocols and classes. </p>
</dd>

### -field <b>RxWords</b>

<dd>
<p>Reports the number of fibre channel words received for all protocols and classes. </p>
</dd>

### -field <b>LIPCount</b>

<dd>
<p>Reports the number of LIP events that have occurred on a arbitrated loop.</p>
</dd>

### -field <b>NOSCount</b>

<dd>
<p>Reports the number of NOS events that have occurred on the switched fabric.</p>
</dd>

### -field <b>ErrorFrames</b>

<dd>
<p>Reports the number of frames that have been received in error.</p>
</dd>

### -field <b>DumpedFrames</b>

<dd>
<p>Reports the number of frames that were lost due to a lack of host buffers available. </p>
</dd>

### -field <b>LinkFailureCount</b>

<dd>
<p>Reports the link failure count field of the error status block for the port. </p>
</dd>

### -field <b>LossOfSyncCount</b>

<dd>
<p>Reports the value of the loss of synchronization count field of the link error status block for the port.  </p>
</dd>

### -field <b>LossOfSignalCount</b>

<dd>
<p>Reports the value of the loss of signal count field of the link error status block for the specified port. </p>
</dd>

### -field <b>PrimitiveSeqProtocolErrCount</b>

<dd>
<p>Reports the value of the primitive sequence protocol error field of the link error status block for the port. </p>
</dd>

### -field <b>InvalidTxWordCount</b>

<dd>
<p>Reports the value of the invalid transmission word field of the link error status block for the specified port. </p>
</dd>

### -field <b>InvalidCRCCount</b>

<dd>
<p>Reports the value of the invalid CRC count field of the link error status block for the specified port. </p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbaapi.h (include Hbaapi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556107">HBA_GetPortStatistics</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20HBA_PortStatistics structure%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
