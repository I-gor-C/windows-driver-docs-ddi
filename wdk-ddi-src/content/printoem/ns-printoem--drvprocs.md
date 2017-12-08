---
UID: NS.printoem._DRVPROCS
title: DRVPROCS
author: windows-driver-content
description: The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.
old-location: print\drvprocs.htm
old-project: print
ms.assetid: fcdfb7ba-cbb4-454b-b366-82d0c95b4afd
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: DRVPROCS, DRVPROCS, *PDRVPROCS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: printoem.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DRVPROCS
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

# DRVPROCS structure



## -description
<p>The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.</p>
<p>The structure contains the addresses of helper functions that are provided to rendering plug-ins by Microsoft printer drivers.</p>
<p>All of the functions pointed to by members of this structure are obsolete. For information about each see:</p>
<p>
<a href="print.drvwritespoolbuf">DrvWriteSpoolBuf</a>
</p>
<p>
<a href="print.drvxmoveto">DrvXMoveTo</a>
</p>
<p>
<a href="print.drvymoveto">DrvYMoveTo</a>
</p>
<p>
<a href="print.drvgetdriversetting">DrvGetDriverSetting</a>
</p>
<p>
<a href="print.drvgetstandardvariable">DrvGetStandardVariable</a> (for information about BGetStandardVariable)</p>
<p>
<a href="print.drvunidrivertextout">DrvUnidriverTextOut</a>
</p>
<p>
<a href="print.drvwriteabortbuf">DrvWriteAbortBuf</a>
</p>


## -syntax

````
typedef struct _DRVPROCS {
  PFN_DrvWriteSpoolBuf       DrvWriteSpoolBuf;
  PFN_DrvXMoveTo             DrvXMoveTo;
  PFN_DrvYMoveTo             DrvYMoveTo;
  PFN_DrvGetDriverSetting    DrvGetDriverSetting;
  PFN_DrvGetStandardVariable BGetStandardVariable;
  PFN_DrvUnidriverTextOut    DrvUnidriverTextOut;
  PFN_DrvWriteAbortBuf       DrvWriteAbortBuf;
} DRVPROCS, *PDRVPROCS;
````


## -struct-fields
<dl>
<dd>
<p>
<a href="print.drvwritespoolbuf">DrvWriteSpoolBuf</a>
</p>
</dd>
<dd>
<p>
<a href="print.drvxmoveto">DrvXMoveTo</a>
</p>
</dd>
<dd>
<p>
<a href="print.drvymoveto">DrvYMoveTo</a>
</p>
</dd>
<dd>
<p>
<a href="print.drvgetdriversetting">DrvGetDriverSetting</a>
</p>
</dd>
<dd>
<p>
<a href="print.drvgetstandardvariable">DrvGetStandardVariable</a> (for information about BGetStandardVariable)</p>
</dd>
<dd>
<p>
<a href="print.drvunidrivertextout">DrvUnidriverTextOut</a>
</p>
</dd>
<dd>
<p>
<a href="print.drvwriteabortbuf">DrvWriteAbortBuf</a>
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
<dt>Printoem.h</dt>
</dl>
</td>
</tr>
</table>