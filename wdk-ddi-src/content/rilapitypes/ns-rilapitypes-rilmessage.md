---
UID: NS.rilapitypes.RILMESSAGE
title: RILMESSAGE
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmessage_2.htm
old-project: netvista
ms.assetid: 731ae115-2394-4651-9b79-6d640d07a328
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILMESSAGE, RILMESSAGE
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
req.alt-api: RILMESSAGE
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

# RILMESSAGE structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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
  NULL                 switch_is;
  NULL                 dwType;
  RILMSGINDELIVER      unMsgInDeliver;
  NULL                 case;
  NULL                 RIL_MSGTYPE_IN_DELIVER;
  RILMSGINSTATUS       unMsgInStatus;
  NULL                 case;
  NULL                 RIL_MSGTYPE_IN_STATUS;
  RILMSGOUTSUBMIT      unMsgOutSubmit;
  NULL                 case;
  NULL                 RIL_MSGTYPE_OUT_SUBMIT;
  RILMSGBCGENERAL      unMsgBcGeneral;
  NULL                 case;
  NULL                 RIL_MSGTYPE_BC_GENERAL;
  RILMSGIS637INSTATUS  unMsgIS637InStatus;
  NULL                 case;
  NULL                 RIL_MSGTYPE_IN_IS637STATUS;
  RILMSGCDMAINDELIVER  unMsgCDMAInDeliver;
  NULL                 case;
  NULL                 RIL_MSGTYPE_IN_CDMADELIVER;
  RILMSGCDMAOUTSUBMIT  unMsgCDMAOutSubmit;
  NULL                 case;
  NULL                 RIL_MSGTYPE_OUT_CDMASUBMIT;
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

### -field switch_is

<dd></dd>

### -field dwType

<dd></dd>

### -field unMsgInDeliver

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_IN_DELIVER

<dd></dd>

### -field unMsgInStatus

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_IN_STATUS

<dd></dd>

### -field unMsgOutSubmit

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_OUT_SUBMIT

<dd></dd>

### -field unMsgBcGeneral

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_BC_GENERAL

<dd></dd>

### -field unMsgIS637InStatus

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_IN_IS637STATUS

<dd></dd>

### -field unMsgCDMAInDeliver

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_IN_CDMADELIVER

<dd></dd>

### -field unMsgCDMAOutSubmit

<dd></dd>

### -field case

<dd></dd>

### -field RIL_MSGTYPE_OUT_CDMASUBMIT

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