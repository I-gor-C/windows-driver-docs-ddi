---
UID: NE.wdm._MONITOR_DISPLAY_STATE
title: MONITOR_DISPLAY_STATE
author: windows-driver-content
description: Indicates the power state of the monitor being displayed on.
old-location: kernel\monitor_display_state.htm
old-project: kernel
ms.assetid: 50F5C1AD-BA51-4376-8093-E8596265FDAF
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wdm.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MONITOR_DISPLAY_STATE
req.alt-loc: wdm.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# MONITOR_DISPLAY_STATE enumeration



## -description
<p>Indicates the power state of the monitor being displayed on.</p>


## -syntax

````
typedef enum _MONITOR_DISPLAY_STATE { 
  PowerMonitorOff  = 0,
  PowerMonitorOn,
  PowerMonitorDim
} MONITOR_DISPLAY_STATE;
````


## -enum-fields
<dl>

### -field <a id="PowerMonitorOff"></a><a id="powermonitoroff"></a><a id="POWERMONITOROFF"></a><b>PowerMonitorOff</b>

<dd>
<p>This indicates that the monitor is off.</p>
</dd>

### -field <a id="PowerMonitorOn"></a><a id="powermonitoron"></a><a id="POWERMONITORON"></a><b>PowerMonitorOn</b>

<dd>
<p>This indicates that the monitor is on.</p>
</dd>

### -field <a id="PowerMonitorDim"></a><a id="powermonitordim"></a><a id="POWERMONITORDIM"></a><b>PowerMonitorDim</b>

<dd>
<p>This indicates that the monitor is dim.</p>
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
<dt>Wdm.h</dt>
</dl>
</td>
</tr>
</table>