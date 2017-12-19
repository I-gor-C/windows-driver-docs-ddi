---
UID: NF.wdm.RtlAnsiStringToUnicodeSize
title: RtlAnsiStringToUnicodeSize macro
author: windows-driver-content
description: The RtlAnsiStringToUnicodeSize routine returns the number of bytes required to hold an ANSI string converted into a Unicode string.
old-location: kernel\rtlansistringtounicodesize.htm
old-project: kernel
ms.assetid: 32687aa7-4e14-40cb-baa3-4a97d834bf86
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlAnsiStringToUnicodeSize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAnsiStringToUnicodeSize
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# RtlAnsiStringToUnicodeSize macro



## -description
The <b>RtlAnsiStringToUnicodeSize</b> routine returns the number of bytes required to hold an ANSI string converted into a Unicode string. 



## -syntax

````
ULONG RtlAnsiStringToUnicodeSize(
  _In_ PANSI_STRING AnsiString
);
````


## -parameters

### -param AnsiString [in]

Pointer to a buffer containing the ANSI string. 


## -remarks
Callers of <b>RtlAnsiStringToUnicodeSize</b> must be running at IRQL = PASSIVE_LEVEL.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlansistringtounicodestring">RtlAnsiStringToUnicodeString</a>
</dt>
<dt>
<a href="kernel.rtlxansistringtounicodesize">RtlxAnsiStringToUnicodeSize</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlAnsiStringToUnicodeSize routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

