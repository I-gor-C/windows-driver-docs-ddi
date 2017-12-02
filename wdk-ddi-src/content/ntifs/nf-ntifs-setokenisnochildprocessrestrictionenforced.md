---
UID: NF.ntifs.SeTokenIsNoChildProcessRestrictionEnforced
title: SeTokenIsNoChildProcessRestrictionEnforced
author: windows-driver-content
description: The SeTokenIsNoChildProcessRestrictionEnforced routine determines if the token carries the no child process restriction.
old-location: ifsk\setokenisnochildprocessrestrictionenforced.htm
old-project: ifsk
ms.assetid: 6D214346-8CE6-4E9C-B054-1C72B928ED2B
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SeTokenIsNoChildProcessRestrictionEnforced
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows 10, version 1709.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SeTokenIsNoChildProcessRestrictionEnforced
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
req.irql: 
req.iface: 
---

# SeTokenIsNoChildProcessRestrictionEnforced function



## -description
<p>The <b>SeTokenIsNoChildProcessRestrictionEnforced</b> routine determines if the token carries the no child process restriction.</p>


## -syntax

````
BOOLEAN NTKERNELAPI SeTokenIsNoChildProcessRestrictionEnforced(
  _In_      PACCESS_TOKEN Token,
  _Out_opt_ PBOOLEAN      UnlessSecure
);
````


## -parameters
<dl>

### -param Token [in]

<dd>
<p>Specifies a pointer to the access token.</p>
</dd>

### -param UnlessSecure [out, optional]

<dd>
<p>Optionally provides a pointer to the value that will
        be set to TRUE when secure process creation is enabled even if
        process creation is restricted.</p>
</dd>
</dl>

## -returns
<p>This routine returns <b>TRUE</b> if <i>Token</i> carries the no child process restriction.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting with Windows 10, version 1709.</p>
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
</table>