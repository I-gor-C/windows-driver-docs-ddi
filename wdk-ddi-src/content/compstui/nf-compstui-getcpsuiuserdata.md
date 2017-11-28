---
UID: NF.compstui.GetCPSUIUserData
title: GetCPSUIUserData
author: windows-driver-content
description: CPSUI's GetCPSUIUserData function retrieves data that was previously stored using the SetCPSUIUserData function.
old-location: print\getcpsuiuserdata.htm
old-project: print
ms.assetid: 2a0a74cd-2dcf-4485-8941-7f205dcecede
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: GetCPSUIUserData
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: compstui.h
req.include-header: Compstui.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: GetCPSUIUserData
req.alt-loc: Compstui.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Compstui.lib
req.dll: Compstui.dll
req.irql: 
req.iface: 
---

# GetCPSUIUserData function



## -description
<p>CPSUI's <b>GetCPSUIUserData</b> function retrieves data that was previously stored using the <a href="https://msdn.microsoft.com/library/windows/hardware/ff562624">SetCPSUIUserData</a> function.</p>


## -syntax

````
ULONG_PTR GetCPSUIUserData(
   HWND hDlg
);
````


## -parameters
<dl>

### -param <i>hDlg</i> 

<dd>
<p>Caller-supplied handle to a property sheet dialog box. For more information, see the following Remarks section.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the function returns the value that was previously supplied to <a href="https://msdn.microsoft.com/library/windows/hardware/ff562624">SetCPSUIUserData</a>; otherwise the function returns zero.</p>

## -remarks
<p>The <b>GetCPSUIUserData</b> function should only be called from within a dialog box procedure that has been associated with a dialog box by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a> structure.</p>

<p>The handle specified for <i>hDlg</i> must be the handle received as input to the dialog box procedure. (Dialog box procedures are described in the Microsoft Windows SDK documentation.)</p>

<p>The <b>GetCPSUIUserData</b> function should only be called from within a dialog box procedure that has been associated with a dialog box by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a> structure.</p>

<p>The handle specified for <i>hDlg</i> must be the handle received as input to the dialog box procedure. (Dialog box procedures are described in the Microsoft Windows SDK documentation.)</p>

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
<dt>Compstui.h (include Compstui.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Compstui.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Compstui.dll</dt>
</dl>
</td>
</tr>
</table>