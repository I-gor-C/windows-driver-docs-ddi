---
UID: NS.bdatypes._BDA_WMDRM_STATUS
title: BDA_WMDRM_STATUS
author: windows-driver-content
description: .
old-location: stream\bda_wmdrm_status.htm
old-project: stream
ms.assetid: FEE7B3B2-2433-4772-8E79-C325ECC343FF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BDA_WMDRM_STATUS, BDA_WMDRM_STATUS, *PBDA_WMDRM_STATUS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: bdatypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BDA_WMDRM_STATUS
req.alt-loc: Bdatypes.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# BDA_WMDRM_STATUS structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_WMDRM_STATUS {
  PBDARESULT lResult;
  ULONG      ulMaxCaptureTokenSize;
  ULONG      uMaxStreamingPid;
  ULONG      ulMaxLicense;
  ULONG      ulMinSecurityLevel;
  ULONG      ulRevInfoSequenceNumber;
  ULONGLONG  ulRevInfoIssuedTime;
  ULONG      ulRevListVersion;
  ULONG      ulRevInfoTTL;
  ULONG      ulState;
} BDA_WMDRM_STATUS, *PBDA_WMDRM_STATUS;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd></dd>

### -field <b>ulMaxCaptureTokenSize</b>

<dd></dd>

### -field <b>uMaxStreamingPid</b>

<dd></dd>

### -field <b>ulMaxLicense</b>

<dd></dd>

### -field <b>ulMinSecurityLevel</b>

<dd></dd>

### -field <b>ulRevInfoSequenceNumber</b>

<dd></dd>

### -field <b>ulRevInfoIssuedTime</b>

<dd></dd>

### -field <b>ulRevListVersion</b>

<dd></dd>

### -field <b>ulRevInfoTTL</b>

<dd></dd>

### -field <b>ulState</b>

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
<dt>Bdatypes.h</dt>
</dl>
</td>
</tr>
</table>