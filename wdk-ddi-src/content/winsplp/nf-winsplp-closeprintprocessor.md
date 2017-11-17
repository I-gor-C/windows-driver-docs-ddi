---
UID: NF.winsplp.ClosePrintProcessor
title: ClosePrintProcessor
author: windows-driver-content
description: A print processor's ClosePrintProcessor function completes the printing of a print job and makes the associated handle invalid.
old-location: print\closeprintprocessor.htm
ms.assetid: 3cf87a18-8b5a-40f2-9c0e-2b29167e283d
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ClosePrintProcessor
req.alt-loc: Nwprint.lib,Nwprint.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Nwprint.lib
req.dll: 
req.irql: 
ms.keywords: ClosePrintProcessor
req.iface: 
req.product: Windows 10 or later.
---

# ClosePrintProcessor function



## -description
<p>A print processor's <b>ClosePrintProcessor</b> function completes the printing of a print job and makes the associated handle invalid.</p>


## -syntax

````
BOOL ClosePrintProcessor(
  _Inout_ HANDLE hPrintProcessor
);
````


## -parameters
<dl>

### -param <i>hPrintProcessor</i> [in, out]

<dd>
<p>Caller-supplied print processor handle. This is the handle returned by a previous call to <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function should return <b>TRUE</b>. If the operation fails, the function should call SetLastError to set an error code, and then return <b>FALSE</b>.</p>

## -remarks
<p>Print processors are required to export a <b>ClosePrintProcessor</b> function. The spooler calls the function after the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> returns. The function should free all resources that were allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

<p>Print processors are required to export a <b>ClosePrintProcessor</b> function. The spooler calls the function after the print processor's <a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a> returns. The function should free all resources that were allocated by the <a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a> function.</p>

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
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Nwprint.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff559604">OpenPrintProcessor</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560724">PrintDocumentOnPrintProcessor</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20ClosePrintProcessor function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
