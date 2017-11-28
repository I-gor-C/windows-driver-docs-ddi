---
UID: NS.rilapitypes.RILDELETEPHONEBOOKENTRYPARAMS
title: RILDELETEPHONEBOOKENTRYPARAMS
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildeletephonebookentryparams_2.htm
old-project: netvista
ms.assetid: 33e64f4f-a632-47d0-a133-f64d6f4b1cda
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS
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
req.alt-api: RILDELETEPHONEBOOKENTRYPARAMS
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

# RILDELETEPHONEBOOKENTRYPARAMS structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


## -syntax

````
typedef struct _RILDELETEPHONEBOOKENTRYPARAMS {
  HUICCAPP                    hUiccApp;
  RILPHONEENTRYSTORELOCATION  dwStoreLocation;
  DWORD                       dwIndex;
  BOOL                        fHasLockVerification;
  RILUICCLOCKCREDENTIAL       lockVerification;
} RILDELETEPHONEBOOKENTRYPARAMS, RILDELETEPHONEBOOKENTRYPARAMS;
````


## -struct-fields
<dl>

### -field <b>hUiccApp</b>

<dd></dd>

### -field <b>dwStoreLocation</b>

<dd></dd>

### -field <b>dwIndex</b>

<dd></dd>

### -field <b>fHasLockVerification</b>

<dd></dd>

### -field <b>lockVerification</b>

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