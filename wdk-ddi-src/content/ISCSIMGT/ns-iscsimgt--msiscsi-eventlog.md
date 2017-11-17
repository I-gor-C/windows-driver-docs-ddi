---
UID: NS.iscsimgt._MSiSCSI_Eventlog
title: MSiSCSI_Eventlog
author: windows-driver-content
description: This MSiSCSI_EventLog method is used to log any messages to the event log.
old-location: storage\msiscsi_eventlog.htm
ms.assetid: a31a8688-6002-4ad7-b135-0a8111e2c849
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: iscsimgt.h
req.include-header: Iscsimgt.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MSiSCSI_EventLog
req.alt-loc: Iscsimgt.h
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
ms.keywords: MSiSCSI_Eventlog, MSiSCSI_Eventlog, *PMSiSCSI_Eventlog
req.iface: 
---

# MSiSCSI_Eventlog structure



## -description
<p>This MSiSCSI_EventLog method is used to log any messages to the event log.</p>


## -syntax

````
typedef struct _MSiSCSI_EventLog {
  ULONG Type;
  ULONG LogToEventLog;
  ULONG Size;
  UCHAR AdditionalData[1];
} MSiSCSI_EventLog, *PMSiSCSI_EventLog;
````


## -struct-fields
<dl>

### -field <b>Type</b>

<dd>
<p>This specifies the EVENTLOG_MESSAGE_QUALIFIERS type of event log message.</p>
</dd>

### -field <b>LogToEventLog</b>

<dd>
<p>If this value it set to 1, the message will be logged to the system event log.</p>
</dd>

### -field <b>Size</b>

<dd>
<p>This specifies the size of the Additional Data field.</p>
</dd>

### -field <b>AdditionalData[1]</b>

<dd>
<p>This provides additional information associated with this event.</p>
</dd>
</dl>

## -remarks
<p>We recommend that you implement this class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iscsimgt.h (include Iscsimgt.h)</dt>
</dl>
</td>
</tr>
</table>