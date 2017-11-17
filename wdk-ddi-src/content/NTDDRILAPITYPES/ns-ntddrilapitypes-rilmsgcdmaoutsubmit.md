---
UID: NS.ntddrilapitypes.RILMSGCDMAOUTSUBMIT
title: RILMSGCDMAOUTSUBMIT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmaoutsubmit.htm
ms.assetid: 3ed93cff-7974-4cf9-9b89-f4a8e52c4c3d
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGCDMAOUTSUBMIT
req.alt-loc: ntddrilapitypes.h
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
ms.keywords: RILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT, *LPRILMSGCDMAOUTSUBMIT
req.iface: 
---

# RILMSGCDMAOUTSUBMIT structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILMSGCDMAOUTSUBMIT {
  RILADDRESS                raDestAddress;
  RILSUBADDRESS             rsaDestSubaddr;
  BOOL                      bDigit;
  RILSYSTEMTIME             stValidityPeriodAbs;
  RILSYSTEMTIME             stValidityPeriodRel;
  RILSYSTEMTIME             stDeferredDelTimeAbs;
  RILSYSTEMTIME             stDeferredDelTimeRel;
  BOOL                      bDeliveryAckRequest;
  BOOL                      bUserAckRequest;
  BOOL                      bBearerReplyRequest;
  DWORD                     dwReplySeqNumber;
  RILMSGCDMAMSGDISPLAYMODE  dwMsgDisplayMode;
  RILADDRESS                raCallBackNumber;
  RILMSGCDMAMSGPRIORITY     dwMsgPriority;
  RILMSGCDMAMSGPRIVACY      dwMsgPrivacy;
  DWORD                     dwTeleservice;
  DWORD                     dwMsgID;
  RILMSGCDMALANGUAGE        dwMsgLang;
  RILMSGCDMAMSGENCODING     dwMsgEncoding;
  DWORD                     cbHdrLength;
  DWORD                     cchMsgLength;
  BYTE [140]                rgbHdr;
  BYTE [256]                rgbMsg;
} RILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT;
````


## -struct-fields
<dl>

### -field <b>raDestAddress</b>

<dd></dd>

### -field <b>rsaDestSubaddr</b>

<dd></dd>

### -field <b>bDigit</b>

<dd></dd>

### -field <b>stValidityPeriodAbs</b>

<dd></dd>

### -field <b>stValidityPeriodRel</b>

<dd></dd>

### -field <b>stDeferredDelTimeAbs</b>

<dd></dd>

### -field <b>stDeferredDelTimeRel</b>

<dd></dd>

### -field <b>bDeliveryAckRequest</b>

<dd></dd>

### -field <b>bUserAckRequest</b>

<dd></dd>

### -field <b>bBearerReplyRequest</b>

<dd></dd>

### -field <b>dwReplySeqNumber</b>

<dd></dd>

### -field <b>dwMsgDisplayMode</b>

<dd></dd>

### -field <b>raCallBackNumber</b>

<dd></dd>

### -field <b>dwMsgPriority</b>

<dd></dd>

### -field <b>dwMsgPrivacy</b>

<dd></dd>

### -field <b>dwTeleservice</b>

<dd></dd>

### -field <b>dwMsgID</b>

<dd></dd>

### -field <b>dwMsgLang</b>

<dd></dd>

### -field <b>dwMsgEncoding</b>

<dd></dd>

### -field <b>cbHdrLength</b>

<dd></dd>

### -field <b>cchMsgLength</b>

<dd></dd>

### -field <b>rgbHdr</b>

<dd></dd>

### -field <b>rgbMsg</b>

<dd></dd>
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>