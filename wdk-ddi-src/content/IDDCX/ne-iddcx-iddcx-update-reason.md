---
UID: NE.iddcx.IDDCX_UPDATE_REASON
title: IDDCX_UPDATE_REASON
author: windows-driver-content
description: Describes why the driver is calling to update the mode list.
old-location: display\iddcx_update_reason.htm
ms.assetid: e451e4e3-0b8a-4a17-8e4e-2da99d336a39
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
req.alt-api: IDDCX_UPDATE_REASON
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

# IDDCX_UPDATE_REASON enumeration



## -description
<p>
                    Describes why the driver is calling to update the mode list
                </p>


## -syntax

````
typedef enum _IDDCX_UPDATE_REASON { 
  IDDCX_UPDATE_REASON_UNINITIALIZED              = 0,
  IDDCX_UPDATE_REASON_POWER_CONSTRAINTS          = 1,
  IDDCX_UPDATE_REASON_HOST_LINK_BANDWIDTH        = 2,
  IDDCX_UPDATE_REASON_DISPLAY_LINK_BANDWIDTH     = 3,
  IDDCX_UPDATE_REASON_CONFIGURATION_CONSTRAINTS  = 4,
  IDDCX_UPDATE_REASON_OTHER                      = 5
} IDDCX_UPDATE_REASON;
````


## -enum-fields
<dl>

### -field <a id="IDDCX_UPDATE_REASON_UNINITIALIZED"></a><a id="iddcx_update_reason_uninitialized"></a><b>IDDCX_UPDATE_REASON_UNINITIALIZED</b>

<dd>
<p>
                        
                    Indicates that an <b>IDDCX_UPDATE_REASON</b> variable has not yet been assigned a meaningful value.</p>
</dd>

### -field <a id="IDDCX_UPDATE_REASON_POWER_CONSTRAINTS"></a><a id="iddcx_update_reason_power_constraints"></a><b>IDDCX_UPDATE_REASON_POWER_CONSTRAINTS</b>

<dd>
<p>
                        The mode list is changing due to changed power constraints on the host system
                    </p>
</dd>

### -field <a id="IDDCX_UPDATE_REASON_HOST_LINK_BANDWIDTH"></a><a id="iddcx_update_reason_host_link_bandwidth"></a><b>IDDCX_UPDATE_REASON_HOST_LINK_BANDWIDTH</b>

<dd>
<p>
                        The mode list is changing due to changes in bandwidth between the system and the indirect display device
                    </p>
</dd>

### -field <a id="IDDCX_UPDATE_REASON_DISPLAY_LINK_BANDWIDTH"></a><a id="iddcx_update_reason_display_link_bandwidth"></a><b>IDDCX_UPDATE_REASON_DISPLAY_LINK_BANDWIDTH</b>

<dd>
<p>
                        The mode list is changing due to changes in bandwidth between the indirect display device and the monitor
                    </p>
</dd>

### -field <a id="IDDCX_UPDATE_REASON_CONFIGURATION_CONSTRAINTS"></a><a id="iddcx_update_reason_configuration_constraints"></a><b>IDDCX_UPDATE_REASON_CONFIGURATION_CONSTRAINTS</b>

<dd>
<p>
                        The mode list is changing due to constraints of the product when in a new configuration
                    </p>
</dd>

### -field <a id="IDDCX_UPDATE_REASON_OTHER"></a><a id="iddcx_update_reason_other"></a><b>IDDCX_UPDATE_REASON_OTHER</b>

<dd>
<p>
                        The mode list is changing due to another reason not listed above
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