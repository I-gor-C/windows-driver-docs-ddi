---
UID: NF.winsplp.SplPromptUIInUsersSession
title: SplPromptUIInUsersSession
author: windows-driver-content
description: The SplPromptUIInUsersSession function displays a standard message box in the session indicated by the printer handle and job ID.
old-location: print\splpromptuiinuserssession.htm
ms.assetid: 5e458e3b-cfe2-4d48-b386-34d2a6c1d15e
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: print
req.header: winsplp.h
req.include-header: Winsplp.h
req.target-type: Desktop
req.target-min-winverclnt: The SplPromptUIInUsersSession function is available in Windows XP and later
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SplPromptUIInUsersSession
req.alt-loc: Spoolss.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Spoolss.lib
req.dll: Spoolss.dll
req.irql: 
ms.keywords: SplPromptUIInUsersSession
req.iface: 
req.product: Windows 10 or later.
---

# SplPromptUIInUsersSession function



## -description
<p>The <code>SplPromptUIInUsersSession</code> function displays a standard message box in the session indicated by the printer handle and job ID. </p>


## -syntax

````
BOOL SplPromptUIInUsersSession(
  _In_  HANDLE        hPrinter,
  _In_  DWORD         JobId,
  _In_  PSHOWUIPARAMS pUIParams,
  _Out_ DWORD         *pResponse
);
````


## -parameters
<dl>

### -param <i>hPrinter</i> [in]

<dd>
<p>Handle to the printer.</p>
</dd>

### -param <i>JobId</i> [in]

<dd>
<p>Specifies the print job.</p>
</dd>

### -param <i>pUIParams</i> [in]

<dd>
<p>Pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff562645">SHOWUIPARAMS</a> structure that contains values that determine the appearance and behavior of the message box.</p>
</dd>

### -param <i>pResponse</i> [out]

<dd>
<p>Pointer to a memory location that contains either the user's response or the IDASYNC constant. For more information, see the Remarks section.</p>
</dd>
</dl>

## -returns
<p>On success, the <code>SplPromptUIInUsersSession</code> function returns <b>TRUE</b>; otherwise it returns <b>FALSE</b>.</p>

## -remarks
<p>If <i>pUIParams</i> -&gt;<b>bWait</b> is <b>FALSE</b>, this function returns immediately without waiting for the user's response. In that case, *<i>pResponse</i> is set to IDASYNC. </p>

<p>If you plan to use this function in a driver intended to run under Windows 2000, you must load spoolss.dll by a call to the <b>LoadLibrary</b> function, and then find the address of this function within that DLL by a call to the <b>GetProcAddress</b> function. (<b>LoadLibrary</b> and <b>GetProcAddress</b> are described in the Microsoft Windows SDK documentation.) If the call to <b>GetProcAddress</b> fails, you must use an alternative mechanism to display user interface elements.</p>

<p>If <i>pUIParams</i> -&gt;<b>bWait</b> is <b>FALSE</b>, this function returns immediately without waiting for the user's response. In that case, *<i>pResponse</i> is set to IDASYNC. </p>

<p>If you plan to use this function in a driver intended to run under Windows 2000, you must load spoolss.dll by a call to the <b>LoadLibrary</b> function, and then find the address of this function within that DLL by a call to the <b>GetProcAddress</b> function. (<b>LoadLibrary</b> and <b>GetProcAddress</b> are described in the Microsoft Windows SDK documentation.) If the call to <b>GetProcAddress</b> fails, you must use an alternative mechanism to display user interface elements.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>The SplPromptUIInUsersSession function is available in Windows XP and later</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsplp.h (include Winsplp.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Spoolss.dll</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562645">SHOWUIPARAMS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562677">SplIsSessionZero</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [print\print]:%20SplPromptUIInUsersSession function%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
