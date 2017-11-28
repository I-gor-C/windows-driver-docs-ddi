---
UID: NF.printerextension.IPrinterScriptablePropertyBag2.GetReadStreamAsXML
title: IPrinterScriptablePropertyBag2::GetReadStreamAsXML
author: windows-driver-content
description: .
old-location: print\iprinterscriptablepropertybag2_getreadstreamasxml.htm
old-project: print
ms.assetid: 1C6477C4-3038-4F8A-871F-7F336E631C8F
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterScriptablePropertyBag2, GetReadStreamAsXML, IPrinterScriptablePropertyBag2::GetReadStreamAsXML
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterScriptablePropertyBag2.GetReadStreamAsXML
req.alt-loc: Printerextension.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: IPrinterScriptablePropertyBag2
req.product: Windows 10 or later.
---

# IPrinterScriptablePropertyBag2::GetReadStreamAsXML method



## -description
<p></p>


## -syntax

````
HRESULT GetReadStreamAsXML(
  [in]  BSTR     bstrName,
  [out] IUnknown **ppXmlNode
);
````


## -parameters
<dl>

### -param <i>bstrName</i> [in]

<dd></dd>

### -param <i>ppXmlNode</i> [out]

<dd></dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablepropertybag2.md">IPrinterScriptablePropertyBag2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptablePropertyBag2::GetReadStreamAsXML method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
