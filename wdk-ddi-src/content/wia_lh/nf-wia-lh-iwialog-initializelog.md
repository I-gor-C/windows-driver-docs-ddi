---
UID: NF.wia_lh.IWiaLog.InitializeLog
title: IWiaLog::InitializeLog
author: windows-driver-content
description: Note that the IWiaLog interface is obsolete for Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.The IWiaLog::InitializeLog method initializes the lWiaLog interface.
old-location: image\iwialog_initializelog.htm
old-project: image
ms.assetid: ef637329-a291-445b-8ac7-6e55d5d7931e
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaLog, InitializeLog, IWiaLog::InitializeLog
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
req.alt-api: IWiaLog.InitializeLog
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

# IWiaLog::InitializeLog method



## -description
<p>Note that the <b>IWiaLog</b> interface is <b>obsolete</b> for Microsoft Windows XP and later, and is no longer supported. Instead, use the <a href="image.diagnostic_log_macros">Diagnostic Log Macros</a>.</p>
<p>The <b>IWiaLog::InitializeLog</b> method initializes the <b>lWiaLog</b> interface.</p>


## -syntax

````
HRESULT InitializeLog(
  [in] LONG hInstance
);
````


## -parameters
<dl>

### -param <i>hInstance</i> [in]

<dd>
<p>Specifies the module handle. This parameter indicates which module is calling the method.</p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK. If the method fails, it returns a standard COM error code.</p>

## -remarks
<p>The minidriver should call <b>CoCreateInstance</b> or <b>CoCreateInstanceEx </b>(which are described in the Microsoft Windows SDK documentation) to obtain the <b>IWiaLog</b> interface.</p>

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