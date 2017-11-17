---
UID: NS.iddcx.IDD_DRIVER_GLOBALS~r1
title: IDD_DRIVER_GLOBALS
author: windows-driver-content
description: Holds per-driver Indirect Display information. Reserved for use by the system.
old-location: display\idd_driver_globals.htm
ms.assetid: 77d2c668-21e4-4c6d-9f3d-7e34c660d1da
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDD_DRIVER_GLOBALS
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
ms.keywords: IDD_DRIVER_GLOBALS, IDD_DRIVER_GLOBALS, *PIDD_DRIVER_GLOBALS
req.iface: 
---

# IDD_DRIVER_GLOBALS structure



## -description
<p>
                 Holds per-driver Indirect Display information. Reserved for use by the system.
             </p>


## -syntax

````
typedef struct IDD_DRIVER_GLOBALS {
  ULONG Reserved;
} IDD_DRIVER_GLOBALS, *IDD_DRIVER_GLOBALS;
````


## -struct-fields
<dl>

### -field <b>Reserved</b>

<dd>
<p>
                     This value is reserved for use by the system.
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