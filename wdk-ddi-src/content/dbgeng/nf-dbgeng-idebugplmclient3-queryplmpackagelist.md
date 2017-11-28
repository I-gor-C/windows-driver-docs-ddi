---
UID: NF.dbgeng.IDebugPlmClient3.QueryPlmPackageList
title: IDebugPlmClient3::QueryPlmPackageList
author: windows-driver-content
description: Query a Process Lifecycle Management (PLM) package list.
old-location: debugger\idebugplmclient3_queryplmpackagelist.htm
old-project: debugger
ms.assetid: BAAAF09B-F39D-44E0-9409-1C98B0C6A56B
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDebugPlmClient3, QueryPlmPackageList, IDebugPlmClient3::QueryPlmPackageList
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
req.alt-api: IDebugPlmClient3.QueryPlmPackageList
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
req.iface: IDebugPlmClient3
---

# IDebugPlmClient3::QueryPlmPackageList method



## -description
<p>Query a Process Lifecycle Management (PLM) package list.</p>


## -syntax

````
HRESULT QueryPlmPackageList(
  [in] ULONG64              Server,
  [in] PDEBUG_OUTPUT_STREAM Stream
);
````


## -parameters
<dl>

### -param <i>Server</i> [in]

<dd>
<p>The server of the package.</p>
</dd>

### -param <i>Stream</i> [in]

<dd>
<p>A pointer to an output stream for results.</p>
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
<a href="..\dbgeng\nn-dbgeng-idebugplmclient3.md">IDebugPlmClient3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugPlmClient3::QueryPlmPackageList method%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
