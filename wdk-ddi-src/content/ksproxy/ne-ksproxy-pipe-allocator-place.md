---
UID: NE.ksproxy.PIPE_ALLOCATOR_PLACE
title: PIPE_ALLOCATOR_PLACE
author: windows-driver-content
description: .
old-location: stream\pipe_allocator_place.htm
old-project: stream
ms.assetid: 86B1D8BB-7213-403C-8EAB-D681A5DBF49E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: tagTRANSPORTVIDEOPARMS, TRANSPORTVIDEOPARMS, *PTRANSPORTVIDEOPARMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksproxy.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PIPE_ALLOCATOR_PLACE
req.alt-loc: Ksproxy.h
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

# PIPE_ALLOCATOR_PLACE enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  Pipe_Allocator_None,
  Pipe_Allocator_FirstPin,
  Pipe_Allocator_LastPin,
  Pipe_Allocator_MiddlePin
} PIPE_ALLOCATOR_PLACE;
````


## -enum-fields
<dl>

### -field <a id="Pipe_Allocator_None"></a><a id="pipe_allocator_none"></a><a id="PIPE_ALLOCATOR_NONE"></a><b>Pipe_Allocator_None</b>

<dd></dd>

### -field <a id="Pipe_Allocator_FirstPin"></a><a id="pipe_allocator_firstpin"></a><a id="PIPE_ALLOCATOR_FIRSTPIN"></a><b>Pipe_Allocator_FirstPin</b>

<dd></dd>

### -field <a id="Pipe_Allocator_LastPin"></a><a id="pipe_allocator_lastpin"></a><a id="PIPE_ALLOCATOR_LASTPIN"></a><b>Pipe_Allocator_LastPin</b>

<dd></dd>

### -field <a id="Pipe_Allocator_MiddlePin"></a><a id="pipe_allocator_middlepin"></a><a id="PIPE_ALLOCATOR_MIDDLEPIN"></a><b>Pipe_Allocator_MiddlePin</b>

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
<dt>Ksproxy.h</dt>
</dl>
</td>
</tr>
</table>