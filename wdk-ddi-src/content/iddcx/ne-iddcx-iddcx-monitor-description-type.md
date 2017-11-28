---
UID: NE.iddcx.IDDCX_MONITOR_DESCRIPTION_TYPE
title: IDDCX_MONITOR_DESCRIPTION_TYPE
author: windows-driver-content
description: Used to describe the monitor description.
old-location: display\iddcx_monitor_description_type.htm
old-project: display
ms.assetid: ca50256b-2b37-4d39-ad4c-e2eaaa0adbb1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: WcsTranslateColors
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_MONITOR_DESCRIPTION_TYPE
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
req.iface: 
---

# IDDCX_MONITOR_DESCRIPTION_TYPE enumeration



## -description
<p>
                     Used to describe the monitor description.
                </p>


## -syntax

````
typedef enum _IDDCX_MONITOR_DESCRIPTION_TYPE { 
  IDDCX_MONITOR_DESCRIPTION_TYPE_UNINITIALIZED  = 0,
  IDDCX_MONITOR_DESCRIPTION_TYPE_EDID           = 1,
  IDDCX_MONITOR_DESCRIPTION_TYPE_DISPLAYID      = 2
} IDDCX_MONITOR_DESCRIPTION_TYPE;
````


## -enum-fields
<dl>

### -field <a id="IDDCX_MONITOR_DESCRIPTION_TYPE_UNINITIALIZED"></a><a id="iddcx_monitor_description_type_uninitialized"></a><b>IDDCX_MONITOR_DESCRIPTION_TYPE_UNINITIALIZED</b>

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_MONITOR_DESCRIPTION_TYPE</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="IDDCX_MONITOR_DESCRIPTION_TYPE_EDID"></a><a id="iddcx_monitor_description_type_edid"></a><b>IDDCX_MONITOR_DESCRIPTION_TYPE_EDID</b>

<dd>
<p>
                        The monitor description is EdId
                    </p>
</dd>

### -field <a id="IDDCX_MONITOR_DESCRIPTION_TYPE_DISPLAYID"></a><a id="iddcx_monitor_description_type_displayid"></a><b>IDDCX_MONITOR_DESCRIPTION_TYPE_DISPLAYID</b>

<dd>
<p>
                        The monitor description is DisplayId
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