---
UID: NS.d3dkmddi._DXGK_MONITORLINKINFO
title: DXGK_MONITORLINKINFO
author: windows-driver-content
description: This structure was defined in WDDM 2.1, however the usage hints and capabilities structure definitions were nested within DXGK_MONITORLINKINFO.
old-location: display\dxgk_monitorlinkinfo.htm
ms.assetid: 4A22CC69-F529-4D0B-BF00-877468E29429
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITORLINKINFO
req.alt-loc: d3dkmddi.h
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
ms.keywords: DXGK_MONITORLINKINFO, DXGK_MONITORLINKINFO
req.iface: 
---

# DXGK_MONITORLINKINFO structure



## -description
<p>This structure was defined in WDDM 2.1, however the usage hints and capabilities structure definitions were nested within DXGK_MONITORLINKINFO.  In order to allow the same capabilities structure to be reused in DXGK_QUERYINTEGRATEDDISPLAYOUT, the nested definitions have been extracted into their own structures.</p>


## -syntax

````
typedef struct _DXGK_MONITORLINKINFO {
  DXGK_MONITORLINKINFO_USAGEHINTS   UsageHints;
  DXGK_MONITORLINKINFO_CAPABILITIES Capabilities;
} DXGK_MONITORLINKINFO, *PDXGK_MONITORLINKINFO;
````


## -struct-fields
<dl>

### -field <b>UsageHints</b>

<dd>
<p>Hints to the driver on the intended usage of the display device.</p>
</dd>

### -field <b>Capabilities</b>

<dd>
<p>Flags which describe the capabilities for driving the monitor.</p>
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
<dt>D3dkmddi.h</dt>
</dl>
</td>
</tr>
</table>