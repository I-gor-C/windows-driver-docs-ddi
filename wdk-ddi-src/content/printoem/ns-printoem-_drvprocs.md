---
UID: NS.PRINTOEM._DRVPROCS
title: _DRVPROCS
author: windows-driver-content
description: The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.
old-location: print\drvprocs.htm
old-project: print
ms.assetid: fcdfb7ba-cbb4-454b-b366-82d0c95b4afd
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: _DRVPROCS, *PDRVPROCS, DRVPROCS
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
req.product: Windows 10 or later.
---

# _DRVPROCS structure



## -description
The DRVPROCS structure is obsolete and is not used with the COM interfaces for Microsoft printer drivers.
The structure contains the addresses of helper functions that are provided to rendering plug-ins by Microsoft printer drivers.
All of the functions pointed to by members of this structure are obsolete. For information about each see:

<a href="print.drvwritespoolbuf">DrvWriteSpoolBuf</a>


<a href="print.drvxmoveto">DrvXMoveTo</a>


<a href="print.drvymoveto">DrvYMoveTo</a>


<a href="print.drvgetdriversetting">DrvGetDriverSetting</a>


<a href="print.drvgetstandardvariable">DrvGetStandardVariable</a> (for information about BGetStandardVariable)

<a href="print.drvunidrivertextout">DrvUnidriverTextOut</a>


<a href="print.drvwriteabortbuf">DrvWriteAbortBuf</a>



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

<a href="print.drvwritespoolbuf">DrvWriteSpoolBuf</a>

</dd>
<dd>

<a href="print.drvxmoveto">DrvXMoveTo</a>

</dd>
<dd>

<a href="print.drvymoveto">DrvYMoveTo</a>

</dd>
<dd>

<a href="print.drvgetdriversetting">DrvGetDriverSetting</a>

</dd>
<dd>

<a href="print.drvgetstandardvariable">DrvGetStandardVariable</a> (for information about BGetStandardVariable)
</dd>
<dd>

<a href="print.drvunidrivertextout">DrvUnidriverTextOut</a>

</dd>
<dd>

<a href="print.drvwriteabortbuf">DrvWriteAbortBuf</a>

</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Printoem.h</dt>
</dl>
</td>
</tr>
</table>