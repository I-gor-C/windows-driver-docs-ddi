---
UID: NS.smclib._T1_DATA
title: T1_DATA
author: windows-driver-content
description: The T1_DATA structure is used by the smart card driver library to process T1 I/O.
old-location: smartcrd\t1_data.htm
old-project: smartcrd
ms.assetid: af20cab0-c70b-404c-b6bd-54d9ecf75714
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: T1_DATA, T1_DATA, *PT1_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: smclib.h
req.include-header: Smclib.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: T1_DATA, *PT1_DATA
req.alt-loc: Smclib.h
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

# T1_DATA structure



## -description
<p>The T1_DATA structure is used by the smart card driver library to process T1 I/O. </p>


## -syntax

````
typedef struct {
  UCHAR   InfSize;
  ULONG   BytesReceived;
  ULONG   BytesSent;
  ULONG   BytesToSend;
  UCHAR   LastError;
  UCHAR   NAD;
  ULONG   PrevState;
  UCHAR   Resend;
  UCHAR   Resynch;
  UCHAR   RSN;
  UCHAR   SSN;
  ULONG   State;
  UCHAR   Wtx;
  PUCHAR  ReplyData;
  BOOLEAN WaitForReply;
} T1_DATA, *PT1_DATA;
````


## -struct-fields
<dl>

### -field <b>InfSize</b>

<dd>
<p>Contains the current information field size to transmit. </p>
</dd>

### -field <b>BytesReceived</b>

<dd>
<p>Contains the number of bytes already received from the smart card. </p>
</dd>

### -field <b>BytesSent</b>

<dd>
<p>Contains the number of bytes already sent to the smart card. </p>
</dd>

### -field <b>BytesToSend</b>

<dd>
<p>Contains the total number of remaining bytes to send. </p>
</dd>

### -field <b>LastError</b>

<dd>
<p>Contains the T1 error code of the last received block. </p>
</dd>

### -field <b>NAD</b>

<dd>
<p>Contains the node address byte to send to the smart card. </p>
</dd>

### -field <b>PrevState</b>

<dd>
<p>Contains the state before the error occurred. </p>
</dd>

### -field <b>Resend</b>

<dd>
<p>Contains the resend counter. </p>
</dd>

### -field <b>Resynch</b>

<dd>
<p>Contains the resynch counter. </p>
</dd>

### -field <b>RSN</b>

<dd>
<p>Contains the number of sent I-Blocks, as defined in the <i>ISO 7816-3 Specification</i>. </p>
</dd>

### -field <b>SSN</b>

<dd>
<p>Contains the send sequence number (SSN). This member has a value of 0 or 1 as defined in the <i>ISO 7816-3 Specification</i>.</p>
</dd>

### -field <b>State</b>

<dd>
<p>Contains the current state of the protocol. </p>
</dd>

### -field <b>Wtx</b>

<dd>
<p>Contains the waiting time extension for a T=1 transmission. If nonzero, this is a multiplier for the block waiting time. Usually, the driver will time out if the block waiting time expires. Several smart card operations require more time. The smart card answers with a waiting time extension. Therefore, the block waiting time must be multiplied with the <b>Wtx</b> value. If this value is nonzero, it applies as a waiting extension. </p>
</dd>

### -field <b>ReplyData</b>

<dd>
<p>A pointer to the buffer that contains the result of the operation. </p>
</dd>

### -field <b>WaitForReply</b>

<dd>
<p>If <b>TRUE</b>, execute the operation synchronously.</p>
</dd>
</dl>

## -remarks
<p>This structure must not be directly modified by a reader driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Smclib.h (include Smclib.h)</dt>
</dl>
</td>
</tr>
</table>