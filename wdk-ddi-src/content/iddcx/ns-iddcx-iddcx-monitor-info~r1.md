---
UID: NS.iddcx.IDDCX_MONITOR_INFO~r1
title: IDDCX_MONITOR_INFO
author: windows-driver-content
description: Gives information about the current monitor and its connection type.
old-location: display\iddcx_monitor_info.htm
old-project: display
ms.assetid: 62c2182c-af55-4482-a890-803f92dc863a
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_MONITOR_INFO,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDDCX_MONITOR_INFO
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
req.irql: _Must_inspect_result_
req.iface: 
---

# IDDCX_MONITOR_INFO structure



## -description
<p>Gives information about the current monitor and its connection type.
             </p>


## -syntax

````
typedef struct IDDCX_MONITOR_INFO {
  UINT                                  Size;
  DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY MonitorType;
  UINT                                  ConnectorIndex;
  IDDCX_MONITOR_DESCRIPTION             MonitorDescription;
  GUID                                  MonitorContainerId;
} IDDCX_MONITOR_INFO, *IDDCX_MONITOR_INFO;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     Total size of the structure
                 </p>
</dd>

### -field MonitorType

<dd>
<p>The monitor connector type of the monitor
                 </p>
</dd>

### -field ConnectorIndex

<dd>
<p>
                     This is a zero-based unique identifier for this connector. It should be unique for this adapter and the value should not change for this connector across system reboot or driver upgrade. </p>
<div class="alert"><b>Note</b>  The value has to be between 0 and the <a href="..\iddcx\ns-iddcx-iddcx-adapter-caps.md">IDDCX_ADAPTER_CAPS</a> value MaxMonitorsSupported minus 1.
                 </div>
<div> </div>
</dd>

### -field MonitorDescription

<dd>
<p>
                     Pointer to the monitor description for the monitor. If the monitor does not have any description data, this should be set to NULL
                 </p>
</dd>

### -field MonitorContainerId

<dd>
<p>
                     Container Id of the monitor being connected. If any device is also inside the monitor (eg audio, touch etc), then those devices should all have the same container id.
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