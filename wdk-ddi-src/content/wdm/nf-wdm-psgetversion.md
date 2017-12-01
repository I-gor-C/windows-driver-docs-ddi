---
UID: NF.wdm.PsGetVersion
title: PsGetVersion
author: windows-driver-content
description: This function is obsolete in Windows XP and later versions of the Windows operating system. Use RtlGetVersion instead.PsGetVersion returns caller-selected information about the current version of the NT-based operating system.
old-location: kernel\psgetversion.htm
old-project: kernel
ms.assetid: db3d2e34-3d83-423d-b446-2800d53a8220
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PsGetVersion
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdm.h
req.include-header: Ntddk.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PsGetVersion
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: IrqlPsPassive, PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
req.product: Windows 10 or later.
---

# PsGetVersion function



## -description
<p>This function is <u>obsolete</u> in Windows XP and later versions of the Windows operating system. Use <a href="..\wdm\nf-wdm-rtlgetversion.md">RtlGetVersion</a> instead.</p>
<p><b>PsGetVersion</b> returns caller-selected information about the current version of the NT-based operating system. </p>


## -syntax

````
BOOLEAN PsGetVersion(
  _Out_opt_ PULONG          MajorVersion,
  _Out_opt_ PULONG          MinorVersion,
  _Out_opt_ PULONG          BuildNumber,
  _Out_opt_ PUNICODE_STRING CSDVersion
);
````


## -parameters
<dl>

### -param <i>MajorVersion</i> [out, optional]

<dd>
<p>Points to a caller-supplied variable that this routine sets to the major version of the operating system. This optional parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>MinorVersion</i> [out, optional]

<dd>
<p>Points to a caller-supplied variable that this routine sets to the minor version of the operating system. This optional parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>BuildNumber</i> [out, optional]

<dd>
<p>Points to a caller-supplied variable that this routine sets to the current build number of the operating system. This optional parameter can be <b>NULL</b>. </p>
</dd>

### -param <i>CSDVersion</i> [out, optional]

<dd>
<p>Points to a caller-allocated buffer in which this routine returns the current service-pack version as a Unicode string only during system driver initialization. This optional parameter can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>PsGetVersion</b> returns whether the system is a checked or free build, as follows:</p><dl>
<dt><b><b>TRUE</b> (1)</b></dt>
</dl><p>Checked build of the operating system.</p><dl>
<dt><b><b>FALSE</b> (0)</b></dt>
</dl><p>Free build of the operating system. </p>

<p> </p>

## -remarks
<p><b>PsGetVersion</b> returns the requested information, depending on which optional parameter(s) the caller supplies.</p>

<p>To retrieve the current service-pack number, it is easier and more efficient to make an application-level call within the Win32 environment than to call <b>PsGetVersion</b> during system driver initialization, which then must parse the string it returns at <i>CSDVersion</i>. When the registry is initialized, a driver cannot obtain this string from <b>PsGetVersion</b>, but must read the <b>CmCSDVersionString</b> value from the registry. </p>

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
<dt>Wdm.h (include Ntddk.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_irqlpspassive">IrqlPsPassive</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>