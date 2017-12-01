---
UID: NF.prcomoem.IPrintCoreHelperUni.CreateDefaultGDLSnapshot
title: IPrintCoreHelperUni::CreateDefaultGDLSnapshot
author: windows-driver-content
description: The IPrintCoreHelperUni::CreateDefaultGDLSnapshot method gets a GDL snapshot based on the driver default configuration.
old-location: print\iprintcorehelperuni_createdefaultgdlsnapshot.htm
old-project: print
ms.assetid: 987c3721-d8a8-4aac-8f42-6eac9b5ccdc5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreHelperUni, CreateDefaultGDLSnapshot, IPrintCoreHelperUni::CreateDefaultGDLSnapshot
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreHelperUni.CreateDefaultGDLSnapshot
req.alt-loc: prcomoem.h
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
req.iface: IPrintCoreHelperUni
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni::CreateDefaultGDLSnapshot method



## -description
<p>The <code>IPrintCoreHelperUni::CreateDefaultGDLSnapshot</code> method gets a GDL snapshot based on the driver default configuration.</p>


## -syntax

````
HRESULT CreateDefaultGDLSnapshot(
  [in]  DWORD    dwFlags,
  [out] LPSTREAM *ppSnapshotStream
);
````


## -parameters
<dl>

### -param <i>dwFlags</i> [in]

<dd>
<p>This parameter is reserved and must be set to zero.</p>
</dd>

### -param <i>ppSnapshotStream</i> [out]

<dd>
<p>A pointer to a stream that supplies the XML version of the GDL snapshot.</p>
</dd>
</dl>

## -returns
<p><code>IPrintCoreHelperUni::CreateDefaultGDLSnapshot</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.</p>

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
<dt>Prcomoem.h (include Prcomoem.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iprintcorehelperuni_creategdlsnapshot">IPrintCoreHelperUni::CreateGDLSnapshot</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelperUni::CreateDefaultGDLSnapshot method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
