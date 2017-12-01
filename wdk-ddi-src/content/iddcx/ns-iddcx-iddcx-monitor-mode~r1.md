---
UID: NS.iddcx.IDDCX_MONITOR_MODE~r1
title: IDDCX_MONITOR_MODE
author: windows-driver-content
description: Gives information about the current monitor mode.
old-location: display\iddcx_monitor_mode.htm
old-project: display
ms.assetid: 95e1778a-4f65-40ee-8ad2-f797ce9e95b0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_MONITOR_MODE,
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
req.alt-api: IDDCX_MONITOR_MODE
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

# IDDCX_MONITOR_MODE structure



## -description
<p>
                 Gives information about the current monitor mode.</p>


## -syntax

````
typedef struct IDDCX_MONITOR_MODE {
  UINT                            Size;
  IDDCX_MONITOR_MODE_ORIGIN       Origin;
  DISPLAYCONFIG_VIDEO_SIGNAL_INFO MonitorVideoSignalInfo;
} IDDCX_MONITOR_MODE, *IDDCX_MONITOR_MODE;
````


## -struct-fields
<dl>

### -field <b>Size</b>

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field <b>Origin</b>

<dd>
<p>
                     Where the driver derived this mode from.
                 </p>
</dd>

### -field <b>MonitorVideoSignalInfo</b>

<dd>
<p>
                     This is the details of the Monitor mode.</p>
<div class="alert"><b>Note</b>  The<a href="display.displayconfig_video_signal_info">DISPLAYCONFIG_VIDEO_SIGNAL_INFO</a><b>AdditionalSignalInfo</b> value vSyncFreqDivider has to have a zero value.</div>
<div> </div>
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