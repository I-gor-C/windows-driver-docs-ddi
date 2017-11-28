---
UID: NF.ntifs.RtlOemStringToCountedUnicodeSize
title: RtlOemStringToCountedUnicodeSize
author: windows-driver-content
description: The RtlOemStringToCountedUnicodeSize routine determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string.
old-location: ifsk\rtloemstringtocountedunicodesize.htm
old-project: ifsk
ms.assetid: a618420f-ea69-471d-82a0-1e86f85e270b
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RtlOemStringToCountedUnicodeSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlOemStringToCountedUnicodeSize
req.alt-loc: ntifs.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: < DISPATCH_LEVEL
req.iface: 
---

# RtlOemStringToCountedUnicodeSize function



## -description
<p>The <b>RtlOemStringToCountedUnicodeSize</b> routine determines the size, in bytes, that a given OEM string will be after it is translated into a counted Unicode string. </p>


## -syntax

````
ULONG RtlOemStringToCountedUnicodeSize(
  _In_ POEM_STRING OemString
);
````


## -parameters
<dl>

### -param <i>OemString</i> [in]

<dd>
<p>Pointer to a caller-allocated OEM string. </p>
</dd>
</dl>

## -returns
<p><b>RtlOemStringToCountedUnicodeSize</b> returns the number of bytes that are required to contain a given OEM string when it has been translated into a counted Unicode string. </p>

## -remarks
<p><b>RtlOemStringToCountedUnicodeSize</b> can be called to determine how much memory to allocate when translating an OEM string to Unicode with <b>RtlOemStringToCountedUnicodeString</b>. The returned value does not include space for a NULL terminator for the Unicode string.</p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

<p><b>RtlOemStringToCountedUnicodeSize</b> can be called to determine how much memory to allocate when translating an OEM string to Unicode with <b>RtlOemStringToCountedUnicodeString</b>. The returned value does not include space for a NULL terminator for the Unicode string.</p>

<p>For information about other string-handling routines, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563884">Strings</a>. </p>

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
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt; DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff558741">OEM_STRING</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553142">RtlOemStringToCountedUnicodeString</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553147">RtlOemStringToUnicodeSize</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlOemStringToCountedUnicodeSize routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
