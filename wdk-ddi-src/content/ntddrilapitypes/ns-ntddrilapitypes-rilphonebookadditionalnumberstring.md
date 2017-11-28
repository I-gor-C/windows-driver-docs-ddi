---
UID: NS.ntddrilapitypes.RILPHONEBOOKADDITIONALNUMBERSTRING
title: RILPHONEBOOKADDITIONALNUMBERSTRING
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilphonebookadditionalnumberstring.htm
old-project: netvista
ms.assetid: 1d201c4d-606d-4461-ad3d-df48d3455724
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: RILPHONEBOOKADDITIONALNUMBERSTRING, RILPHONEBOOKADDITIONALNUMBERSTRING, *LPRILPHONEBOOKADDITIONALNUMBERSTRING
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
req.alt-api: RILPHONEBOOKADDITIONALNUMBERSTRING
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

# RILPHONEBOOKADDITIONALNUMBERSTRING structure



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef struct _RILPHONEBOOKADDITIONALNUMBERSTRING {
  DWORD       cbSize;
  DWORD       dwNumId;
  WCHAR [256] wszText;
} RILPHONEBOOKADDITIONALNUMBERSTRING, RILPHONEBOOKADDITIONALNUMBERSTRING;
````


## -struct-fields
<dl>

### -field <b>cbSize</b>

<dd></dd>

### -field <b>dwNumId</b>

<dd></dd>

### -field <b>wszText</b>

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