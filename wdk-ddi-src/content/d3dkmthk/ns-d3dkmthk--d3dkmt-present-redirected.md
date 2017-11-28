---
UID: NS.d3dkmthk._D3DKMT_PRESENT_REDIRECTED
title: D3DKMT_PRESENT_REDIRECTED
author: windows-driver-content
description: Used to give information on the status of the present history token.
old-location: display\d3dkmt-present-redirected.htm
old-project: display
ms.assetid: a883d80a-0240-4a2a-b3d8-ca87080717ee
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DKMT_PRESENT_REDIRECTED, D3DKMT_PRESENT_REDIRECTED
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_PRESENT_REDIRECTED
req.alt-loc: d3dkmthk.h
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

# D3DKMT_PRESENT_REDIRECTED structure



## -description
<p>Used to give information on the status of the present history token.</p>


## -syntax

````
typedef struct _D3DKMT_PRESENT_REDIRECTED {
  D3DKMT_HANDLE                   hSyncObj;
  ULONGLONG                       WaitedFenceValue;
  D3DKMT_PRESENTHISTORYTOKEN      PresentHistoryToken;
  D3DKMT_PRESENT_REDIRECTED_FLAGS Flags;
} D3DKMT_PRESENT_REDIRECTED;
````


## -struct-fields
<dl>

### -field <b>hSyncObj</b>

<dd>
<p>The sync object that the PHT waits on.</p>
</dd>

### -field <b>WaitedFenceValue</b>

<dd>
<p>The fence value of hSyncObj that PHT waits on</p>
</dd>

### -field <b>PresentHistoryToken</b>

<dd>
<p>The present history token.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>The flags needed to give the status of the present history token.</p>
</dd>
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>