---
UID: NF.dbgeng.IDebugPlmClient.LaunchPlmPackageForDebugWide
title: IDebugPlmClient::LaunchPlmPackageForDebugWide
author: windows-driver-content
description: Launches a suspended Process Lifecycle Management (PLM) application.
old-location: debugger\idebugplmclient_launchplmpackagefordebugwide.htm
old-project: debugger
ms.assetid: DE11B4A5-5AE3-4369-AF6D-6CE34B9AAFAB
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IDebugPlmClient, LaunchPlmPackageForDebugWide, IDebugPlmClient::LaunchPlmPackageForDebugWide
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
req.alt-api: IDebugPlmClient.LaunchPlmPackageForDebugWide
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
req.iface: IDebugPlmClient
---

# IDebugPlmClient::LaunchPlmPackageForDebugWide method



## -description
<p>Launches a suspended Process Lifecycle Management (PLM) application.</p>


## -syntax

````
HRESULT LaunchPlmPackageForDebugWide(
  [in]           ULONG64 Server,
  [in]           ULONG   Timeout,
  [in]           PCWSTR  PackageFullName,
  [in]           PCWSTR  AppName,
  [in, optional] PCWSTR  Arguments,
  [out]          PULONG  ProcessId,
  [out]          PULONG  ThreadId
);
````


## -parameters
<dl>

### -param Server [in]

<dd>
<p>The server of the application.</p>
</dd>

### -param Timeout [in]

<dd>
<p>A time-out value.</p>
</dd>

### -param PackageFullName [in]

<dd>
<p>A pointer to the package name.</p>
</dd>

### -param AppName [in]

<dd>
<p>A pointer to the application name. </p>
</dd>

### -param Arguments [in, optional]

<dd>
<p>A pointer an arguments string.</p>
</dd>

### -param ProcessId [out]

<dd>
<p>A pointer to a process ID output.</p>
</dd>

### -param ThreadId [out]

<dd>
<p>A pointer to a thread ID output.</p>
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
<a href="..\dbgeng\nn-dbgeng-idebugplmclient.md">IDebugPlmClient</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [debugger\debugger]:%20IDebugPlmClient::LaunchPlmPackageForDebugWide method%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
