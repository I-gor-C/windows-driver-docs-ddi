---
UID: NF.prcomoem.IPrintCoreHelperUni2.GetNamedCommand
title: IPrintCoreHelperUni2::GetNamedCommand
author: windows-driver-content
description: The GetNamedCommand method returns the specified command.
old-location: print\iprintcorehelperuni2_getnamedcommand.htm
old-project: print
ms.assetid: A9C9C69E-8C89-4131-996F-A48AD9E9D244
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: IPrintCoreHelperUni2, GetNamedCommand, IPrintCoreHelperUni2::GetNamedCommand
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: prcomoem.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPrintCoreHelperUni2.GetNamedCommand
req.alt-loc: prcomoem.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: IPrintCoreHelperUni2
req.product: Windows 10 or later.
---

# IPrintCoreHelperUni2::GetNamedCommand method



## -description
<p>The <b>GetNamedCommand</b> method returns the specified command.</p>


## -syntax

````
HRESULT GetNamedCommand(
  [in]  PDEVMODE pDevmode,
  [in]  DWORD    cbSize,
  [in]  LPCWSTR  pszCommandName,
  [out] PBYTE    **ppCommandBytes,
  [out] DWORD    *pcbCommandSize
);
````


## -parameters
<dl>

### -param <i>pDevmode</i> [in]

<dd>
<p>A pointer to a DEVMODE structure.</p>
</dd>

### -param <i>cbSize</i> [in]

<dd>
<p>The number of bytes in <i>pDevmode</i>, not the number of bytes written.</p>
</dd>

### -param <i>pszCommandName</i> [in]

<dd>
<p>The command name. This parameter accepts standard command names from the GPD, except for those that require an *Order attribute. Those six sections of ordered command sequences are accessible via the following special command names:</p>
<ul>
<li>L"SectionJobSetup"</li>
<li>L"SectionDocSetup"</li>
<li>L"SectionPageSetup"</li>
<li>L"SectionPageFinish"</li>
<li>L"SectionDocFinish"</li>
<li>L"SectionJobFinish"</li>
</ul>
</dd>

### -param <i>ppCommandBytes</i> [out]

<dd>
<p>The output buffer. This buffer does not need to be freed by the caller.</p>
</dd>

### -param <i>pcbCommandSize</i> [out]

<dd>
<p>The size of the output buffer.    </p>
</dd>
</dl>

## -returns
<p>This method returns an <b>HRESULT</b> value.</p>

## -remarks
<p>The <b>GetNamedCommand</b> method will not return commands containing references to Standard Variables.</p>

<p>The <b>GetNamedCommand</b> method will not return commands containing references to Standard Variables.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Prcomoem.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="print.iprintcorehelperuni2_interface">IPrintCoreHelperUni2</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20IPrintCoreHelperUni2::GetNamedCommand method%20 RELEASE:%20(11/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
