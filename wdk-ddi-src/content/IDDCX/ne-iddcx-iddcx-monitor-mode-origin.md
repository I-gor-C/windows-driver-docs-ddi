---
UID: NE.iddcx.IDDCX_MONITOR_MODE_ORIGIN
title: IDDCX_MONITOR_MODE_ORIGIN
author: windows-driver-content
description: Used to describe a mode the monitor supports based on the monitor description.
old-location: display\iddcx_monitor_mode_origin.htm
ms.assetid: 96aac09b-c6fc-43a7-a6d8-36f642e0f5d7
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_MONITOR_MODE_ORIGIN
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _requires_same_
ms.keywords: WcsTranslateColors
req.iface: 
---

# IDDCX_MONITOR_MODE_ORIGIN enumeration



## -description
<p>
                     Used to describe a mode the monitor supports based on the monitor description.
                </p>


## -syntax

````
typedef enum _IDDCX_MONITOR_MODE_ORIGIN { 
  IDDCX_MONITOR_MODE_ORIGIN_UNINITIALIZED      = 0,
  IDDCX_MONITOR_MODE_ORIGIN_MONITORDESCRIPTOR  = 1,
  IDDCX_MONITOR_MODE_ORIGIN_DRIVER             = 2
} IDDCX_MONITOR_MODE_ORIGIN;
````


## -enum-fields
<dl>

### -field <a id="IDDCX_MONITOR_MODE_ORIGIN_UNINITIALIZED"></a><a id="iddcx_monitor_mode_origin_uninitialized"></a><b>IDDCX_MONITOR_MODE_ORIGIN_UNINITIALIZED</b>

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_MONITOR_MODE_ORIGIN</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="IDDCX_MONITOR_MODE_ORIGIN_MONITORDESCRIPTOR"></a><a id="iddcx_monitor_mode_origin_monitordescriptor"></a><b>IDDCX_MONITOR_MODE_ORIGIN_MONITORDESCRIPTOR</b>

<dd>
<p>
                        Indicates that the driver added this mode from directly processing the monitor description
                    </p>
</dd>

### -field <a id="IDDCX_MONITOR_MODE_ORIGIN_DRIVER"></a><a id="iddcx_monitor_mode_origin_driver"></a><b>IDDCX_MONITOR_MODE_ORIGIN_DRIVER</b>

<dd>
<p>
                        Indicates that the driver did not add this mode as a direct resolution of processing the modes/ supported by the monitor but because of separate additional knowledge it has about the monitor
                    </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>