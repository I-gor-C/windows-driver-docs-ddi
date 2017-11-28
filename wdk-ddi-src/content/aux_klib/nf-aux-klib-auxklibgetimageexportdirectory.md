---
UID: NF.aux_klib.AuxKlibGetImageExportDirectory
title: AuxKlibGetImageExportDirectory
author: windows-driver-content
description: The AuxKlibGetImageExportDirectory routine returns an image module's export directory.
old-location: kernel\auxklibgetimageexportdirectory.htm
old-project: kernel
ms.assetid: 994ba853-88b6-4456-8fdb-3199979df05e
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: AuxKlibGetImageExportDirectory
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: aux_klib.h
req.include-header: Aux_klib.h
req.target-type: Universal
req.target-min-winverclnt: Supported starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: AuxKlibGetImageExportDirectory
req.alt-loc: Aux_Klib.lib,Aux_Klib.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Aux_Klib.lib
req.dll: 
req.irql: 
req.iface: 
---

# AuxKlibGetImageExportDirectory function



## -description
<p>The <b>AuxKlibGetImageExportDirectory</b> routine returns an image module's export directory.</p>


## -syntax

````
PIMAGE_EXPORT_DIRECTORY AuxKlibGetImageExportDirectory(
  _In_ PVOID ImageBase
);
````


## -parameters
<dl>

### -param <i>ImageBase</i> [in]

<dd>
<p>A pointer to the base of an image, which is obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff540639">AuxKlibQueryModuleInformation</a>. </p>
</dd>
</dl>

## -returns
<p><b>AuxKlibGetImageExportDirectory</b> returns a pointer to an <b>IMAGE_EXPORT_DIRECTORY</b> structure. This structure is defined in Ntimage.h, which is included in the Microsoft Windows Driver Kit (WDK).</p>

## -remarks
<p>Drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff540636">AuxKlibInitialize</a> before calling <b>AuxKlibGetImageExportDirectory</b>.</p>

<p>Drivers must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff540636">AuxKlibInitialize</a> before calling <b>AuxKlibGetImageExportDirectory</b>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with Windows 2000.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Aux_klib.h (include Aux_klib.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Aux_Klib.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540639">AuxKlibQueryModuleInformation</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20AuxKlibGetImageExportDirectory routine%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
