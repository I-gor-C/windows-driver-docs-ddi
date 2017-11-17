---
UID: NF.prcomoem.IPrintCoreHelperUni.CreateGDLSnapshot
title: IPrintCoreHelperUni::CreateGDLSnapshot
author: windows-driver-content
description: The IPrintCoreHelperUni::CreateGDLSnapshot method creates a GDL snapshot of the driver configuration file based on the current configuration.
old-location: print\iprintcorehelperuni_creategdlsnapshot.htm
ms.assetid: 3dd9c7f9-27d4-45d2-8692-4270818c1823
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: prcomoem.h
req.include-header: Prcomoem.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreHelperUni.CreateGDLSnapshot
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
ms.keywords: IPrintCoreHelperUni, CreateGDLSnapshot, IPrintCoreHelperUni::CreateGDLSnapshot
req.iface: IPrintCoreHelperUni
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni::CreateGDLSnapshot method



## -description
<p>The <code>IPrintCoreHelperUni::CreateGDLSnapshot</code> method creates a GDL snapshot of the driver configuration file based on the current configuration. </p>


## -syntax

````
HRESULT CreateGDLSnapshot(
  [in]  PDEVMODE pDevmode,
  [in]  DWORD    cbSize,
  [in]  DWORD    dwFlags,
  [out] LPSTREAM *ppSnapshotStream
);
````


## -parameters
<dl>

### -param <i>pDevmode</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff552837">DEVMODEW</a> structure. If this pointer is provided, <code>IPrintCoreHelperUni::CreateGDLSnapshot</code>  should use the DEVMODEW structure that is pointed to by <i>pDevmode</i> instead of the default or current DEVMODEW structure. If this method is called from the plug-in provider, there is no default DEVMODEW structure and the <i>pDevmode</i> parameter is required.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>The size, in bytes, of the DEVMODEW structure that is pointed to by the <i>pDevmode</i> parameter. </p>
</dd>

### -param <i>dwFlags</i> [in]

<dd>
<p>Reserved for system use. This parameter must be set to zero.</p>
</dd>

### -param <i>ppSnapshotStream</i> [out]

<dd>
<p>A pointer to a stream that supplies the XML version of the GDL snapshot.</p>
</dd>
</dl>

## -returns
<p><code>IPrintCoreHelperUni::CreateGDLSnapshot</code> should return S_OK if the operation succeeds. Otherwise, this method should return a standard COM error code.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff552917">IPrintCoreHelperUni::CreateDefaultGDLSnapshot</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelperUni::CreateGDLSnapshot method%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
