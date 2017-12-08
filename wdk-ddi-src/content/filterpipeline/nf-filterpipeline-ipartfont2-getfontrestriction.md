---
UID: NF.filterpipeline.IPartFont2.GetFontRestriction
title: IPartFont2::GetFontRestriction
author: windows-driver-content
description: .
old-location: print\ipartfont2_getfontrestriction.htm
old-project: print
ms.assetid: C6289E38-281A-46A2-8E28-138A20BF6684
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPartFont2, GetFontRestriction, IPartFont2::GetFontRestriction
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: filterpipeline.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPartFont2.GetFontRestriction
req.alt-loc: Filterpipeline.h
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
req.iface: IPartFont2
---

# IPartFont2::GetFontRestriction method



## -description
<p></p>


## -syntax

````
HRESULT GetFontRestriction(
  [out] EXpsFontRestriction *pRestriction
);
````


## -parameters
<dl>

### -param pRestriction [out]

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
<dt>Filterpipeline.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\filterpipeline\nn-filterpipeline-ipartfont2.md">IPartFont2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPartFont2::GetFontRestriction method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
