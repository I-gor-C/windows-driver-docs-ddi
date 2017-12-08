---
UID: NF.dbgeng.IDebugClient5.PushOutputLinePrefix
title: IDebugClient5::PushOutputLinePrefix
author: windows-driver-content
description: Saves an output line prefix.
old-location: debugger\idebugclient5_pushoutputlineprefix.htm
old-project: debugger
ms.assetid: 20446E2D-94D3-43D6-ABBF-2FA15F089659
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugClient5, PushOutputLinePrefix, IDebugClient5::PushOutputLinePrefix
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: dbgeng.h
req.include-header: Dbgeng.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDebugClient5.PushOutputLinePrefix
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
req.iface: IDebugClient5
---

# IDebugClient5::PushOutputLinePrefix method



## -description
<p>    Saves an output line prefix.</p>


## -syntax

````
HRESULT PushOutputLinePrefix(
  [in, optional] PCSTR    NewPrefix,
  [out]          PULONG64 Handle
);
````


## -parameters
<dl>

### -param NewPrefix [in, optional]

<dd>
<p>A pointer to the new output line prefix.</p>
</dd>

### -param Handle [out]

<dd>
<p>The handle of the previous output line prefix.</p>
</dd>
</dl>

## -returns
<p>If this method succeeds, it returns <b xmlns:loc="http://microsoft.com/wdcml/l10n">S_OK</b>. Otherwise, it returns an <b xmlns:loc="http://microsoft.com/wdcml/l10n">HRESULT</b> error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dbgeng.h (include Dbgeng.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\dbgeng\nn-dbgeng-idebugclient5.md">IDebugClient5</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugClient5::PushOutputLinePrefix method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
