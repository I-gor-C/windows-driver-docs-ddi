---
UID: NS.ntddrilapitypes.RILSUPSERVICEDATA
title: RILSUPSERVICEDATA
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilsupservicedata.htm
old-project: netvista
ms.assetid: 1cb4afae-75ad-4c9b-8b21-f9aade2c5fd8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RILSUPSERVICEDATA, RILSUPSERVICEDATA, *LPRILSUPSERVICEDATA
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
req.alt-api: RILSUPSERVICEDATA
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

# RILSUPSERVICEDATA structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILSUPSERVICEDATA {
  DWORD                    cbSize;
  DWORD                    dwParams;
  DWORD                    dwExecutor;
  RILSUPSERVICEDATASTATUS  dwStatus;
  DWORD                    dwNetworkSSErrorCause;
  DWORD                    dwNetworkCCErrorCause;
  DWORD                    dwVendorErrorCause;
  DWORD                    dwDataSize;
  WCHAR [1]                wszData;
} RILSUPSERVICEDATA, RILSUPSERVICEDATA;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwParams</b>

<dd></dd>

### -field <b>dwExecutor</b>

<dd></dd>

### -field <b>dwStatus</b>

<dd></dd>

### -field <b>dwNetworkSSErrorCause</b>

<dd></dd>

### -field <b>dwNetworkCCErrorCause</b>

<dd></dd>

### -field <b>dwVendorErrorCause</b>

<dd></dd>

### -field <b>dwDataSize</b>

<dd></dd>

### -field <b>wszData</b>

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