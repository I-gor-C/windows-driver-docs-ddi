---
UID: NS.rilapitypes.RILMSGCDMAINDELIVER
title: RILMSGCDMAINDELIVER
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgcdmaindeliver_2.htm
old-project: netvista
ms.assetid: 0729c3e5-c95d-44fb-9aa4-079833b94619
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILMSGCDMAINDELIVER, RILMSGCDMAINDELIVER
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
req.alt-api: RILMSGCDMAINDELIVER
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

# RILMSGCDMAINDELIVER structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILMSGCDMAINDELIVER {
  RILADDRESS                raOrigAddress;
  RILSUBADDRESS             rsaOrigSubaddr;
  RILSYSTEMTIME             stSCReceiveTime;
  RILSYSTEMTIME             stValidityPeriodAbs;
  RILSYSTEMTIME             stValidityPeriodRel;
  RILSYSTEMTIME             stDeferredDelTimeAbs;
  RILSYSTEMTIME             stDeferredDelTimeRel;
  DWORD                     dwNumMsgs;
  RILADDRESS                raCallBackNumber;
  RILMSGCDMAMSGPRIORITY     dwMsgPriority;
  DWORD                     dwAlertOnMsgDelivery;
  RILMSGCDMAMSGPRIVACY      dwMsgPrivacy;
  BOOL                      bUserAckRequest;
  RILMSGCDMAMSGDISPLAYMODE  dwMsgDisplayMode;
  DWORD                     dwTeleservice;
  DWORD                     dwServiceID;
  DWORD                     dwMsgID;
  RILMSGCDMALANGUAGE        dwMsgLang;
  RILMSGCDMAMSGENCODING     dwMsgEncoding;
  DWORD                     cbHdrLength;
  DWORD                     cchMsgLength;
  BYTE [MAXLENGTH_CDMAHDR]  rgbHdr;
  BYTE [MAXLENGTH_CDMAMSG]  rgbMsg;
} RILMSGCDMAINDELIVER, RILMSGCDMAINDELIVER;
````


## -struct-fields
<dl>

### -field <b>raOrigAddress</b>

<dd></dd>

### -field <b>rsaOrigSubaddr</b>

<dd></dd>

### -field <b>stSCReceiveTime</b>

<dd></dd>

### -field <b>stValidityPeriodAbs</b>

<dd></dd>

### -field <b>stValidityPeriodRel</b>

<dd></dd>

### -field <b>stDeferredDelTimeAbs</b>

<dd></dd>

### -field <b>stDeferredDelTimeRel</b>

<dd></dd>

### -field <b>dwNumMsgs</b>

<dd></dd>

### -field <b>raCallBackNumber</b>

<dd></dd>

### -field <b>dwMsgPriority</b>

<dd></dd>

### -field <b>dwAlertOnMsgDelivery</b>

<dd></dd>

### -field <b>dwMsgPrivacy</b>

<dd></dd>

### -field <b>bUserAckRequest</b>

<dd></dd>

### -field <b>dwMsgDisplayMode</b>

<dd></dd>

### -field <b>dwTeleservice</b>

<dd></dd>

### -field <b>dwServiceID</b>

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>