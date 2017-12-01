---
UID: NE.ks.KSSTREAM_POINTER_STATE
title: KSSTREAM_POINTER_STATE
author: windows-driver-content
description: .
old-location: stream\ksstream_pointer_state.htm
old-project: stream
ms.assetid: E3DF002D-825C-4DF6-935F-53D73F12FE2E
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSSTREAM_POINTER_STATE
req.alt-loc: Ks.h
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

# KSSTREAM_POINTER_STATE enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  KSSTREAM_POINTER_STATE_UNLOCKED  = 0,
  KSSTREAM_POINTER_STATE_LOCKED
} KSSTREAM_POINTER_STATE;
````


## -enum-fields
<dl>

### -field <a id="KSSTREAM_POINTER_STATE_UNLOCKED"></a><a id="ksstream_pointer_state_unlocked"></a><b>KSSTREAM_POINTER_STATE_UNLOCKED</b>

<dd></dd>

### -field <a id="KSSTREAM_POINTER_STATE_LOCKED"></a><a id="ksstream_pointer_state_locked"></a><b>KSSTREAM_POINTER_STATE_LOCKED</b>

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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>