---
UID: NF.wdm.RtlAppendUnicodeStringToString
title: RtlAppendUnicodeStringToString function
author: windows-driver-content
description: The RtlAppendUnicodeStringToString routine concatenates two Unicode strings.
old-location: kernel\rtlappendunicodestringtostring.htm
old-project: kernel
ms.assetid: fb076688-ae8e-430b-ac06-dfef7284591d
ms.author: windowsdriverdev
ms.date: 12/15/2017
ms.keywords: RtlAppendUnicodeStringToString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlAppendUnicodeStringToString
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
req.irql: See Remarks section.
req.product: Windows 10 or later.
---

# RtlAppendUnicodeStringToString function



## -description
The <b>RtlAppendUnicodeStringToString</b> routine concatenates two Unicode strings. 



## -syntax

````
NTSTATUS RtlAppendUnicodeStringToString(
  _Inout_ PUNICODE_STRING  Destination,
  _In_    PCUNICODE_STRING Source
);
````


## -parameters

### -param Destination [in, out]

Pointer to a buffered Unicode string.


### -param Source [in]

Pointer to the buffered string to be concatenated. 


## -returns
<b>RtlAppendUnicodeStringToString</b> can return one of the following:
<dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl>The source string was successfully appended to the destination counted string. The destination string length is updated to include the appended bytes.
<dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl>The destination string length is too small to allow the source string to be concatenated. Accordingly, the destination string length is not updated.

 


## -remarks
<b>RtlAppendUnicodeStringToString</b> copies bytes from the source up to the length of the destination buffer.

The <i>Destination</i> and <i>Source</i> buffers must be resident if the caller is running at IRQL &gt;= DISPATCH_LEVEL. 


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
See Remarks section.

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.rtlappendunicodetostring">RtlAppendUnicodeToString</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlAppendUnicodeStringToString routine%20 RELEASE:%20(12/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

