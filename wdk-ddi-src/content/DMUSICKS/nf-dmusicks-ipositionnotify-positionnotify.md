---
UID: NF.dmusicks.IPositionNotify.PositionNotify
title: IPositionNotify::PositionNotify
author: windows-driver-content
description: Byte position notify for MXF graph.
old-location: audio\ipositionnotify_positionnotify.htm
ms.assetid: 1C29A0B4-E50D-4EA2-95A4-4845BD14C88A
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: audio
req.header: dmusicks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPositionNotify.PositionNotify
req.alt-loc: Dmusicks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: IPositionNotify, PositionNotify, IPositionNotify::PositionNotify
req.iface: IPositionNotify
---

# IPositionNotify::PositionNotify method



## -description
<p>Byte position notify for MXF graph.</p>


## -syntax

````
HRESULT PositionNotify(
  [in] ULONGLONG bytePosition
);
````


## -parameters
<dl>

### -param <i>bytePosition</i> [in]

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
<dt>Dmusicks.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/DB18BD9D-4BAA-48D8-BA30-E4F7EF4CDEE5">IPositionNotify</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPositionNotify::PositionNotify method%20 RELEASE:%20(10/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
