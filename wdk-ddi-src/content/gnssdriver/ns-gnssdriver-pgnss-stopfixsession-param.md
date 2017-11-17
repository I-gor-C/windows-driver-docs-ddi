---
UID: NS.gnssdriver.PGNSS_STOPFIXSESSION_PARAM
title: PGNSS_STOPFIXSESSION_PARAM
author: windows-driver-content
description: This structure is used to stop an active fix session.
old-location: sensors\gnss_stopfixsession_param.htm
ms.assetid: 37D56DC0-C35B-4651-93E9-28AF76041D5D
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: sensors
req.header: gnssdriver.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GNSS_STOPFIXSESSION_PARAM
req.alt-loc: gnssdriver.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: PGNSS_STOPFIXSESSION_PARAM, GNSS_STOPFIXSESSION_PARAM, *PGNSS_STOPFIXSESSION_PARAM
req.iface: 
---

# PGNSS_STOPFIXSESSION_PARAM structure



## -description
<p>This structure is used to stop an active fix session.</p>


## -syntax

````
typedef struct {
  ULONG Size;
  ULONG Version;
  ULONG FixSessionID;
  BYTE  Unused[512];
} GNSS_STOPFIXSESSION_PARAM, *PGNSS_STOPFIXSESSION_PARAM;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>Structure size.</p>
</dd>

### -field <b>Version</b>

<dd>
<p>Version number.</p>
</dd>

### -field <b>FixSessionID</b>

<dd>
<p>ID of an active fix session.</p>
</dd>

### -field <b>Unused[512]</b>

<dd>
<p>Padding buffer.</p>
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
<dt>Gnssdriver.h</dt>
</dl>
</td>
</tr>
</table>