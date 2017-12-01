---
UID: NS.rilapitypes.RILCHANGECALLBARRINGPASSWORDPARAMS~r1
title: RILCHANGECALLBARRINGPASSWORDPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilchangecallbarringpasswordparams_2.htm
old-project: netvista
ms.assetid: 1a9dda19-329b-4046-bba1-1bbedf37fa31
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILCHANGECALLBARRINGPASSWORDPARAMS,
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
req.alt-api: RILCHANGECALLBARRINGPASSWORDPARAMS
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

# RILCHANGECALLBARRINGPASSWORDPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILCHANGECALLBARRINGPASSWORDPARAMS {
  DWORD                           dwExecutor;
  RILCALLBARRINGSTATUSPARAMSTYPE  dwType;
  char [MAXLENGTH_PASSWORD]       szOldPassword;
  char [MAXLENGTH_PASSWORD]       szNewPassword;
  char [MAXLENGTH_PASSWORD]       szConfirmPassword;
} RILCHANGECALLBARRINGPASSWORDPARAMS, RILCHANGECALLBARRINGPASSWORDPARAMS;
````


## -struct-fields
<dl>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwType</b>

<dd></dd>

### -field <b>szOldPassword</b>

<dd></dd>

### -field <b>szNewPassword</b>

<dd></dd>

### -field <b>szConfirmPassword</b>

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