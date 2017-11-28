---
UID: NS.bdatypes._BDA_WMDRMTUNER_PURCHASEENTITLEMENT
title: BDA_WMDRMTUNER_PURCHASEENTITLEMENT
author: windows-driver-content
description: .
old-location: stream\bda_wmdrmtuner_purchaseentitlement.htm
old-project: stream
ms.assetid: 348E7C25-4998-490E-A732-5780B0A21DE0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: BDA_WMDRMTUNER_PURCHASEENTITLEMENT, BDA_WMDRMTUNER_PURCHASEENTITLEMENT, *PBDA_WMDRMTUNER_PURCHASEENTITLEMENT
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
req.alt-api: BDA_WMDRMTUNER_PURCHASEENTITLEMENT
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

# BDA_WMDRMTUNER_PURCHASEENTITLEMENT structure



## -description
<p></p>


## -syntax

````
typedef struct _BDA_WMDRMTUNER_PURCHASEENTITLEMENT {
  PBDARESULT lResult;
  ULONG      ulDescrambleStatus;
  ULONG      ulCaptureTokenLength;
  BYTE       argbCaptureTokenBuffer[MIN_DIMENSION];
} BDA_WMDRMTUNER_PURCHASEENTITLEMENT, *PBDA_WMDRMTUNER_PURCHASEENTITLEMENT;
````


## -struct-fields
<dl>

### -field <b>lResult</b>

<dd></dd>

### -field <b>ulDescrambleStatus</b>

<dd></dd>

### -field <b>ulCaptureTokenLength</b>

<dd></dd>

### -field <b>argbCaptureTokenBuffer</b>

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