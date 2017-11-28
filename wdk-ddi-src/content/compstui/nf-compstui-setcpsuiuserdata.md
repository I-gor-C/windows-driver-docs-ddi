---
UID: NF.compstui.SetCPSUIUserData
title: SetCPSUIUserData
author: windows-driver-content
description: CPSUI's SetCPSUIUserData function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box.
old-location: print\setcpsuiuserdata.htm
old-project: print
ms.assetid: 35119100-adf9-4376-bb1a-7317733fbcc5
ms.author: windowsdriverdev
ms.date: 11/24/2017
ms.keywords: SetCPSUIUserData
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
req.alt-api: SetCPSUIUserData
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

# SetCPSUIUserData function



## -description
<p>CPSUI's <code>SetCPSUIUserData</code> function allows CPSUI applications (including printer interface DLLs) to associate nondisplayed data with a property sheet dialog box.</p>


## -syntax

````
BOOL SetCPSUIUserData(
   HWND      hDlg,
   ULONG_PTR CPSUIUserData
);
````


## -parameters
<dl>

### -param <i>hDlg</i> 

<dd>
<p>Caller-supplied handle to a property sheet dialog box. For more information, see the following Remarks section.</p>
</dd>

### -param <i>CPSUIUserData</i> 

<dd>
<p>Caller-supplied value to be stored.</p>
</dd>
</dl>

## -returns
<p>The  function returns <b>TRUE</b> if it is successful in associating the nondisplayed data with the property sheet dialog box, and <b>FALSE</b> otherwise.</p>

## -remarks
<p>The <code>SetCPSUIUserData</code> function should be called only from within a dialog box procedure that has been associated with a dialog box by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a> structure.</p>

<p>A value that is stored by calling <code>SetCPSUIUserData</code> can be later retrieved by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549922">GetCPSUIUserData</a>.</p>

<p>The handle specified for <i>hDlg</i> must be the handle received as input to the dialog box procedure. (Dialog box procedures are described in the Microsoft Windows SDK documentation.)</p>

<p>The <code>SetCPSUIUserData</code> function should be called only from within a dialog box procedure that has been associated with a dialog box by using a <a href="https://msdn.microsoft.com/library/windows/hardware/ff547607">DLGPAGE</a> or an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548795">EXTPUSH</a> structure.</p>

<p>A value that is stored by calling <code>SetCPSUIUserData</code> can be later retrieved by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff549922">GetCPSUIUserData</a>.</p>

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