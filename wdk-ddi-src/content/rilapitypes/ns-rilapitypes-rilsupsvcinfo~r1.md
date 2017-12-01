---
UID: NS.rilapitypes.RILSUPSVCINFO~r1
title: RILSUPSVCINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvcinfo_2.htm
old-project: netvista
ms.assetid: b3b86cf8-0e0c-4ed1-9d8c-6f2fef00b9cd
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILSUPSVCINFO,
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
req.alt-api: RILSUPSVCINFO
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

# RILSUPSVCINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILSUPSVCINFO {
  DWORD                            cbSize;
  DWORD                            dwParams;
  DWORD                            dwExecutor;
  DWORD                            fFromNetwork;
  DWORD                            dwFailureReason;
  RILSUPSVCACTION                  dwSupSvcAction;
  RILCALLFORWARDINGSETTINGSREASON  dwCallForwardingReason;
  RILCALLBARRINGSTATUSPARAMSTYPE   dwCallBarringType;
  RILSUPSVCTYPE                    dwSupSvcType;
  DWORD                            dwInfoClasses;
  RILALPHAIDENTIFIER               aiIdentifier;
  char [MAXLENGTH_PASSWORD]        szCallBarringPassword;
  char [MAXLENGTH_PASSWORD]        szNewCallBarringPassword;
  RILCALLFORWARDINGSETTINGS        callForwardSettings;
  RILCALLERIDSETTINGS              callerIdSettings;
  RILDIALEDIDSETTINGS              dialedIdSettings;
  RILHIDEIDSETTINGS                hideIdSettings;
  RILHIDECONNECTEDIDSETTINGS       hideConnectedIdSettings;
  RILSUPSERVICEDATA                supServiceData;
} RILSUPSVCINFO, RILSUPSVCINFO;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>fFromNetwork</b>

<dd></dd>

### -field <b>dwFailureReason</b>

<dd></dd>

### -field <b>dwSupSvcAction</b>

<dd></dd>

### -field <b>dwCallForwardingReason</b>

<dd></dd>

### -field <b>dwCallBarringType</b>

<dd></dd>

### -field <b>dwSupSvcType</b>

<dd></dd>

### -field <b>dwInfoClasses</b>

<dd></dd>

### -field <b>aiIdentifier</b>

<dd></dd>

### -field <b>szCallBarringPassword</b>

<dd></dd>

### -field <b>szNewCallBarringPassword</b>

<dd></dd>

### -field <b>callForwardSettings</b>

<dd></dd>

### -field <b>callerIdSettings</b>

<dd></dd>

### -field <b>dialedIdSettings</b>

<dd></dd>

### -field <b>hideIdSettings</b>

<dd></dd>

### -field <b>hideConnectedIdSettings</b>

<dd></dd>

### -field <b>supServiceData</b>

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