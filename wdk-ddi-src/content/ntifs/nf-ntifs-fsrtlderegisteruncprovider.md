---
UID: NF.ntifs.FsRtlDeregisterUncProvider
title: FsRtlDeregisterUncProvider function
author: windows-driver-content
description: The FsRtlDeregisterUncProvider routine deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP).
old-location: ifsk\fsrtlderegisteruncprovider.htm
old-project: ifsk
ms.assetid: 3f53a22f-b5d6-4e3d-987d-989bd5840b2a
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlDeregisterUncProvider
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
req.alt-api: FsRtlDeregisterUncProvider
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
---

# FsRtlDeregisterUncProvider function



## -description
The <b>FsRtlDeregisterUncProvider</b> routine deregisters a redirector that was registered as a Universal Naming Convention (UNC) provider with the multiple UNC provider (MUP).


## -syntax

````
VOID FsRtlDeregisterUncProvider(
  _In_ HANDLE Handle
);
````


## -parameters

### -param Handle [in]

MUP handle returned by <a href="ifsk.fsrtlregisteruncprovider">FsRtlRegisterUncProvider</a> or <a href="ifsk.fsrtlregisteruncproviderex">FsRtlRegisterUncProviderEx</a>.

## -returns
None

## -remarks
To register a UNC provider on Windows Server 2003, Windows XP, or Windows 2000, use <a href="ifsk.fsrtlregisteruncprovider">FsRtlRegisterUncProvider</a>. 

To register a UNC provider on Windows Vista, use <a href="ifsk.fsrtlregisteruncproviderex">FsRtlRegisterUncProviderEx</a>.

For more information, see the following sections in the Design Guide:


<a href="ifsk.support_for_unc_naming_and_mup">Support for UNC Naming and MUP</a>



<a href="ifsk.mup_changes_in_microsoft_windows_vista">MUP Changes in Microsoft Windows Vista</a>


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
PASSIVE_LEVEL
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsrtlregisteruncprovider">FsRtlRegisterUncProvider</a>
</dt>
<dt>
<a href="ifsk.fsrtlregisteruncproviderex">FsRtlRegisterUncProviderEx</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlDeregisterUncProvider routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
