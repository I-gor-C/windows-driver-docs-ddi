---
UID: NF.ntifs.RtlOemStringToCountedUnicodeString
title: RtlOemStringToCountedUnicodeString function
author: windows-driver-content
description: The RtlOemStringToCountedUnicodeString routine translates the specified source string into a Unicode string using the current system OEM code page.
old-location: ifsk\rtloemstringtocountedunicodestring.htm
old-project: ifsk
ms.assetid: bf36d51f-3e22-489b-a597-652f39242a30
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: RtlOemStringToCountedUnicodeString
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlOemStringToCountedUnicodeString
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
req.irql: < DISPATCH_LEVEL
---

# RtlOemStringToCountedUnicodeString function



## -description
The <b>RtlOemStringToCountedUnicodeString</b> routine translates the specified source string into a Unicode string using the current system OEM code page. 



## -syntax

````
NTSTATUS RtlOemStringToCountedUnicodeString(
       PUNICODE_STRING DestinationString,
  _In_ PCOEM_STRING    SourceString,
  _In_ BOOLEAN         AllocateDestinationString
);
````


## -parameters

### -param DestinationString 

Pointer to a caller-allocated buffer to receive the translated Unicode string. If <i>AllocateDestinationString</i> is <b>FALSE</b>, the caller must also allocate a buffer for the <b>Buffer</b> member of <i>DestinationString</i> to hold the Unicode data. If <i>AllocateDestinationString</i> is <b>TRUE</b>, <b>RtlOemStringToCountedUnicodeString</b> allocates a buffer large enough to hold the string, passes a pointer to it in <b>Buffer</b>, and updates the length and maximum length members of <i>DestinationString</i> accordingly. 


### -param SourceString [in]

Pointer to the OEM string to be translated into Unicode. 


### -param AllocateDestinationString [in]

Set to <b>TRUE</b> if <b>RtlOemStringToCountedUnicodeString</b> should allocate the buffer space for the <i>DestinationString</i>, <b>FALSE</b> otherwise. If this parameter is <b>TRUE</b>, the caller is responsible for freeing the buffer when it is no longer needed by calling <b>RtlFreeUnicodeString</b>. 


## -returns
If the operation succeeds, <b>RtlOemStringToCountedUnicodeString</b> returns STATUS_SUCCESS. Otherwise, no storage was allocated and no conversion was done. 


## -remarks
<b>RtlOemStringToCountedUnicodeString</b> returns a translated string that does not include NULL terminator. It translates the given source string using the OEM code page that was installed as the current system code page at boot time. 

<b>RtlOemStringToCountedUnicodeString</b> does not modify the source string. 

For information about other string-handling routines, see <a href="kernel.strings">Strings</a>. 


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
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
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
&lt; DISPATCH_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.oem_string">OEM_STRING</a>
</dt>
<dt>
<a href="kernel.rtlfreeunicodestring">RtlFreeUnicodeString</a>
</dt>
<dt>
<a href="ifsk.rtloemstringtocountedunicodesize">RtlOemStringToCountedUnicodeSize</a>
</dt>
<dt>
<a href="ifsk.rtloemstringtocountedunicodestring">RtlOemStringToCountedUnicodeString</a>
</dt>
<dt>
<a href="ifsk.rtloemtounicoden">RtlOemToUnicodeN</a>
</dt>
<dt>
<a href="kernel.unicode_string">UNICODE_STRING</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RtlOemStringToCountedUnicodeString routine%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

