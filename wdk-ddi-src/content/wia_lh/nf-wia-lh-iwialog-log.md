---
UID: NF.wia_lh.IWiaLog.Log
title: IWiaLog::Log
author: windows-driver-content
description: The IWiaLog interface is obsolete for Windows XP and later, and is no longer supported. Use the Diagnostic Log Macros instead.The IWiaLog::Log method writes a diagnostic log message to Wiaservc.log.
old-location: image\iwialog_log.htm
old-project: image
ms.assetid: bca012b4-76ae-4ba5-99b4-92a367774de7
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IWiaLog, Log, IWiaLog::Log
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
req.alt-api: IWiaLog.Log
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

# IWiaLog::Log method



## -description
<p>The <b>IWiaLog</b> interface is obsolete for Windows XP and later, and is no longer supported. Use the <a href="image.diagnostic_log_macros">Diagnostic Log Macros</a> instead.The <b>IWiaLog::Log</b> method writes a diagnostic log message to <i>Wiaservc.log</i>.</p>


## -syntax

````
HRESULT Log(
  [in] LONG lFlags,
  [in] LONG lResId,
  [in] LONG lDetail,
  [in] BSTR bstrText
);
````


## -parameters
<dl>

### -param <i>lFlags</i> [in]

<dd>
<p>Specifies the type of diagnostic message. This parameter can be WIA_WARNING, WIA_TRACE or WIA_ERROR.</p>
</dd>

### -param <i>lResId</i> [in]

<dd>
<p>Specifies the resource id. This parameter should be set to WIALOG_NO_RESOURCE_ID.</p>
</dd>

### -param <i>lDetail</i> [in]

<dd>
<p>Specifies the diagnostic detail level of the message. This parameter can be one of the following values.</p>
<table>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>WIALOG_LEVEL1</p>
</td>
<td>
<p>Logs entry and exit points for all WIA methods and functions.</p>
</td>
</tr>
<tr>
<td>
<p>WIALOG_LEVEL2</p>
</td>
<td>
<p>Logs additional details for WIALOG_LEVEL1.</p>
</td>
</tr>
<tr>
<td>
<p>WIALOG_LEVEL3</p>
</td>
<td>
<p>Logs entry and exit points for all WIA methods and functions and additional vendor-supplied functions.</p>
</td>
</tr>
<tr>
<td>
<p>WIALOG_LEVEL4</p>
</td>
<td>
<p>Logs additional details for WIALOG_LEVEL3. </p>
</td>
</tr>
<tr>
<td>
<p>WIALOG_LEVELXXX</p>
</td>
<td>
<p>User-defined log levels.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -param <i>bstrText</i> [in]

<dd>
<p>Specifies the error text. The error text should be prefixed with the full name of the method or function and generate the message in the format of "class::method, error-text".</p>
</dd>
</dl>

## -returns
<p>If the method succeeds, it returns S_OK.  If the method fails, it returns a standard COM error code.</p>

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