---
UID: NF.wdm.RtlCmEncodeMemIoResource
title: RtlCmEncodeMemIoResource
author: windows-driver-content
description: The RtlCmEncodeMemIoResource routine updates a CM_PARTIAL_RESOURCE_DESCRIPTOR structure to describe a range of memory or I/O port addresses.
old-location: kernel\rtlcmencodememioresource.htm
old-project: kernel
ms.assetid: 69b978a2-3895-42fc-a87a-a97064d02e7a
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlCmEncodeMemIoResource
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlCmEncodeMemIoResource
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
req.irql: Any level
req.iface: 
req.product: Windows 10 or later.
---

# RtlCmEncodeMemIoResource function



## -description
<p>The <b>RtlCmEncodeMemIoResource</b> routine updates a <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure to describe a range of memory or I/O port addresses.</p>


## -syntax

````
NTSTATUS RtlCmEncodeMemIoResource(
  _In_ PCM_PARTIAL_RESOURCE_DESCRIPTOR Descriptor,
  _In_ UCHAR                           Type,
  _In_ ULONGLONG                       Length,
  _In_ ULONGLONG                       Start
);
````


## -parameters
<dl>

### -param <i>Descriptor</i> [in]

<dd>
<p>A pointer to the <a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a> structure to update. </p>
</dd>

### -param <i>Type</i> [in]

<dd>
<p>The resource type of the memory. This parameter can be <b>CmResourceTypeMemory</b>, <b>CmResourceTypeMemoryLarge</b>, or <b>CmResourceTypePort</b>.</p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>The length, in bytes, of the range of allocated addresses.</p>
</dd>

### -param <i>Start</i> [in]

<dd>
<p>The starting address of the range of memory or I/O port addresses.</p>
</dd>
</dl>

## -returns
<p><b>RtlCmEncodeMemIoResource</b> returns an NTSTATUS value. This routine might return one of the following values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure has been updated.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The specified value for <i>Length</i> cannot be encoded in a <b>CM_PARTIAL_RESOURCE_DESCRIPTOR</b> structure.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p>One or more of the specified parameters are invalid.</p>

<p> </p>

## -remarks
<p>Addresses that are larger than 32 bits in length must satisfy certain alignment restrictions or else the routine returns STATUS_UNSUCCESSFUL.</p>

<p>40 bits</p>

<p>Lowest 8 bits must be zero.</p>

<p>48 bits</p>

<p>Lowest 16 bits must be zero.</p>

<p>64 bits</p>

<p>Lowest 32 bits must be zero.</p>

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
<p>Available in Windows Vista and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--cm-partial-resource-descriptor.md">CM_PARTIAL_RESOURCE_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-rtlcmdecodememioresource.md">RtlCmDecodeMemIoResource</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlCmEncodeMemIoResource routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
