---
UID: NS.ntddrilapitypes.RILMSGINDELIVER
title: RILMSGINDELIVER
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgindeliver.htm
old-project: netvista
ms.assetid: a4bfdc26-46a9-404e-9cd0-10dabba01dc2
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILMSGINDELIVER, RILMSGINDELIVER, *LPRILMSGINDELIVER
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
req.alt-api: RILMSGINDELIVER
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

# RILMSGINDELIVER structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILMSGINDELIVER {
  RILADDRESS        raOrigAddress;
  RILMSGPROTOCOLID  dwProtocolID;
  RILMSGDCS         rmdDataCoding;
  RILSYSTEMTIME     stSCReceiveTime;
  DWORD             dwMsgID;
  DWORD             cbHdrLength;
  DWORD             cchMsgLength;
  BYTE [256]        rgbHdr;
  BYTE [512]        rgbMsg;
} RILMSGINDELIVER, RILMSGINDELIVER;
````


## -struct-fields
<dl>

### -field <b>raOrigAddress</b>

<dd></dd>

### -field <b>dwProtocolID</b>

<dd></dd>

### -field <b>rmdDataCoding</b>

<dd></dd>

### -field <b>stSCReceiveTime</b>

<dd></dd>

### -field <b>dwMsgID</b>

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