---
UID: NF.prnasntp.RouterGetPrintClassObject
title: RouterGetPrintClassObject
author: windows-driver-content
description: The RouterGetPrintClassObject function enumerates the list of print providers, searching for the print provider with the specified name and interface ID.
old-location: print\routergetprintclassobject.htm
old-project: print
ms.assetid: e2df591d-59bd-4aae-ac1b-8fdf01da3ea7
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: RouterGetPrintClassObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prnasntp.h
req.include-header: Prnasntp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RouterGetPrintClassObject
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
req.iface: 
req.product: Windows 10 or later.
---

# RouterGetPrintClassObject function



## -description
<p>The <code>RouterGetPrintClassObject</code> function enumerates the list of print providers, searching for the print provider with the specified name and interface ID. </p>


## -syntax

````
HRESULT RouterGetPrintClassObject(
  _In_  PCWSTR pPrinter,
  _In_  REFIID riid,
  _Out_ VOID   **ppv
);
````


## -parameters
<dl>

### -param pPrinter [in]

<dd>
<p>A pointer to a null-terminated string that contains the name of the printer or print server.</p>
</dd>

### -param riid [in]

<dd>
<p>The identifier of the requested COM interface.</p>
</dd>

### -param ppv [out]

<dd>
<p>A pointer to a variable that supplies the address of the COM interface requested in the <i>iid</i> parameter.</p>
</dd>
</dl>

## -returns
<p>This function returns S_OK on success, and a standard COM error code otherwise.</p>

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
<dt>Prnasntp.h (include Prnasntp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>