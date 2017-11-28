---
UID: NS.printoem._OEMUIPROCS
title: OEMUIPROCS
author: windows-driver-content
description: The OEMUIPROCS structure is obsolete.The OEMUIPROCS structure contains the address of the DrvGetDriverSetting and DrvUpdateUISetting functions that are exported by Microsoft printer drivers.
old-location: print\oemuiprocs.htm
old-project: print
ms.assetid: 67dfb4bd-c43c-4da3-833d-34050d49dea3
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: OEMUIPROCS, OEMUIPROCS, *POEMUIPROCS
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
req.iface: IPrintSchemaTicket2
req.product: Windows 10 or later.
---

# OEMUIPROCS structure



## -description
<p>The OEMUIPROCS structure is obsolete.</p>
<p>The OEMUIPROCS structure contains the address of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548556">DrvGetDriverSetting</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548641">DrvUpdateUISetting</a> functions that are exported by Microsoft printer drivers.</p>


## -syntax

````
typedef struct _OEMUIPROCS {
  PFN_DrvGetDriverSetting DrvGetDriverSetting;
  PFN_DrvUpdateUISetting  DrvUpdateUISetting;
} OEMUIPROCS, *POEMUIPROCS;
````


## -struct-fields
<dl>

### -field <b>DrvGetDriverSetting</b>

<dd>
<p>Pointer to the printer driver's <b>DrvGetDriverSetting</b> function. (To obtain this function's address in kernel mode, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff548571">DRVPROCS</a>.)</p>
</dd>

### -field <b>DrvUpdateUISetting</b>

<dd>
<p>Pointer to the printer driver's <b>DrvUpdateUISetting</b> function.</p>
</dd>
</dl>

## -remarks
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548556">DrvGetDriverSetting</a> and <a href="https://msdn.microsoft.com/library/windows/hardware/ff548641">DrvUpdateUISetting</a> have been superseded by COM-based interfaces. </p>

<p>The OEMUIPROCS structure's address is contained in an <a href="https://msdn.microsoft.com/library/windows/hardware/ff559571">OEMUIOBJ</a> structure.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printoem.h (include Printoem.h)</dt>
</dl>
</td>
</tr>
</table>