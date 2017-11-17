---
UID: NS.ntddrilapitypes.RILSUPSVCINFO
title: RILSUPSVCINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupsvcinfo.htm
ms.assetid: 1f8f7c8c-f09a-4bf5-a15b-42f210122b54
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILSUPSVCINFO
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
ms.keywords: RILSUPSVCINFO, RILSUPSVCINFO, *LPRILSUPSVCINFO
req.iface: 
---

# RILSUPSVCINFO structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


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
  char [256]                       szCallBarringPassword;
  char [256]                       szNewCallBarringPassword;
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
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>