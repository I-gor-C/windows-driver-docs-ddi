---
UID: NS.rilapitypes.RILCALLINFO_V5
title: RILCALLINFO_V5
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilcallinfo_v5_2.htm
old-project: netvista
ms.assetid: a2cadee5-40e4-4044-b631-1824099e2fd7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RILCALLINFO_V5, RILCALLINFO_V5
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
req.alt-api: RILCALLINFO_V5
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

# RILCALLINFO_V5 structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCALLINFO_V5 {
  DWORD                           cbSize;
  DWORD                           dwParams;
  DWORD                           dwExecutor;
  DWORD                           dwID;
  RILCALLINFODIRECTION            dwDirection;
  RILCALLINFOSTATUS               dwStatus;
  RILCALLTYPE                     dwType;
  RILCALLINFOMULTIPARTY           dwMultiparty;
  RILADDRESS                      raAddress;
  RILSUBADDRESS                   rsaSubAddress;
  WCHAR [MAXLENGTH_DESCRIPTION]   wszDescription;
  RILREMOTEPARTYINFOVALUE         dwNumberPresentationIndicator;
  RILREMOTEPARTYINFOVALUE         dwNamePresentationIndicator;
  DWORD                           dwFlags;
  RILCALLINFODISCONNECTINITIATOR  dwDisconnectInitiator;
  RILCALLINFODISCONNECTREASON     dwDisconnectReason;
  RILCALLDISCONNECTDETAILS        stDisconnectDetails;
  RILCALLMEDIAOFFERANSWERSET      rcmOfferAnswer;
  RILCALLHANDOVERSTATE            rchsHandoverState;
  RILCALLMODIFICATIONCAUSECODE    dwCallModificationCauseCode;
  RILCALLRTT                      stRTTInfo;
} RILCALLINFO_V5, RILCALLINFO_V5;
````


## -struct-fields
<dl>

### -field cbSize

<dd></dd>

### -field dwParams

<dd></dd>

### -field dwExecutor

<dd></dd>

### -field dwID

<dd></dd>

### -field dwDirection

<dd></dd>

### -field dwStatus

<dd></dd>

### -field dwType

<dd></dd>

### -field dwMultiparty

<dd></dd>

### -field raAddress

<dd></dd>

### -field rsaSubAddress

<dd></dd>

### -field wszDescription

<dd></dd>

### -field dwNumberPresentationIndicator

<dd></dd>

### -field dwNamePresentationIndicator

<dd></dd>

### -field dwFlags

<dd></dd>

### -field dwDisconnectInitiator

<dd></dd>

### -field dwDisconnectReason

<dd></dd>

### -field stDisconnectDetails

<dd></dd>

### -field rcmOfferAnswer

<dd></dd>

### -field rchsHandoverState

<dd></dd>

### -field dwCallModificationCauseCode

<dd></dd>

### -field stRTTInfo

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