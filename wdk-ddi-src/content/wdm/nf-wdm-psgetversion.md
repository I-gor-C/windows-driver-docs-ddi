---
UID: NF.wdm.PsGetVersion
title: PsGetVersion function
author: windows-driver-content
description: This function is obsolete in Windows XP and later versions of the Windows operating system. Use RtlGetVersion instead.PsGetVersion returns caller-selected information about the current version of the NT-based operating system.
old-location: kernel\psgetversion.htm
old-project: kernel
ms.assetid: db3d2e34-3d83-423d-b446-2800d53a8220
ms.author: windowsdriverdev
ms.date: 12/15/2017
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
req.product: Windows 10 or later.
---

# PsGetVersion function



## -description
This function is <u>obsolete</u> in Windows XP and later versions of the Windows operating system. Use <a href="kernel.rtlgetversion">RtlGetVersion</a> instead.

<b>PsGetVersion</b> returns caller-selected information about the current version of the NT-based operating system. 



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

### -param MajorVersion [out, optional]

Points to a caller-supplied variable that this routine sets to the major version of the operating system. This optional parameter can be <b>NULL</b>. 


### -param MinorVersion [out, optional]

Points to a caller-supplied variable that this routine sets to the minor version of the operating system. This optional parameter can be <b>NULL</b>. 


### -param BuildNumber [out, optional]

Points to a caller-supplied variable that this routine sets to the current build number of the operating system. This optional parameter can be <b>NULL</b>. 


### -param CSDVersion [out, optional]

Points to a caller-allocated buffer in which this routine returns the current service-pack version as a Unicode string only during system driver initialization. This optional parameter can be <b>NULL</b>. 


## -returns
<b>PsGetVersion</b> returns whether the system is a checked or free build, as follows:
<dl>
<dt><b><b>TRUE</b> (1)</b></dt>
</dl>Checked build of the operating system.
<dl>
<dt><b><b>FALSE</b> (0)</b></dt>
</dl>Free build of the operating system. 

 


## -remarks
<b>PsGetVersion</b> returns the requested information, depending on which optional parameter(s) the caller supplies.

To retrieve the current service-pack number, it is easier and more efficient to make an application-level call within the Win32 environment than to call <b>PsGetVersion</b> during system driver initialization, which then must parse the string it returns at <i>CSDVersion</i>. When the registry is initialized, a driver cannot obtain this string from <b>PsGetVersion</b>, but must read the <b>CmCSDVersionString</b> value from the registry. 


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
<dt>Wdm.h (include Ntddk.h)</dt>
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
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqlpspassive">IrqlPsPassive</a>, <a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>