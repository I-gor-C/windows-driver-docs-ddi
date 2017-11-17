---
UID: NF.printerextension.IPrinterPropertyBag.GetBytes
title: IPrinterPropertyBag::GetBytes
author: windows-driver-content
description: Reads a byte array property.
old-location: print\iprinterpropertybag_getbytes.htm
ms.assetid: F75E182D-90FA-4597-95E0-60A6326CF68D
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: printerextension.h
req.include-header: Printerextension.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterPropertyBag.GetBytes
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
ms.keywords: IPrinterPropertyBag, GetBytes, IPrinterPropertyBag::GetBytes
req.iface: IPrinterPropertyBag
req.product: Windows 10 or later.
---

# IPrinterPropertyBag::GetBytes method



## -description
<p>Reads a byte array property.</p>
<p>The <a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a> interface is used by all the printer property bags, including driver property bag, user property bag, queue property bag, and DEVMODE property bag.</p>


## -syntax

````
HRESULT GetBytes(
  [in]  BSTR  bstrName,
  [out] DWORD *pcbValue,
  [out] BYTE  *rgbValue
);
````


## -parameters
<dl>

### -param <i>bstrName</i> [in]

<dd>
<p>The property to read.</p>
</dd>

### -param <i>pcbValue</i> [out]

<dd>
<p>The number of bytes read.</p>
</dd>

### -param <i>rgbValue</i> [out]

<dd>
<p>The returned array. This array must be freed by using CoTaskFree.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

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
<dt>Printerextension.h (include Printerextension.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439547">IPrinterPropertyBag</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterPropertyBag::GetBytes method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
