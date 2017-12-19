---
UID: NF.wia_lh.IWiaLog.Log
title: IWiaLog::Log method
author: windows-driver-content
description: The IWiaLog interface is obsolete for Windows XP and later, and is no longer supported. Use the Diagnostic Log Macros instead.The IWiaLog::Log method writes a diagnostic log message to Wiaservc.log.
old-location: image\iwialog_log.htm
old-project: Image
ms.assetid: bca012b4-76ae-4ba5-99b4-92a367774de7
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IWiaLog, IWiaLog::Log, Log
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
req.product: Windows 10 or later.
---

# IWiaLog::Log method



## -description
The <b>IWiaLog</b> interface is obsolete for Windows XP and later, and is no longer supported. Use the <a href="image.diagnostic_log_macros">Diagnostic Log Macros</a> instead.The <b>IWiaLog::Log</b> method writes a diagnostic log message to <i>Wiaservc.log</i>.



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

### -param lFlags [in]

Specifies the type of diagnostic message. This parameter can be WIA_WARNING, WIA_TRACE or WIA_ERROR.


### -param lResId [in]

Specifies the resource id. This parameter should be set to WIALOG_NO_RESOURCE_ID.


### -param lDetail [in]

Specifies the diagnostic detail level of the message. This parameter can be one of the following values.

<table>
<tr>
<th>Level</th>
<th>Description</th>
</tr>
<tr>
<td>
WIALOG_LEVEL1

</td>
<td>
Logs entry and exit points for all WIA methods and functions.

</td>
</tr>
<tr>
<td>
WIALOG_LEVEL2

</td>
<td>
Logs additional details for WIALOG_LEVEL1.

</td>
</tr>
<tr>
<td>
WIALOG_LEVEL3

</td>
<td>
Logs entry and exit points for all WIA methods and functions and additional vendor-supplied functions.

</td>
</tr>
<tr>
<td>
WIALOG_LEVEL4

</td>
<td>
Logs additional details for WIALOG_LEVEL3. 

</td>
</tr>
<tr>
<td>
WIALOG_LEVELXXX

</td>
<td>
User-defined log levels.

</td>
</tr>
</table>
 


### -param bstrText [in]

Specifies the error text. The error text should be prefixed with the full name of the method or function and generate the message in the format of "class::method, error-text".


## -returns
If the method succeeds, it returns S_OK.  If the method fails, it returns a standard COM error code.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Windows Me, Windows XP, and later. Obsoletefor Microsoft Windows XP and later, and is no longer supported. Instead, use the Diagnostic Log Macros.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wia_lh.h (include Wia.h)</dt>
</dl>
</td>
</tr>
</table>