---
UID: NS.ntddrilapitypes.RILMSGIS637INSTATUS
title: RILMSGIS637INSTATUS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgis637instatus.htm
old-project: netvista
ms.assetid: ba87baa2-7d96-4418-bfbc-411bb4cda3fb
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILMSGIS637INSTATUS, RILMSGIS637INSTATUS, *LPRILMSGIS637INSTATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMSGIS637INSTATUS
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
req.iface: 
---

# RILMSGIS637INSTATUS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILMSGIS637INSTATUS {
  RILADDRESS               raOrigAddress;
  RILSUBADDRESS            rsaOrigSubaddr;
  RILSYSTEMTIME            stSCReceiveTime;
  DWORD                    dwCauseCode;
  DWORD                    dwReplySeqNumber;
  DWORD                    dwUserResponseCode;
  RILMSGCDMAMSGSTATUSTYPE  dwMsgStatusType;
  DWORD                    dwMsgID;
  RILMSGCDMALANGUAGE       dwMsgLang;
  RILMSGCDMAMSGENCODING    dwMsgEncoding;
  DWORD                    cchMsgLength;
  BYTE [512]               rgbMsg;
} RILMSGIS637INSTATUS, RILMSGIS637INSTATUS;
````


## -struct-fields
<dl>

### -field raOrigAddress

<dd></dd>

### -field rsaOrigSubaddr

<dd></dd>

### -field stSCReceiveTime

<dd></dd>

### -field dwCauseCode

<dd></dd>

### -field dwReplySeqNumber

<dd></dd>

### -field dwUserResponseCode

<dd></dd>

### -field dwMsgStatusType

<dd></dd>

### -field dwMsgID

<dd></dd>

### -field dwMsgLang

<dd></dd>

### -field dwMsgEncoding

<dd></dd>

### -field cchMsgLength

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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>