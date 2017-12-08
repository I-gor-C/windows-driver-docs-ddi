---
UID: NS.PRINTOEM._OEMUIPROCS
title: _OEMUIPROCS
author: windows-driver-content
description: The OEMUIPROCS structure is obsolete.The OEMUIPROCS structure contains the address of the DrvGetDriverSetting and DrvUpdateUISetting functions that are exported by Microsoft printer drivers.
old-location: print\oemuiprocs.htm
old-project: print
ms.assetid: 67dfb4bd-c43c-4da3-833d-34050d49dea3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: _OEMUIPROCS, *POEMUIPROCS, OEMUIPROCS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: Printoem.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OEMUIPROCS
req.alt-loc: printoem.h
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
req.product: Windows 10 or later.
---

# _OEMUIPROCS structure



## -description
The OEMUIPROCS structure is obsolete.
The OEMUIPROCS structure contains the address of the <a href="print.drvgetdriversetting">DrvGetDriverSetting</a> and <a href="print.drvupdateuisetting">DrvUpdateUISetting</a> functions that are exported by Microsoft printer drivers.


## -syntax

````
typedef struct _OEMUIPROCS {
  PFN_DrvGetDriverSetting DrvGetDriverSetting;
  PFN_DrvUpdateUISetting  DrvUpdateUISetting;
} OEMUIPROCS, *POEMUIPROCS;
````


## -struct-fields

### -field DrvGetDriverSetting

Pointer to the printer driver's <b>DrvGetDriverSetting</b> function. (To obtain this function's address in kernel mode, see <a href="print.drvprocs">DRVPROCS</a>.)

### -field DrvUpdateUISetting

Pointer to the printer driver's <b>DrvUpdateUISetting</b> function.

## -remarks

<a href="print.drvgetdriversetting">DrvGetDriverSetting</a> and <a href="print.drvupdateuisetting">DrvUpdateUISetting</a> have been superseded by COM-based interfaces. 

The OEMUIPROCS structure's address is contained in an <a href="print.oemuiobj">OEMUIOBJ</a> structure.

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>