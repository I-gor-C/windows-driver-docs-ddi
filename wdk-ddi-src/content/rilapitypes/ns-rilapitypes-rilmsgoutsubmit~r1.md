---
UID: NS.rilapitypes.RILMSGOUTSUBMIT~r1
title: RILMSGOUTSUBMIT
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgoutsubmit_2.htm
old-project: netvista
ms.assetid: 1e310fc1-383c-4dbc-9c72-3eb8aa8db285
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILMSGOUTSUBMIT,
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
req.alt-api: RILMSGOUTSUBMIT
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

# RILMSGOUTSUBMIT structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILMSGOUTSUBMIT {
  RILADDRESS               raDestAddress;
  RILMSGPROTOCOLID         dwProtocolID;
  RILMSGDCS                rmdDataCoding;
  RILMSGOUTSUBMITVPFORMAT  dwVPFormat;
  RILSYSTEMTIME            stVP;
  DWORD                    dwMsgID;
  DWORD                    cbHdrLength;
  DWORD                    cchMsgLength;
  BYTE [MAXLENGTH_HDR]     rgbHdr;
  BYTE [MAXLENGTH_MSG]     rgbMsg;
} RILMSGOUTSUBMIT, RILMSGOUTSUBMIT;
````


## -struct-fields
<dl>

### -field raDestAddress

<dd></dd>

### -field dwProtocolID

<dd></dd>

### -field rmdDataCoding

<dd></dd>

### -field dwVPFormat

<dd></dd>

### -field stVP

<dd></dd>

### -field dwMsgID

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