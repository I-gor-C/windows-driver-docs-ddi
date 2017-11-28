---
UID: NS.d4drvif._DOT4_DC_OPEN_DATA
title: DOT4_DC_OPEN_DATA
author: windows-driver-content
description: This topic describes the DOT4_DC_OPEN_DATA structure.
old-location: print\dot4_dc_open_data.htm
old-project: print
ms.assetid: 72AE7A78-C02D-4C14-B017-9CEECF34FEDF
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DOT4_DC_OPEN_DATA, DOT4_DC_OPEN_DATA, *PDOT4_DC_OPEN_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d4drvif.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DOT4_DC_OPEN_DATA
req.alt-loc: D4drvif.h
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

# DOT4_DC_OPEN_DATA structure



## -description
<p>This topic describes the <b>DOT4_DC_OPEN_DATA</b> structure.</p>


## -syntax

````
typedef struct _DOT4_DC_OPEN_DATA {
  unsigned char  bHsid;
  fAddActivity   unsigned char;
  CHANNEL_HANDLE hChannelHandle;
} DOT4_DC_OPEN_DATA, *PDOT4_DC_OPEN_DATA;
````


## -struct-fields
<dl>

### -field <b>bHsid</b>

<dd>
<p>Specifies the host socket created by CREATE_SOCKET.</p>
</dd>

### -field <b>unsigned char</b>

<dd>
<p>Specify TRUE to immediately add activity broadcast upon creation.</p>
</dd>

### -field <b>hChannelHandle</b>

<dd>
<p>Specifies the handle to the channel returned.</p>
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
<dt>D4drvif.h</dt>
</dl>
</td>
</tr>
</table>