---
UID: NS.d3dkmdt._DXGK_MONITORLINKINFO_USAGEHINTS
title: DXGK_MONITORLINKINFO_USAGEHINTS
author: windows-driver-content
description: Hints to the driver on the intended usage of the display device.
old-location: display\dxgk_monitorlinkinfo_usagehints.htm
old-project: display
ms.assetid: 4FC2509A-9983-41F8-901F-60DCEDBC163F
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MONITORLINKINFO_USAGEHINTS, DXGK_MONITORLINKINFO_USAGEHINTS, *PDXGK_MONITORLINKINFO_USAGEHINTS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dkmdt.h
req.include-header: D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MONITORLINKINFO_USAGEHINTS
req.alt-loc: d3dkmdt.h
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

# DXGK_MONITORLINKINFO_USAGEHINTS structure



## -description
<p>Hints to the driver on the intended usage of the display device.</p>


## -syntax

````
typedef union _DXGK_MONITORLINKINFO_USAGEHINTS {
  UINT Hidden;
  UINT Reserved ;
} DXGK_MONITORLINKINFO_USAGEHINTS, *PDXGK_MONITORLINKINFO_USAGEHINTS;
````


## -struct-fields
<dl>

### -field Hidden

<dd>
<p>If TRUE, DxgKrnl will hide this display from Win32 so it cannot be a part of the desktop.</p>
</dd>

### -field Reserved 

<dd>
<p>This value is reserved for system use.</p>
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
<dt>D3dkmdt.h (include D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>