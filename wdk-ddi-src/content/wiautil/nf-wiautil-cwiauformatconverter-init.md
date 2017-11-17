---
UID: NF.wiautil.CWiauFormatConverter.Init
title: CWiauFormatConverter::Init
author: windows-driver-content
description: The CWiauFormatConverter::Init method initializes the CWiauFormatConverter class and GDI+ for converting images. This method should be called only once.
old-location: image\cwiauformatconverter_init.htm
ms.assetid: 342ea1ae-ff8c-429d-bee8-08559fe75b40
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h, Wiamindr.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: CWiauFormatConverter.Init
req.alt-loc: Wiautil.h
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
ms.keywords: CWiauFormatConverter, Init, CWiauFormatConverter::Init
req.iface: CWiauFormatConverter
req.product: Windows 10 or later.
---

# CWiauFormatConverter::Init method



## -description
<p>The <b>CWiauFormatConverter::Init</b> method initializes the <b>CWiauFormatConverter</b> class and GDI+ for converting images. This method should be called only once.</p>


## -syntax

````
HRESULT Init();
````


## -parameters


## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

## -remarks


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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h or Wiamindr.h)</dt>
</dl>
</td>
</tr>
</table>