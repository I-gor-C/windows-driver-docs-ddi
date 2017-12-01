---
UID: NS.ntddrilapitypes.RILMESSAGE
title: RILMESSAGE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessage.htm
old-project: netvista
ms.assetid: b776b060-79bf-4848-807d-1999d38075ad
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILMESSAGE, RILMESSAGE, *LPRILMESSAGE
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
req.alt-api: RILMESSAGE
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

# RILMESSAGE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILMESSAGE {
  DWORD                cbSize;
  DWORD                dwParams;
  RILADDRESS           raSvcCtrAddress;
  RILMESSAGETYPE       dwType;
  DWORD                dwFlags;
  NULL                 RILMSGUNION;
  RILMSGUNION          msgUnion;
  RILMSGINDELIVER      unMsgInDeliver;
  RILMSGINSTATUS       unMsgInStatus;
  RILMSGOUTSUBMIT      unMsgOutSubmit;
  RILMSGBCGENERAL      unMsgBcGeneral;
  RILMSGIS637INSTATUS  unMsgIS637InStatus;
  RILMSGCDMAINDELIVER  unMsgCDMAInDeliver;
  RILMSGCDMAOUTSUBMIT  unMsgCDMAOutSubmit;
} RILMESSAGE, RILMESSAGE;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>raSvcCtrAddress</b>

<dd></dd>

### -field <b>dwType</b>

<dd></dd>

### -field <b>dwFlags</b>

<dd></dd>

### -field <b>RILMSGUNION</b>

<dd></dd>

### -field <b>msgUnion</b>

<dd></dd>

### -field <b>unMsgInDeliver</b>

<dd></dd>

### -field <b>unMsgInStatus</b>

<dd></dd>

### -field <b>unMsgOutSubmit</b>

<dd></dd>

### -field <b>unMsgBcGeneral</b>

<dd></dd>

### -field <b>unMsgIS637InStatus</b>

<dd></dd>

### -field <b>unMsgCDMAInDeliver</b>

<dd></dd>

### -field <b>unMsgCDMAOutSubmit</b>

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