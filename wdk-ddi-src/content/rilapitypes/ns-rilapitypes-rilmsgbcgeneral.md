---
UID: NS.rilapitypes.RILMSGBCGENERAL
title: RILMSGBCGENERAL
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmsgbcgeneral_2.htm
old-project: netvista
ms.assetid: 7202683f-5e02-48dd-b8b7-cb998fd660df
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILMSGBCGENERAL, RILMSGBCGENERAL
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
req.alt-api: RILMSGBCGENERAL
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

# RILMSGBCGENERAL structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILMSGBCGENERAL {
  RILGEOSCOPE                       dwGeoScope;
  DWORD                             dwMsgCode;
  DWORD                             dwUpdateNumber;
  DWORD                             dwID;
  DWORD                             dwSerialNumber;
  RILMSGDCS                         rmdDataCoding;
  DWORD                             dwTotalPages;
  DWORD                             dwPageNumber;
  RILMSGBCGENERALWARNINGTYPE        dwWarningType;
  BOOL                              bEmergencyUserAlert;
  BOOL                              bMessagePopup;
  RILSYSTEMTIME                     stSCReceiveTime;
  BYTE [MAXLENGTH_DIGITALSIGNATURE] digSig;
  DWORD                             cchMsgLength;
  BYTE [MAXLENGTH_MSG]              rgbMsg;
} RILMSGBCGENERAL, RILMSGBCGENERAL;
````


## -struct-fields
<dl>

### -field dwGeoScope

<dd></dd>

### -field dwMsgCode

<dd></dd>

### -field dwUpdateNumber

<dd></dd>

### -field dwID

<dd></dd>

### -field dwSerialNumber

<dd></dd>

### -field rmdDataCoding

<dd></dd>

### -field dwTotalPages

<dd></dd>

### -field dwPageNumber

<dd></dd>

### -field dwWarningType

<dd></dd>

### -field bEmergencyUserAlert

<dd></dd>

### -field bMessagePopup

<dd></dd>

### -field stSCReceiveTime

<dd></dd>

### -field digSig

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>