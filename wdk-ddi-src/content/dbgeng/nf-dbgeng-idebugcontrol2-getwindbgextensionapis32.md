---
UID: NF.dbgeng.IDebugControl2.GetWindbgExtensionApis32
title: IDebugControl2::GetWindbgExtensionApis32
author: windows-driver-content
description: The GetWindbgExtensionApis32 method returns a structure that facilitates using the WdbgExts API.
old-location: debugger\idebugcontrol_getwindbgextensionapis32.htm
old-project: debugger
ms.assetid: 84661E3C-9AC7-4852-BABF-BFC0A793E83D
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugControl2, GetWindbgExtensionApis32, IDebugControl2::GetWindbgExtensionApis32
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugControl.GetWindbgExtensionApis32,IDebugControl2.GetWindbgExtensionApis32,IDebugControl3.GetWindbgExtensionApis32
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
req.iface: IDebugControl2
---

# IDebugControl2::GetWindbgExtensionApis32 method



## -description
<p>The <b>GetWindbgExtensionApis32</b> method returns a structure that facilitates using the WdbgExts API.</p>


## -syntax

````
HRESULT GetWindbgExtensionApis32(
  [in, out] PWINDBG_EXTENSION_APIS32 Api
);
````


## -parameters
<dl>

### -param <i>Api</i> [in, out]

<dd>
<p>Receives a WINDBG_EXTENSION_APIS32 structure.  This structure contains the functions used by the WdbgExts API.  The <b>nSize</b> member of this structure must be set to the size of the structure before it is passed to this method.</p>
</dd>
</dl>

## -returns
<p>This method may also return other error values.  See <a href="debugger.hresult_values">Return Values</a> for more details.</p><dl>
<dt><b>S_OK</b></dt>
</dl><p>The method was successful.</p><dl>
<dt><b>E_INVALIDARG</b></dt>
</dl><p>The value of <i>Api</i>-&gt;<b>nSize</b> does not equal the size of the structure WINDBG_EXTENSION_APIS32.</p>

<p> </p>

## -remarks
<p>If you are including Wdbgexts.h in your extension code, you should call this method during the initialization of the extension DLL (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540476">DebugExtensionInitialize</a>).</p>

<p>Many WdbgExts functions are really macros.  To ensure that these macros work correctly, the structure received by the <i>Api</i> parameter should be stored in a global variable named <b>ExtensionApis</b>.  </p>

<p>For a list of the functions provided by the WdbgExts API, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561258">WdbgExts Functions</a>.</p>

<p>If you are including Wdbgexts.h in your extension code, you should call this method during the initialization of the extension DLL (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff540476">DebugExtensionInitialize</a>).</p>

<p>Many WdbgExts functions are really macros.  To ensure that these macros work correctly, the structure received by the <i>Api</i> parameter should be stored in a global variable named <b>ExtensionApis</b>.  </p>

<p>For a list of the functions provided by the WdbgExts API, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff561258">WdbgExts Functions</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550512">IDebugControl2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550519">IDebugControl3</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540476">DebugExtensionInitialize</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff550508">IDebugControl</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561258">WdbgExts Functions</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugControl::GetWindbgExtensionApis32 method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
