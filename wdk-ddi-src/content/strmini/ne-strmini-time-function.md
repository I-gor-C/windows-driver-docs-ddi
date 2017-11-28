---
UID: NE.strmini.TIME_FUNCTION
title: TIME_FUNCTION
author: windows-driver-content
description: .
old-location: stream\time_function.htm
old-project: stream
ms.assetid: 9335B3FB-B46B-404C-BCF9-F4E2F7A4C216
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PST_PARAMETER_DATA, ST_PARAMETER_DATA, *PST_PARAMETER_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: strmini.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TIME_FUNCTION
req.alt-loc: Strmini.h
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

# TIME_FUNCTION enumeration



## -description
<p></p>


## -syntax

````
typedef enum  { 
  TIME_GET_STREAM_TIME,
  TIME_READ_ONBOARD_CLOCK,
  TIME_SET_ONBOARD_CLOCK
} TIME_FUNCTION;
````


## -enum-fields
<dl>

### -field <a id="TIME_GET_STREAM_TIME"></a><a id="time_get_stream_time"></a><b>TIME_GET_STREAM_TIME</b>

<dd></dd>

### -field <a id="TIME_READ_ONBOARD_CLOCK"></a><a id="time_read_onboard_clock"></a><b>TIME_READ_ONBOARD_CLOCK</b>

<dd></dd>

### -field <a id="TIME_SET_ONBOARD_CLOCK"></a><a id="time_set_onboard_clock"></a><b>TIME_SET_ONBOARD_CLOCK</b>

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
<dt>Strmini.h</dt>
</dl>
</td>
</tr>
</table>