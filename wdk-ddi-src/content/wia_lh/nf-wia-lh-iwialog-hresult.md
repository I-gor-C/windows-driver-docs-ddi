---
UID: NF.wia_lh.IWiaLog.hResult
title: IWiaLog::hResult
author: windows-driver-content
description: Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported.
old-location: image\iwialog_hresult.htm
old-project: image
ms.assetid: 74d9b770-c2b6-483d-a6d7-070ac2a55133
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaLog, hResult, IWiaLog::hResult
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wia_lh.h
req.include-header: Wia.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Me, Windows XP, and later. Obsoletefor Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IWiaLog.hResult
req.alt-loc: wia_lh.h
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
req.iface: IWiaLog
req.product: Windows 10 or later.
---

# IWiaLog::hResult method



## -description
<p>Note that the <b>IWiaLog</b> interface is <b>obsolete </b>for Microsoft Windows XP and later, and is no longer supported. Instead, use the <a href="image.diagnostic_log_macros">Diagnostic Log Macros</a>.</p>
<p>The <b>IWiaLog::hResult</b> method translates an HRESULT value into a string and writes the string to <i>Wiaservc.log</i>.</p>


## -syntax

````
HRESULT hResult(
  [in] HRESULT hResult
);
````


## -parameters
<dl>

### -param <i>hResult</i> [in]

<dd>
<p>Specifies the HRESULT value to translate into a string.</p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK. If the method fails, it returns a standard COM error code.</p>

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
<p>Available in Windows Me, Windows XP, and later. Obsoletefor Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia.h)</dt>
</dl>
</td>
</tr>
</table>