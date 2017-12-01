---
UID: NF.wdm.RtlValidRelativeSecurityDescriptor
title: RtlValidRelativeSecurityDescriptor
author: windows-driver-content
description: The RtlValidRelativeSecurityDescriptor routine checks the validity of a self-relative security descriptor.
old-location: kernel\rtlvalidrelativesecuritydescriptor.htm
old-project: kernel
ms.assetid: 1fb993f0-4289-4406-8a56-47b12c73f4e6
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: RtlValidRelativeSecurityDescriptor
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
req.alt-api: RtlValidRelativeSecurityDescriptor
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
req.irql: <= APC_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# RtlValidRelativeSecurityDescriptor function



## -description
<p>The <b>RtlValidRelativeSecurityDescriptor</b> routine checks the validity of a self-relative security descriptor.</p>


## -syntax

````
BOOLEAN RtlValidRelativeSecurityDescriptor(
  _In_ PSECURITY_DESCRIPTOR SecurityDescriptorInput,
  _In_ ULONG                SecurityDescriptorLength,
  _In_ SECURITY_INFORMATION RequiredInformation
);
````


## -parameters
<dl>

### -param <i>SecurityDescriptorInput</i> [in]

<dd>
<p>A pointer to the buffer that contains the security descriptor in self-relative format. The buffer must begin with a <a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a> structure, which is followed by the rest of the security descriptor data.</p>
</dd>

### -param <i>SecurityDescriptorLength</i> [in]

<dd>
<p>The size of the <i>SecurityDescriptorInput</i> structure. </p>
</dd>

### -param <i>RequiredInformation</i> [in]

<dd>
<p>A <a href="ifsk.security_information">SECURITY_INFORMATION</a> value that specifies the information that is required to be contained in the security descriptor. </p>
</dd>
</dl>

## -returns
<p><b>RtlValidRelativeSecurityDescriptor</b> returns <b>TRUE</b> if the security descriptor is valid and includes the information that the <i>RequiredInformation</i> parameter specifies. Otherwise, this routine returns <b>FALSE</b>.</p>

## -remarks
<p>To check the validity of a security descriptor in absolute format, use <a href="..\wdm\nf-wdm-rtlvalidsecuritydescriptor.md">RtlValidSecurityDescriptor</a> instead.</p>

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
<p>Available starting with Windows 2000.</p>
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
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-rtlvalidsecuritydescriptor.md">RtlValidSecurityDescriptor</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--security-descriptor.md">SECURITY_DESCRIPTOR</a>
</dt>
<dt>
<a href="ifsk.security_information">SECURITY_INFORMATION</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20RtlValidRelativeSecurityDescriptor routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
