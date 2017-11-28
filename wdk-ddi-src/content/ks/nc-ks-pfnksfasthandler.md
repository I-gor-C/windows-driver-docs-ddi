---
UID: NC.ks.PFNKSFASTHANDLER
title: PFNKSFASTHANDLER
author: windows-driver-content
description: KStrFastHandler is a driver-supplied routine that handles a property or method request without the creation of an IRP.
old-location: stream\kstrfasthandler.htm
old-project: stream
ms.assetid: 9a72cdb5-2b57-4331-9836-82653732decf
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NpdBrokerUninitialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KStrFastHandler
req.alt-loc: ks.h
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

# PFNKSFASTHANDLER callback



## -description
<p><i>KStrFastHandler</i> is a driver-supplied routine that handles a property or method request without the creation of an IRP.</p>


## -prototype

````
PFNKSFASTHANDLER KStrFastHandler;

BOOLEAN KStrFastHandler(
  _In_    PFILE_OBJECT     FileObject,
  _In_    PKSIDENTIFIER    Request,
  _In_    ULONG            RequestLength,
  _Inout_ PVOID            Data,
  _In_    ULONG            DataLength,
  _Out_   PIO_STATUS_BLOCK IoStatus
)
{ ... }
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Specifies the file object on which the request was made.</p>
</dd>

### -param <i>Request</i> [in]

<dd>
<p>Specifies the original property parameter. This will always be on FILE_LONG_ALIGNMENT, but cannot be on FILE_QUAD_ALIGNMENT.</p>
</dd>

### -param <i>RequestLength</i> [in]

<dd>
<p>Specifies the length indicated by the caller of the property parameter.</p>
</dd>

### -param <i>Data</i> [in, out]

<dd>
<p>Specifies the original unaligned data parameter.</p>
</dd>

### -param <i>DataLength</i> [in]

<dd>
<p>Specifies the length indicated by the caller of the data parameter.</p>
</dd>

### -param <i>IoStatus</i> [out]

<dd>
<p>Specifies an aligned structure that is used to return error status and information. This information is then copied to the original I/O status structure on completion.</p>
</dd>
</dl>

## -returns
<p><i>KStrFastHandler</i> returns <b>TRUE</b> if the call was handled. If the call was not handled, it returns <b>FALSE</b> and an IRP is generated to handle the request.</p>

## -remarks
<p>The minidriver provides an entry point for this routine in <a href="https://msdn.microsoft.com/library/windows/hardware/ff562521">KSFASTPROPERTY_ITEM</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561944">KSFASTMETHOD_ITEM</a>.</p>

<p>The minidriver provides an entry point for this routine in <a href="https://msdn.microsoft.com/library/windows/hardware/ff562521">KSFASTPROPERTY_ITEM</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff561944">KSFASTMETHOD_ITEM</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>