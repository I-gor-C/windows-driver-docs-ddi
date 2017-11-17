---
UID: NE.ks.KSEVENT_CONNECTION
title: KSEVENT_CONNECTION
author: windows-driver-content
description: TBD.
old-location: stream\ksevent_connection.htm
ms.assetid: E85946B3-90B6-41CA-9F69-47B33AE8D851
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_CONNECTION
req.alt-loc: 
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# KSEVENT_CONNECTION enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum  { 
  KSEVENT_CONNECTION_POSITIONUPDATE,
  KSEVENT_CONNECTION_DATADISCONTINUITY,
  KSEVENT_CONNECTION_TIMEDISCONTINUITY,
  KSEVENT_CONNECTION_PRIORITY,
  KSEVENT_CONNECTION_ENDOFSTREAM
} KSEVENT_CONNECTION;
````


## -enum-fields
<dl>

### -field <a id="KSEVENT_CONNECTION_POSITIONUPDATE"></a><a id="ksevent_connection_positionupdate"></a><b>KSEVENT_CONNECTION_POSITIONUPDATE</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="KSEVENT_CONNECTION_DATADISCONTINUITY"></a><a id="ksevent_connection_datadiscontinuity"></a><b>KSEVENT_CONNECTION_DATADISCONTINUITY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="KSEVENT_CONNECTION_TIMEDISCONTINUITY"></a><a id="ksevent_connection_timediscontinuity"></a><b>KSEVENT_CONNECTION_TIMEDISCONTINUITY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="KSEVENT_CONNECTION_PRIORITY"></a><a id="ksevent_connection_priority"></a><b>KSEVENT_CONNECTION_PRIORITY</b>

<dd>
<p>TBD</p>
</dd>

### -field <a id="KSEVENT_CONNECTION_ENDOFSTREAM"></a><a id="ksevent_connection_endofstream"></a><b>KSEVENT_CONNECTION_ENDOFSTREAM</b>

<dd>
<p>TBD</p>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>