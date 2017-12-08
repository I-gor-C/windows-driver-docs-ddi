---
UID: NS.iddcx.IDDCX_PATH~r1
title: IDDCX_PATH
author: windows-driver-content
description: Call IDDCX_PATH_INIT to initialize this structure.
old-location: display\iddcx_path.htm
old-project: display
ms.assetid: c0126718-6bb0-493c-9fdd-78ae372f8fd4
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDDCX_PATH,
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
req.alt-api: IDDCX_PATH
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

# IDDCX_PATH structure



## -description
<p>
                 Call <a href="display.iddcx_path_init">IDDCX_PATH_INIT</a> to initialize this structure.
             </p>


## -syntax

````
typedef struct IDDCX_PATH {
  UINT                            Size;
  IDDCX_MONITOR                   MonitorObject;
  IDDCX_PATH_FLAGS                Flags;
  DISPLAYCONFIG_VIDEO_SIGNAL_INFO TargetVideoSignalInfo;
} IDDCX_PATH, *IDDCX_PATH;
````


## -struct-fields
<dl>

### -field Size

<dd>
<p>
                     Total size of the structure.
                 </p>
</dd>

### -field MonitorObject

<dd>
<p>
                     The handle the driver provides to identify the monitor this path is targeted at.
                 </p>
</dd>

### -field Flags

<dd>
<p>
                     Contains flags for this path, like the path's active state and whether it changed.
                 </p>
</dd>

### -field TargetVideoSignalInfo

<dd>
<p>The details of the target mode signal. 
                 </p>
</dd>
</dl>

## -remarks
<p>The <a href="display.displayconfig_video_signal_info">DISPLAYCONFIG_VIDEO_SIGNAL_INFO</a> value <b>vSyncFreq</b> is the Vsync rate between the Indirect Display device and the connected monitor.  <b>vSyncFreqDivider</b> is used to calculate the rate at which the OS will update the desktop image.</p>

<p>The desktop update rate will be calculated by the formula: <a href="display.displayconfig_video_signal_info">DISPLAYCONFIG_VIDEO_SIGNAL_INFO</a> value <b>vSyncFreq</b>  divided by the <b>DISPLAYCONFIG_VIDEO_SIGNAL_INFO</b> value <b>vSyncFreqDivider</b>. </p>

<p>The <a href="display.displayconfig_video_signal_info">DISPLAYCONFIG_VIDEO_SIGNAL_INFO</a>  value <b>vSyncFreqDivider</b> cannot be zero</p>

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