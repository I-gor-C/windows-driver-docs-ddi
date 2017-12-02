---
UID: NS.rilapitypes.RILMSGCDMAOUTSUBMIT
title: RILMSGCDMAOUTSUBMIT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmaoutsubmit_2.htm
old-project: netvista
ms.assetid: f74fe6cb-f38c-49ab-957f-9b3d163059c6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGCDMAOUTSUBMIT
req.alt-loc: rilapitypes.h
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

# RILMSGCDMAOUTSUBMIT structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
  BYTE [MAXLENGTH_CDMAHDR]  rgbHdr;
  BYTE [MAXLENGTH_CDMAMSG]  rgbMsg;
} RILMSGCDMAOUTSUBMIT, RILMSGCDMAOUTSUBMIT;
````


## -struct-fields
<dl>

### -field raDestAddress

<dd></dd>

### -field rsaDestSubaddr

<dd></dd>

### -field bDigit

<dd></dd>

### -field stValidityPeriodAbs

<dd></dd>

### -field stValidityPeriodRel

<dd></dd>

### -field stDeferredDelTimeAbs

<dd></dd>

### -field stDeferredDelTimeRel

<dd></dd>

### -field bDeliveryAckRequest

<dd></dd>

### -field bUserAckRequest

<dd></dd>

### -field bBearerReplyRequest

<dd></dd>

### -field dwReplySeqNumber

<dd></dd>

### -field dwMsgDisplayMode

<dd></dd>

### -field raCallBackNumber

<dd></dd>

### -field dwMsgPriority

<dd></dd>

### -field dwMsgPrivacy

<dd></dd>

### -field dwTeleservice

<dd></dd>

### -field dwMsgID

<dd></dd>

### -field dwMsgLang

<dd></dd>

### -field dwMsgEncoding

<dd></dd>

### -field cbHdrLength

<dd></dd>

### -field cchMsgLength

<dd></dd>

### -field rgbHdr

<dd></dd>

### -field rgbMsg

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>