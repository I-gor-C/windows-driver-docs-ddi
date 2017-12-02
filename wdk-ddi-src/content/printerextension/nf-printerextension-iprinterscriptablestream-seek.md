---
UID: NF.printerextension.IPrinterScriptableStream.Seek
title: IPrinterScriptableStream::Seek
author: windows-driver-content
description: Sets the seek pointer.
old-location: print\iprinterscriptablestream__seek.htm
old-project: print
ms.assetid: 82080353-2252-4BF2-B7F4-F297DCA99FA0
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrinterScriptableStream, Seek, IPrinterScriptableStream::Seek
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: printerextension.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrinterScriptableStream.Seek
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
req.iface: IPrinterScriptableStream
req.product: Windows 10 or later.
---

# IPrinterScriptableStream::Seek method



## -description
<p>Sets the seek pointer.</p>


## -syntax

````
HRESULT Seek(
  [in]          LONG        lOffset,
  [in]          STREAM_SEEK streamSeek,
  [out, retval] LONG        *plPosition
);
````


## -parameters
<dl>

### -param lOffset [in]

<dd>
<p>The displacement to be added to the location indicated by the <i>streamSeek</i> parameter.</p>
</dd>

### -param streamSeek [in]

<dd>
<p>The origin for the displacement specified <i>lOffset</i>.</p>
</dd>

### -param plPosition [out, retval]

<dd>
<p>The new pointer position.</p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
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
<dt>Printerextension.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\printerextension\nn-printerextension-iprinterscriptablestream.md">IPrinterScriptableStream</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrinterScriptableStream::Seek method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
