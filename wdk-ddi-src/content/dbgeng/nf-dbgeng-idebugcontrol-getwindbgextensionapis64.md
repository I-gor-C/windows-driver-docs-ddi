---
UID: NF.dbgeng.IDebugControl.GetWindbgExtensionApis64
title: IDebugControl::GetWindbgExtensionApis64
author: windows-driver-content
description: The GetWindbgExtensionApis64 method returns a structure that facilitates using the WdbgExts API.
old-location: debugger\getwindbgextensionapis64.htm
old-project: debugger
ms.assetid: 01b34b26-2835-4a58-abf3-190da63d25eb
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugControl, GetWindbgExtensionApis64, IDebugControl::GetWindbgExtensionApis64
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Wdbgexts.h, Dbgeng.h, Wdbgexts.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetWindbgExtensionApis64,IDebugControl2.GetWindbgExtensionApis64,IDebugControl3.GetWindbgExtensionApis64
req.alt-loc: dbgeng.h
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
req.iface: IDebugControl
---

# IDebugControl::GetWindbgExtensionApis64 method



## -description
<p>The <b>GetWindbgExtensionApis64</b> method returns a structure that facilitates using the WdbgExts API.</p>


## -syntax

````
HRESULT GetWindbgExtensionApis64(
  [in, out] PWINDBG_EXTENSION_APIS64 Api
);
````


## -parameters
<dl>

### -param Api [in, out]

<dd>
<p>Receives a WINDBG_EXTENSION_APIS64 structure.  This structure contains the functions used by the WdbgExts API.  The <b>nSize</b> member of this structure must be set to the size of the structure before it is passed to this method.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="https://msdn.microsoft.com/713f3ee2-2f5b-415e-9908-90f5ae428b43">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The value of <i>Api</i>-&gt;<b>nSize</b> does not equal the size of the structure WINDBG_EXTENSION_APIS64.</p>

<p> </p>

## -remarks
<p>If you are including Wdbgexts.h in your extension code, you should call this method during the initialization of the extension DLL (see <a href="debugger.debugextensioninitialize">DebugExtensionInitialize</a>).</p>

<p>Many WdbgExts functions are really macros.  To ensure that these macros work correctly, the structure received by the <i>Api</i> parameter should be stored in a global variable named <b>ExtensionApis</b>.  </p>

<p>The WINDBG_EXTENSION_APIS64 structure returned by this method serves the same purpose as the one provided to the callback function <a href="debugger.windbgextensiondllinit">WinDbgExtensionDllInit</a> (used by WdbgExts extensions).</p>

<p>For a list of the functions provided by the WdbgExts API, see <a href="debugger.wdbgexts_functions">WdbgExts Functions</a>.</p>

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
<dt>Dbgeng.h (include Wdbgexts.h, Dbgeng.h, or Wdbgexts.h)</dt>
</dl>
</td>
</tr>
</table>