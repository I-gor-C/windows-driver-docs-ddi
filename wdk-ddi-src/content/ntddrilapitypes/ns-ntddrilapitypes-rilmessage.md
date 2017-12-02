---
UID: NS.ntddrilapitypes.RILMESSAGE
title: RILMESSAGE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessage.htm
old-project: netvista
ms.assetid: b776b060-79bf-4848-807d-1999d38075ad
ms.author: windowsdriverdev
ms.date: 11/30/2017
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

### -field cbSize

<dd></dd>

### -field dwParams

<dd></dd>

### -field raSvcCtrAddress

<dd></dd>

### -field dwType

<dd></dd>

### -field dwFlags

<dd></dd>

### -field RILMSGUNION

<dd></dd>

### -field msgUnion

<dd></dd>

### -field unMsgInDeliver

<dd></dd>

### -field unMsgInStatus

<dd></dd>

### -field unMsgOutSubmit

<dd></dd>

### -field unMsgBcGeneral

<dd></dd>

### -field unMsgIS637InStatus

<dd></dd>

### -field unMsgCDMAInDeliver

<dd></dd>

### -field unMsgCDMAOutSubmit

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