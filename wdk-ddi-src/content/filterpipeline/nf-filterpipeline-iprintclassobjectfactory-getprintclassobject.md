---
UID: NF.filterpipeline.IPrintClassObjectFactory.GetPrintClassObject
title: IPrintClassObjectFactory::GetPrintClassObject
author: windows-driver-content
description: The GetPrintClassObject method creates a print filter-related object for a specified printer by using the IID of the interface object to create.
old-location: print\iprintclassobjectfactory_getprintclassobject.htm
old-project: print
ms.assetid: 96ba0c27-d512-4bca-9053-a753434e461d
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintClassObjectFactory, GetPrintClassObject, IPrintClassObjectFactory::GetPrintClassObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintClassObjectFactory.GetPrintClassObject
req.alt-loc: filterpipeline.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: Filterpipeline.idl
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPrintClassObjectFactory
---

# IPrintClassObjectFactory::GetPrintClassObject method



## -description
<p>The <b>GetPrintClassObject</b> method creates a print filter-related object for a specified printer by using the IID of the interface object to create.</p>


## -syntax

````
HRESULT GetPrintClassObject(
  [in]  const wchar_t *pszPrinterName,
  [in]        REFIID  riid,
  [out]       void    **ppNewObject
);
````


## -parameters
<dl>

### -param <i>pszPrinterName</i> [in]

<dd>
<p>The printer name.</p>
</dd>

### -param <i>riid</i> [in]

<dd>
<p>The IID of the interface to create. Filters should use IID_IPrintAsyncNotify to create notification channels.</p>
</dd>

### -param <i>ppNewObject</i> [out]

<dd>
<p>The new object that this method creates.</p>
</dd>
</dl>

## -returns
<p><b>GetPrintClassObject</b> returns an <b>HRESULT</b> value.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IDL</p>
</th>
<td width="70%">
<dl>
<dt>Filterpipeline.idl</dt>
</dl>
</td>
</tr>
</table>