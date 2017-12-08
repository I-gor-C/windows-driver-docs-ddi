---
UID: NF.wdm.RtlStringFromGUID
title: RtlStringFromGUID function
author: windows-driver-content
description: The RtlStringFromGUID routine converts a given GUID from binary format into a Unicode string.
old-location: kernel\rtlstringfromguid.htm
old-project: kernel
ms.assetid: 89a3ca92-7c8a-40e3-a818-0127af6f2e91
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: RtlStringFromGUID
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
req.alt-api: RtlStringFromGUID
req.alt-loc: NtosKrnl.exe,Ntdll.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode); Ntdll.dll (user mode)
req.irql: PASSIVE_LEVEL
req.product: Windows 10 or later.
---

# RtlStringFromGUID function



## -description
The <b>RtlStringFromGUID</b> routine converts a given GUID from binary format into a Unicode string. 


## -syntax

````
NTSTATUS RtlStringFromGUID(
  _In_  REFGUID         Guid,
  _Out_ PUNICODE_STRING GuidString
);
````


## -parameters

### -param Guid [in]

Specifies the binary-format GUID to convert. 

### -param GuidString [out]

Pointer to a caller-supplied variable in which a pointer to the converted GUID string is returned. <b>RtlStringFromGUID</b> allocates the buffer space for the string, which the caller must free by calling <b>RtlFreeUnicodeString</b>. 

## -returns
If the conversion succeeds, <b>RtlStringFromGUID</b> returns STATUS_SUCCESS. Otherwise, no storage was allocated, nor was the conversion performed.

## -remarks


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
<dt>NtosKrnl.exe (kernel mode); </dt>
<dt>Ntdll.dll (user mode)</dt>
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
<a href="kernel.rtlguidfromstring">RtlGUIDFromString</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlStringFromGUID routine%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
